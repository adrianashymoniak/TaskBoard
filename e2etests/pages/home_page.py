from selene import browser


class HomePage:
    def greeting(self):
        return browser.element('#greeting')
