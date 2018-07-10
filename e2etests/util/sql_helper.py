from datetime import datetime

import psycopg2
from django.contrib.auth.hashers import PBKDF2PasswordHasher

from e2etests.configs import DB_SETUP


class SQLHelper:
    @staticmethod
    def create_connection():
        connection = psycopg2.connect(host=DB_SETUP['host'], user=DB_SETUP['user'], password=DB_SETUP['password'],
                                      database=DB_SETUP['database'])
        return connection

    @staticmethod
    def get_user_id(user):
        connection = SQLHelper.create_connection()
        with connection:
            get_user_sql = ''' SELECT id FROM auth_user WHERE username = %s '''
            cursor = connection.cursor()
            cursor.execute(get_user_sql, (user.username,))
            user_id = cursor.fetchone()[0]
            return user_id

    @staticmethod
    def create_user(user):
        connection = SQLHelper.create_connection()
        with connection:
            create_user_sql = ''' INSERT INTO
                auth_user(password, last_login, is_superuser, username, first_name, last_name,
                email, is_staff, is_active, date_joined)
                VALUES(%s,NULL,'0',%s,'', '','admin@test.com','0','1',%s) '''
            cursor = connection.cursor()
            cursor.execute(create_user_sql,
                           (PBKDF2PasswordHasher().encode(user.password, 'salt'), user.username, datetime.now()))
            return cursor.lastrowid

    @staticmethod
    def create_user_if_not_present(user):
        connection = SQLHelper.create_connection()
        with connection:
            find_user_sql = ''' SELECT id FROM auth_user WHERE username = %s '''
            cursor = connection.cursor()
            cursor.execute(find_user_sql, (user.username,))
            ids = cursor.fetchall()
            if len(ids) == 0:
                return SQLHelper.create_user(user)
            else:
                return ids[0][0]

    @staticmethod
    def create_task(task):
        connection = SQLHelper.create_connection()
        with connection:
            create_task_sql = ''' INSERT INTO tasks_task(task_title, task_description, time_published, time_edited, user_id, time_estimated, status, priorities)
            VALUES(%s, %s, %s, NULL, %s, %s, 'New', %s)'''
            cursor = connection.cursor()
            cursor.execute(create_task_sql,
                           (task.title, task.description, task.published, task.user_id, task.estimated, task.priorities))

    @staticmethod
    def delete_user(user):
        connection = SQLHelper.create_connection()
        with connection:
            delete_user_sql = ''' DELETE FROM auth_user WHERE username = %s '''
            cursor = connection.cursor()
            cursor.execute(delete_user_sql, (user.username,))

    @staticmethod
    def delete_tasks_for_user(user):
        connection = SQLHelper.create_connection()
        with connection:
            delete_task_sql = ''' DELETE FROM tasks_task WHERE user_id = %s '''
            cursor = connection.cursor()
            cursor.execute(delete_task_sql, (user.user_id,))
