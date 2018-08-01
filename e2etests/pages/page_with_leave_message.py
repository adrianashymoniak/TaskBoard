from e2etests.pages.base_page import BasePage


class PageWithLeaveMessage(BasePage):
    def navigate_to_task_detail_page_with_message(self):
        self.click('#go_detail_page')
        return self

    def navigate_to_task_detail_page_without_message(self):
        self.click('#go_detail_page')
        return self.task_detail_page()

    def discard_leaving(self):
        self.dismiss_alert()
        return self

    def confirm_leaving_to_task_detail_page(self):
        self.accept_alert()
        return self.task_detail_page()

    def confirm_leaving_to_home_page(self):
        self.accept_alert()
        return self.home_page()

    def navigate_to_home_page(self):
        self.click('#home_page')
        return self
