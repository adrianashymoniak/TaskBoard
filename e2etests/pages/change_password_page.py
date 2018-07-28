from selene import browser

from e2etests.pages.page_with_leave_message import PageWithLeaveMessage
from e2etests.pages.view_profile_page import ViewProfilePage


class ChangePasswordPage(PageWithLeaveMessage):
    def fill_new_password(self, old_password, new_password):
        browser.element('#id_old_password').set_value(old_password)
        browser.element('#id_new_password1').set_value(new_password)
        browser.element('#id_new_password2').set_value(new_password)
        return self

    def change_password(self):
        browser.element('#submit_btn').click()
        return ViewProfilePage()
