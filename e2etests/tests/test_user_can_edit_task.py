from datetime import datetime, date

from e2etests.domain.task import Task
from e2etests.pages.login_page import LoginPage
from e2etests.tests.test_base import BaseTest


class UserCanEditTask(BaseTest):
    def test_user_can_edit_task(self):
        user = self.get_first_test_user()
        test_task = self.get_test_task(user)
        expected_task = Task('Test title', 'Test description', date.today(),
                             datetime.now().replace(second=0, microsecond=0),
                             datetime.now().replace(second=0, microsecond=0))
        actual_task = (LoginPage
                       .open()
                       .login_as(user)
                       .open_task(test_task)
                       .edit_task()
                       .edit(expected_task)
                       .read_edited_task())
        self.assertEqual(expected_task, actual_task, 'Edited task is not displayed as expected on Task Details page')
