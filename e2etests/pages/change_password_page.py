from e2etests.pages.page_with_leave_message import PageWithLeaveMessage


class ChangePasswordPage(PageWithLeaveMessage):
    def fill_new_password(self, old_password, new_password):
        self.set_value('#id-old-password', old_password)
        self.set_value('#id-new-password1', new_password)
        self.set_value('#id-new-password2', new_password)
        return self

    def change_password(self):
        self.click('#submit-btn')
        return self.view_profile_page()
