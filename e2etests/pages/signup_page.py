from e2etests.pages.base_page import BasePage


class SignUpPage(BasePage):
    @staticmethod
    def open():
        SignUpPage.load_relative_url("/signup/")
        return SignUpPage()

    def signup_as(self, user):
        self.set_value('#username', user.username)
        self.set_value('#email', user.email)
        self.set_value('#password1', user.password)
        self.set_value('#password2', user.password_confirm)
        self.click('#signup_btn')
        return self.home_page()
