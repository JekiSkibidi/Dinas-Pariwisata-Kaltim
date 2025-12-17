"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from pathlib import Path

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Collect static files on first run
BASE_DIR = Path(__file__).resolve().parent.parent
staticfiles_dir = BASE_DIR / 'staticfiles'
if not staticfiles_dir.exists():
    try:
        from django.core.management import call_command
        call_command('collectstatic', '--noinput', '--clear')
    except Exception as e:
        print(f"Warning: Could not collect static files: {e}")

application = get_wsgi_application()
app = application
