from .base import *
import dj_database_url

ENVIRONMENT = 'staging'
ALLOWED_HOSTS = ['*']
SECRET_KEY = 'SECRET_KEY'
DEBUG = True
DATABASES = {
    'default': dj_database_url.config(
        default='DATABASE_URL'
    )
}
