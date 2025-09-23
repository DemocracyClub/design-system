import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import List
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

from playwright.sync_api import sync_playwright

# Ignore these URLS in visual tests
IGNORE_URLS = (
    # Maps render a little differently and cause flakey tests.
    "/components/map-leaflet/",
)

BROWSERS = {
    "chromium": {
        "user_data_dir": tempfile.mkdtemp(),
        "headless": True,
        "args": [
            "--disable-gpu",
            "--force-color-profile=srgb",
            "--disable-lcd-text",
            "--disable-font-subpixel-positioning",
        ],
        "device_scale_factor": 1,
        "locale": "en-GB",
        "timezone_id": "Europe/London",
    },
    "firefox": {
        "user_data_dir": tempfile.mkdtemp(),
        "headless": True,
        "args": ["--disable-gpu"],
        "firefox_user_prefs": {
            "layout.css.devPixelsPerPx": "1.0",
            "intl.accept_languages": "en-GB,en",
            "browser.display.use_document_fonts": 1,
            "gfx.font_rendering.fontconfig.fontlist.enabled": False,
            "gfx.font_rendering.opentype_svg.enabled": False,
            "gfx.downloadable_fonts.enabled": True,
            "gfx.color_management.mode": 1,
            "gfx.font_rendering.cleartype_params.cleartype_level": 0,
            "gfx.font_rendering.cleartype_params.rendering_mode": 5,
            "gfx.font_rendering.cleartype_params.enhanced_contrast": 0,
            "gfx.color_management.display_profile": "",
        },
        "device_scale_factor": 1,
        "locale": "en-GB",
        "timezone_id": "Europe/London",
    },
    "webkit": {
        "user_data_dir": tempfile.mkdtemp(),
        "headless": True,
    },
}

VIEWPORTS = {
    "mobile": {"width": 375, "height": 667},
    "tablet": {"width": 768, "height": 1024},
    "desktop": {"width": 1440, "height": 900},
}


@dataclass
class HTMLElement:
    theme: str
    url: str
    selector: int

    def __post_init__(self):
        if self.theme not in ("light", "dark"):
            raise ValueError(f"Invalid theme: {self.theme}")

    @property
    def url_path(self):
        return urlparse(self.url).path


def get_screenshot_filename(viewport: str, browser_name: str, element: HTMLElement):
    label = element.url_path

    path = (
        Path(label.lstrip("/"))
        / browser_name
        / f"element-{element.selector}"
        / f"{element.theme}-{viewport}"
    )
    return path.with_suffix(".png")


def get_screenshot_root(prefix):
    root = Path("./tests/screenshots").absolute()
    path = root / prefix
    path.mkdir(parents=True, exist_ok=True)
    return path


def get_soup(url):
    resp = requests.get(url)
    return BeautifulSoup(resp.text, features="html.parser")


def parse_component_page(url):
    soup = get_soup(url)
    page_elements: List[HTMLElement] = []
    for theme in ["light", "dark"]:
        for i, element in enumerate(soup.select(f".ds-example-{theme}")):
            page_elements.append(HTMLElement(theme=theme, url=url, selector=i))
    return page_elements


def build_screenshot_list(local_server):
    """
    Scrapes the documentation page and looks for examples.

    Used them to build a list of elements that we want to screenshot.

    """
    soup = get_soup(local_server)
    elements_to_capture: List[HTMLElement] = []

    # Iterate over all the pages in the nav and look for examples
    for page in soup.select("nav ul li a"):
        page_url = urljoin(local_server, page["href"])
        elements_to_capture += parse_component_page(page_url)
    return elements_to_capture


def generate_screenshots(url, baseline=False, playwright_instance=None):
    """
    Using the docs site, find elements to screenshot and save the images
    to a path.

    The two 'modes' are either 'test' or 'baseline' Baseline will write files
    that are intended to be checked in, where as test image are ephemeral.

    The playwright instance arg is needed to get around using the page fixture
    from pytest-playwright. When using that, a browser context is set up in a way
    that errors if we try to set up our own playwright. We need to use our own
    when we're making the baseline. Essentially this conditional is a way to get
    a working playwright both in and out of pytest.

    """
    elements = build_screenshot_list(url)

    if playwright_instance:
        for filename in iterate_matrix(
            playwright_instance, elements, baseline=baseline
        ):
            yield filename
    else:
        with sync_playwright() as p:
            for filename in iterate_matrix(p, elements, baseline=baseline):
                yield filename


def iterate_matrix(playwright, elements, baseline=False):
    for browser_name, browser_config in BROWSERS.items():
        context = getattr(playwright, browser_name).launch_persistent_context(
            **browser_config
        )

        for viewport_name, viewport in VIEWPORTS.items():
            page = context.new_page()
            page.set_viewport_size(viewport)
            for element in elements:
                if element.url_path in IGNORE_URLS:
                    continue
                page.goto(element.url, wait_until="domcontentloaded")
                page.wait_for_function(
                    """() =>
                        document.fonts?.status === 'loaded' &&
                        Array.from(document.images).every(
                          img => img.complete && img.naturalWidth > 0
                        )
                    """
                )
                page.wait_for_timeout(30)
                filename = get_screenshot_filename(viewport_name, browser_name, element)

                el = page.locator(f".ds-example-{element.theme}").nth(element.selector)
                el.scroll_into_view_if_needed()
                prefix = "test"
                if baseline:
                    prefix = "baseline"
                full_path = get_screenshot_root(prefix) / filename
                full_path.parent.mkdir(exist_ok=True, parents=True)
                el.screenshot(path=full_path)
                yield filename
        context.close()
