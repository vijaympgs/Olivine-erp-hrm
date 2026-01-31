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
        'table_name',
        'id',
        'menu_id',
        'menu_name',
        'module_name',
        'submodule',
        'view_type',
        'toolbar_config',
        'toolbar_config_backup',
        'applicable_toolbar_config',
        'original_toolbar_string',
        'toolbar_list_truncated',
        'toolbar_view_truncated',
        'toolbar_edit_truncated',
        'toolbar_create_truncated',
        'route_path',
        'component_name',
        'description',
        'menu_order',
        'display_order',
        'is_license_controlled',
        'is_active',
        'is_system_menu',
        'parent_menu_id',
        'created_by_id',
        'updated_by_id',
        'created_at',
        'updated_at',
    ]
    
    list_per_page = 20  # Show more items per page to see all columns
    
    def table_name(self, obj):
        """Display the database table name"""
        return obj._meta.db_table
    table_name.short_description = 'Table Name'
    table_name.admin_order_field = 'id'
    
    def toolbar_list_truncated(self, obj):
        """Display toolbar_list truncated to 15 chars"""
        return obj.toolbar_list[:15] if obj.toolbar_list else ''
    toolbar_list_truncated.short_description = 'Toolbar List (N=New, E=Edit, S=Save, C=Cancel, K=Clear, V=View, D=Delete, P=Print)'
    toolbar_list_truncated.admin_order_field = 'toolbar_list'
    
    def toolbar_view_truncated(self, obj):
        """Display toolbar_view truncated to 15 chars"""
        return obj.toolbar_view[:15] if obj.toolbar_view else ''
    toolbar_view_truncated.short_description = 'Toolbar View (Toolbar config for VIEW mode)'
    toolbar_view_truncated.admin_order_field = 'toolbar_view'
    
    def toolbar_edit_truncated(self, obj):
        """Display toolbar_edit truncated to 15 chars"""
        return obj.toolbar_edit[:15] if obj.toolbar_edit else ''
    toolbar_edit_truncated.short_description = 'Toolbar Edit (Toolbar config for EDIT mode)'
    toolbar_edit_truncated.admin_order_field = 'toolbar_edit'
    
    def toolbar_create_truncated(self, obj):
        """Display toolbar_create truncated to 15 chars"""
        return obj.toolbar_create[:15] if obj.toolbar_create else ''
    toolbar_create_truncated.short_description = 'Toolbar Create (Toolbar config for CREATE mode)'
    toolbar_create_truncated.admin_order_field = 'toolbar_create'
    
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
            'fields': ('menu_id', 'menu_name', 'module_name', 'submodule', 'component_name', 'description')
        }),
        ('Toolbar Configuration', {
            'fields': ('view_type', 'toolbar_config', 'toolbar_config_backup', 'applicable_toolbar_config', 'original_toolbar_string', 'toolbar_list', 'toolbar_view', 'toolbar_edit', 'toolbar_create')
        }),
        ('Navigation', {
            'fields': ('route_path', 'parent_menu_id', 'menu_order', 'display_order')
        }),
        ('Status', {
            'fields': ('is_license_controlled', 'is_active', 'is_system_menu')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'created_by_id', 'updated_by_id')
        }),
    )
    
    readonly_fields = ('applicable_toolbar_config', 'original_toolbar_string')
    
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
