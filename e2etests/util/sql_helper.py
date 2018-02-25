import sqlite3

from django.contrib.auth.hashers import PBKDF2PasswordHasher

from e2etests.configs import DB_PATH


class SQLHelper:
    @staticmethod
    def create_connection():
        connection = sqlite3.connect(DB_PATH)
        return connection

    @staticmethod
    def get_user_id(user):
        connection = SQLHelper.create_connection()
        with connection:
            get_user_sql = ''' SELECT id FROM auth_user WHERE username = ? '''
            cursor = connection.cursor()
            cursor.execute(get_user_sql, (user.username,))
            user_id = cursor.fetchone()[0]
            return user_id

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
            return cursor.lastrowid

    @staticmethod
    def create_user_if_not_present(user):
        connection = SQLHelper.create_connection()
        with connection:
            find_user_sql = ''' SELECT id FROM auth_user WHERE username = ? '''
            cursor = connection.cursor()
            cursor.execute(find_user_sql, (user.username,))
            ids = cursor.fetchall()
            if len(ids) == 0:
                SQLHelper.create_user(user)
            else:
                return ids[0][0]

    @staticmethod
    def create_task(task):
        connection = SQLHelper.create_connection()
        with connection:
            create_task_sql = ''' INSERT INTO tasks_task(task_title, task_description, time_published, time_edited, user_id, time_estimated)
            VALUES(?, ?, ?, '', ?, ?)'''
            cursor = connection.cursor()
            cursor.execute(create_task_sql,
                           (task.title, task.description, task.published, task.user_id, task.estimated))

    @staticmethod
    def delete_user(user):
        connection = SQLHelper.create_connection()
        with connection:
            delete_user_sql = ''' DELETE FROM auth_user WHERE username = ? '''
            cursor = connection.cursor()
            cursor.execute(delete_user_sql, (user.username,))
