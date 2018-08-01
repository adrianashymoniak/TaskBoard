from e2etests.tests.test_base import BaseTest


class UserCanDiscardChangingPasswordProcess(BaseTest):
    def test_user_can_discard_changing_password_process(self):
        test_user = self.get_first_test_user()
        new_password = 'qazwsx123'

        home_page = (self.login_as(test_user)
                     .open_change_password()
                     .fill_new_password(test_user.password, new_password)
                     .navigate_to_home_page()
                     .confirm_leaving_to_home_page())

        self.assertTrue((home_page.is_opened()), 'Home page is not opened')
