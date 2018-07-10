from selene import browser
from selenium.webdriver.support.ui import Select

from e2etests.pages.delete_single_task_page import DeleteSingleTaskPage
from e2etests.pages.page_with_leave_message import PageWithLeaveMessage


class EditTaskPage(DeleteSingleTaskPage, PageWithLeaveMessage):
    def fill_edited_task(self, task=None):
        if task is not None:
            browser.element('#task_title').set_value(task.title)
            browser.element('#task_description').set_value(task.description)
            browser.element('#time_estimated').send_keys(task.estimated.strftime("%m-%d-%Y"))
            priorities = Select(browser.element('#id_priorities')).select_by_visible_text(task.priorities)
        return self

    def edit(self, task=None):
        self.fill_edited_task(task)
        browser.element('#edit_task').click()
        from e2etests.pages.task_detail_page import TaskDetailPage
        return TaskDetailPage()

    def select_status_by_visible_text(self, visible_text):
        select = Select(browser.element('#id_status'))
        select.select_by_visible_text(visible_text)
        return self
