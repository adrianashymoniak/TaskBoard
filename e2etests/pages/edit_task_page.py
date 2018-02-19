from selene import browser


class EditTaskPage:
    def edit(self, task):
        browser.element('#task_title').set_value(task.title)
        browser.element('#task_description').set_value(task.description)
        browser.element('#time_estimated').send_keys(task.estimated.strftime("%m-%d-%Y"))
        browser.element('#edit_task').click()
        from e2etests.pages.task_detail_page import TaskDetailPage
        return TaskDetailPage()
