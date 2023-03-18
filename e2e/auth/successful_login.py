import unittest
from selenium import webdriver
from support.commands import login_with
from config.credentials import VALID_PASSWORD, VALID_USERNAME


class SuccessfulLogin (unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()

    def tearDown(self):
        self.browser.quit()

    # A_01_001
    def valid_username_and_password(self):
        login_with(self.browser, VALID_USERNAME, VALID_PASSWORD)
        assert "/dashboard" in self.browser.current_url


if __name__ == "__main__":
    unittest.main()
