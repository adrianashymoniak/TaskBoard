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
        browser.element(by.xpath("//a[text()='{}']".format(task.title))).click()
        return TaskDetailPage()

    def get_tasks_titles(self):
        return [e.text for e in browser.elements('#task_title')]

    def delete_all(self):
        browser.element('#delete_all_tasks').click()
        return self

    def logout(self):
        browser.element('#logout').click()
        from e2etests.pages.login_page import LoginPage
        return LoginPage()
