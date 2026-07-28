"""
Shared pytest fixtures for the Selenium Playground test suite.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    """
    Function-scoped driver fixture - a fresh browser instance per test.
    scope='function' means each test is fully isolated (new browser each time).
    scope='session' would reuse one browser across all tests - faster, but tests
    can leak state (cookies, open tabs, alerts) into each other.
    """
    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service)
    drv.maximize_window()

    yield drv  # --- setup complete, test runs here ---

    drv.quit()  # --- teardown: runs after the test, even if it fails ---


@pytest.fixture(scope='session')
def base_url():
    """Task 48: session-scoped base_url constant, reused by all tests."""
    return "https://www.lambdatest.com/selenium-playground/"


# ---------------------------------------------------------------------------
# Task 46: Screenshot on test failure
# ---------------------------------------------------------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver_fixture = item.funcargs.get("driver")
        if driver_fixture is not None:
            test_name = item.name.replace("/", "_").replace("::", "_")
            screenshot_path = f"{test_name}_failure.png"
            driver_fixture.save_screenshot(screenshot_path)
            print(f"\nScreenshot captured on failure: {screenshot_path}")