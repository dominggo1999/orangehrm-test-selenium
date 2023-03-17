from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils.create_target_url import create_target_url


class AddUserPage:
    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.url = create_target_url("/admin/saveSystemUser")

    def user_role_options(self):
        return self.browser.find_element(By.CSS_SELECTOR, ":nth-child(1) > .oxd-input-group > :nth-child(2) > .oxd-select-wrapper")

    def employee_name_autocomplete(self):
        return self.browser.find_element(By.CSS_SELECTOR, ":nth-child(1) > .oxd-grid-2 > :nth-child(2) > .oxd-input-group .oxd-autocomplete-wrapper")

    def status_options(self):
        return self.browser.find_element(By.CSS_SELECTOR, ":nth-child(3) > .oxd-input-group > :nth-child(2) > .oxd-select-wrapper")

    def username_field(self):
        return self.browser.find_element(By.CSS_SELECTOR, ":nth-child(4) > .oxd-input-group > :nth-child(2) > .oxd-input")

    def password_field(self):
        return self.browser.find_element(By.CSS_SELECTOR, ".user-password-cell > .oxd-input-group > :nth-child(2) > .oxd-input")

    def confirm_password_field(self):
        return self.browser.find_element(By.CSS_SELECTOR, ":nth-child(2) > .oxd-input-group > :nth-child(2) > .oxd-input")

    def save_button(self):
        return self.browser.find_element(By.CSS_SELECTOR, ".oxd-button--secondary")

    def cancel_button(self):
        return self.browser.find_element(By.CSS_SELECTOR, ".oxd-button--ghost")

    def visit(self):
        self.browser.get(self.url)

    def submit(self):
        self.save_button().click()

    def cancel(self):
        self.cancel_button().click()
