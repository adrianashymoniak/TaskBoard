from datetime import datetime

from e2etests.domain.user import User
from e2etests.pages.login_page import LoginPage
from e2etests.tests.test_base import BaseTest


class UserCanDiscardEditingProfile(BaseTest):
    def test_user_can_discard_editing_profile(self):
        test_user = User(username=self.get_first_test_user().username,
                         first_name=datetime.utcnow().strftime("%m-%d-%Y_%H.%M_%S") + 'First_name',
                         last_name='Last_name',
                         email='test@mail.com')

        home_page = (LoginPage
                     .open()
                     .login_as(self.get_first_test_user())
                     .open_profile_dropdown()
                     .open_edit_profile()
                     .fill_new_profile_information(test_user)
                     .navigate_to_home_page()
                     .confirm_leaving_to_home_page())

        self.assertTrue((home_page.is_opened()), 'Home page is not opened.')
