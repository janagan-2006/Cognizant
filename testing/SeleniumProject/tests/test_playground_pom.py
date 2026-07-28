"""
Hands-On 7 - Task 2: Fully POM-compliant test suite.
Zero driver.find_element calls appear in this file - all interaction logic
lives in the pages/ classes. This file only contains test setup and assertions.
"""

from pages.simple_form_page import SimpleFormPage
from pages.checkbox_page import CheckboxPage
from pages.dropdown_page import DropdownPage
from pages.input_form_page import InputFormPage


def test_simple_form_submission(driver, base_url):
    """Task 55: refactored to use SimpleFormPage."""
    page = SimpleFormPage(driver)
    page.navigate_to(base_url + "simple-form-demo/")
    page.enter_message("Hello Selenium")
    page.click_submit()

    assert page.get_displayed_message() == "Hello Selenium"


def test_checkbox_demo(driver, base_url):
    """Task 56: refactored to use CheckboxPage."""
    page = CheckboxPage(driver)
    page.navigate_to(base_url + "checkbox-demo/")

    page.check_option(1)
    assert page.is_option_checked(1) is True

    page.uncheck_option(1)
    assert page.is_option_checked(1) is False


def test_dropdown_selection(driver, base_url):
    """Task 56: refactored to use DropdownPage."""
    page = DropdownPage(driver)
    page.navigate_to(base_url + "select-dropdown-demo/")

    page.select_day("Wednesday")
    assert page.get_selected_day() == "Wednesday"


def test_input_form_submit(driver, base_url):
    """Task 57: new test using InputFormPage."""
    page = InputFormPage(driver)
    page.navigate_to(base_url + "input-form-demo/")

    page.fill_form(
        name="Charles J",
        email="charles@example.com",
        phone="9876543210",
        address="Chennai, India"
    )
    page.submit_form()

    assert "successfully" in page.get_success_message().lower()