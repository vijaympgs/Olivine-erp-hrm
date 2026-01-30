from django.contrib import admin
from .models import LicenseConfiguration
from core.licensing.backend.business_entities.models import Company


@admin.register(LicenseConfiguration)
class LicenseConfigurationAdmin(admin.ModelAdmin):
    """
    🔒 LICENSE CONFIGURATION (Platform Admin Only)
    
    Defines limits for Companies and Locations.
    Only one active license allowed at a time.
    """
    list_display = ('licensee_name', 'license_key', 'max_companies', 'max_locations_per_company', 
                    'max_total_locations', 'is_active', 'valid_from', 'valid_until')
    list_filter = ('is_active', 'valid_from')
    search_fields = ('licensee_name', 'license_key')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('🔒 License Identification', {
            'fields': ('license_key', 'licensee_name')
        }),
        ('📊 Platform Limits', {
            'fields': ('max_companies', 'max_locations_per_company', 'max_total_locations'),
            'description': 'These limits govern how many Companies and Locations can be created'
        }),
        ('⏰ Validity', {
            'fields': ('is_active', 'valid_from', 'valid_until')
        }),
        ('Audit', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def has_module_permission(self, request):
        """Only superusers can access licensing"""
        return request.user.is_superuser
    
    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser
    
    def has_add_permission(self, request):
        return request.user.is_superuser
    
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser
    
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


# LicensedEntity is a proxy for Company - for viewing only
from .models import LicensedEntity

@admin.register(LicensedEntity)
class LicensedEntityAdmin(admin.ModelAdmin):
    """
    🏢 BUSINESS ENTITY (Read-Only View)
    
    This is a read-only view of Companies from a licensing perspective.
    Use the Companies section to manage operational companies.
    """
    list_display = ('name', 'code', 'status', 'current_usage')
    readonly_fields = ('name', 'code', 'legal_entity_type', 'status', 'default_currency', 
                      'created_at', 'updated_at')
    search_fields = ('name', 'code')
    
    def current_usage(self, obj):
        """Show current vs allowed usage"""
        try:
            license_config = LicenseConfiguration.get_active_license()
            total_companies = Company.objects.count()
            return f"{total_companies} / {license_config.max_companies} Companies"
        except:
            return "No active license"
    current_usage.short_description = 'Current Usage'
    
    def has_add_permission(self, request):
        return False  # Use Companies section to add
    
    def has_delete_permission(self, request, obj=None):
        return False  # Use Companies section to delete
    
    def has_change_permission(self, request, obj=None):
        return False  # Use Companies section to edit
    
    def has_module_permission(self, request):
        return request.user.is_superuser  # Platform admin only






