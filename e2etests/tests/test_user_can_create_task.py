from e2etests.tests.test_base import BaseTest


class UserCanCreateTask(BaseTest):
    def test_user_can_create_task(self):
        task_to_enter = self.get_task_to_enter()

        actual_task = (self.login_as(self.get_first_test_user())
                       .create_task()
                       .save_task(task_to_enter)
                       .read_task())

        self.assertObjectsEqual(task_to_enter, actual_task,
                                'Created task is not displayed as expected on Task Details page')
