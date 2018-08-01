from e2etests.tests.test_base import BaseTest


class UserCanDiscardEditingProfile(BaseTest):
    def test_user_can_discard_editing_profile(self):
        test_user = self.get_user_to_enter()

        home_page = (self.login_as(self.get_first_test_user())
                     .open_edit_profile()
                     .fill_new_profile_information(test_user)
                     .navigate_to_home_page()
                     .confirm_leaving_to_home_page())

        self.assertTrue((home_page.is_opened()), 'Home page is not opened')
