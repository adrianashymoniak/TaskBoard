from datetime import datetime

from e2etests.domain.task import Task
from e2etests.pages.delete_single_task_page import DeleteSingleTaskPage


class TaskDetailPage(DeleteSingleTaskPage):
    def edit_task(self):
        self.click('#edit_task_task_detail')
        return self.edit_task_page()

    def read_task(self):
        title = self.read_task_title()
        description = self.read_text('#task_description')
        estimated = self.read_text('#estimated').replace('Estimation: ', '')
        published = self.read_text('#published_at').replace('Published at: ', '')
        priorities = self.read_text('#id_priorities')

        task = Task(title, description, datetime.strptime(estimated, '%b. %d, %Y').date(), priorities,
                    datetime.strptime(published, '%b. %d, %Y, %I:%M %p'))

        if self.get_elements_count('#edited_at') == 1:
            edited = self.read_text('#edited_at').replace('Edited at: ', '')
            task.edited = datetime.strptime(edited, '%b. %d, %Y, %I:%M %p')

        return task

    def read_task_title(self):
        return self.read_text('#task_title_detail')

    def navigate_to_home_page(self):
        self.click('#home_page')
        return self.home_page()
