from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver


class ToastSection():
    def __init__(self, browser: WebDriver):
        self.browser = browser

    def container(self) -> WebElement:
        return self.browser.find_element(
            By.CSS_SELECTOR, ".oxd-toast-container")

    def success(self) -> WebElement:
        return self.container().find_element(
            By.CSS_SELECTOR, ".oxd-toast--success")

    def warn(self) -> WebElement:
        return self.container().find_element(
            By.CSS_SELECTOR, ".oxd-toast--warn")

    def error(self) -> WebElement:
        return self.container().find_element(
            By.CSS_SELECTOR, ".oxd-toast--error")

    def info(self) -> WebElement:
        return self.container().find_element(
            By.CSS_SELECTOR, ".oxd-toast--info")
