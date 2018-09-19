from e2etests.pages.base_page import BasePage


class LoginPage(BasePage):
    def login_as(self, user):
        self.set_value('#id-username', user.username)
        self.set_value('#id-password', user.password)
        self.click('#login-btn')
        return self.home_page()

    def is_signup_link_displayed(self):
        return self.is_element_displayed('#signup')
