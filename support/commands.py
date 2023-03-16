# This project is mimicking how cypress can create a reusable commands
import time
from selenium import webdriver
from config.credentials import VALID_USERNAME, VALID_PASSWORD
from pages.login_page import LoginPage


def loginWith(browser: webdriver.Chrome, username, password):
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
    loginWith(browser, VALID_USERNAME, VALID_PASSWORD)


def should_include_login_page_url(browser: webdriver.Chrome):
    login_page = LoginPage(browser)
    assert login_page.url in browser.current_url
