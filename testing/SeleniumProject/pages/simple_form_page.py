"""
SimpleFormPage - encapsulates locators and actions for the Simple Form Demo page.

Golden rule of POM: this file performs ACTIONS and returns VALUES.
It contains NO assert statements - assertions belong only in test files.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SimpleFormPage(BasePage):
    # Locators as class-level tuples - never hardcoded inside methods
    MESSAGE_INPUT = (By.ID, "user-message")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[onclick='showInput()']")
    DISPLAYED_MESSAGE = (By.ID, "message")

    def enter_message(self, text):
        message_box = self.wait_for_element(self.MESSAGE_INPUT)
        message_box.clear()
        message_box.send_keys(text)

    def click_submit(self):
        submit_btn = self.wait_for_clickable(self.SUBMIT_BUTTON)
        submit_btn.click()

    def get_displayed_message(self):
        displayed = self.wait_for_element(self.DISPLAYED_MESSAGE)
        return displayed.text