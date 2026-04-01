#!/usr/bin/env python3
"""
Update Montserrat font subsets used by the design system.

This script downloads the full Montserrat font from Google Fonts' GitHub
repository, reads the current character set from the existing font subsets,
merges in any additional characters defined in EXTRA_UNICODES, and regenerates
all four font files (light/medium × woff/woff2).

Usage:
    uv run --with fonttools --with brotli scripts/update-fonts.py

To add new characters, add their Unicode codepoints (as hex strings) to the
EXTRA_UNICODES list below, then re-run the script.

See the "Updating fonts" section of README.md for more details.
"""

import sys
import urllib.request
from pathlib import Path


# ── Characters to add beyond what the current subsets already contain ────────
#
# Add hex codepoints here (e.g. "U+0175" or "0x0175"). Checked against the
# existing subset automatically, so safe to leave old values in.
#
EXTRA_UNICODES = [
    "U+00C8",  # È  – Scottish Gaelic (e.g. Èirisgeigh)
    "U+00D9",  # Ù  – Scottish Gaelic (e.g. Ùige)
    "U+00E0",  # à  – Scottish Gaelic (e.g. Càrlabhagh)
    "U+00E1",  # á  – Welsh (e.g. Llandygái)
    "U+00EC",  # ì  – Scottish Gaelic (e.g. Sgìre)
    "U+00F2",  # ò  – Scottish Gaelic (e.g. Steòrnabhagh)
    "U+00F4",  # ô  – Welsh (e.g. Môn, Bôn-y-maen)
    "U+0174",  # Ŵ  – Welsh uppercase w with circumflex
    "U+0175",  # ŵ  – Welsh lowercase w with circumflex (e.g. Gŵyr, Glyndŵr)
    "U+0176",  # Ŷ  – Welsh uppercase y with circumflex
    "U+0177",  # ŷ  – Welsh lowercase y with circumflex (e.g. Tŷ, Llŷn)
    "U+2032",  # ′  – Prime (used as apostrophe in Scottish Gaelic, e.g. Eilean a′ Cheò)
]


try:
    from fontTools.ttLib import TTFont
    from fontTools.subset import Subsetter, Options
except ImportError:
    print(
        "ERROR: fonttools not found. Run with: uv run --with fonttools --with brotli scripts/update-fonts.py"
    )
    sys.exit(1)

REPO_ROOT = Path(__file__).parent.parent
FONT_DIR = REPO_ROOT / "system" / "fonts"
CACHE_DIR = REPO_ROOT / ".font-cache"

# Source: Google Fonts GitHub repository (OFL licence)
FONT_SOURCES = {
    "light": {
        "url": "https://github.com/JulietaUla/Montserrat/raw/master/fonts/ttf/Montserrat-Light.ttf",
        "existing_woff2": FONT_DIR / "montserrat-light.woff2",
        "existing_woff": FONT_DIR / "montserrat-light.woff",
        "out_stem": "montserrat-light",
    },
    "medium": {
        "url": "https://github.com/JulietaUla/Montserrat/raw/master/fonts/ttf/Montserrat-Medium.ttf",
        "existing_woff2": FONT_DIR / "montserrat-medium.woff2",
        "existing_woff": FONT_DIR / "montserrat-medium.woff",
        "out_stem": "montserrat-medium",
    },
}

MIRROR_DIR = REPO_ROOT / "src-site" / "styles" / "fonts"


def parse_codepoint(value: str) -> int:
    return int(value.replace("U+", "").replace("0x", ""), 16)


def get_existing_codepoints(woff2_path: Path) -> set[int]:
    font = TTFont(woff2_path)
    return set(font.getBestCmap().keys())


def download_if_needed(url: str, dest: Path) -> Path:
    if dest.exists():
        print(f"  Cached: {dest.name}")
        return dest
    print(f"  Downloading {url} ...")
    dest.parent.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(url, dest)
    print(f"  Saved to {dest}")
    return dest


def build_unicode_string(codepoints: set[int]) -> str:
    """Convert a set of codepoints to the comma-separated U+XXXX format
    that fontTools Subsetter expects."""
    return ",".join(f"U+{cp:04X}" for cp in sorted(codepoints))


def subset_font(source_ttf: Path, codepoints: set[int], out_path: Path, flavor: str):
    """Subset source_ttf to codepoints and save as woff or woff2."""
    font = TTFont(source_ttf)
    options = Options()
    options.flavor = flavor  # "woff" or "woff2"
    options.layout_features = ["*"]
    options.name_IDs = ["*"]

    subsetter = Subsetter(options=options)
    subsetter.populate(unicodes=codepoints)
    subsetter.subset(font)

    font.save(out_path)
    print(
        f"  Written {out_path.relative_to(REPO_ROOT)}  ({out_path.stat().st_size // 1024} KB)"
    )


def main():
    extra = {parse_codepoint(u) for u in EXTRA_UNICODES}

    for weight, cfg in FONT_SOURCES.items():
        print(f"\n=== {weight} ===")

        existing = get_existing_codepoints(cfg["existing_woff2"])
        combined = existing | extra
        new_chars = combined - existing
        if new_chars:
            print(
                f"  Adding {len(new_chars)} new codepoints: "
                + " ".join(f"U+{cp:04X}({chr(cp)})" for cp in sorted(new_chars))
            )
        else:
            print("  No new codepoints to add – font already up to date.")

        ttf_cache = CACHE_DIR / f"Montserrat-{weight.capitalize()}.ttf"
        source_ttf = download_if_needed(cfg["url"], ttf_cache)

        for flavor, existing_path in [
            ("woff2", cfg["existing_woff2"]),
            ("woff", cfg["existing_woff"]),
        ]:
            out_path = FONT_DIR / f"{cfg['out_stem']}.{flavor}"
            subset_font(source_ttf, combined, out_path, flavor)

    # Mirror to src-site
    print("\n=== Mirroring to src-site/styles/fonts/ ===")
    MIRROR_DIR.mkdir(parents=True, exist_ok=True)
    import shutil

    for f in FONT_DIR.glob("montserrat-*"):
        dest = MIRROR_DIR / f.name
        shutil.copy2(f, dest)
        print(f"  Copied {f.name}")

    print("\nDone. Remember to bump the version in package.json before releasing.")


if __name__ == "__main__":
    main()
