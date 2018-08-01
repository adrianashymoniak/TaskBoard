from e2etests.tests.test_base import BaseTest


class UserCanDeleteTask(BaseTest):
    def test_user_can_delete_task(self):
        user = self.get_first_test_user()
        task_for_deleting = self.get_test_task(user)
        additional_task = self.get_test_task(user)

        available_tasks = (self.delete_task_for_user(user, task_for_deleting)
                           .confirm_deleting()
                           .get_tasks_titles())

        self.assertNotIn(task_for_deleting.title, available_tasks, 'Deleted task is still displayed on Home page')
        self.assertIn(additional_task.title, available_tasks, 'Another task is removed')
