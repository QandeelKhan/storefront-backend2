release: python manage.py migrate
web: gunicorn StorefrontBackend2.wsgi
worker: celery -A StorefrontBackend2 worker