from selene import browser


class PageNotFoundPage:
    def read_error_message(self):
        return browser.element('#page_not_found').text
