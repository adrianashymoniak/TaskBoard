from datetime import datetime, date
from unittest import TestCase

from selene import browser
from selene import config
from selene.browsers import BrowserName

from e2etests.configs import BASE_URL
from e2etests.domain.task import Task
from e2etests.domain.user import User
from e2etests.util.sql_helper import SQLHelper


class BaseTest(TestCase):
    def setUp(self):
        config.browser_name = BrowserName.CHROME
        config.base_url = BASE_URL

    first_test_user = None
    second_test_user = None

    def get_first_test_user(self):
        if BaseTest.first_test_user is None:
            user = User('admin', 'qazwsx123456')
            user.user_id = SQLHelper.create_user_if_not_present(user)
            BaseTest.first_test_user = user
        return BaseTest.first_test_user

    def get_second_test_user(self):
        if BaseTest.second_test_user is None:
            user = User('admin2', 'qazwsx123456')
            user.user_id = SQLHelper.create_user_if_not_present(user)
            BaseTest.second_test_user = user
        return BaseTest.second_test_user

    def get_test_task(self, user):
        task = Task((str(datetime.now()) + ' Task title'), 'task description',
                    date.today(), datetime.utcnow().replace(second=0, microsecond=0),
                    user_id=user.user_id)
        SQLHelper.create_task(task)
        return task

    def tearDown(self):
        browser.close()
