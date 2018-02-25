from datetime import datetime

from e2etests.domain.user import User
from e2etests.pages.signup_page import SignUpPage
from e2etests.tests.test_base import BaseTest
from e2etests.util.sql_helper import SQLHelper


class UserCanSignup(BaseTest):
    def setUp(self):
        super(UserCanSignup, self).setUp()
        self.user_signing_up = User((datetime.utcnow().strftime("%m-%d-%Y_%H.%M_%S") + '_adminaccount'),
                                    'admin123', email='testemail@email.com',
                                    password_confirm='admin123')

    def test_user_can_signup(self):
        greeting = (SignUpPage
                    .open()
                    .signup_as(self.user_signing_up)
                    .read_greeting())
        self.assertIn(self.user_signing_up.username, greeting, 'Greeting does not contain username')

    def tearDown(self):
        SQLHelper.delete_user(self.user_signing_up)
