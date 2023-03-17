from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from typing import List


class SidebarSection():
    def __init__(self, browser: WebDriver):
        self.browser = browser

    def search_field(self) -> WebElement:
        return self.browser.find_element(
            By.CSS_SELECTOR, ".oxd-sidepanel-body .oxd-main-menu-search > input")

    def sidebar(self) -> WebElement:
        return self.browser.find_element(
            By.CSS_SELECTOR, ".oxd-sidepanel")

    def toggle_button(self) -> WebElement:
        return self.browser.find_element(
            By.CSS_SELECTOR, ".oxd-sidepanel-body > div > div > button")

    def get_all_links(self) -> List[WebElement]:
        return self.browser.find_elements(
            By.CSS_SELECTOR, ".oxd-sidepanel-body ul.oxd-main-menu a")

    def toggle(self):
        self.toggle_button().click()

    def click_link_with_text(self, text):
        self.sidebar().find_element(By.LINK_TEXT,
                                    text).click()
