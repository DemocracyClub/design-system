import shutil
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops
from screenshot_utils import generate_screenshots, get_screenshot_root


def visual_diff(
    baseline_path: str,
    test_path: str,
    out_path: Path,
    per_channel_delta: int = 8,  # tolerance per channel (0..255)
    allowed_mismatch: float = 0,  # % of pixels allowed to differ
):
    """
    Image visual diff.

    Take two image paths and error if the pixel diff isn't within
    `allowed_mismatch`. The value of this is a bit of a magic number: there are
    minor changes between screenshots for random reasons (antialiasing, browser
    minor versions etc). These don't produce useful test fails, so we set a
    'fuzzy' diff level.

    If the test fails (the diff is over the given percent) then we write an
    image with the baseline, test and diff highlighted. This is useful for
    seeing what changed.
    """
    baseline_image = Image.open(baseline_path).convert("RGBA")
    test_image = Image.open(test_path).convert("RGBA")

    # pad to same size
    max_w, max_h = (
        max(baseline_image.width, test_image.width),
        max(baseline_image.height, test_image.height),
    )

    def pad(im):
        canvas = Image.new("RGBA", (max_w, max_h), (255, 0, 255, 255))
        canvas.paste(im, (0, 0))
        return canvas

    baseline_padded, test_padded = pad(baseline_image), pad(test_image)

    # pixel diff
    diff = ImageChops.difference(baseline_padded, test_padded)
    arr = np.asarray(diff)

    # mismatch mask (any channel difference > per_channel_delta)
    mismatch_mack = (arr[:, :, :3] > per_channel_delta).any(axis=2)
    mismatches = int(mismatch_mack.sum())
    total = arr.shape[0] * arr.shape[1]
    mismatch_pct = mismatches * 100.0 / total

    # build overlay (baseline + red mismatches)
    overlay_arr = np.array(baseline_padded)
    overlay_arr[mismatch_mack] = [255, 0, 0, 255]
    overlay = Image.fromarray(overlay_arr, "RGBA")

    passing = mismatch_pct <= allowed_mismatch
    if not passing:
        # composite image: baseline | actual | overlay
        composite = Image.new("RGBA", (max_w * 3, max_h))
        composite.paste(baseline_padded, (0, 0))
        composite.paste(test_padded, (max_w, 0))
        composite.paste(overlay, (max_w * 2, 0))
        out_path.parent.mkdir(exist_ok=True, parents=True)
        composite.save(out_path)

    assert passing, (
        f"Visual diff failed: {mismatch_pct:.3f}% mismatched pixels "
        f"(allowed {allowed_mismatch}%) — see {out_path}"
    )


def test_live_images_against_baseline(local_server, subtests, playwright):
    diff_root = get_screenshot_root("diff")
    test_root = get_screenshot_root("test")

    # We can't use shutil.rmtree in Docker because we're mounting the directories with tmpfs.
    for dir in (diff_root, test_root):
        for item in test_root.iterdir():
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()

    for filename in generate_screenshots(
        local_server, baseline=False, playwright_instance=playwright
    ):
        with subtests.test(msg=f"{filename}"):
            baseline_path = get_screenshot_root("baseline") / filename
            test_path = test_root / filename
            diff_path = diff_root / filename
            visual_diff(baseline_path, test_path, diff_path)
