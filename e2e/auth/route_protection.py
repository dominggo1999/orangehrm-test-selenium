import unittest
from selenium import webdriver
from support.commands import should_include_login_page_url
from pages.dashboard_page import DashboardPage


class RouteProtection (unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.dashboard_page = DashboardPage(self.browser)

    def tearDown(self):
        self.browser.quit()

    # A_05_001
    def protect_dashboard_page(self):
        self.dashboard_page.visit()
        should_include_login_page_url(self.browser)
