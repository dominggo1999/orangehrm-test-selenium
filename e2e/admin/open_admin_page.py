import time
import unittest
from selenium import webdriver
from support.commands import login
from sections.sidebar_section import SidebarSection
from pages.admin.users_page import UsersPage


class OpenAdminPage(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.sidebar_section = SidebarSection(self.browser)
        self.users_page = UsersPage(self.browser)

    def tearDown(self):
        self.browser.quit()

    # ADM_01_001
    def admin_link_redirection(self):
        login(self.browser)

        # Wait for login to complete
        time.sleep(2)

        # Visit admin page
        self.users_page.visit()
        time.sleep(2)

        # Click Admin link in sidebar
        self.sidebar_section.click_link_with_text("Admin")

        # Verify users page URL is displayed
        assert self.users_page.url in self.browser.current_url
