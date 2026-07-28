import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_driver(headless: bool = False):
    """Initialise and return a Chrome WebDriver instance using webdriver-manager."""
    options = Options()
    if headless:
        # Task 27: run without a visible browser window
        options.add_argument('--headless=new')
        options.add_argument('--window-size=1280,800')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Task 26: implicit wait
    # NOTE: Setting implicit wait globally is considered bad practice because it applies the
    # SAME wait time to EVERY find_element call across the entire test suite, even when an
    # element should appear instantly. This can mask real timing issues, slow down failure
    # detection (a missing element waits the full timeout before raising NoSuchElementException),
    # and conflicts/produces unpredictable behaviour when mixed with explicit waits
    # (WebDriverWait) later in Hands-On 5. Explicit waits let you wait for a SPECIFIC condition
    # on a SPECIFIC element, which is more precise and predictable.
    driver.implicitly_wait(10)
    return driver


def main():
    driver = get_driver(headless=False)
    try:
        driver.get("https://www.lambdatest.com/selenium-playground/")
        print("Page title:", driver.title)
    finally:
        driver.close()
        driver.quit()


def main_headless():
    """Task 27: headless mode verification."""
    driver = get_driver(headless=True)
    try:
        driver.get("https://www.lambdatest.com/selenium-playground/")
        print("Headless mode - Page title:", driver.title)
    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":
    main()
    main_headless()