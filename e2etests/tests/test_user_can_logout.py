from e2etests.pages.login_page import LoginPage
from e2etests.tests.test_base import BaseTest


class UserCanLogout(BaseTest):
    def test_user_can_logout(self):
        link = (LoginPage
                .open()
                .login_as(self.get_first_test_user())
                .logout()
                .is_signup_link_displayed())

        self.assertTrue(link, "User not logged out")
