from e2etests.pages.page_with_leave_message import PageWithLeaveMessage


class EditProfilePage(PageWithLeaveMessage):
    def fill_new_profile_information(self, user):
        self.set_value('#id_first_name', user.first_name)
        self.set_value('#id_last_name', user.last_name)
        self.set_value('#id_email', user.email)
        return self

    def submit_edited_profile(self):
        self.click('#submit_btn')
        return self.view_profile_page()
