from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from utils.create_target_url import create_target_url


class ResetPasswordPage():
    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.url = create_target_url("/auth/requestPasswordResetCode")

    def visit(self):
        self.browser.get(self.url)

    def cancel_button(self) -> WebElement:
        return self.browser.find_element(
            By.CSS_SELECTOR, ".oxd-button--ghost")

    def reset_password_button(self) -> WebElement:
        return self.browser.find_element(
            By.CSS_SELECTOR, ".oxd-button--secondary")

    def username_field(self) -> WebElement:
        return self.browser.find_element(
            By.CSS_SELECTOR, ".oxd-input")

    def username_error_msg(self) -> WebElement:
        return self.browser.find_element(
            By.CSS_SELECTOR, ".oxd-input-field-error-message")

    def success_message_title(self) -> WebElement:
        return self.browser.find_element(
            By.CSS_SELECTOR, ".oxd-text--h6")
