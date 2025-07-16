"""
WSGI config for guitar_backend project.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'guitar_backend.settings')

application = get_wsgi_application()

# === TEMPORARY: Auto-run migrate and create superuser ===
import django
django.setup()

from django.core.management import call_command
from django.contrib.auth import get_user_model

call_command('migrate')

User = get_user_model()
username = "admin"
password = "admin122"
email = "admin@example.com"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, password=password, email=email)
