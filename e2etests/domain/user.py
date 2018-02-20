class User:
    def __init__(self, username, password, email=None, password_confirm=None):
        self.username = username
        self.password = password
        self.email = email
        self.password_confirm = password_confirm
