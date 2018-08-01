from e2etests.tests.test_base import BaseTest


class UserCanGoFromEditTaskToTaskDetailPage(BaseTest):
    def test_user_can_go_from_edit_task_to_task_detail_page(self):
        user = self.get_first_test_user()
        task = self.get_test_task(user)

        tasks_titles = (self.edit_task_for_user(user, task)
                        .navigate_to_task_detail_page_without_message()
                        .read_task_title()
                        )

        self.assertIn(task.title, tasks_titles, 'User is not redirected to Task Detail page')
