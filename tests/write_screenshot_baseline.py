import shutil

from conftest import run_local_server
from screenshot_utils import generate_screenshots, get_screenshot_root

if __name__ == "__main__":
    baseline_root = get_screenshot_root("baseline")

    for item in baseline_root.iterdir():
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()
    with run_local_server() as url:
        for filename in generate_screenshots(url, baseline=True):
            print(f"Writing {filename}")
