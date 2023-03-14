import time
import unittest
from selenium import webdriver
from support.commands import login, should_include_login_page_url
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


class Logout (unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.login_page = LoginPage(self.browser)
        self.dashboard_page = DashboardPage(self.browser)

    def tearDown(self):
        self.browser.quit()

    # A_03_001
    def log_out(self):
        login(self.browser)
        time.sleep(2)
        self.dashboard_page.profile_button().click()
        self.dashboard_page.logout_button().click()
        time.sleep(2)
        should_include_login_page_url(self.browser)
