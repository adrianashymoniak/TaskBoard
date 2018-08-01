from e2etests.domain.user import User
from e2etests.pages.delete_user_account_page import DeleteUserAccountPage


class ViewProfilePage(DeleteUserAccountPage):
    def read_profile_information(self):
        username = self.read_user_name()
        first_name = self.read_text('#first_name')
        last_name = self.read_text('#last_name')
        email = self.read_text('#email')
        user = User(username=username, first_name=first_name, last_name=last_name, email=email)
        return user

    def read_user_name(self):
        return self.read_text('#username')

    def logout(self):
        self.click('#logout')
        return self.login_page()
