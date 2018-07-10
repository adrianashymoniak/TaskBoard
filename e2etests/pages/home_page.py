import re

from selene import browser
from selene.support import by
from selenium.common.exceptions import NoAlertPresentException

from e2etests.pages.confirm_task_deleting_page import ConfirmTaskDeletingPage
from e2etests.pages.create_task_page import CreateTaskPage
from e2etests.pages.task_detail_page import TaskDetailPage


class HomePage(ConfirmTaskDeletingPage):
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

    def logout(self):
        browser.element('#logout').click()
        from e2etests.pages.login_page import LoginPage
        return LoginPage()

    def is_alert_present(self):
        try:
            browser.driver().switch_to.alert
            return True
        except NoAlertPresentException:
            return False

    def is_opened(self):
        return browser.elements('.task_column').size() == 3
