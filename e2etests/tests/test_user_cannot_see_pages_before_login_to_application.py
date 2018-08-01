from e2etests.tests.test_base import BaseTest


class UserCannotSeePagesBeforeLoginToApplication(BaseTest):
    def test_user_cannot_see_pages_before_login_to_application(self):
        self.open_login_page()

        actual_error_message = self.open_incorrect_url('/delete_all_tasks').read_error_message()

        expected_error_message = 'You should be logged in to see that page. Please go to Login page or to Sign up page!'

        self.assertEqual(expected_error_message, actual_error_message,
                         'Error message is not displayed after incorrect redirection')
