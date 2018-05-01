from .base import *
import dj_database_url

ENVIRONMENT = 'production'
ALLOWED_HOSTS = ['']
SECRET_KEY = 'SECRET_KEY'
DEBUG = False
DATABASES = {
    'default': dj_database_url.config(
        default='DATABASE_URL'
    )
}
