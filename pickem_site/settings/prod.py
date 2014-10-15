from .common import *

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pickem',
        'USER': 'atheiman',
        'PASSWORD': 'atheimanpass',
        'HOST': 'pickem.cih0o8lc13of.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}
