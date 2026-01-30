import os
import django
import sys

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.dev')
sys.path.append(os.getcwd())
sys.path.append(os.path.join(os.getcwd(), 'backend'))
django.setup()

from django.contrib import admin

site = admin.site
print(f"Admin Site: {site}")

registered_models = site._registry.keys()
app_labels = sorted(set(m._meta.app_label for m in registered_models))

print("\nRegistered App Labels Count:", len(app_labels))
print("Labels:", ", ".join(app_labels))

# Check for specific expected labels
expected = ['pos', 'inventory', 'sales', 'procurement', 'business_entities', 'company', 'company_master']
print("\nChecking expected labels:")
for exp in expected:
    status = "OK" if exp in app_labels else "MISSING"
    print(f"- {exp}: {status}")
