from datetime import date, datetime

from e2etests.domain.task import Task
from e2etests.pages.login_page import LoginPage
from e2etests.tests.test_base import BaseTest


class UserCanCreateTask(BaseTest):
    def test_user_can_create_task(self):
        expected_task = Task('Test title', 'Test description', date.today(),
                             datetime.now().replace(second=0, microsecond=0))
        actual_task = (LoginPage
                       .open()
                       .login_as(self.get_user())
                       .create_task()
                       .save_task(expected_task)
                       .read_task())
        self.assertEqual(expected_task, actual_task, 'Created task is not displayed as expected on Task Details page')
