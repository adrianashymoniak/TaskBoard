from e2etests.tests.test_base import BaseTest


class UserCanResetFilledTaskFields(BaseTest):
    def test_user_can_reset_filled_task_fields(self):
        user = self.get_first_test_user()
        task_to_enter = self.get_task_to_enter()

        entered_task = (self.fill_task_for_user(user, task_to_enter)
                        .reset_task()
                        .confirm_resetting()
                        .read_filled_task())

        self.assertEqual(len(entered_task.title), 0, "Title field is not cleared")
        self.assertEqual(len(entered_task.description), 0, "Description field is not cleared")
        self.assertEqual(len(entered_task.estimated), 0, "Estimation field is not cleared")

