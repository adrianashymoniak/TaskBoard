from datetime import date

from e2etests.domain.task import Task
from e2etests.pages.login_page import LoginPage
from e2etests.tests.test_base import BaseTest


class UserCanResetFilledTaskFields(BaseTest):
    def test_user_can_reset_filled_task_fields(self):
        user = self.get_first_test_user()
        task_to_enter = Task('Test title', 'Test description', date.today(), 'Minor')

        entered_task = (LoginPage
                        .open()
                        .login_as(user)
                        .create_task()
                        .fill_task(task_to_enter)
                        .reset_task()
                        .confirm_resetting()
                        .read_filled_task())

        self.assertEquals(len(entered_task.title), 0, "Title field not cleared")
        self.assertEquals(len(entered_task.description), 0, "Description field not cleared")
        self.assertEquals(len(entered_task.estimated), 0, "Estimation field not cleared")
