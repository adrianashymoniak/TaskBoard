from datetime import date

from e2etests.domain.task import Task
from e2etests.pages.login_page import LoginPage
from e2etests.tests.test_base import BaseTest


class TestUserCanDiscardWarningMessageOnCreateTaskPage(BaseTest):
    def test_user_can_discard_warning_message_on_create_task_page(self):
        user = self.get_first_test_user()
        task_to_enter = Task('Test title', 'Test description', date.today(), 'Critical')

        entered_task = (LoginPage
                        .open()
                        .login_as(user)
                        .create_task()
                        .fill_task(task_to_enter)
                        .click_on_task_board_link()
                        .discard_leaving()
                        .read_filled_task())

        self.assertEqual(entered_task, task_to_enter, 'Entered task was cleared')
