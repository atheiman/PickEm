from .common import *

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# ---------------------------------------------------------------------------- #
# Steps to create a local dev db
# Create the local sqlite db:
# $ python manage.py migrate --settings=settings.dev
# Get a batch of data from the prod db:
# $ python manage.py dumpdata --settings=settings.prod > /tmp/datadump.json
# Import the data dump to the local dev db:
# $ python manage.py loaddata /tmp/datadump.json --settings=settings.dev
# ---------------------------------------------------------------------------- #

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
