from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from utils.create_target_url import create_target_url


class DashboardPage():
    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.url = create_target_url("/dashboard/index")

    def visit(self):
        self.browser.get(self.url)

    def profile_button(self) -> WebElement:
        return self.browser.find_element(
            By.CSS_SELECTOR, ".oxd-userdropdown-tab")

    def logout_button(self) -> WebElement:
        return self.browser.find_element(
            By.CSS_SELECTOR, ":nth-child(4) > .oxd-userdropdown-link")
