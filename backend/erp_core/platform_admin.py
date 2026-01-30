"""
Django Admin Restructuring - Platform Governance
Implements clear architectural layer visibility through admin grouping
"""

from django.contrib import admin
from django.contrib.admin import AdminSite


class PlatformAdminSite(AdminSite):
    """
    Custom Admin Site with clear architectural layer separation
    """
    site_header = "Retail ERP Platform Administration"
    site_title = "Platform Admin"
    index_title = "Platform Governance & Operations"
    
    def get_app_list(self, request):
        """
        Override to enforce custom grouping and ordering
        """
        app_dict = self._build_app_dict(request)
        
        # Define explicit ordering
        app_order = [
            'licensing',  # Section 1
            'business_entities_opco',  # Section 2
            'business_entities_canonical',  # Section 3
            'business_entities_operational',  # Section 4
            'procurement',  # Section 5
            'pos',  # Section 5
            'inventory',  # Section 5
            'user_management',  # Section 6
            'auth',  # Section 6
        ]
        
        # Sort apps according to defined order
        app_list = sorted(
            app_dict.values(),
            key=lambda x: app_order.index(x['app_label']) if x['app_label'] in app_order else 999
        )
        
        return app_list


# Create custom admin site instance
platform_admin_site = PlatformAdminSite(name='platform_admin')


# ============================================================================
# ADMIN CONFIGURATION HELPERS
# ============================================================================

class ReadOnlyAdmin(admin.ModelAdmin):
    """
    Base class for read-only models (Canonical Masters, Audits)
    """
    def has_add_permission(self, request):
        return request.user.is_superuser
    
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser
    
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


class CanonicalMasterAdmin(ReadOnlyAdmin):
    """
    Canonical Masters - Definition Only
    Help text emphasizes non-transactional nature
    """
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return [f.name for f in self.model._meta.fields]
        return super().get_readonly_fields(request, obj)


class PlatformOnlyAdmin(admin.ModelAdmin):
    """
    Platform/Licensing - Superuser Only
    """
    def has_module_permission(self, request):
        return request.user.is_superuser
    
    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser


class AuditAdmin(admin.ModelAdmin):
    """
    Audit records - Read-only for all
    """
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser  # Allow cleanup by superuser only




