import logging
import os
import re
import shutil
from pathlib import Path

import pytest
from selenium import webdriver

REPORT_TITLE = "Test Results"
CHROME_VERSION = "stable"


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s",
)


# use Chrome-for-Testing instead of system Chrome unless overridden
os.environ.setdefault("SE_FORCE_BROWSER_DOWNLOAD", "true")


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Run browser in headless mode")


def pytest_sessionstart(session):
    screenshots_dir = Path(__file__).resolve().parent / "report" / "screenshots"
    shutil.rmtree(screenshots_dir, ignore_errors=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        if report.failed:
            driver = item.funcargs["request"].getfixturevalue("driver")
            if driver:
                screenshots_dir = Path(__file__).resolve().parent / "report" / "screenshots"
                screenshots_dir.mkdir(exist_ok=True)
                clean_name = re.sub(r"[/\\?%*:|\"<>\x7F\x00-\x1F]", "-", item.name)[:255]
                path = str(screenshots_dir / f"{clean_name}.png")
                driver.save_screenshot(path)
                extras.append(pytest_html.extras.png(path))
        report.extras = extras


def pytest_html_results_table_header(cells):
    cells.pop()


def pytest_html_results_table_row(report, cells):
    cells.pop()


def pytest_html_report_title(report):
    report.title = REPORT_TITLE


@pytest.fixture(scope="session")
def browser_options(request):
    options = webdriver.ChromeOptions()
    options.browser_version = CHROME_VERSION
    if request.config.getoption("--headless"):
        options.add_argument("--headless")
    return options


@pytest.fixture
def driver(browser_options):
    driver = webdriver.Chrome(options=browser_options)
    driver.maximize_window()
    yield driver
    driver.quit()
