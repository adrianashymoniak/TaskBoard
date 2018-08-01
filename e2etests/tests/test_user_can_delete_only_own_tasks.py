from e2etests.tests.test_base import BaseTest


class UserCanDeleteOnlyOwnTasks(BaseTest):
    def test_user_can_delete_only_own_task(self):
        first_user = self.get_first_test_user()
        self.get_test_task(first_user)

        second_user = self.get_second_test_user()
        second_user_test_task = self.get_test_task(second_user)

        available_tasks_for_second_user = (self.login_as(first_user)
                                           .click_delete_all()
                                           .confirm_deleting()
                                           .logout()
                                           .login_as(second_user)
                                           .get_tasks_titles())

        self.assertIn(second_user_test_task.title, available_tasks_for_second_user,
                      'Tasks are deleted for second user')
