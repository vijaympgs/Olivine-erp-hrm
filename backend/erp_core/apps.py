from django.contrib.admin.apps import AdminConfig


class RetailAdminConfig(AdminConfig):
    default_site = 'erp_core.admin_site.RetailAdminSite'
    
    def ready(self):
        super().ready()  # This triggers autodiscover()
        # Import unified admin registrations (HRM, FMS, CRM)
        try:
            from erp_core import unified_full_admin  # noqa: F401
        except ImportError as e:
            print(f"Warning: Could not import unified admin: {e}")


