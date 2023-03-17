from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver


class HeaderSection():
    def __init__(self, browser: WebDriver):
        self.browser = browser

    def hamburger_icon(self) -> WebElement:
        return self.browser.find_element(
            By.CSS_SELECTOR, ".oxd-topbar-header .oxd-topbar-header-hamburger")

    def profile_button(self) -> WebElement:
        return self.browser.find_element(
            By.CSS_SELECTOR, ".oxd-userdropdown-tab")

    def logout_button(self) -> WebElement:
        return self.browser.find_element(
            By.CSS_SELECTOR, ":nth-child(4) > .oxd-userdropdown-link")

    def active_user_name(self) -> WebElement:
        return self.browser.find_element(
            By.CSS_SELECTOR, ".oxd-userdropdown-name")

    def hamburger_toggle(self):
        self.hamburger_icon().click()

    def logout(self):
        self.profile_button().click()
        self.logout_button().click()
