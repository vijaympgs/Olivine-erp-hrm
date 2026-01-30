from django.contrib import admin, messages
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from .models import (
    Employee, Role, UserProfile,
    UserRole, PermissionAudit, RoleAssignmentAudit,
    GroupPermission, POSFunction, RolePOSFunctionMapping, RolePermission,
    UserCompanyMapping, ERPMenuItem, ERPToolbarControl
)

User = get_user_model()

# ============================================================================
# LEGACY MODELS (Read-Only)
# ============================================================================

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_code', 'first_name', 'last_name', 'email', 'department', 'designation', 'status']
    list_filter = ['status', 'department', 'employment_type', 'gender']
    search_fields = ['employee_code', 'first_name', 'last_name', 'email']
    readonly_fields = ['employee_code', 'created_at', 'updated_at']
    ordering = ['last_name', 'first_name']
    
    def has_add_permission(self, request):
        return False  # Read-only for legacy model
    
    def has_delete_permission(self, request, obj=None):
        return False  # Read-only for legacy model


# ============================================================================
# USER & PERMISSION MANAGEMENT MODELS
# ============================================================================

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fields = ['employee_code', 'department', 'designation', 'is_active']


class UserRoleInline(admin.TabularInline):
    model = UserRole
    fk_name = 'user'  # Specify which ForeignKey to use
    extra = 1
    fields = ['role', 'assigned_by', 'assigned_at', 'is_active']
    readonly_fields = ['assigned_at']


class UserCompanyInline(admin.TabularInline):
    model = UserCompanyMapping
    fk_name = 'user'
    extra = 1
    fields = ['company', 'is_active', 'is_default']


class CustomUserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline, UserRoleInline, UserCompanyInline)
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'get_employee_code']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'groups']
    
    def get_employee_code(self, obj):
        return obj.profile.employee_code if hasattr(obj, 'profile') else '-'
    get_employee_code.short_description = 'Employee Code'


# Re-register User with our custom admin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)



@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['role_key', 'role_name', 'is_system_role', 'is_active', 'created_at']
    list_filter = ['is_system_role', 'is_active']
    search_fields = ['role_key', 'role_name']
    readonly_fields = ['created_at']
    ordering = ['role_name']


