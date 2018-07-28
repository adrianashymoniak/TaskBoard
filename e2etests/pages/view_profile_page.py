from selene import browser

from e2etests.domain.user import User
from e2etests.pages.delete_user_account_page import DeleteUserAccountPage


class ViewProfilePage(DeleteUserAccountPage):
    def read_profile_information(self):
        username = self.read_user_name()
        first_name = browser.element('#first_name').text
        last_name = browser.element('#last_name').text
        email = browser.element('#email').text
        user = User(username=username, first_name=first_name, last_name=last_name, email=email)
        return user

    def read_user_name(self):
        return browser.element('#username').text

    def logout(self):
        browser.element('#logout').click()
        from e2etests.pages.login_page import LoginPage
        return LoginPage()
