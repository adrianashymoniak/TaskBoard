from e2etests.pages.base_page import BasePage


class ConfirmTaskDeletingPage(BasePage):
    def confirm_deleting(self):
        self.accept_alert()
        return self.home_page()

    def discard_deleting(self):
        self.dismiss_alert()
        return self

    def click_delete_all(self):
        self.click('#delete-all-tasks')
        return self
