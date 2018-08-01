import re

from e2etests.pages.confirm_task_deleting_page import ConfirmTaskDeletingPage


class HomePage(ConfirmTaskDeletingPage):
    def read_greeting(self):
        return self.read_text('#greeting')

    def create_task(self):
        self.click('#create_task')
        return self.create_task_page()

    def open_task(self, task):
        self.click_by_xpath("//span[contains(text(),'{}')]/ancestor::a", task.title)
        return self.task_detail_page()

    def __parse_task_titles_by_css_selector(self, css_selector):
        return [re.sub("#(\d)+: ", "", t) for t in self.read_texts(css_selector)]

    def get_tasks_titles(self):
        return self.__parse_task_titles_by_css_selector('#task_title')

    def get_tasks_titles_in_status_new(self):
        return self.__parse_task_titles_by_css_selector('.column_name_new+.task_column #task_title')

    def get_tasks_titles_in_status_in_progress(self):
        return self.__parse_task_titles_by_css_selector('.column_name_in_progress+.task_column #task_title')

    def get_tasks_titles_in_status_done(self):
        return self.__parse_task_titles_by_css_selector('.column_name_done+.task_column #task_title')

    def logout(self):
        self.click('#logout')
        return self.login_page()

    def is_opened(self):
        return self.get_elements_count('.task_column') == 3

    def open_profile_dropdown(self):
        self.move_to_element('#greeting')
        return self

    def open_edit_profile(self):
        self.open_profile_dropdown()
        self.click('#id_edit_profile')
        return self.edit_pofile_page()

    def open_change_password(self):
        self.open_profile_dropdown()
        self.click('#id_change_password')
        return self.change_password_page()

    def open_view_profile(self):
        self.open_profile_dropdown()
        self.click('#id_view_profile')
        return self.view_profile_page()
