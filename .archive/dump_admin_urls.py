import os
import sys
import django

sys.path.append(os.path.join(os.getcwd(), 'backend'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.dev')
django.setup()

from django.contrib import admin
from django.apps import apps

print("Installed Apps:")
for app_config in apps.get_app_configs():
    if 'toolbar' in app_config.name:
        print(f"  {app_config.name} ({app_config.label})")

print("Consolidated Toolbar & Menu Models:")
for model, model_admin in admin.site._registry.items():
    if 'toolbar' in model._meta.app_label or 'toolbar' in model._meta.model_name or model._meta.app_label == 'user_management':
        app_label = model._meta.app_label
        model_name = model._meta.model_name
        verbose_name = model._meta.verbose_name
        url = f"/admin/{app_label}/{model_name}/"
        print(f"{app_label:<20} | {verbose_name:<30} | {url}")
