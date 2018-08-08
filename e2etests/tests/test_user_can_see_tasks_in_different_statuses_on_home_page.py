from e2etests.tests.test_base import BaseTest
from e2etests.domain.task_statuses import TaskStatuses


class UserCanSeeTasksInDifferentStatusesOnHomePage(BaseTest):
    def test_user_can_see_tasks_in_different_statuses_on_home_page(self):
        user = self.get_first_test_user()
        test_task = self.get_test_task(user)

        home_page = self.login_as(user)
        self.assert_task_in_new_column(home_page, test_task)

        home_page = self.change_task_status(home_page, test_task, TaskStatuses.IN_PROGRESS)
        self.assert_task_in_in_progress_column(home_page, test_task)

        home_page = self.change_task_status(home_page, test_task, TaskStatuses.DONE)
        self.assert_task_in_done_column(home_page, test_task)

        home_page = self.change_task_status(home_page, test_task, TaskStatuses.NEW)
        self.assert_task_in_new_column(home_page, test_task)

    def change_task_status(self, home_page, test_task, status):
        return (home_page.open_task(test_task).edit_task()
                .select_status(status).edit().navigate_to_home_page())

    def assert_task_in_done_column(self, home_page, test_task):
        self.assertIn(test_task.title, home_page.get_tasks_titles_in_status_done(), 'Task is not in Done column')
        self.assertFalse(home_page.get_tasks_titles_in_status_new(), 'Task is displayed in New column')
        self.assertFalse(home_page.get_tasks_titles_in_status_in_progress(), 'Task is displayed in In progress column')

    def assert_task_in_in_progress_column(self, home_page, test_task):
        self.assertIn(test_task.title, home_page.get_tasks_titles_in_status_in_progress(),
                      'Task is not in In progress column')
        self.assertFalse(home_page.get_tasks_titles_in_status_new(), 'Task is displayed in New column')
        self.assertFalse(home_page.get_tasks_titles_in_status_done(), 'Task is displayed in Done column')

    def assert_task_in_new_column(self, home_page, test_task):
        self.assertIn(test_task.title, home_page.get_tasks_titles_in_status_new(), 'Task is not in New column')
        self.assertFalse(home_page.get_tasks_titles_in_status_in_progress(), 'Task is displayed in In progress column')
        self.assertFalse(home_page.get_tasks_titles_in_status_done(), 'Task is displayed in Done column')
