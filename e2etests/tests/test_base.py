from datetime import datetime, date
from unittest import TestCase

import pytz
from selene import browser
from selene import config
from selene.browsers import BrowserName
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from e2etests.configs import BASE_URL, HEADLESS, APP_TIME_ZONE
from e2etests.domain.task import Task
from e2etests.domain.user import User
from e2etests.util.sql_helper import SQLHelper


class BaseTest(TestCase):
    def setUp(self):
        config.browser_name = BrowserName.CHROME
        config.base_url = BASE_URL
        chrome_options = Options()
        if HEADLESS:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("window-size=1024,768")
            chrome_options.add_argument("--no-sandbox")
        browser.set_driver(webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options))

    first_test_user = None
    second_test_user = None

    def get_first_test_user(self):
        if BaseTest.first_test_user is None:
            user = User('first_test_user', 'admin123')
            user.user_id = SQLHelper.create_user_if_not_present(user)
            BaseTest.first_test_user = user
        return BaseTest.first_test_user

    def get_second_test_user(self):
        if BaseTest.second_test_user is None:
            user = User('second_test_user', 'admin123')
            user.user_id = SQLHelper.create_user_if_not_present(user)
            BaseTest.second_test_user = user
        return BaseTest.second_test_user

    def get_test_task(self, user):
        task = Task((str(datetime.now()) + ' Task title'), 'task description',
                    date.today(), datetime.utcnow().replace(second=0, microsecond=0),
                    user_id=user.user_id)
        SQLHelper.create_task(task)
        return task

    def get_app_time(self):
        return datetime.now(pytz.timezone(APP_TIME_ZONE)).replace(second=0, microsecond=0, tzinfo=None)

    def tearDown(self):
        SQLHelper.delete_tasks_for_user(self.get_first_test_user())
        SQLHelper.delete_tasks_for_user(self.get_second_test_user())
        browser.close()
