from e2etests.tests.test_base import BaseTest


class UserCanLogin(BaseTest):
    def test_user_can_login(self):
        user = self.get_first_test_user()

        greeting = (self.login_as(user).read_greeting())

        self.assertIn(user.username, greeting, 'Greeting does not contain username')
