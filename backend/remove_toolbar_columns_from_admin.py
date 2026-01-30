import re

def remove_toolbar_columns_from_admin():
    """Remove toolbar_list, toolbar_view, toolbar_edit, toolbar_create from admin classes"""
    
    # Fix core/auth_access/backend/user_management/admin.py
    file_path = 'core/auth_access/backend/user_management/admin.py'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove toolbar columns from ERPMenuItemAdmin list_display
    content = re.sub(
        r"'toolbar_list',\s*'toolbar_view',\s*'toolbar_edit',\s*'toolbar_create',",
        "",
        content
    )
    
    # Remove toolbar columns from ERPMenuItemAdmin list_editable
    content = re.sub(
        r"'toolbar_list',\s*'toolbar_view',\s*'toolbar_edit',\s*'toolbar_create',",
        "",
        content
    )
    
    # Remove toolbar columns from ERPMenuItemAdmin fieldsets
    content = re.sub(
        r"'toolbar_list',\s*'toolbar_view',\s*'toolbar_edit',\s*'toolbar_create',",
        "",
        content
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Removed toolbar columns from core/auth_access/backend/user_management/admin.py")
    
    # Fix core/auth_access/backend/toolbar_control/admin.py
    file_path = 'core/auth_access/backend/toolbar_control/admin.py'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove toolbar columns from ItemAdmin list_display
    content = re.sub(
        r"'toolbar_list',\s*'toolbar_view',\s*'toolbar_edit',\s*'toolbar_create',",
        "",
        content
    )
    
    # Remove toolbar columns from ItemAdmin list_editable
    content = re.sub(
        r"'toolbar_list',\s*'toolbar_view',\s*'toolbar_edit',\s*'toolbar_create',",
        "",
        content
    )
    
    # Remove toolbar columns from ItemAdmin fieldsets
    content = re.sub(
        r"'toolbar_list',\s*'toolbar_view',\s*'toolbar_edit',\s*'toolbar_create',",
        "",
        content
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Removed toolbar columns from core/auth_access/backend/toolbar_control/admin.py")

if __name__ == "__main__":
    remove_toolbar_columns_from_admin()
