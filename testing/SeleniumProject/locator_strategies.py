"""
Hands-On 5 - Task 1: Locator Strategies
Target: Simple Form Demo & Checkbox Demo on LambdaTest Selenium Playground
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://www.lambdatest.com/selenium-playground/"


def get_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    return driver


def test_all_locator_strategies(driver):
    """Task 32: locate the message input field using 6 different strategies."""
    driver.get(BASE_URL + "simple-form-demo/")

    # 1. By ID
    el_id = driver.find_element(By.ID, "user-message")
    print("By.ID found:", el_id.is_displayed())

    # 2. By NAME
    el_name = driver.find_element(By.NAME, "message")
    print("By.NAME found:", el_name.is_displayed())

    # 3. By CLASS_NAME
    el_class = driver.find_element(By.CLASS_NAME, "form-control")
    print("By.CLASS_NAME found:", el_class.is_displayed())

    # 4. By TAG_NAME (locates the FIRST <input> tag on the page)
    el_tag = driver.find_element(By.TAG_NAME, "input")
    print("By.TAG_NAME found:", el_tag.is_displayed())

    # 5. By XPATH - absolute path (fragile, included only to demonstrate)
    el_xpath_abs = driver.find_element(
        By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input"
    )
    print("By.XPATH absolute found:", el_xpath_abs.is_displayed())

    # 6. By XPATH - relative path using attributes (robust)
    el_xpath_rel = driver.find_element(By.XPATH, "//input[@id='user-message']")
    print("By.XPATH relative found:", el_xpath_rel.is_displayed())


def test_css_selectors(driver):
    """Task 33: 3 different CSS selectors for the same element."""
    driver.get(BASE_URL + "simple-form-demo/")

    # By ID
    css_by_id = driver.find_element(By.CSS_SELECTOR, "#user-message")
    print("CSS by ID found:", css_by_id.is_displayed())

    # By attribute
    css_by_attr = driver.find_element(By.CSS_SELECTOR, "[name='message']")
    print("CSS by attribute found:", css_by_attr.is_displayed())

    # By parent-child relationship
    css_by_parent_child = driver.find_element(By.CSS_SELECTOR, "div.form-group > input")
    print("CSS by parent-child found:", css_by_parent_child.is_displayed())


def test_checkbox_xpath_text(driver):
    """Task 34: XPath text() and contains() on Checkbox Demo."""
    driver.get(BASE_URL + "checkbox-demo/")

    # Exact text match
    exact_label = driver.find_element(By.XPATH, "//label[text()='Option 1']")
    print("Exact text() match found:", exact_label.is_displayed())

    # Partial text match - finds ALL labels containing 'Option'
    contains_labels = driver.find_elements(By.XPATH, "//label[contains(text(),'Option')]")
    print(f"contains() found {len(contains_labels)} matching labels")


def locator_ranking():
    """
    Task 35: Ranking locator strategies from MOST to LEAST preferred.

    1. ID            - Unique per element (by HTML spec), fastest to locate, highly readable,
                        and rarely changes during routine UI tweaks. Most preferred.
    2. CSS_SELECTOR  - Fast (native browser support), flexible, readable, and far less brittle
                        than XPath for attribute/class-based lookups.
    3. NAME          - Often unique within a form, readable, but less universally present than ID.
    4. CLASS_NAME    - Can match multiple elements if the class is reused for styling elsewhere -
                        less reliable as a unique locator.
    5. XPATH (relative, attribute-based) - Powerful (can traverse parent/sibling axes, match text),
                        but slower than CSS and more verbose. Use only when CSS can't express
                        the condition.
    6. TAG_NAME / XPATH (absolute) - Least preferred. TAG_NAME matches many elements (not unique).
                        Absolute XPath breaks the instant any ancestor element is added, removed,
                        or reordered in the HTML structure - the most brittle of all strategies.
    """
    pass


if __name__ == "__main__":
    driver = get_driver()
    try:
        test_all_locator_strategies(driver)
        test_css_selectors(driver)
        test_checkbox_xpath_text(driver)
        locator_ranking()
    finally:
        driver.quit()