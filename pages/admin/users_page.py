from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils.create_target_url import create_target_url
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List


class UsersPage:
    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.url = create_target_url("/admin/viewSystemUsers")
        self.displayed_user_data = [
            "Username",
            "User Role",
            "Employee Name",
            "Status",
            "Actions",
        ]

    def user_table(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR, ".oxd-table")

    def user_table_header(self) -> WebElement:
        return self.user_table().find_element(By.CSS_SELECTOR, ".oxd-table-header")

    def user_table_body(self) -> WebElement:
        wait = WebDriverWait(self.browser, 10)

        return wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".oxd-table-body")))

    def user_filter(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR, ".oxd-table-filter")

    def username_field(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR, ":nth-child(2) > .oxd-input")

    def user_role_options(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR, ":nth-child(2) > .oxd-input-group > :nth-child(2) > .oxd-select-wrapper")

    def employee_name_autocomplete(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR, ".oxd-autocomplete-wrapper")

    def status_field(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR, ":nth-child(4) > .oxd-input-group > :nth-child(2) > .oxd-select-wrapper")

    def add_user_button(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR, ".orangehrm-header-container > .oxd-button")

    def user_table_rows(self) -> List[WebElement]:
        return self.user_table().find_elements(By.CSS_SELECTOR, ".oxd-table-card")

    def last_user_row(self) -> WebElement:
        return self.user_table_body().find_element(By.CSS_SELECTOR, ".oxd-table-card:last-child")

    def last_user_username(self) -> WebElement:
        return self.user_table_body().find_element(By.CSS_SELECTOR, ".oxd-table-card:last-child .oxd-table-cell:nth-of-type(2)")

    def delete_user_confirm_button(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR, ".oxd-dialog-container-default--inner .oxd-button--label-danger")

    def delete_user_cancel_button(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR, ".oxd-dialog-container-default--inner .oxd-button--text")

    def apply_filter_button(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR, ".oxd-form-actions > .oxd-button--secondary")

    def reset_filter_button(self) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR, ".oxd-button--ghost")

    def visit(self):
        self.browser.get(self.url)

    def edit_last_user_row(self) -> WebElement:
        self.last_user_row().find_element(
            By.CSS_SELECTOR, ".oxd-table-cell-actions button:nth-of-type(2)").click()

    def delete_last_user_row(self) -> WebElement:
        self.last_user_row().find_element(
            By.CSS_SELECTOR, ".oxd-table-cell-actions button:nth-of-type(1)").click()

    def cancel_delete(self):
        self.delete_user_cancel_button().click()

    def confirm_delete(self):
        self.delete_user_confirm_button().click()

    def apply_filter(self):
        self.apply_filter_button().click()

    def reset_filter(self):
        self.reset_filter_button().click()
