from selene.conditions import text

from e2etests.pages.login_page import LoginPage
from e2etests.tests.test_base import BaseTest


class UserCanLogin(BaseTest):
    def test_user_can_login(self):
        greeting = (LoginPage
                    .open()
                    .login_as(self.get_first_test_user())
                    .read_greeting())

        self.assertIn(self.get_first_test_user().username, greeting, 'Greeting does not contain username')
