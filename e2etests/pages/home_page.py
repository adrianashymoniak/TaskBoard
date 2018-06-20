import re

from selene import browser
from selene.support import by

from e2etests.pages.create_task_page import CreateTaskPage
from e2etests.pages.task_detail_page import TaskDetailPage


class HomePage:
    def read_greeting(self):
        return browser.element('#greeting').text

    def create_task(self):
        browser.element('#create_task').click()
        return CreateTaskPage()

    def open_task(self, task):
        browser.element(by.xpath("//span[contains(text(),'{}')]/ancestor::a".format(task.title))).click()
        return TaskDetailPage()

    def __parse_task_titles_by_css_selector(self, css_selector):
        return [re.sub("#(\d)+: ", "", e.text) for e in browser.elements(css_selector)]

    def get_tasks_titles(self):
        return self.__parse_task_titles_by_css_selector('#task_title')

    def get_tasks_titles_in_status_new(self):
        return self.__parse_task_titles_by_css_selector('.column_name_new+.task_column #task_title')

    def get_tasks_titles_in_status_in_progress(self):
        return self.__parse_task_titles_by_css_selector('.column_name_in_progress+.task_column #task_title')

    def get_tasks_titles_in_status_done(self):
        return self.__parse_task_titles_by_css_selector('.column_name_done+.task_column #task_title')

    def delete_all(self):
        browser.element('#delete_all_tasks').click()
        return self

    def logout(self):
        browser.element('#logout').click()
        from e2etests.pages.login_page import LoginPage
        return LoginPage()
