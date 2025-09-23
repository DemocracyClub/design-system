import shutil

from conftest import run_local_server
from screenshot_utils import generate_screenshots, get_screenshot_root

if __name__ == "__main__":
    baseline_root = get_screenshot_root("baseline")
    shutil.rmtree(baseline_root)
    with run_local_server() as url:
        for filename in generate_screenshots(url, baseline=True):
            print(f"Writing {filename}")
