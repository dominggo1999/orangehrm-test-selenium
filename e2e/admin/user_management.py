import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from support.commands import login, logout, select_option, fill_auto_complete, login_with, clear_input
from pages.admin.users_page import UsersPage
from pages.admin.add_user_page import AddUserPage
from pages.admin.edit_user_page import EditUserPage
from pages.dashboard_page import DashboardPage
from sections.toast_section import ToastSection
from sections.header_section import HeaderSection
from shortuuid import uuid
from selenium.webdriver.common.keys import Keys


class UserManagement(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.users_page = UsersPage(self.browser)
        self.add_user_page = AddUserPage(self.browser)
        self.edit_user_page = EditUserPage(self.browser)
        self.dashboard_page = DashboardPage(self.browser)
        self.toast_section = ToastSection(self.browser)
        self.header_section = HeaderSection(self.browser)

    def tearDown(self):
        self.browser.quit()

    def beforeEach(self):
        login(self.browser)
        time.sleep(2)

        self.users_page.visit()
        time.sleep(2)

    # ADM_02_001
    def display_users_table(self):
        self.beforeEach()

        self.users_page.user_table()

        # The first column is a checkbox, we don't need that
        table_titles = self.users_page.user_table_header().find_elements(
            By.CSS_SELECTOR, ".oxd-table-header-cell:not(:first-child)")

        for item in table_titles:
            assert item.text in self.users_page.displayed_user_data

    # ADM_03_002
    def display_user_filter(self):
        self.beforeEach()

        self.users_page.user_filter()
        self.users_page.username_field()
        self.users_page.user_role_options()
        self.users_page.employee_name_autocomplete()
        self.users_page.status_field()

    # ADM_03_003
    def add_new_user(self):
        self.beforeEach()

        USERNAME = "a_new_username_" + uuid()
        PASSWORD = "Secure_password_123"
        CURRENT_USER = self.header_section.active_user_name().text

        # Navigate to AddUser page
        self.users_page.add_user_button().click()
        time.sleep(2)

        # Fill all fields

        # Options
        select_option(
            self.browser, self.add_user_page.user_role_options(), "ESS")

        time.sleep(2)

        select_option(
            self.browser, self.add_user_page.status_options(), "Enabled")

        # Autocomplete fields
        fill_auto_complete(
            self.browser, self.add_user_page.employee_name_autocomplete(), CURRENT_USER)

        # Normal input
        self.add_user_page.username_field().send_keys(USERNAME)
        self.add_user_page.password_field().send_keys(PASSWORD)
        self.add_user_page.confirm_password_field().send_keys(PASSWORD)

        time.sleep(1)

        # Submit
        self.add_user_page.submit()

        time.sleep(3)

        # Should displaying success message
        self.toast_section.success()

        # Should back to the users page
        assert self.add_user_page.url in self.browser.current_url

        # TODO
        # Should display the new user

        # Logout
        logout(self.browser)

        time.sleep(2)

        # Try login with newly created user
        login_with(self.browser, USERNAME, PASSWORD)

        assert self.dashboard_page.url in self.browser.current_url

    # ADM_02_004
    def add_user_blank_data(self):
        self.beforeEach()

        self.users_page.add_user_button().click()
        time.sleep(2)

        self.add_user_page.submit()
        time.sleep(1)

        error = self.browser.find_elements(
            By.CSS_SELECTOR, "span.oxd-input-field-error-message")
        assert len(error) == 6

    # ADM_02_005
    def cancel_add_user(self):
        self.beforeEach()

        # Navigate to AddUser page
        self.users_page.add_user_button().click()
        time.sleep(2)

        # Cancel
        self.add_user_page.cancel()

        assert self.users_page.url in self.browser.current_url

    # ADM_02_006
    def edit_user(self):
        self.beforeEach()
        USERNAME = "a_new_username_" + uuid()

        # Navigate to AddUser page
        self.users_page.edit_last_user_row()
        time.sleep(2)

        # Edit fields

        clear_input(self.edit_user_page.username_field())

        self.edit_user_page.username_field().send_keys(USERNAME)

        time.sleep(1)

        # Click save
        self.edit_user_page.submit()
        time.sleep(2)

        self.toast_section.success()

        # TODO
        # Should display the updated user data in the user table

    # ADM_02_007
    def edit_user_blank_data(self):
        self.beforeEach()

        # Navigate to AddUser page
        self.users_page.edit_last_user_row()
        time.sleep(2)

        # Make fields empty

        # Options
        select_option(
            self.browser, self.add_user_page.user_role_options(), "")

        time.sleep(2)

        select_option(
            self.browser, self.add_user_page.status_options(), "")

        clear_input(self.edit_user_page.username_field())

        # Click save
        self.edit_user_page.submit()
        time.sleep(2)

        error = self.browser.find_elements(
            By.CSS_SELECTOR, "span.oxd-input-field-error-message")

        assert len(error) == 3

    # ADM_02_008
    def cancel_edit(self):
        self.beforeEach()

        # Cancel edit user
        self.users_page.edit_last_user_row()
        time.sleep(1)

        # Cancel
        self.edit_user_page.cancel()
        time.sleep(1)

        assert self.users_page.url in self.browser.current_url

    # ADM_02_009
    def delete_user(self):
        self.beforeEach()
        deletedUserUsername = self.users_page.last_user_username().text

        self.users_page.delete_last_user_row()
        time.sleep(1)

        self.users_page.confirm_delete()
        time.sleep(2)

        self.toast_section.success()

        time.sleep(4)
        # check that the deleted user is not in the table
        self.assertNotIn(
            deletedUserUsername, self.users_page.user_table_body().text)

    # ADM_02_010
    def cancel_delete_user(self):
        self.beforeEach()
        deletedUserUsername = self.users_page.last_user_username().text

        self.users_page.delete_last_user_row()
        time.sleep(1)

        self.users_page.cancel_delete()

        # Should not remove user from table
        self.assertIn(
            deletedUserUsername, self.users_page.user_table_body().text)

    # ADM_02_011
    def filter_user(self):
        self.beforeEach()

        CURRENT_USER = self.header_section.active_user_name().text

        # Normal input
        self.users_page.username_field().send_keys("Admin")

        # Options

        # Options
        select_option(
            self.browser, self.users_page.user_role_options(), "Admin")

        time.sleep(2)

        select_option(
            self.browser, self.users_page.status_field(), "Enabled")

        # Autocomplete fields
        # Autocomplete fields
        fill_auto_complete(
            self.browser, self.users_page.employee_name_autocomplete(), CURRENT_USER)

        time.sleep(1)

        self.users_page.apply_filter()

        time.sleep(3)

        self.assertEqual(len(self.users_page.user_table_rows()), 1)

        # check that the user table contains the expected text
        user_table_text = self.users_page.user_table_body().text

        self.assertIn("Admin", user_table_text)
        self.assertIn(CURRENT_USER, user_table_text)

      # ADM_02_012
    def reset_user_filter(self):
        self.beforeEach()

        CURRENT_USER = self.header_section.active_user_name().text

        # Normal input
        self.users_page.username_field().send_keys("Admin")

        # Options
        select_option(
            self.browser, self.users_page.user_role_options(), "Admin")

        time.sleep(2)

        select_option(
            self.browser, self.users_page.status_field(), "Enabled")

        # Autocomplete fields
        fill_auto_complete(
            self.browser, self.users_page.employee_name_autocomplete(), CURRENT_USER)

        time.sleep(1)

        self.users_page.apply_filter()

        time.sleep(2)

        self.users_page.reset_filter()

        time.sleep(2)

        self.assertNotEqual(len(self.users_page.user_table_rows()), 1)
