import unittest
from e2e.auth.successful_login import SuccessfulLogin
from e2e.auth.failed_login import FailedLogin
from e2e.auth.log_out import Logout
from e2e.auth.reset_password import ResetPassword
from e2e.auth.protected_route import ProtectedRoute
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
    # Successful login
    suite.addTest(SuccessfulLogin("valid_username_and_password"))

    # Failed login
    suite.addTest(FailedLogin("invalid_username"))
    suite.addTest(FailedLogin("invalid_password"))
    suite.addTest(FailedLogin("blank_username_and_password"))
    suite.addTest(FailedLogin("valid_username_blank_password"))
    suite.addTest(FailedLogin("blank_username_valid_password"))

    # Logout
    suite.addTest(Logout("log_out"))

    # Reset password
    suite.addTest(ResetPassword("redirect_to_reset_password_page"))
    suite.addTest(ResetPassword("cancel_reset_password"))
    suite.addTest(ResetPassword("valid_username"))
    suite.addTest(ResetPassword("blank_username"))

    # Route Protection
    suite.addTest(ProtectedRoute("protect_dashboard_page"))

    runner = unittest.TextTestRunner()
    results = runner.run(suite)

    # Check if there were any failures and return non-zero exit status code
    # This is to ensure that Github Actions fails the build when there are failing tests
    if is_running_on_github_actions and results.failures:
        sys.exit(1)
