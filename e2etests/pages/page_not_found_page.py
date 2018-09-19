from e2etests.pages.base_page import BasePage


class PageNotFoundPage(BasePage):
    def read_error_message(self):
        return self.read_text('#page-not-found')
