"""
Django Admin for User Management Models
Includes CSV export functionality for ERPMenuItem
"""

from django.contrib import admin
from django.http import HttpResponse
import csv
from datetime import datetime

from .models import ERPMenuItem, Role, RolePermission


class ExportCsvMixin:
    """
    Mixin to add CSV export functionality to any ModelAdmin
    """
    def export_as_csv(self, request, queryset):
        """
        Export selected items as CSV
        """
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={meta.verbose_name_plural.replace(" ", "_")}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
        
        writer = csv.writer(response)
        writer.writerow(field_names)
        
        for obj in queryset:
            row = []
            for field in field_names:
                value = getattr(obj, field)
                # Handle foreign keys
                if hasattr(value, 'pk'):
                    value = value.pk
                row.append(value)
            writer.writerow(row)
        
        return response
    
    export_as_csv.short_description = "Export Selected as CSV"


@admin.register(ERPMenuItem)
class ERPMenuItemAdmin(admin.ModelAdmin, ExportCsvMixin):
    """
    Admin interface for ERPMenuItem with export functionality
    """
    list_display = [
        'menu_id',
        'menu_name',
        'module_name',
        'view_type',
        'toolbar_config',
        'applicable_toolbar_config',
        'route_path',
        'is_active',
        'display_order'
    ]
    
    list_filter = [
        'module_name',
        'view_type',
        'is_active',
    ]
    
    search_fields = [
        'menu_id',
        'menu_name',
        'route_path',
    ]
    
    ordering = ['module_name', 'display_order', 'menu_name']
    
    # Export actions
    actions = ['export_as_csv', 'export_retail_only', 'export_all_modules']
    
    def export_retail_only(self, request, queryset):
        """
        Export only RETAIL module items
        """
        retail_items = ERPMenuItem.objects.filter(module_name='RETAIL', is_active=True)
        return self.export_as_csv(request, retail_items)
    
    export_retail_only.short_description = "Export ALL RETAIL Items as CSV"
    
    def export_all_modules(self, request, queryset):
        """
        Export all active items from all modules
        """
        all_items = ERPMenuItem.objects.filter(is_active=True).order_by('module_name', 'display_order')
        return self.export_as_csv(request, all_items)
    
    export_all_modules.short_description = "Export ALL Active Items (All Modules)"
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('menu_id', 'menu_name', 'module_name')
        }),
        ('Toolbar Configuration', {
            'fields': ('view_type', 'toolbar_config', 'applicable_toolbar_config')
        }),
        ('Navigation', {
            'fields': ('route_path', 'parent_menu', 'display_order')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )
    
    def get_readonly_fields(self, request, obj=None):
        """
        Make fields read-only for non-superusers
        """
        if not request.user.is_superuser:
            return ['menu_id', 'module_name', 'view_type']
        return []


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin, ExportCsvMixin):
    """
    Admin interface for Role
    """
    list_display = ['role_name', 'description', 'is_active']
    list_filter = ['is_active']
    search_fields = ['role_name', 'description']
    actions = ['export_as_csv']


@admin.register(RolePermission)
class RolePermissionAdmin(admin.ModelAdmin, ExportCsvMixin):
    """
    Admin interface for RolePermission
    """
    list_display = ['role', 'menu_item', 'can_view', 'can_create', 'can_edit', 'can_delete']
    list_filter = ['role', 'can_view', 'can_create', 'can_edit', 'can_delete']
    search_fields = ['role__role_name', 'menu_item__menu_name']
    actions = ['export_as_csv']
