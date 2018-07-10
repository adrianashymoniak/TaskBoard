from selene import browser


class ConfirmTaskDeletingPage:
    def confirm_deleting(self):
        browser.driver().switch_to.alert.accept()
        from e2etests.pages.home_page import HomePage
        return HomePage()

    def discard_deleting(self):
        browser.driver().switch_to.alert.dismiss()
        from e2etests.pages.home_page import HomePage
        return HomePage()

    def click_delete_all(self):
        browser.element('#delete_all_tasks').click()
        return self
