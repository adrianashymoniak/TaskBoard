from datetime import datetime

from selene.conditions import text

from e2etests.domain.user import User
from e2etests.pages.signup_page import SignUpPage
from e2etests.tests.test_base import BaseTest
from e2etests.util.sql_helper import SQLHelper


class UserCanSignup(BaseTest):
    user_signing_up = None

    def setUp(self):
        super(UserCanSignup, self).setUp()
        UserCanSignup.user_signing_up = User((datetime.utcnow().strftime("%m-%d-%Y_%H.%M_%S") + '_adminaccount'),
                                             'admin123', email='testemail@email.com',
                                             password_confirm='admin123')

    def test_user_can_signup(self):
        (SignUpPage
         .open()
         .signup_as(UserCanSignup.user_signing_up)
         .greeting()
         .assure(text(UserCanSignup.user_signing_up.username)))

    def tearDown(self):
        SQLHelper.delete_user(UserCanSignup.user_signing_up)
