import unittest
from e2e.auth.successful_login import SuccessfulLogin
from e2e.auth.failed_login import FailedLogin
from e2e.auth.log_out import Logout
from e2e.auth.reset_password import ResetPassword
from e2e.auth.route_protection import RouteProtection
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

    runner = unittest.TextTestRunner()
    results = runner.run(suite)

    # Check if there were any failures and return non-zero exit status code
    # This is to ensure that Github Actions fails the build when there are failing tests
    if is_running_on_github_actions and results.failures:
        sys.exit(1)
