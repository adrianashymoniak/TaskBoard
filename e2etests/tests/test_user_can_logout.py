from e2etests.tests.test_base import BaseTest


class UserCanLogout(BaseTest):
    def test_user_can_logout(self):
        is_signup_link_displayed = (self.login_as(self.get_first_test_user()).logout().is_signup_link_displayed())

        self.assertTrue(is_signup_link_displayed, "User is not logged out")
