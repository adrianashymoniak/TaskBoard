from selene import browser


class PageWithLeaveMessage:
    def navigate_to_task_detail_page_with_message(self):
        browser.element('#go_detail_page').click()
        return self

    def navigate_to_task_detail_page_without_message(self):
        browser.element('#go_detail_page').click()
        from e2etests.pages.task_detail_page import TaskDetailPage
        return TaskDetailPage()

    def discard_leaving(self):
        browser.driver().switch_to.alert.dismiss()
        return self

    def confirm_leaving_to_task_detail_page(self):
        browser.driver().switch_to.alert.accept()
        from e2etests.pages.task_detail_page import TaskDetailPage
        return TaskDetailPage()

    def confirm_leaving_to_home_page(self):
        browser.driver().switch_to.alert.accept()
        from e2etests.pages.home_page import HomePage
        return HomePage()

    def navigate_to_home_page(self):
        browser.element('#home_page').click()
        return self
