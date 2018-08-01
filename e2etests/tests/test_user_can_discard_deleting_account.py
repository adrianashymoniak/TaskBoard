from e2etests.tests.test_base import BaseTest


class UserCanDiscardDeletingAccount(BaseTest):
    def test_user_can_discard_deleting_account(self):
        test_user = self.get_first_test_user()

        username = (self.login_as(test_user)
                    .open_view_profile()
                    .click_delete_user_account()
                    .discard_deleting_account()
                    .read_user_name())

        self.assertIn(test_user.username, username, 'User account was deleted')
