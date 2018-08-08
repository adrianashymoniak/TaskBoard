from e2etests.tests.test_base import BaseTest


class TestUserCanDiscardDeletingTask(BaseTest):
    def test_user_can_discard_deleting_task(self):
        user = self.get_first_test_user()
        task_for_deleting = self.get_test_task(user)

        available_tasks = (self.delete_task_for_user(user, task_for_deleting)
                           .discard_deleting()
                           .read_task_title())

        self.assertIn(task_for_deleting.title, available_tasks, 'Task is removed')
