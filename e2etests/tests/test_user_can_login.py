from selene.conditions import text

from e2etests.pages.login_page import LoginPage
from e2etests.tests.test_base import BaseTest


class UserCanLogin(BaseTest):
    def test_user_can_login(self):
        (LoginPage
         .open()
         .login_as(self.get_user())
         .greeting()
         .assure(text(self.get_user().username)))
