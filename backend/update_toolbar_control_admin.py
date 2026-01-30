import re

def update_toolbar_control_admin():
    """Update toolbar_control/admin.py to add TableNameDisplayMixin and new toolbar columns"""
    
    file_path = 'core/auth_access/backend/toolbar_control/admin.py'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Add import for TableNameDisplayMixin
    if 'from ..user_management.admin_mixins import TableNameDisplayMixin' not in content:
        content = content.replace(
            'from ..user_management.admin import MenuLevelFilter, SubgroupL2Filter',
            'from ..user_management.admin_mixins import TableNameDisplayMixin\nfrom ..user_management.admin import MenuLevelFilter, SubgroupL2Filter'
        )
    
    # 2. Add TableNameDisplayMixin to ERPToolbarControlAdmin
    content = re.sub(
        r'class ERPToolbarControlAdmin\(admin\.ModelAdmin\):',
        'class ERPToolbarControlAdmin(TableNameDisplayMixin, admin.ModelAdmin):',
        content
    )
    
    # 3. Add TableNameDisplayMixin to ItemAdmin
    content = re.sub(
        r'class ItemAdmin\(admin\.ModelAdmin\):',
        'class ItemAdmin(TableNameDisplayMixin, admin.ModelAdmin):',
        content
    )
    
    # 4. Add TableNameDisplayMixin to RolePermissionAdmin
    content = re.sub(
        r'class RolePermissionAdmin\(admin\.ModelAdmin\):',
        'class RolePermissionAdmin(TableNameDisplayMixin, admin.ModelAdmin):',
        content
    )
    
    # 5. Add TableNameDisplayMixin to UserPermissionAdmin
    content = re.sub(
        r'class UserPermissionAdmin\(admin\.ModelAdmin\):',
        'class UserPermissionAdmin(TableNameDisplayMixin, admin.ModelAdmin):',
        content
    )
    
    # 6. Add new toolbar columns to ItemAdmin list_display
    # Find the list_display and add the new columns after 'applicable_toolbar_config'
    content = re.sub(
        r"'applicable_toolbar_config',\s*'button_count_display',",
        "'applicable_toolbar_config',\n        'toolbar_list',\n        'toolbar_view',\n        'toolbar_edit',\n        'toolbar_create',\n        'button_count_display',",
        content
    )
    
    # 7. Add new toolbar columns to list_editable
    content = re.sub(
        r"list_editable = \('applicable_toolbar_config', 'is_active'\)",
        "list_editable = ('applicable_toolbar_config', 'toolbar_list', 'toolbar_view', 'toolbar_edit', 'toolbar_create', 'is_active')",
        content
    )
    
    # 8. Add new toolbar columns to fieldsets
    content = re.sub(
        r"\('Toolbar Configuration', \{\s*'fields': \('applicable_toolbar_config', 'original_toolbar_string', 'is_license_controlled'\),",
        "('Toolbar Configuration', {\n            'fields': ('applicable_toolbar_config', 'toolbar_list', 'toolbar_view', 'toolbar_edit', 'toolbar_create', 'original_toolbar_string', 'is_license_controlled'),",
        content
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Updated core/auth_access/backend/toolbar_control/admin.py:")
    print("  - Added TableNameDisplayMixin import")
    print("  - Added TableNameDisplayMixin to ERPToolbarControlAdmin")
    print("  - Added TableNameDisplayMixin to ItemAdmin")
    print("  - Added TableNameDisplayMixin to RolePermissionAdmin")
    print("  - Added TableNameDisplayMixin to UserPermissionAdmin")
    print("  - Added toolbar_list, toolbar_view, toolbar_edit, toolbar_create to list_display")
    print("  - Added toolbar_list, toolbar_view, toolbar_edit, toolbar_create to list_editable")
    print("  - Added toolbar_list, toolbar_view, toolbar_edit, toolbar_create to fieldsets")

if __name__ == "__main__":
    update_toolbar_control_admin()
