from datetime import datetime

from selene import browser

from e2etests.domain.task import Task
from e2etests.pages.delete_single_task_page import DeleteSingleTaskPage
from e2etests.pages.edit_task_page import EditTaskPage


class TaskDetailPage(DeleteSingleTaskPage):
    def edit_task(self):
        browser.element('#edit_task_task_detail').click()
        return EditTaskPage()

    def read_task(self):
        title = self.read_task_title()
        description = browser.element('#task_description').text
        estimated = browser.element('#estimated').text.replace('Estimation: ', '')
        published = browser.element('#published_at').text.replace('Published at: ', '')
        priorities = browser.element('#id_priorities').text

        task = Task(title, description, datetime.strptime(estimated, '%b. %d, %Y').date(), priorities,
                    datetime.strptime(published, '%b. %d, %Y, %I:%M %p'))

        if browser.elements('#edited_at').size() == 1:
            edited = browser.element('#edited_at').text.replace('Edited at: ', '')
            task.edited = datetime.strptime(edited, '%b. %d, %Y, %I:%M %p')

        return task

    def read_task_title(self):
        return browser.element('#task_title_detail').text

    def navigate_to_home_page(self):
        browser.element('#home_page').click()
        from e2etests.pages.home_page import HomePage
        return HomePage()
