from e2etests.tests.test_base import BaseTest


class TestUserCanGoFromCreateToHomePageWithoutWarning(BaseTest):
    def test_user_can_go_from_create_to_home_page_without_warning(self):
        user = self.get_first_test_user()

        home_page = self.login_as(user).create_task().click_on_task_board_link_without_modifying_fields()

        self.assertFalse((home_page.is_alert_present()), 'Warning message is present')
        self.assertTrue((home_page.is_opened()), 'Home page is not opened')
