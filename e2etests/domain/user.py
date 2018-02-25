class User:
    def __init__(self, username, password, email=None, password_confirm=None, user_id=None):
        self.username = username
        self.password = password
        self.email = email
        self.password_confirm = password_confirm
        self.user_id = user_id
