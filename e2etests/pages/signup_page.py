from selene import browser

from e2etests.pages.home_page import HomePage


class SignUpPage:
    @staticmethod
    def open():
        browser.open_url("/signup/")
        return SignUpPage()

    def signup_as(self, user):
        browser.element('#username').set_value(user.username)
        browser.element('#email').set_value(user.email)
        browser.element('#password1').set_value(user.password)
        browser.element('#password2').set_value(user.password_confirm)
        browser.element('#signup_btn').click()
        return HomePage()
