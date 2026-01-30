import re

def update_django_builtin_admin():
    """Update core admin.py to add TableNameDisplayMixin to Django's built-in User, Group, and Token admin classes"""
    
    file_path = 'core/auth_access/backend/user_management/admin.py'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add code to unregister and re-register Django's built-in admin classes with TableNameDisplayMixin
    # Find the end of the file (before the admin site customization)
    
    django_admin_code = '''
# ============================================================================
# DJANGO BUILT-IN ADMIN CLASSES WITH TABLE NAME DISPLAY
# ============================================================================

# Unregister and re-register User with TableNameDisplayMixin
from django.contrib.auth.models import User, Group
try:
    from rest_framework.authtoken.models import Token
    HAS_TOKEN_MODEL = True
except ImportError:
    HAS_TOKEN_MODEL = False

    # Unregister default admin classes (check if registered first)
    if admin.site.is_registered(User):
        admin.site.unregister(User)
    if admin.site.is_registered(Group):
        admin.site.unregister(Group)
    if HAS_TOKEN_MODEL and admin.site.is_registered(Token):
        admin.site.unregister(Token)

# Re-register with TableNameDisplayMixin
@admin.register(User)
class UserAdminWithTableName(TableNameDisplayMixin, BaseUserAdmin):
    pass

@admin.register(Group)
class GroupAdminWithTableName(TableNameDisplayMixin, admin.ModelAdmin):
    list_display = ['name', 'permissions_count']
    
    def permissions_count(self, obj):
        return obj.permissions.count()
    permissions_count.short_description = 'Permissions'

if HAS_TOKEN_MODEL:
    @admin.register(Token)
    class TokenAdminWithTableName(TableNameDisplayMixin, admin.ModelAdmin):
        list_display = ['user', 'key', 'created']
        list_filter = ['created']
        search_fields = ['user__username', 'key']

'''
    
    # Insert before the admin site customization section
    content = content.replace(
        '# ============================================================================\n# ADMIN SITE CUSTOMIZATION',
        django_admin_code + '\n# ============================================================================\n# ADMIN SITE CUSTOMIZATION'
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Updated core/auth_access/backend/user_management/admin.py:")
    print("  - Added TableNameDisplayMixin to Django's built-in User admin")
    print("  - Added TableNameDisplayMixin to Django's built-in Group admin")
    print("  - Added TableNameDisplayMixin to Django's built-in Token admin (if available)")

if __name__ == "__main__":
    update_django_builtin_admin()
