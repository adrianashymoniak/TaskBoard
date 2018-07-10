from selene import browser

from e2etests.pages.confirm_task_deleting_page import ConfirmTaskDeletingPage


class DeleteSingleTaskPage(ConfirmTaskDeletingPage):
    def click_delete_task(self):
        browser.element('#delete_task_edit_page').click()
        return self

    def discard_deleting(self):
        browser.driver().switch_to.alert.dismiss()
        return self
