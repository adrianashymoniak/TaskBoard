from e2etests.pages.login_page import LoginPage
from e2etests.tests.test_base import BaseTest


class UserCanDeleteTaskFromEditPage(BaseTest):
    def test_user_can_delete_task_from_edit_page(self):
        user = self.get_first_test_user()
        task_for_deleting = self.get_test_task(user)
        additional_task = self.get_test_task(user)

        available_tasks = (LoginPage
                           .open()
                           .login_as(user)
                           .open_task(task_for_deleting)
                           .edit_task()
                           .delete_task()
                           .get_tasks_titles())

        self.assertNotIn(task_for_deleting.title, available_tasks, 'Deleted task is still displayed on Home page')
        self.assertIn(additional_task.title, available_tasks, 'Another task is removed')