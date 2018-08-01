from e2etests.pages.delete_single_task_page import DeleteSingleTaskPage
from e2etests.pages.page_with_leave_message import PageWithLeaveMessage


class EditTaskPage(DeleteSingleTaskPage, PageWithLeaveMessage):
    def fill_edited_task(self, task=None):
        if task is not None:
            self.set_value('#task_title', task.title)
            self.set_value('#task_description', task.description)
            self.send_keys('#time_estimated', task.estimated.strftime("%m-%d-%Y"))
            self.select('#id_priorities', task.priorities)
        return self

    def edit(self, task=None):
        self.fill_edited_task(task)
        self.click('#edit_task')
        return self.task_detail_page()

    def select_status_by_visible_text(self, visible_text):
        self.select('#id_status', visible_text)
        return self
