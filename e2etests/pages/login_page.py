from selene import browser

from e2etests.pages.home_page import HomePage


class LoginPage:
    @staticmethod
    def open():
        browser.open_url('/')
        return LoginPage()

    def login_as(self, user):
        browser.element('#id_username').set_value(user.username)
        browser.element('#id_password').set_value(user.password)
        browser.element('#login').click()
        return HomePage()
