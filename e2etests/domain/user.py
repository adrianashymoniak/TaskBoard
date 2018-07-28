class User:
    def __init__(self, username=None, password=None, email=None, password_confirm=None, user_id=None, first_name=None,
                 last_name=None):
        self.username = username
        self.password = password
        self.email = email
        self.password_confirm = password_confirm
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
