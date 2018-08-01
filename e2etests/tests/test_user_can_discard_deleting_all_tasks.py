from e2etests.tests.test_base import BaseTest


class TestUserCanDiscardDeletingAllTasks(BaseTest):
    def test_user_can_discard_deleting_all_tasks(self):
        user = self.get_first_test_user()
        first_test_task = self.get_test_task(user)
        second_test_task = self.get_test_task(user)

        available_tasks = (self.login_as(user)
                           .click_delete_all()
                           .discard_deleting()
                           .get_tasks_titles())

        self.assertIn(first_test_task.title, available_tasks,
                      'Tasks was deleted')

        self.assertIn(second_test_task.title, available_tasks,
                      'Tasks was deleted')
