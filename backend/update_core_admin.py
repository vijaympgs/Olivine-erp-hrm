import re

def update_core_admin():
    """Update core admin.py to add TableNameDisplayMixin and new toolbar columns"""
    
    file_path = 'core/auth_access/backend/user_management/admin.py'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Add import for TableNameDisplayMixin
    if 'from .admin_mixins import TableNameDisplayMixin' not in content:
        content = content.replace(
            'from .models import (',
            'from .admin_mixins import TableNameDisplayMixin\n\nfrom .models import ('
        )
    
    # 2. Add TableNameDisplayMixin to ERPToolbarControlAdmin
    content = re.sub(
        r'class ERPToolbarControlAdmin\(admin\.ModelAdmin\):',
        'class ERPToolbarControlAdmin(TableNameDisplayMixin, admin.ModelAdmin):',
        content
    )
    
    # 3. Add TableNameDisplayMixin to ERPMenuItemAdmin
    content = re.sub(
        r'class ERPMenuItemAdmin\(admin\.ModelAdmin\):',
        'class ERPMenuItemAdmin(TableNameDisplayMixin, admin.ModelAdmin):',
        content
    )
    
    # 4. Add new toolbar columns to ERPMenuItemAdmin list_display
    # Find the list_display and add the new columns after 'applicable_toolbar_config'
    content = re.sub(
        r"list_display = \[\s*'menu_id',\s*'menu_name',\s*'module_name',\s*'view_type',\s*'applicable_toolbar_config',",
        "list_display = [\n        'menu_id',\n        'menu_name',\n        'module_name',\n        'view_type',\n        'applicable_toolbar_config',\n        'toolbar_list',\n        'toolbar_view',\n        'toolbar_edit',\n        'toolbar_create',",
        content
    )
    
    # 5. Add new toolbar columns to list_editable
    content = re.sub(
        r"list_editable = \[\s*'applicable_toolbar_config',\s*'is_active',\s*\]",
        "list_editable = [\n        'applicable_toolbar_config',\n        'toolbar_list',\n        'toolbar_view',\n        'toolbar_edit',\n        'toolbar_create',\n        'is_active',\n    ]",
        content
    )
    
    # 6. Add new toolbar columns to fieldsets
    content = re.sub(
        r"\('Toolbar Configuration', \{\s*'fields': \(\s*'applicable_toolbar_config',\s*'button_count_display',",
        "('Toolbar Configuration', {\n            'fields': (\n                'applicable_toolbar_config',\n                'toolbar_list',\n                'toolbar_view',\n                'toolbar_edit',\n                'toolbar_create',\n                'button_count_display',",
        content
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Updated core/auth_access/backend/user_management/admin.py:")
    print("  - Added TableNameDisplayMixin import")
    print("  - Added TableNameDisplayMixin to ERPToolbarControlAdmin")
    print("  - Added TableNameDisplayMixin to ERPMenuItemAdmin")
    print("  - Added toolbar_list, toolbar_view, toolbar_edit, toolbar_create to list_display")
    print("  - Added toolbar_list, toolbar_view, toolbar_edit, toolbar_create to list_editable")
    print("  - Added toolbar_list, toolbar_view, toolbar_edit, toolbar_create to fieldsets")

if __name__ == "__main__":
    update_core_admin()
