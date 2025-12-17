"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Collect static files on first request (Vercel serverless)
try:
    from django.core.management import call_command
    if os.environ.get('VERCEL'):
        call_command('collectstatic', '--noinput', '--clear')
except Exception as e:
    print(f"Static files collection skipped: {e}")

application = get_wsgi_application()
app = application
