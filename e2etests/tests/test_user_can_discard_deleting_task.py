from e2etests.pages.login_page import LoginPage
from e2etests.tests.test_base import BaseTest


class TestUserCanDiscardDeletingTask(BaseTest):
    def test_user_can_discard_deleting_task(self):
        user = self.get_first_test_user()
        task_for_deleting = self.get_test_task(user)

        available_tasks = (LoginPage
                           .open()
                           .login_as(user)
                           .open_task(task_for_deleting)
                           .click_delete_task()
                           .discard_deleting()
                           .read_task_title())

        self.assertIn(task_for_deleting.title, available_tasks, 'Task is removed')
