from datetime import date, datetime

from e2etests.domain.task import Task
from e2etests.pages.login_page import LoginPage
from e2etests.tests.test_base import BaseTest


class UserCanCancelTaskCreation(BaseTest):
    def test_user_can_cancel_task_creation(self):
        user = self.get_first_test_user()
        task_to_enter = Task('Test title', 'Test description', date.today(),
                             datetime.now().replace(second=0, microsecond=0))

        available_tasks = (LoginPage
                           .open()
                           .login_as(user)
                           .create_task()
                           .fill_task(task_to_enter)
                           .cancel()
                           .get_tasks_titles())

        self.assertNotIn(task_to_enter.title, available_tasks, 'Task creation is not canceled')