@admin.register(RolePermission)
class RolePermissionAdmin(admin.ModelAdmin):
    list_display = ['role', 'menu_item', 'override_enabled', 'created_at']
    list_filter = ['override_enabled', 'role']
    search_fields = ['role__role_name', 'menu_item__menu_name']
    fieldsets = (
        ('Permission Configuration', {
            'fields': ('role', 'menu_item', 'toolbar_override', 'override_enabled')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )





# ============================================================================
# MENU ITEM TYPE ADMIN - HIERARCHICAL DISPLAY
# ============================================================================

# Custom filter for menu level
class MenuLevelFilter(admin.SimpleListFilter):
    """Filter by menu level (L1, L2, L3, L4)"""
    title = 'Menu Level'
    parameter_name = 'menu_level'
    
    def lookups(self, request, model_admin):
        return [
            ('1', 'L1 only'),
            ('2', 'L2 only'),
            ('3', 'L3 only'),
            ('4', 'L4 only'),
        ]
    
    def queryset(self, request, queryset):
        if self.value():
            target_depth = int(self.value()) - 1
            filtered_ids = []
            for item in queryset:
                depth = 0
                current = item
                while current.parent_menu:
                    depth += 1
                    current = current.parent_menu
                if depth == target_depth:
                    filtered_ids.append(item.id)
            return queryset.filter(id__in=filtered_ids)
        return queryset


class SubgroupL2Filter(admin.SimpleListFilter):
    """Filter by L2 Subgroup"""
    title = 'Subgroup (L2)'
    parameter_name = 'subgroup_l2'
    
    def lookups(self, request, model_admin):
        selected_module = request.GET.get('module_name', None)
        l2_items = MenuItemType.objects.filter(
            parent_menu__isnull=False,
            parent_menu__parent_menu__isnull=True
        ).select_related('parent_menu')
        
        if selected_module:
            l2_items = l2_items.filter(module_name=selected_module)
        
        l2_items = l2_items.order_by('module_name', 'parent_menu__menu_order', 'menu_order', 'menu_name')
        return [(item.id, item.menu_name) for item in l2_items]
    
    def queryset(self, request, queryset):
        if self.value():
            try:
                l2_item = MenuItemType.objects.get(id=self.value())
                l3_items = MenuItemType.objects.filter(parent_menu=l2_item)
                l4_items = MenuItemType.objects.filter(parent_menu__parent_menu=l2_item)
                item_ids = [l2_item.id] + list(l3_items.values_list('id', flat=True)) + list(l4_items.values_list('id', flat=True))
                return queryset.filter(id__in=item_ids)
            except MenuItemType.DoesNotExist:
                return queryset
        return queryset





@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'assigned_by', 'assigned_at', 'is_active']
    list_filter = ['role', 'is_active', 'assigned_at']
    search_fields = ['user__username', 'user__email', 'role__role_name']
    readonly_fields = ['assigned_at']
    ordering = ['-assigned_at']


@admin.register(UserCompanyMapping)
class UserCompanyMappingAdmin(admin.ModelAdmin):
    list_display = ['user', 'company', 'is_active', 'is_default', 'created_at']
    list_filter = ['is_active', 'is_default']
    search_fields = ['user__username', 'company__name']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']





@admin.register(GroupPermission)
class GroupPermissionAdmin(admin.ModelAdmin):
    list_display = ['group', 'role_key', 'menu_item', 'can_access', 'can_view', 'can_create', 'can_edit', 'can_delete']
    list_filter = ['role_key', 'menu_item__module_name', 'can_access']
    search_fields = ['group__name', 'menu_item__menu_name']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['group__name', 'menu_item__menu_name']


@admin.register(POSFunction)
class POSFunctionAdmin(admin.ModelAdmin):
    list_display = ['function_code', 'function_name', 'category', 'keyboard_shortcut', 'is_critical', 'order', 'is_active']
    list_filter = ['category', 'is_critical', 'is_active']
    search_fields = ['function_code', 'function_name']
    ordering = ['category', 'order', 'function_name']


@admin.register(RolePOSFunctionMapping)
class RolePOSFunctionMappingAdmin(admin.ModelAdmin):
    list_display = ['role', 'function', 'is_allowed', 'requires_approval', 'created_by']
    list_filter = ['role', 'function__category', 'is_allowed', 'requires_approval']
    search_fields = ['function__function_name']
    ordering = ['role', 'function__function_name']


# ============================================================================
# TOOLBAR & MENU MANAGEMENT CLASSES (Without Registration)
# ============================================================================
# These classes are kept here because they are imported by other modules (e.g. HRM)
# but they are not registered to the default admin site to avoid duplicates.
# Use toolbar_control app for management.

class ERPToolbarControlAdmin(admin.ModelAdmin):
    list_display = ['module_name', 'master_toolbar_string']
    list_editable = ['master_toolbar_string']


class ERPMenuItemAdmin(admin.ModelAdmin):
    list_display = [
        'menu_id',
        'menu_name',
        'module_name',
        'view_type',
        'applicable_toolbar_config',
        'button_count_display',
        'config_type_display',
        'is_active',
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
        'applicable_toolbar_config',
    ]
    
    list_editable = [
        'applicable_toolbar_config',
        'is_active',
    ]
    
    readonly_fields = [
        'button_count_display',
        'config_type_display',
        'config_breakdown',
    ]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('menu_id', 'menu_name', 'module_name', 'view_type')
        }),
        ('Routing', {
            'fields': ('route_path', 'parent_menu')
        }),
        ('Toolbar Configuration', {
            'fields': (
                'applicable_toolbar_config',
                'button_count_display',
                'config_type_display',
                'config_breakdown',
            ),
            'description': 'Configure which toolbar buttons appear for this screen'
        }),
        ('Status', {
            'fields': ('is_active', 'is_license_controlled')
        }),
    )
    
    def button_count_display(self, obj):
        if obj.applicable_toolbar_config:
            return len(obj.applicable_toolbar_config)
        return 0
    button_count_display.short_description = 'Buttons'
    
    def config_type_display(self, obj):
        config = obj.applicable_toolbar_config or ''
        
        # Determine config type based on pattern
        if config == 'NESCKVDXRQF':
            return format_html('<span style="color: blue; font-weight: bold;">📋 Master</span>')
        elif config == 'NESCKVDXRQFIO':
            return format_html('<span style="color: green; font-weight: bold;">📦 Master+</span>')
        elif config == 'NESCKZTJAVPMRDX1234QF':
            return format_html('<span style="color: purple; font-weight: bold;">📄 Transaction</span>')
        elif config == 'VRXPYQFG':
            return format_html('<span style="color: orange; font-weight: bold;">📊 Report</span>')
        elif config == 'VRXQFG':
            return format_html('<span style="color: darkorange; font-weight: bold;">📈 Dashboard</span>')
        elif config == 'NRQFX':
            return format_html('<span style="color: gray; font-weight: bold;">📑 List View</span>')
        elif config == 'ESCKXR':
            return format_html('<span style="color: teal; font-weight: bold;">⚙️ Config</span>')
        else:
            return format_html('<span style="color: red; font-weight: bold;">❓ Custom</span>')
    config_type_display.short_description = 'Type Label'
    
    def config_breakdown(self, obj):
        if not obj.applicable_toolbar_config:
            return "No configuration set"
        
        config = obj.applicable_toolbar_config
        
        # Character mapping
        ACTION_MAP = {
            'N': 'New (F2)',
            'E': 'Edit (F3)',
            'S': 'Save (F8)',
            'C': 'Cancel (Esc)',
            'K': 'Clear (F5)',
            'V': 'View (F7)',
            'D': 'Delete (F4)',
            'X': 'Exit (Esc)',
            'R': 'Refresh (F9)',
            'Q': 'Search (Ctrl+F)',
            'F': 'Filter (Alt+F)',
            'I': 'Import (Ctrl+I)',
            'O': 'Export (Ctrl+E)',
            'Y': 'Export (Ctrl+E)',
            'Z': 'Authorize (F10)',
            'T': 'Submit (Alt+S)',
            'J': 'Reject (Alt+R)',
            'A': 'Amend (Alt+A)',
            'H': 'Hold (Alt+H)',
            'W': 'Void (Alt+V)',
            'P': 'Print (Ctrl+P)',
            'M': 'Email (Ctrl+M)',
            'L': 'Clone (Ctrl+Shift+C)',
            '1': 'First (Home)',
            '2': 'Prev (PgUp)',
            '3': 'Next (PgDn)',
            '4': 'Last (End)',
            'B': 'Notes (Alt+N)',
            'G': 'Attach (Alt+U)',
            '?': 'Help (F1)',
        }
        
        breakdown = []
        for char in config:
            action = ACTION_MAP.get(char, f'Unknown ({char})')
            breakdown.append(f'<li><code>{char}</code> = {action}</li>')
        
        html = f'''
        <div style="background: #f5f5f5; padding: 15px; border: 1px solid #ddd; border-radius: 5px;">
            <strong>Configuration: <span style="font-family: monospace; font-size: 1.2em;">{config}</span></strong> ({len(config)} buttons)
            <ul style="margin: 10px 0; padding-left: 20px; columns: 2;">
                {''.join(breakdown)}
            </ul>
        </div>
        '''
        return format_html(html)
    config_breakdown.short_description = 'Configuration Breakdown'




