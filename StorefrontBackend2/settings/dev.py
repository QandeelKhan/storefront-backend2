import os
from .common import *
from dotenv import load_dotenv
load_dotenv()

DEBUG = True

ALLOWED_HOSTS = ["*"]

SECRET_KEY = os.getenv('SECRET_KEY')
# for mysql:
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql',
        # or
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'storefront2',
        'HOST': 'localhost',
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD')
    },
    'mysql': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront2',
        # 'HOST': 'mysql',
        'HOST': 'localhost',
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD')
    },
}


# for postgresql:
# - sudo su
# - su postgres -c psql postgres
# - CREATE DATABASE dbname;
# - CREATE USER djangouser WITH ENCRYPTED PASSWORD 'myPasswordHere';
# - GRANT ALL PRIVILEGES ON DATABASE dbname TO djangouser;

# moving mysql or sqlite3 to postgresql steps
# 1 (Create all DB data to a json file): python manage.py dumpdata > dumpdata.json
# set postgresql(any) in settings.py
# 2 (Sync new DB) :python manage.py migrate --run-syncdb
# 3 [exclude all content(contenttype) data]: python manage.py shell
# 4 [inside shell, import contenttype data from django]: from django.contrib.contenttypes.models import ContentType
# 5 [deleting all the content type data]: ContentType.objects.all().delete()
# 6 [quit]: quit()
# 7 [loading data from json file to the db we want]: python manage.py loaddata datadump.json

# DATABASES = {
#     'default': {
#         # 'ENGINE': 'django.db.backends.postgresql',
#         # or
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'storefront2',
#         'HOST': 'localhost',
#         # or default postgresql port 'PORT': 5432,
#         'USER': os.getenv('DB_USER'),
#         'PASSWORD': os.getenv('DB_PASSWORD')
#     }
# }

CELERY_BROKER_URL = 'redis://redis:6379/1'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/2',
        'TIMEOUT': 10 * 60,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp4dev'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = os.getenv('PASSWORD')
EMAIL_PORT = 2525
DEFAULT_FROM_EMAIL = os.getenv('EMAIL')

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True
}
