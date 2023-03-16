from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from utils.create_target_url import create_target_url


class LoginPage():
    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.url = create_target_url("/auth/login")

    def visit(self):
        self.browser.get(self.url)

    def usernameField(self) -> WebElement:
        wait = WebDriverWait(self.browser, 10)
        return wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ":nth-child(2) > .oxd-input-group > :nth-child(2) > .oxd-input")))

    def usernameErrorMsg(self) -> WebElement:
        return self.browser.find_element(
            By.CSS_SELECTOR, ".orangehrm-login-form > form > div:nth-child(2) > div > span")

    def passwordField(self) -> WebElement:
        wait = WebDriverWait(self.browser, 10)
        return wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ":nth-child(3) > .oxd-input-group > :nth-child(2) > .oxd-input")))

    def passwordErrorMsg(self) -> WebElement:
        return self.browser.find_element(
            By.CSS_SELECTOR, ".orangehrm-login-form > form > div:nth-child(3) > div > span")

    def loginButton(self) -> WebElement:
        wait = WebDriverWait(self.browser, 10)

        return wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".oxd-button")))

    def forgotPasswordLink(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR, ".orangehrm-login-forgot > .oxd-text")

    def invalidCredentialsMsg(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR, ".oxd-alert-content > .oxd-text")

    def submit(self):
        self.loginButton().click()