# ============================================================================
# AUDIT MODELS (Read-Only)
# ============================================================================

@admin.register(PermissionAudit)
class PermissionAuditAdmin(admin.ModelAdmin):
    list_display = ['changed_at', 'changed_by', 'role', 'menu_item', 'action', 'ip_address']
    list_filter = ['action', 'changed_at', 'role', 'menu_item__module_name']
    search_fields = ['changed_by__username', 'role__role_name', 'menu_item__menu_name']
    readonly_fields = ['changed_at', 'old_permissions', 'new_permissions', 'ip_address', 'user_agent']
    ordering = ['-changed_at']
    
    def has_add_permission(self, request):
        return False  # Audit records are created automatically
    
    def has_change_permission(self, request, obj=None):
        return False  # Audit records should not be modified
    
    def has_delete_permission(self, request, obj=None):
        return False  # Audit records should not be deleted


@admin.register(RoleAssignmentAudit)
class RoleAssignmentAuditAdmin(admin.ModelAdmin):
    list_display = ['assigned_at', 'assigned_by', 'user', 'role', 'action', 'ip_address']
    list_filter = ['action', 'assigned_at', 'role']
    search_fields = ['assigned_by__username', 'user__username', 'role__role_name']
    readonly_fields = ['assigned_at', 'ip_address']
    ordering = ['-assigned_at']
    
    def has_add_permission(self, request):
        return False  # Audit records are created automatically
    
    def has_change_permission(self, request, obj=None):
        return False  # Audit records should not be modified
    
    def has_delete_permission(self, request, obj=None):
        return False  # Audit records should not be deleted


# ============================================================================
# ADMIN SITE CUSTOMIZATION
# ============================================================================

admin.site.site_header = "EnterpriseGPT Administration"
admin.site.site_title = "EnterpriseGPT Admin"
admin.site.index_title = "Welcome to EnterpriseGPT Administration"
