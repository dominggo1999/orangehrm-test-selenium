import time
from sections.sidebar_section import SidebarSection
import unittest
from selenium import webdriver
from support.commands import login
from config.routes import sidebar_links
from utils.create_target_url import create_target_url


class Sidebar (unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.sidebar_section = SidebarSection(self.browser)

    def tearDown(self):
        self.browser.quit()

    def is_sidebar_expanded(self):
        self.sidebar_section.sidebar().is_displayed()
        assert "toggled" not in self.sidebar_section.sidebar().get_attribute("class")

    def is_sidebar_collapsed(self):
        self.sidebar_section.sidebar().is_displayed()
        assert "toggled" in self.sidebar_section.sidebar().get_attribute("class")

    # SB_01_001
    def sidebar_is_visible_on_large_screen(self):
        login(self.browser)
        time.sleep(2)
        self.is_sidebar_expanded()

    # SB_01_002
    def toggling_sidebar_on_large_screen_size(self):
        login(self.browser)
        time.sleep(2)
        self.is_sidebar_expanded()

        # Close sidebar
        self.sidebar_section.toggle()
        self.is_sidebar_collapsed()
        time.sleep(1)

        # Open sidebar again
        self.sidebar_section.toggle()
        self.is_sidebar_expanded()

    # SB_01_003
    def all_links_work_properly(self):
        login(self.browser)
        time.sleep(2)
        link_texts = [link["text"].lower() for link in sidebar_links]
        link_paths = [link["path"] for link in sidebar_links]

        for link in self.sidebar_section.get_all_links():
            assert link.text.lower() in link_texts
            path = link.get_attribute("href")
            link_path = path.replace(create_target_url("/"), "/")
            assert link_path in link_paths

    # SB_01_004
    def sidebar_search_valid_value(self):
        login(self.browser)
        time.sleep(2)
        self.sidebar_section.search_field().send_keys("Admin")
        links = self.sidebar_section.get_all_links()
        assert len(links) == 1
        assert links[0].text == "Admin"

    # SB_01_005
    def sidebar_search_invalid_value(self):
        login(self.browser)
        time.sleep(2)
        self.sidebar_section.search_field().send_keys("invalid_search")
        links = self.sidebar_section.get_all_links()
        assert len(links) == 0


if __name__ == "__main__":
    unittest.main()
