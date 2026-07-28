"""
CheckboxPage - encapsulates locators and actions for the Checkbox Demo page.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckboxPage(BasePage):
    CHECKBOX_OPTION = (By.XPATH, "//div[@id='multipleCheckbox']//input[{index}]")

    def _get_checkbox(self, index):
        locator = (By.XPATH, self.CHECKBOX_OPTION[1].format(index=index))
        return self.wait_for_element(locator)

    def check_option(self, index):
        checkbox = self._get_checkbox(index)
        if not checkbox.is_selected():
            checkbox.click()

    def uncheck_option(self, index):
        checkbox = self._get_checkbox(index)
        if checkbox.is_selected():
            checkbox.click()

    def is_option_checked(self, index):
        return self._get_checkbox(index).is_selected()