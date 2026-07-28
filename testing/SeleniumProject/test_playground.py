"""
Hands-On 6 - pytest-based Selenium tests for the Selenium Playground.
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


def test_simple_form_submission(driver, base_url):
    """Task 42: enter message, submit, assert displayed message."""
    driver.get(base_url + "simple-form-demo/")

    message_input = driver.find_element(By.ID, "user-message")
    message_input.send_keys("Hello Selenium")

    submit_btn = driver.find_element(By.CSS_SELECTOR, "input[onclick='showInput()']")
    submit_btn.click()

    displayed_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )
    assert displayed_message.text == "Hello Selenium"


def test_checkbox_demo(driver, base_url):
    """Task 43: check, assert selected, uncheck, assert deselected."""
    driver.get(base_url + "checkbox-demo/")

    checkbox = driver.find_element(By.XPATH, "//div[@id='multipleCheckbox']//input[1]")

    checkbox.click()
    assert checkbox.is_selected() is True

    checkbox.click()
    assert checkbox.is_selected() is False

@pytest.mark.parametrize("message", ["Hello", "Selenium Automation", "12345"])
def test_simple_form_submission_parametrized(driver, base_url, message):
    """Task 45: parameterised form submission - 3 separate test runs."""
    driver.get(base_url + "simple-form-demo/")

    message_input = driver.find_element(By.ID, "user-message")
    message_input.send_keys(message)

    submit_btn = driver.find_element(By.CSS_SELECTOR, "input[onclick='showInput()']")
    submit_btn.click()

    displayed_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )
    assert displayed_message.text == message


def test_dropdown_selection(driver, base_url):
    """Task 49: select 'Wednesday' from Select Dropdown List demo."""
    driver.get(base_url + "select-dropdown-demo/")

    dropdown_element = driver.find_element(By.ID, "select-demo")
    select = Select(dropdown_element)
    select.select_by_visible_text("Wednesday")

    selected_option = select.first_selected_option
    assert selected_option.text == "Wednesday"