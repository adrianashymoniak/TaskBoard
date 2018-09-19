from e2etests.pages.base_page import BasePage


class DeleteUserAccountPage(BasePage):
    def click_delete_user_account(self):
        self.click('#delete-user')
        return self

    def confirm_deleting_account(self):
        self.accept_alert()
        return self.login_page()

    def discard_deleting_account(self):
        self.dismiss_alert()
        return self.view_profile_page()
