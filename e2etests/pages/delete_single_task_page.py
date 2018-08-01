from e2etests.pages.confirm_task_deleting_page import ConfirmTaskDeletingPage


class DeleteSingleTaskPage(ConfirmTaskDeletingPage):
    def click_delete_task(self):
        self.click('#delete_task_edit_page')
        return self
