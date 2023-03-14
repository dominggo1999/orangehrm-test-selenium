import time
import unittest
from selenium import webdriver
from support.commands import should_include_login_page_url
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage
from config.credentials import VALID_PASSWORD


class ResetPassword (unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.login_page = LoginPage(self.browser)
        self.reset_password_page = ResetPasswordPage(self.browser)

    def tearDown(self):
        self.browser.quit()

    # A_04_001
    def redirect_to_reset_password_page(self):
        self.login_page.visit()
        time.sleep(2)
        self.login_page.forgotPasswordLink().click()
        time.sleep(2)
        assert self.reset_password_page.url in self.browser.current_url

    # A_04_002
    def cancel_reset_password(self):
        self.login_page.visit()
        time.sleep(2)
        self.login_page.forgotPasswordLink().click()
        time.sleep(2)
        self.reset_password_page.cancel_button().click()
        time.sleep(2)
        should_include_login_page_url(self.browser)

    # A_04_003
    def valid_username(self):
        self.reset_password_page.visit()
        time.sleep(2)
        self.reset_password_page.username_field().send_keys(VALID_PASSWORD)
        self.reset_password_page.reset_password_button().click()
        time.sleep(1)
        assert self.reset_password_page. success_message_title(
        ).text == "Reset Password link sent successfully", "Error message is incorrect"

    # A_04_004
    def blank_username(self):
        self.reset_password_page.visit()
        time.sleep(2)
        self.reset_password_page.reset_password_button().click()
        time.sleep(1)
        self.reset_password_page.username_error_msg().is_displayed()
        assert self.reset_password_page. success_message_title(
        ).text != "Reset Password link sent successfully", "Error message is incorrect"
