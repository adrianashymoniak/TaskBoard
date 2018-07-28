from e2etests.pages.login_page import LoginPage
from e2etests.tests.test_base import BaseTest


class UserCanSeePageNotFoundError(BaseTest):
    def test_user_can_see_page_not_found_error(self):
        user = self.get_first_test_user()

        LoginPage.open().login_as(user)
        actual_error_message = self.open_incorrect_url('/creates').read_error_message()

        expected_error_message = 'No such page. Please go to Home page!'
        self.assertObjectsEqual(expected_error_message, actual_error_message,
                                'Error message is not displayed after incorrect redirection')
