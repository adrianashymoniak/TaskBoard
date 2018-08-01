from e2etests.tests.test_base import BaseTest


class UserCanEditTask(BaseTest):
    def test_user_can_edit_task(self):
        user = self.get_first_test_user()
        test_task = self.get_test_task(user)
        expected_task = self.get_task_edited()

        actual_task = (self.edit_task_for_user(user, test_task)
                       .fill_edited_task(expected_task)
                       .edit()
                       .read_task())

        self.assertObjectsEqual(expected_task, actual_task,
                                'Edited task is not displayed as expected on Task Details page')
