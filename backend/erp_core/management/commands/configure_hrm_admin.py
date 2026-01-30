"""
Django management command to configure admin site for HRM

This command hides non-HRM models from the Django admin interface.
Run: python manage.py configure_hrm_admin
"""

from django.core.management.base import BaseCommand
from django.contrib import admin


class Command(BaseCommand):
    help = 'Configure admin site for HRM by hiding non-HRM models'

    def handle(self, *args, **options):
        self.stdout.write("Configuring admin site for HRM...")
        
        # Models to hide from admin (FMS, CRM, non-essential platform models)
        MODELS_TO_HIDE = [
            # FMS Models
            ('fms', 'paymentmethod'),
            ('fms', 'taxclassenhanced'),
            
            # CRM Models
            ('crm', 'customergroup'),
            ('crm', 'promotion'),
            ('crm', 'loyaltyprogram'),
            ('crm', 'customerloyalty'),
            
            # Non-essential Platform Models (Retail-specific)
            ('retail', 'itemmaster'),
            ('retail', 'brand'),
            ('retail', 'supplier'),
            ('retail', 'customer'),
            ('retail', 'taxclass'),
            ('retail', 'attribute'),
            ('retail', 'productattributetemplate'),
        ]
        
        # Set custom admin site headers
        admin.site.site_header = "HRM Administration"
        admin.site.site_title = "HRM Admin"
        admin.site.index_title = "Welcome to HRM Administration"
        
        # Hide non-HRM models
        hidden_count = 0
        for app_label, model_name in MODELS_TO_HIDE:
            try:
                model = admin.site.get_model(app_label, model_name)
                admin.site.unregister(model)
                self.stdout.write(self.style.SUCCESS(f"✓ Hidden {app_label}.{model_name} from admin"))
                hidden_count += 1
            except admin.sites.NotRegistered:
                # Model not registered, skip it
                pass
            except LookupError:
                # Model doesn't exist, skip it
                pass
        
        self.stdout.write(self.style.SUCCESS(f"\n✓ Admin site configured for HRM"))
        self.stdout.write(f"✓ Hidden {hidden_count} non-HRM models from admin")
