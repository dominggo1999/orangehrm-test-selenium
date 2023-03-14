# This project is mimicking how cypress can create a reusable commands
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.credentials import VALID_USERNAME, VALID_PASSWORD


def loginWith(browser: webdriver.Chrome, username, password):
    # visit the login page
    browser.get(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # wait for the username input field to appear
    wait = WebDriverWait(browser, 10)
    username_input = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ":nth-child(2) > .oxd-input-group > :nth-child(2) > .oxd-input")))

    # enter the username and password
    username_input.send_keys(username)

    password_input = browser.find_element(
        By.CSS_SELECTOR, ":nth-child(3) > .oxd-input-group > :nth-child(2) > .oxd-input")
    password_input.send_keys(password)

    # click the login button
    login_button = browser.find_element(By.CSS_SELECTOR, ".oxd-button")
    login_button.click()


def login(browser: webdriver.Chrome):
    loginWith(browser, VALID_USERNAME, VALID_PASSWORD)
