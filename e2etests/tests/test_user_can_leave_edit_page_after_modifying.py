from e2etests.tests.test_base import BaseTest


class TestUserCanLeaveEditPageAfterModifying(BaseTest):
    def test_user_can_leave_edit_page_after_modifying(self):
        user = self.get_first_test_user()

        test_task = self.get_test_task(user)
        test_task.user_id = None
        test_task.published = self.get_app_time()

        task_to_set = self.get_task_edited()

        actual_task = (self.edit_task_for_user(user, test_task)
                       .fill_edited_task(task_to_set)
                       .navigate_to_task_detail_page_with_message()
                       .confirm_leaving_to_task_detail_page()
                       .read_task())

        self.assertObjectsEqual(test_task, actual_task, 'Task was edited')
