
import os
import sys
import django
from django.conf import settings

sys.path.append(os.path.join(os.getcwd(), 'backend'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.dev')
django.setup()

print(f"MEDIA_URL: '{settings.MEDIA_URL}'")
print(f"STATIC_URL: '{settings.STATIC_URL}'")
print(f"APPEND_SLASH: {settings.APPEND_SLASH}")
print(f"DEBUG: {settings.DEBUG}")
print(f"MIDDLEWARE: {settings.MIDDLEWARE}")



