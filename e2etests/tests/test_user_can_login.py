from selene.conditions import text

from e2etests.domain.user import User
from e2etests.pages.login_page import LoginPage
from e2etests.tests.test_base import BaseTest


class UserCanLogin(BaseTest):
    def test_user_can_login(self):
        user = User('adriana', 'admin123456')
        (LoginPage
         .open()
         .login_as(user)
         .greeting()
         .assure(text(user.username)))
