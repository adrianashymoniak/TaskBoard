from selene import browser

from e2etests.pages.page_with_leave_message import PageWithLeaveMessage
from e2etests.pages.view_profile_page import ViewProfilePage


class EditProfilePage(PageWithLeaveMessage):
    def fill_new_profile_information(self, user):
        browser.element('#id_first_name').set_value(user.first_name)
        browser.element('#id_last_name').set_value(user.last_name)
        browser.element('#id_email').set_value(user.email)
        return self

    def submit_edited_profile(self):
        browser.element('#submit_btn').click()
        return ViewProfilePage()
