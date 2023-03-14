import time
import unittest
from selenium import webdriver
from support.commands import loginWith, should_include_login_page_url
from config.credentials import VALID_PASSWORD, VALID_USERNAME, INVALID_PASSWORD, INVALID_USERNAME
from pages.login_page import LoginPage


class FailedLogin (unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.login_page = LoginPage(self.browser)

    def tearDown(self):
        self.browser.quit()

    # A_02_001
    def invalid_username(self):
        loginWith(self.browser, INVALID_USERNAME, VALID_PASSWORD)
        should_include_login_page_url(self.browser)
        time.sleep(2)
        self.login_page.invalidCredentialsMsg().is_displayed()

    # A_02_002
    def invalid_password(self):
        loginWith(self.browser, VALID_USERNAME, INVALID_PASSWORD)
        should_include_login_page_url(self.browser)
        time.sleep(2)
        self.login_page.invalidCredentialsMsg().is_displayed()

    # A_02_003
    def blank_username_and_password(self):
        loginWith(self.browser, "", "")
        should_include_login_page_url(self.browser)
        time.sleep(2)
        self.login_page.usernameErrorMsg().is_displayed()
        self.login_page.passwordErrorMsg().is_displayed()

    # A_02_004
    def valid_username_blank_password(self):
        loginWith(self.browser, VALID_USERNAME, "")
        should_include_login_page_url(self.browser)
        time.sleep(2)
        self.login_page.passwordErrorMsg().is_displayed()

    # A_02_005
    def blank_username_valid_password(self):
        loginWith(self.browser, "", VALID_PASSWORD)
        should_include_login_page_url(self.browser)
        time.sleep(2)
        self.login_page.usernameErrorMsg().is_displayed()


if __name__ == "__main__":
    unittest.main()
