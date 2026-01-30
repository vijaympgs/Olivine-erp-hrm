from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .models import (
    Employee, UserProfile, MenuItemType, UserPermission, GroupPermission,
    POSFunction, RolePOSFunctionMapping,
    Role, RolePermission, UserRole, PermissionAudit, RoleAssignmentAudit
)

User = get_user_model()

class EmployeeSerializer(serializers.ModelSerializer):
    """Legacy Employee Serializer - Read Only"""
    class Meta:
        model = Employee
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'full_name', 'profile', 'is_active', 'is_staff', 'is_superuser']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip() or obj.username

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

class MenuItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItemType
        fields = '__all__'

class RolePermissionSerializer(serializers.ModelSerializer):
    role_name = serializers.CharField(source='role.role_name', read_only=True)
    menu_item_name = serializers.CharField(source='menu_item.menu_name', read_only=True)
    
    class Meta:
        model = RolePermission
        fields = '__all__'

class UserRoleSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)
    role_name = serializers.CharField(source='role.role_name', read_only=True)
    assigned_by_username = serializers.CharField(source='assigned_by.username', read_only=True)
    
    class Meta:
        model = UserRole
        fields = '__all__'

class UserPermissionSerializer(serializers.ModelSerializer):
    menu_item_name = serializers.CharField(source='menu_item.display_name', read_only=True)
    
    class Meta:
        model = UserPermission
        fields = '__all__'

class GroupPermissionSerializer(serializers.ModelSerializer):
    menu_item_name = serializers.CharField(source='menu_item.display_name', read_only=True)
    group_name = serializers.CharField(source='group.name', read_only=True)
    
    class Meta:
        model = GroupPermission
        fields = '__all__'

class BulkUserPermissionSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    permissions = serializers.DictField(
        child=serializers.DictField(
            child=serializers.BooleanField()
        )
    )

class BulkRolePermissionSerializer(serializers.Serializer):
    role_key = serializers.CharField()
    permissions = serializers.DictField(
        child=serializers.DictField(
            child=serializers.BooleanField()
        )
    )

class POSFunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = POSFunction
        fields = '__all__'

class RolePOSFunctionMappingSerializer(serializers.ModelSerializer):
    function_name = serializers.CharField(source='function.function_name', read_only=True)
    class Meta:
        model = RolePOSFunctionMapping
        fields = '__all__'

# UserLocationMappingSerializer removed - UserLocationMapping model removed (Location is Retail-only)

class PermissionAuditSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)
    role_name = serializers.CharField(source='role.role_name', read_only=True)
    menu_item_name = serializers.CharField(source='menu_item.menu_name', read_only=True)
    changed_by_username = serializers.CharField(source='changed_by.username', read_only=True)
    
    class Meta:
        model = PermissionAudit
        fields = '__all__'

class RoleAssignmentAuditSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)
    role_name = serializers.CharField(source='role.role_name', read_only=True)
    assigned_by_username = serializers.CharField(source='assigned_by.username', read_only=True)
    
    class Meta:
        model = RoleAssignmentAudit
        fields = '__all__'
