import os
import django
import sys

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.dev')
# Add current directory to path
sys.path.append(os.getcwd())
django.setup()

from django.contrib import admin
from django.apps import apps

site = admin.site
print(f"Admin Site Class: {site.__class__.__module__}.{site.__class__.__name__}")

registered_apps = site._registry.keys()
app_labels = set()
for model in registered_apps:
    app_labels.add(model._meta.app_label)

print("\nRegistered App Labels:")
for label in sorted(list(app_labels)):
    models = [m.__name__ for m in registered_apps if m._meta.app_label == label]
    print(f"- {label}: {', '.join(models)}")

print("\nApp List from get_app_list:")
from django.test import RequestFactory
rf = RequestFactory()
request = rf.get('/admin/')
from django.contrib.auth.models import User
# Just a mock user
user = User.objects.first() or User(is_superuser=True, is_staff=True)
request.user = user

app_list = site.get_app_list(request)
print(f"Number of groups in app_list: {len(app_list)}")
for app in app_list:
    print(f"- Group: {app['name']} (label: {app['app_label']})")
    for model in app['models']:
        print(f"  - {model['object_name']}")
