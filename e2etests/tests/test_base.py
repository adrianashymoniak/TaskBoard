from unittest import TestCase

from selene import browser
from selene import config
from selene.browsers import BrowserName

from e2etests.configs import BASE_URL
from e2etests.domain.user import User
from e2etests.util.sql_helper import SQLHelper


class BaseTest(TestCase):
    def setUp(self):
        config.browser_name = BrowserName.CHROME
        config.base_url = BASE_URL

    def tearDown(self):
        browser.close()

    user = None

    def get_user(self):
        if BaseTest.user is None:
            user = User('admin', 'qazwsx123456')
            SQLHelper.create_user_if_not_present(user)
            BaseTest.user = user
        return BaseTest.user
