from django.apps import AppConfig


class HrmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'HRM.backend.hrm'
    verbose_name = 'Human Resources Management'
    
    def ready(self):
        # Admin is usually auto-discovered, but if manual registration is needed:
        try:
            import HRM.backend.hrm.admin
        except ImportError:
            pass





