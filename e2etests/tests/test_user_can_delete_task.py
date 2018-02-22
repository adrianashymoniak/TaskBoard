from e2etests.pages.login_page import LoginPage
from e2etests.tests.test_base import BaseTest


class UserCanDeleteTask(BaseTest):
    def test_user_can_delete_task(self):
        task_for_deleting = self.get_test_task()
        additional_task = self.get_test_task()

        available_tasks = (LoginPage
                           .open()
                           .login_as(self.get_user())
                           .open_task(task_for_deleting)
                           .delete_task()
                           .get_tasks_titles())

        self.assertNotIn(task_for_deleting.title, available_tasks, 'Deleted task is still displayed on Home page')
        self.assertIn(additional_task.title, available_tasks, 'Another task is removed')
