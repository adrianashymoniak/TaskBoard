from e2etests.pages.page_with_leave_message import PageWithLeaveMessage


class ChangePasswordPage(PageWithLeaveMessage):
    def fill_new_password(self, old_password, new_password):
        self.set_value('#id_old_password', old_password)
        self.set_value('#id_new_password1', new_password)
        self.set_value('#id_new_password2', new_password)
        return self

    def change_password(self):
        self.click('#submit_btn')
        return self.view_profile_page()
