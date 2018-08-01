from e2etests.tests.test_base import BaseTest


class UserCanCancelTaskCreation(BaseTest):
    def test_user_can_cancel_task_creation(self):
        user = self.get_first_test_user()
        task_to_enter = self.get_task_to_enter()

        available_tasks = (self.fill_task_for_user(user, task_to_enter)
                           .click_on_task_board_link()
                           .confirm_canceling()
                           .get_tasks_titles())

        self.assertNotIn(task_to_enter.title, available_tasks, 'Task creation is not canceled')
