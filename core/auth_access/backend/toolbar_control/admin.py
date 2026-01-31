from django.contrib import admin, messages
from django.utils.html import format_html
from django.http import HttpResponse
import csv
from datetime import datetime
from .models import ToolbarControlProxy, ToolbarItemProxy, RoleToolbarPermissionProxy, UserToolbarPermissionProxy

# Re-use filters from user_management if they are exported, but for clean separation let's define them or import them.
# For now, let's import them from the other admin or recreate them.
from ..user_management.admin import MenuLevelFilter, SubgroupL2Filter

class ApplicationFilter(admin.SimpleListFilter):
    title = 'Application'
    parameter_name = 'module_name'

    def lookups(self, request, model_admin):
        # We can dynamically get these or hardcode for performance/clarity
        return [
            ('RETAIL', 'Retail Operations'),
            ('FMS', 'Financial Management'),
            ('HRM', 'Human Resources'),
            ('CRM', 'Customer Relationship Management'),
            ('ADMIN', 'Administration'),
            ('SETUP', 'System Setup'),
            ('SYSTEM', 'System Infrastructure'),
        ]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(module_name=self.value())
        return queryset

class SubmoduleFilter(admin.SimpleListFilter):
    title = 'Submodule'
    parameter_name = 'submodule'

    def lookups(self, request, model_admin):
        module = request.GET.get('module_name')
        if not module:
            return []
        
        # Get unique submodules for the selected application
        submodules = model_admin.model.objects.filter(
            module_name=module,
            submodule__isnull=False
        ).exclude(submodule='').values_list('submodule', flat=True).distinct().order_by('submodule')
        
        return [(s, s.replace('-', ' ').title()) for s in submodules]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(submodule=self.value())
        return queryset

@admin.register(ToolbarControlProxy)
class ERPToolbarControlAdmin(admin.ModelAdmin):
    list_display = ['module_name', 'master_toolbar_string', 'description']
    list_editable = ['master_toolbar_string']
    search_fields = ['module_name', 'master_toolbar_string']

@admin.register(ToolbarItemProxy)
class ItemAdmin(admin.ModelAdmin):
    """
    Toolbar Registry - Registered as 'Item' in Admin
    """
    list_display = (
        'table_name',
        'id',
        'app_badge',
        'menu_id',
        'menu_name',
        'module_name',
        'submodule',
        'view_type',
        'toolbar_config',
        'toolbar_config_backup',
        'applicable_toolbar_config',
        'original_toolbar_string',
        'toolbar_list',
        'toolbar_view',
        'toolbar_edit',
        'toolbar_create',
        'route_path',
        'component_name',
        'description',
        'menu_order',
        'display_order',
        'is_license_controlled',
        'is_active',
        'is_system_menu',
        'parent_menu',
        'created_by',
        'updated_by',
        'created_at',
        'updated_at',
    )
    
    list_per_page = 20  # Show more items per page to see all columns
    
    def table_name(self, obj):
        """Display the database table name"""
        return obj._meta.db_table
    table_name.short_description = 'Table Name'
    table_name.admin_order_field = 'id'

    list_filter = (
        'view_type',
        ApplicationFilter,
        SubmoduleFilter,
        MenuLevelFilter,
    )

    search_fields = (
        'menu_name',
        'menu_id',
        'module_name',
        'submodule',
        'route_path',
    )

    list_editable = ('toolbar_list', 'toolbar_view', 'toolbar_edit', 'toolbar_create', 'is_active')
    ordering = ('module_name', 'menu_order', 'menu_name')

    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Basic Information', {
            'fields': ('menu_name', 'menu_id', 'module_name', 'parent_menu', 'view_type')
        }),
        ('Toolbar Configuration', {
            'fields': ('toolbar_list', 'toolbar_view', 'toolbar_edit', 'toolbar_create', 'applicable_toolbar_config', 'original_toolbar_string', 'is_license_controlled'),
            'description': "Action Codes: N=New, E=Edit, S=Save, C=Cancel, K=Clear, V=View, D=Delete, P=Print, etc."
        }),
        ('Frontend Routing', {
            'fields': ('route_path', 'component_name', 'menu_order'),
            'classes': ('collapse',),
        }),
    )

    def button_count_display(self, obj):
        if obj.applicable_toolbar_config:
            return len(obj.applicable_toolbar_config)
        return 0
    button_count_display.short_description = 'Cnt'

    def app_badge(self, obj):
        colors = {
            'RETAIL': '#f44336',
            'FMS': '#4caf50',
            'CRM': '#2196f3',
            'HRM': '#ff9800',
        }
        color = colors.get(obj.module_name, '#9e9e9e')
        return format_html(
            '<span style="background:{};color:white;padding:3px 8px;border-radius:4px;font-size:11px;font-weight:bold;">{}</span>',
            color,
            obj.module_name
        )
    app_badge.short_description = 'App'

    def menu_name_display(self, obj):
        path = []
        p = obj
        while p:
            path.append(p.menu_name)
            p = p.parent_menu
        path.reverse()
        breadcrumb = " ▸ ".join(path)
        return breadcrumb
    menu_name_display.short_description = 'Lineage'

    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        """
        Export selected menu items as CSV
        """
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename=ERP_Menu_Items_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
        
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
        
        self.message_user(request, f"{queryset.count()} items exported successfully.", messages.SUCCESS)
        return response
    
    export_as_csv.short_description = "Export Selected as CSV"


@admin.register(RoleToolbarPermissionProxy)
class RolePermissionAdmin(admin.ModelAdmin):
    list_display = ['role', 'menu_item', 'toolbar_override', 'override_enabled', 'updated_at']
    list_filter = ['role', 'override_enabled']
    search_fields = ['role__role_name', 'menu_item__menu_name']
    
@admin.register(UserToolbarPermissionProxy)
class UserPermissionAdmin(admin.ModelAdmin):
    list_display = ['user', 'menu_item', 'toolbar_override', 'override', 'updated_at']
    list_filter = ['user', 'override']
    search_fields = ['user__username', 'menu_item__menu_name']
