from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

BASE_URL = "https://www.lambdatest.com/selenium-playground/"


def get_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    return driver


def test_navigation_and_url_assert(driver):
    """Task 28: navigate to Simple Form Demo, assert URL, navigate back."""
    driver.get(BASE_URL)
    simple_form_link = driver.find_element(By.LINK_TEXT, "Simple Form Demo")
    simple_form_link.click()

    assert 'simple-form-demo' in driver.current_url, \
        f"Expected 'simple-form-demo' in URL, got {driver.current_url}"
    print("URL assertion passed:", driver.current_url)

    driver.back()
    print("Navigated back to:", driver.current_url)


def test_multi_window_handling(driver):
    """Task 29 & 30: open new tab, switch between tabs, screenshot."""
    driver.get(BASE_URL)

    # Open a new tab via JS
    driver.execute_script('window.open("https://www.google.com");')

    all_handles = driver.window_handles
    print("Open tabs:", len(all_handles))

    # Switch to the new (second) tab
    driver.switch_to.window(all_handles[1])
    print("Switched tab title:", driver.title)

    # Switch back to the original tab
    driver.switch_to.window(all_handles[0])
    print("Back to original tab:", driver.title)

    # Take a screenshot of the original tab
    screenshot_taken = driver.save_screenshot('playground_screenshot.png')
    assert screenshot_taken, "Screenshot was not saved"
    print("Screenshot saved: playground_screenshot.png")


def test_window_size(driver):
    """Task 31: get/set window size."""
    current_size = driver.get_window_size()
    print("Current window size:", current_size)

    driver.set_window_size(1280, 800)
    new_size = driver.get_window_size()
    print("New window size:", new_size)

    # NOTE: Consistent window size matters for responsive UI automation because many modern
    # web apps use responsive breakpoints (e.g., mobile vs tablet vs desktop layouts). If the
    # browser window size is inconsistent between test runs, elements may shift position, hide
    # behind a hamburger menu, or change layout entirely - causing locators that worked in one
    # run to fail in another. Fixing the window size ensures the DOM/layout is identical every
    # time the suite runs, making locators and assertions reliable.


if __name__ == "__main__":
    driver = get_driver()
    try:
        test_navigation_and_url_assert(driver)
        test_multi_window_handling(driver)
        test_window_size(driver)
    finally:
        driver.quit()