from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class EditUserPage:
    def __init__(self, browser: WebDriver):
        self.browser = browser

    def user_role_options(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR, ":nth-child(1) > .oxd-input-group > :nth-child(2) > .oxd-select-wrapper")

    def employee_name_autocomplete(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR, ":nth-child(1) > .oxd-grid-2 > :nth-child(2) > .oxd-input-group .oxd-autocomplete-wrapper")

    def status_options(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR, ":nth-child(3) > .oxd-input-group > :nth-child(2) > .oxd-select-wrapper")

    def username_field(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR, ":nth-child(4) > .oxd-input-group > :nth-child(2) > .oxd-input")

    def save_button(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR, ".oxd-button--secondary")

    def cancel_button(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR, ".oxd-button--ghost")

    def submit(self):
        self.save_button().click()

    def cancel(self):
        self.cancel_button().click()
