from datetime import datetime

from selene import browser

from e2etests.domain.task import Task
from e2etests.pages.edit_task_page import EditTaskPage


class TaskDetailPage:
    def edit_task(self):
        browser.element('#edit_task_task_detail').click()
        return EditTaskPage()

    def read_task(self):
        title = browser.element('#task_title_detail').text
        description = browser.element('#task_description').text
        estimated = browser.element('#estimated').text.replace('Estimation: ', '')
        published = browser.element('#published_at').text.replace('Published at: ', '')
        return Task(title, description, datetime.strptime(estimated, '%b. %d, %Y').date(),
                    datetime.strptime(published, '%b. %d, %Y, %I:%M %p'))

    def read_edited_task(self):
        task = self.read_task()
        edited = browser.element('#edited_at').text.replace('Edited at: ', '')
        task.edited = datetime.strptime(edited, '%b. %d, %Y, %I:%M %p')
        return task

    def delete_task(self):
        browser.element('#delete_task_edit_page').click()
        from e2etests.pages.home_page import HomePage
        return HomePage()

    def get_tasks_titles(self):
        return [e.text for e in browser.elements('#task_title_detail')]

    def navigate_to_home_page(self):
        browser.element('#home_page').click()
        from e2etests.pages.home_page import HomePage
        return HomePage()
