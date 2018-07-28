from e2etests.pages.login_page import LoginPage
from e2etests.tests.test_base import BaseTest


class UserCanDeleteOwnAccount(BaseTest):
    def test_user_can_delete_own_account(self):
        test_user = self.get_third_test_user()

        sign_up_link = (LoginPage.open()
                        .login_as(test_user)
                        .open_view_profile()
                        .click_delete_user_account()
                        .confirm_deleting_account()
                        .is_signup_link_displayed())

        self.assertTrue(sign_up_link, "User not deleted")
