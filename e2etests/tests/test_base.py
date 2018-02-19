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

    def tearDown(self):
        browser.close()

    user = None
    user_id = None

    def get_user(self):
        if BaseTest.user is None:
            user = User('admin', 'qazwsx123456')
            SQLHelper.create_user_if_not_present(user)
            BaseTest.user = user
        return BaseTest.user

    def get_user_id(self):
        if BaseTest.user_id is None:
            BaseTest.user_id = SQLHelper.get_user_id(self.get_user())
        return BaseTest.user_id

    def get_test_task(self):
        task = Task((str(datetime.now().replace(second=0, microsecond=0)) + ' Task title'), 'task description',
                    date.today(), datetime.utcnow().replace(second=0, microsecond=0),
                    user_id=SQLHelper.get_user_id(self.get_user()))
        SQLHelper.create_task(task)
        return task
