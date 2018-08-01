from e2etests.tests.test_base import BaseTest


class UserCanGoFromTaskDetailToHomePage(BaseTest):
    def test_user_can_go_from_task_detail_to_home_page(self):
        user = self.get_first_test_user()
        task = self.get_test_task(user)

        tasks_titles = (self.open_task_for_user(user, task)
                        .navigate_to_home_page()
                        .get_tasks_titles()
                        )

        self.assertIn(task.title, tasks_titles, 'User is not redirected to Home page')
