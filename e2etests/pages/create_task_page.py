from selene import browser

from e2etests.domain.task import Task
from e2etests.pages.task_detail_page import TaskDetailPage


class CreateTaskPage:
    def __init__(self):
        self.title = browser.element('#task_title')
        self.description = browser.element('#task_description')
        self.estimation = browser.element('#time_estimated')

    def fill_task(self, task):
        self.title.set_value(task.title)
        self.description.set_value(task.description)
        self.estimation.send_keys(task.estimated.strftime("%m-%d-%Y"))
        return self

    def read_filled_task(self):
        title = self.title.get_attribute("value")
        description = self.description.get_attribute("value")
        estimation = self.estimation.get_attribute("value")
        return Task(title, description, estimation)

    def save_task(self, task):
        self.fill_task(task)
        browser.element('#save_task').click()
        return TaskDetailPage()

    def reset_task(self):
        browser.element('#reset_fields').click()
        return self

    def cancel(self):
        browser.element('#cancel').click()
        from e2etests.pages.home_page import HomePage
        return HomePage()
