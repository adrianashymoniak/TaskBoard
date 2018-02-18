import sqlite3

from django.contrib.auth.hashers import PBKDF2PasswordHasher

from e2etests.configs import DB_PATH


class SQLHelper:
    @staticmethod
    def create_connection():
        connection = sqlite3.connect(DB_PATH)
        return connection

    @staticmethod
    def create_user(user):
        connection = SQLHelper.create_connection()
        with connection:
            create_user_sql = ''' INSERT INTO
                'auth_user'('password', 'is_superuser', 'username', 'first_name',
                'email', 'is_staff', 'is_active', 'date_joined', 'last_name')
                VALUES(?,0,?,'','admin@test.com',0,1,'','') '''
            cursor = connection.cursor()
            cursor.execute(create_user_sql, (PBKDF2PasswordHasher().encode(user.password, 'salt'), user.username))

    @staticmethod
    def create_user_if_not_present(user):
        connection = SQLHelper.create_connection()
        with connection:
            find_user_sql = ''' SELECT username FROM auth_user WHERE username = ? '''
            cursor = connection.cursor()
            cursor.execute(find_user_sql, (user.username,))
            if len(cursor.fetchall()) == 0:
                SQLHelper.create_user(user)
