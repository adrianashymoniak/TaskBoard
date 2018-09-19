from datetime import datetime

from e2etests.domain.task import Task
from e2etests.pages.page_with_leave_message import PageWithLeaveMessage


class CreateTaskPage(PageWithLeaveMessage):
    def __init__(self):
        self.title = '#task-title'
        self.description = '#task-description'
        self.estimation = '#time-estimated'
        self.priorities = '#id-priorities'

    def fill_task(self, task):
        self.set_value(self.title, task.title)
        self.set_value(self.description, task.description)
        self.send_keys(self.estimation, task.estimated.strftime("%m-%d-%Y"))
        self.select(self.priorities, task.priorities)
        return self

    def read_filled_task(self):
        title = self.get_value(self.title)
        description = self.get_value(self.description)
        estimation = self.get_value(self.estimation)
        if estimation:
            estimation = datetime.strptime(estimation, '%Y-%m-%d').date()
        priorities = self.get_first_selected_option(self.priorities)
        return Task(title, description, estimation, priorities)

    def save_task(self, task):
        self.fill_task(task)
        self.click('#save-task')
        return self.task_detail_page()

    def confirm_canceling(self):
        self.accept_alert()
        return self.home_page()

    def confirm_resetting(self):
        self.accept_alert()
        return self

    def reset_task(self):
        self.click('#reset-fields')
        return self

    def click_on_task_board_link(self):
        self.click('#home-page')
        return self

    def click_on_task_board_link_without_modifying_fields(self):
        self.click_on_task_board_link()
        return self.home_page()
