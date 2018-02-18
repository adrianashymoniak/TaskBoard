from datetime import datetime

from selene import browser

from e2etests.domain.task import Task


class TaskDetailPage:
    def read_task(self):
        title = browser.element('#task_title_detail').text
        description = browser.element('#task_description').text
        estimated = browser.element('#estimated').text.replace('Estimation: ', '')
        published = browser.element('#published_at').text.replace('Published at: ', '').replace('a.m.', 'AM').replace(
            'p.m.', 'PM')
        return Task(title, description, datetime.strptime(estimated, '%b. %d, %Y').date(),
                    datetime.strptime(published, '%b. %d, %Y, %I:%M %p'))
