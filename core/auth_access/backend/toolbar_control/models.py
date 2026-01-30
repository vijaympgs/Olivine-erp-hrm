from ..user_management.models import ERPToolbarControl, ERPMenuItem, RolePermission, UserPermission

class ToolbarControlProxy(ERPToolbarControl):
    class Meta:
        proxy = True
        app_label = 'toolbar_control'
        verbose_name = "Master Toolbar"
        verbose_name_plural = "Master Toolbars"

class ToolbarItemProxy(ERPMenuItem):
    class Meta:
        proxy = True
        app_label = 'toolbar_control'
        verbose_name = "ERP Menu Item"
        verbose_name_plural = "ERP Menu Items"

class RoleToolbarPermissionProxy(RolePermission):
    class Meta:
        proxy = True
        app_label = 'toolbar_control'
        verbose_name = "Role Toolbar Permission"
        verbose_name_plural = "Role Toolbar Permissions"

class UserToolbarPermissionProxy(UserPermission):
    class Meta:
        proxy = True
        app_label = 'toolbar_control'
        verbose_name = "User Toolbar Permission"
        verbose_name_plural = "User Toolbar Permissions"




