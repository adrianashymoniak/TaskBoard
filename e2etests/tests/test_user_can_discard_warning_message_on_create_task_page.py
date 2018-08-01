from e2etests.tests.test_base import BaseTest


class TestUserCanDiscardWarningMessageOnCreateTaskPage(BaseTest):
    def test_user_can_discard_warning_message_on_create_task_page(self):
        user = self.get_first_test_user()
        task_to_enter = self.get_not_published_task_to_enter()

        entered_task = (self.fill_task_for_user(user, task_to_enter)
                        .click_on_task_board_link()
                        .discard_leaving()
                        .read_filled_task())

        self.assertObjectsEqual(entered_task, task_to_enter, 'Entered task was cleared')
