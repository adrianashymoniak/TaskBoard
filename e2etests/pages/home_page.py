from selene import browser

from e2etests.pages.create_task_page import CreateTaskPage


class HomePage:
    def greeting(self):
        return browser.element('#greeting')

    def create_task(self):
        browser.element('#create_task').click()
        return CreateTaskPage()
