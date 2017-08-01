from .common import *

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['.no-ip.org', '.amazonaws.com']

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pickem',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'pickem.whatever.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}
