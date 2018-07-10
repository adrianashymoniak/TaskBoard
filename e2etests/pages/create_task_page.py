from datetime import datetime

from selene import browser
from selenium.webdriver.support.select import Select

from e2etests.domain.task import Task
from e2etests.pages.page_with_leave_message import PageWithLeaveMessage
from e2etests.pages.task_detail_page import TaskDetailPage


class CreateTaskPage(PageWithLeaveMessage):
    def __init__(self):
        self.title = browser.element('#task_title')
        self.description = browser.element('#task_description')
        self.estimation = browser.element('#time_estimated')
        self.priorities = Select(browser.element('#id_priorities'))

    def fill_task(self, task):
        self.title.set_value(task.title)
        self.description.set_value(task.description)
        self.estimation.send_keys(task.estimated.strftime("%m-%d-%Y"))
        self.priorities.select_by_visible_text(task.priorities)
        return self

    def read_filled_task(self):
        title = self.title.get_attribute("value")
        description = self.description.get_attribute("value")
        estimation = self.estimation.get_attribute("value")
        if estimation:
            estimation = datetime.strptime(estimation, '%Y-%m-%d').date()
        priorities = self.priorities.first_selected_option.text
        return Task(title, description, estimation, priorities)

    def save_task(self, task):
        self.fill_task(task)
        browser.element('#save_task').click()
        return TaskDetailPage()

    def confirm_canceling(self):
        browser.driver().switch_to.alert.accept()
        from e2etests.pages.home_page import HomePage
        return HomePage()

    def confirm_resetting(self):
        browser.driver().switch_to.alert.accept()
        return self

    def reset_task(self):
        browser.element('#reset_fields').click()
        return self

    def click_on_task_board_link(self):
        browser.element('#home_page').click()
        return self

    def click_on_task_board_link_without_modifying_fields(self):
        self.click_on_task_board_link()
        from e2etests.pages.home_page import HomePage
        return HomePage()
