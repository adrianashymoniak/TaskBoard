from selene import browser


class DeleteUserAccountPage:
    def click_delete_user_account(self):
        browser.element('#delete_user').click()
        return self

    def confirm_deleting_account(self):
        browser.driver().switch_to.alert.accept()
        from e2etests.pages.login_page import LoginPage
        return LoginPage()

    def discard_deleting_account(self):
        browser.driver().switch_to.alert.dismiss()
        from e2etests.pages.view_profile_page import ViewProfilePage
        return ViewProfilePage()
