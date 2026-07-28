"""
WSGI config for coursemanager project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""
# wsgi.py: Entry point for WSGI-compatible (synchronous) servers
# like Gunicorn to run this Django project in production.
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coursemanager.settings')

application = get_wsgi_application()
