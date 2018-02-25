from e2etests.pages.login_page import LoginPage
from e2etests.tests.test_base import BaseTest


class UserCanDeleteAllTasks(BaseTest):
    def test_user_can_delete_all_tasks(self):
        user = self.get_first_test_user()
        first_test_task = self.get_test_task(user)
        second_test_task = self.get_test_task(user)

        available_tasks = (LoginPage
                           .open()
                           .login_as(user)
                           .delete_all()
                           .get_tasks_titles()
                           )

        self.assertNotIn((first_test_task.title and second_test_task.title), available_tasks,
                         'Deleted tasks are still displayed on Home page')
        self.assertEqual(len(available_tasks), 0,
                         'Not all tasks are deleted for current user')
