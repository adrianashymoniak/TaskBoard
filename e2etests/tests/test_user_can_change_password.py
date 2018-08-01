from e2etests.domain.user import User
from e2etests.pages.view_profile_page import ViewProfilePage
from e2etests.tests.test_base import BaseTest
from e2etests.util.sql_helper import SQLHelper


class UserCanChangePassword(BaseTest):
    def test_user_can_change_password(self):
        self.test_user = self.get_first_test_user()
        new_password = 'qazwsx123'

        username = (self.login_as(self.test_user)
                    .open_change_password()
                    .fill_new_password(self.test_user.password, new_password)
                    .navigate_to_home_page()
                    .discard_leaving()
                    .change_password()
                    .read_user_name()
                    )

        self.assertEqual(self.test_user.username, username, "User is logged out")

        ViewProfilePage().logout()

        user_with_changed_password = User(username=self.test_user.username, password=new_password)

        greeting = self.login_as(user_with_changed_password).read_greeting()

        self.assertIn(user_with_changed_password.username, greeting, "User not logged in")

    def tearDown(self):
        super(UserCanChangePassword, self).tearDown()
        SQLHelper.change_user_password(self.test_user)
