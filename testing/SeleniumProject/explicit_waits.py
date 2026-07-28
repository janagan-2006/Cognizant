"""
Hands-On 5 - Task 2: WebDriverWait and Expected Conditions
Target: Bootstrap Alerts Demo on LambdaTest Selenium Playground
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait as FluentWait
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://www.lambdatest.com/selenium-playground/"


def get_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver  # NOTE: no implicit wait here - we use explicit waits exclusively


def test_explicit_wait_alert(driver):
    """Task 36: wait for success alert to become visible, assert text."""
    driver.get(BASE_URL + "bootstrap-alerts/")

    success_btn = driver.find_element(By.ID, "successAlertBtn")
    success_btn.click()

    alert = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
    )
    assert "successfully" in alert.text.lower(), f"Unexpected alert text: {alert.text}"
    print("Alert text verified:", alert.text)


def test_sleep_vs_explicit_wait_timing(driver):
    """Task 37: compare time.sleep(3) vs explicit wait timing."""
    driver.get(BASE_URL + "bootstrap-alerts/")

    # --- Version A: time.sleep(3) ---
    start_sleep = time.time()
    btn = driver.find_element(By.ID, "successAlertBtn")
    btn.click()
    time.sleep(3)  # always waits the FULL 3 seconds, even if the alert appeared in 0.2s
    alert = driver.find_element(By.CSS_SELECTOR, ".alert-success")
    sleep_duration = time.time() - start_sleep
    print(f"time.sleep() version took: {sleep_duration:.2f}s")

    driver.refresh()

    # --- Version B: explicit wait ---
    start_wait = time.time()
    btn = driver.find_element(By.ID, "successAlertBtn")
    btn.click()
    alert = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
    )
    wait_duration = time.time() - start_wait
    print(f"Explicit wait version took: {wait_duration:.2f}s")

    # COMMENT: On a fast machine, the explicit wait version finishes almost immediately once the
    # element appears (e.g., ~0.3s), whereas time.sleep(3) always burns the full 3 seconds
    # regardless of how fast the element actually loaded - making the suite slower overall.
    # On a SLOW machine/network, time.sleep(3) might not even be long enough (causing a flaky
    # failure), whereas the explicit wait keeps polling up to 10s and succeeds reliably whenever
    # the element actually appears. Explicit waits are therefore both faster on fast machines
    # AND more reliable on slow ones.


def test_element_to_be_clickable(driver):
    """Task 38: wait for clickable, with explanation comment."""
    driver.get(BASE_URL + "bootstrap-alerts/")

    btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "successAlertBtn"))
    )
    btn.click()

    # COMMENT:
    # visibility_of_element_located only checks that the element exists in the DOM AND has a
    # non-zero size (i.e., it's visible on the page) - it does NOT check whether the element is
    # enabled or clickable. An element could be visible but disabled, or visible but covered by
    # an overlay/modal, and visibility_of_element_located would still consider the wait satisfied.
    #
    # element_to_be_clickable goes further: it checks that the element is VISIBLE, ENABLED
    # (not disabled), AND not obscured by another element on top of it - i.e., a real click would
    # actually succeed. Use element_to_be_clickable specifically before any .click() action to
    # avoid ElementClickInterceptedException or ElementNotInteractableException.


def test_fluent_wait_dynamic_table(driver):
    """Task 39: FluentWait polling every 500ms, ignoring NoSuchElementException."""
    driver.get(BASE_URL + "table-sort-search/")

    fluent_wait = FluentWait(driver, timeout=10, poll_frequency=0.5).ignore(NoSuchElementException)

    row = fluent_wait.until(
        lambda d: d.find_element(By.CSS_SELECTOR, "table tbody tr")
    )
    print("Dynamically loaded row found:", row.is_displayed())


if __name__ == "__main__":
    driver = get_driver()
    try:
        test_explicit_wait_alert(driver)
        driver.get(BASE_URL)
        test_sleep_vs_explicit_wait_timing(driver)
        test_element_to_be_clickable(driver)
        test_fluent_wait_dynamic_table(driver)
    finally:
        driver.quit()