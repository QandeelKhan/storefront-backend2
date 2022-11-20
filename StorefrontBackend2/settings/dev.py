import dj_database_url
import os
from .common import *
from dotenv import load_dotenv
load_dotenv()

DEBUG = True

ALLOWED_HOSTS = ["*"]

SECRET_KEY = os.getenv('SECRET_KEY')
# for mysql:
# DATABASES = {
#     'default': {
#         # 'ENGINE': 'django.db.backends.postgresql',
#         # or
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'storefront2',
#         'HOST': 'localhost',
#         'USER': os.getenv('DEV_DB_USER'),
#         'PASSWORD': os.getenv('DEV_DB_PASSWORD')
#     },
#     'mysql': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'storefront2',
#         # 'HOST': 'mysql',
#         'HOST': 'localhost',
#         'USER': os.getenv('DEV_DB_USER'),
#         'PASSWORD': os.getenv('DEV_DB_PASSWORD')
#     },
# }


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
# 7 [loading data from json file to the db we want]: python manage.py loaddata dumpdata.json


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('PROD_DB_NAME'),
        'USER': os.getenv('PROD_DB_USER'),
        'PASSWORD': os.getenv('PROD_DB_PASSWORD'),
        'HOST': "app-f50b6b84-f0cf-46fb-ae93-f8b96dde1e70-do-user-12706543-0.b.db.ondigitalocean.com",
        'OPTIONS': {'sslmode': 'verify-full', 'sslrootcert': os.path.join(BASE_DIR, 'ca-certificate.crt')},
        'PORT': "25060"
    }
}

# DATABASES = {
#     'default': dj_database_url.config()
# }
# DATABASES['default'] = dj_database_url.config(
#     default='postgresql://user-StorefrontBackend2:AVNS_UrInpPSqKbDIqefihLV@app-f50b6b84-f0cf-46fb-ae93-f8b96dde1e70-do-user-12706543-0.b.db.ondigitalocean.com:25060/StorefrontBackend2')


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
