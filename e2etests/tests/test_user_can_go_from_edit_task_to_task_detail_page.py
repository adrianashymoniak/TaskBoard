from e2etests.pages.login_page import LoginPage
from e2etests.tests.test_base import BaseTest


class UserCanGoFromEditTaskToTaskDetailPage(BaseTest):
    def test_user_can_go_from_edit_task_to_task_detail_page(self):
        user = self.get_first_test_user()
        task = self.get_test_task(user)
        tasks_titles = (LoginPage
                        .open()
                        .login_as(user)
                        .open_task(task)
                        .edit_task()
                        .navigate_to_task_detail_page()
                        .get_tasks_titles()
                        )
        self.assertIn(task.title, tasks_titles, 'User is not redirected to Task Detail page')
