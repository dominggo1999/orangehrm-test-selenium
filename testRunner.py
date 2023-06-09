import unittest

# Auth (A)
from e2e.auth.successful_login import SuccessfulLogin
from e2e.auth.failed_login import FailedLogin
from e2e.auth.log_out import Logout
from e2e.auth.reset_password import ResetPassword
from e2e.auth.route_protection import RouteProtection

# Sidebar (SB)
from e2e.sidebar import Sidebar

# Admin (ADM)
from e2e.admin.open_admin_page import OpenAdminPage
from e2e.admin.user_management import UserManagement

import chromedriver_autoinstaller
import os
import sys


# Check if running on Github Actions
is_running_on_github_actions = os.getenv('GITHUB_ACTIONS') == 'true'

# If running on Github Actions, start virtual display
if is_running_on_github_actions:
    from pyvirtualdisplay import Display
    display = Display(visible=0, size=(1200, 1200))
    display.start()


chromedriver_autoinstaller.install()

if __name__ == "__main__":
    suite = unittest.TestSuite()

    # AUTH
    # Add successful login tests
    successful_login_tests = [SuccessfulLogin("valid_username_and_password")]

    # Add failed login tests
    failed_login_tests = [
        FailedLogin("invalid_username"),
        FailedLogin("invalid_password"),
        FailedLogin("blank_username_and_password"),
        FailedLogin("valid_username_blank_password"),
        FailedLogin("blank_username_valid_password")
    ]

    # Add logout tests
    logout_tests = [Logout("log_out")]

    # Add reset password tests
    reset_password_tests = [
        ResetPassword("redirect_to_reset_password_page"),
        ResetPassword("cancel_reset_password"),
        ResetPassword("valid_username"),
        ResetPassword("blank_username")
    ]

    # Add route protection tests
    protected_route_tests = [RouteProtection("protect_dashboard_page")]

    # Add all the tests to the suite using addTests
    suite.addTests(successful_login_tests)
    suite.addTests(failed_login_tests)
    suite.addTests(logout_tests)
    suite.addTests(reset_password_tests)
    suite.addTests(protected_route_tests)

    # SIDEBAR
    sidebar = [
        Sidebar("sidebar_is_visible_on_large_screen"),
        Sidebar("toggling_sidebar_on_large_screen_size"),
        Sidebar("all_links_work_properly"),
        Sidebar("sidebar_search_valid_value"),
        Sidebar("sidebar_search_invalid_value"),
    ]

    suite.addTests(sidebar)

    # Admin
    open_admin_page = [OpenAdminPage("admin_link_redirection")]
    user_management = [
        UserManagement("display_users_table"),
        UserManagement("display_user_filter"),
        UserManagement("add_new_user"),
        UserManagement("add_user_blank_data"),
        UserManagement("cancel_add_user"),
        UserManagement("edit_user"),
        UserManagement("edit_user_blank_data"),
        UserManagement("cancel_edit"),
        UserManagement("delete_user"),
        UserManagement("cancel_delete_user"),
        UserManagement("filter_user"),
        UserManagement("reset_user_filter"),
    ]

    suite.addTests(open_admin_page)
    suite.addTests(user_management)

    runner = unittest.TextTestRunner()
    results = runner.run(suite)

    # Check if there were any failures and return non-zero exit status code
    # This is to ensure that Github Actions fails the build when there are failing tests
    if is_running_on_github_actions and (results.failures or results.errors):
        sys.exit(1)
