# This project is mimicking how cypress can create a reusable commands
import time
from selenium import webdriver
from config.credentials import VALID_USERNAME, VALID_PASSWORD
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from sections.header_section import HeaderSection
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def login_with(browser: webdriver.Chrome, username, password):
    login_page = LoginPage(browser)

    # visit the login page
    login_page.visit()

    # enter the username and password
    if username:
        login_page.usernameField().send_keys(username)

    if password:
        login_page.passwordField().send_keys(password)

    # click the login button
    login_page.submit()


def login(browser: webdriver.Chrome):
    login_with(browser, VALID_USERNAME, VALID_PASSWORD)


def should_include_login_page_url(browser: webdriver.Chrome):
    login_page = LoginPage(browser)
    assert login_page.url in browser.current_url


def logout(browser: webdriver.Chrome):
    header_section = HeaderSection(browser)
    header_section.logout()


def select_option(browser: webdriver.Chrome, wrapper: WebElement, value: str):
    try:
        # For some reasons clicking the wrapper will throw an error
        wrapper.click()

        # Get options
        options = wrapper.find_elements(
            By.CSS_SELECTOR, '[role="listbox"] div')

        # Click on the first option
        if options:
            for option in options:
                if option.text.strip() == value.strip():
                    wait = WebDriverWait(browser, 10)
                    wait.until(EC.element_to_be_clickable(option))
                    option.click()
                    break

            options[0].click()
    except:
        pass


def fill_auto_complete(browser: webdriver.Chrome, wrapper: WebElement, value: str):
    input = wrapper.find_element(By.CSS_SELECTOR, "input")
    input.send_keys(value)

    time.sleep(5)

    # Get options
    options = wrapper.find_elements(
        By.CSS_SELECTOR, '[role="listbox"] div')

    # Click on the first option
    if options:
        options[0].click()


def scroll_to_top(browser: webdriver.Chrome):
    # Scroll to the top of the page
    body = browser.find_element_by_tag_name("body")
    body.send_keys(Keys.CONTROL + Keys.HOME)


# For clearing input or text area
def clear_input(element: WebElement):
    element.send_keys(Keys.CONTROL + "a")
    element.send_keys(Keys.DELETE)
