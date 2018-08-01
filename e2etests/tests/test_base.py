import random
from datetime import datetime, date
from unittest import TestCase

import pytz
from faker import Faker
from selene import browser
from selene import config
from selene.browsers import BrowserName
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from e2etests.configs import BASE_URL, HEADLESS, APP_TIME_ZONE, AUTO_INSTALL_DRIVER
from e2etests.domain.task import Task
from e2etests.domain.user import User
from e2etests.pages.login_page import LoginPage
from e2etests.pages.page_not_found_page import PageNotFoundPage
from e2etests.util.sql_helper import SQLHelper


class BaseTest(TestCase):
    auto_installed_driver_path = None

    def setUp(self):
        config.browser_name = BrowserName.CHROME
        config.base_url = BASE_URL
        chrome_options = Options()
        if HEADLESS:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("window-size=1024,768")
            chrome_options.add_argument("--no-sandbox")
        if AUTO_INSTALL_DRIVER:
            if BaseTest.auto_installed_driver_path is None:
                BaseTest.auto_installed_driver_path = ChromeDriverManager().install()
            browser.set_driver(webdriver.Chrome(BaseTest.auto_installed_driver_path, options=chrome_options))
        else:
            browser.set_driver(webdriver.Chrome(options=chrome_options))

    first_test_user = None
    second_test_user = None
    third_test_user = None

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

    def get_third_test_user(self):
        if BaseTest.third_test_user is None:
            user = User('third_test_user', 'admin123')
            user.user_id = SQLHelper.create_user_if_not_present(user)
            BaseTest.third_test_user = user
        return BaseTest.third_test_user

    def get_test_task(self, user):
        task = self.get_task_to_enter()
        task.published = datetime.utcnow().replace(second=0, microsecond=0)
        task.user_id = user.user_id

        SQLHelper.create_task(task)

        return task

    def get_app_time(self):
        return datetime.now(pytz.timezone(APP_TIME_ZONE)).replace(second=0, microsecond=0, tzinfo=None)

    def tearDown(self):
        SQLHelper.delete_tasks_for_user(self.get_first_test_user())
        SQLHelper.delete_tasks_for_user(self.get_second_test_user())
        browser.quit()

    def open_incorrect_url(self, incorrect_url):
        browser.open_url(incorrect_url)
        return PageNotFoundPage()

    def assertObjectsEqual(self, first_object, second_object, message):
        return self.assertDictEqual(vars(first_object), vars(second_object), message)

    def login_as(self, user):
        self.open_login_page()
        return LoginPage().login_as(user)

    def open_login_page(self):
        LoginPage.load_relative_url('/')
        return self

    def open_task_for_user(self, user, task):
        self.open_login_page()
        return LoginPage().login_as(user).open_task(task)

    def edit_task_for_user(self, user, task):
        return self.open_task_for_user(user, task).edit_task()

    def fill_task_for_user(self, user, task):
        return self.login_as(user).create_task().fill_task(task)

    def delete_task_for_user(self, user, task):
        return self.open_task_for_user(user, task).click_delete_task()

    faker = Faker()

    def get_task_to_enter(self):
        priority = random.choice(['Critical', 'Normal', 'Minor', 'Major'])
        return Task(BaseTest.faker.word(), BaseTest.faker.sentence(), date.today(), priority, self.get_app_time())

    def get_not_published_task_to_enter(self):
        task_to_enter = self.get_task_to_enter()
        task_to_enter.published = None
        return task_to_enter

    def get_task_edited(self):
        edited_task = self.get_task_to_enter()
        edited_task.edited = self.get_app_time()
        return edited_task

    def get_user_to_enter(self):
        return User(username=None, first_name=BaseTest.faker.first_name(), last_name=BaseTest.faker.last_name(),
                    email=BaseTest.faker.email())
