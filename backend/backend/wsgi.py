"""
wsgi.py
WSGI config for the ZenJob Clone backend project. Used for deploying with WSGI servers.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_wsgi_application()
