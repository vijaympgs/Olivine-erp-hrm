"""
User Management & Permissions Module
Includes Legacy Employee (Deprecated) and New Permission Models (Parity with 02practice)
"""
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import uuid
import warnings
from core.shared.backend.common.legacy_manager import LegacyReadonlyManager


# Location model is now imported from core.licensing.backend.business_entities


class Employee(models.Model):
    """Legacy Employee Model - Deprecated/Read-Only"""
    objects = LegacyReadonlyManager()
    LEGACY_DEPRECATED = True

    def delete(self, *args, **kwargs):
        raise ValidationError("Legacy user_management.Employee is Read-Only (Phase 4).")

    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    MARITAL_STATUS_CHOICES = [('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('widowed', 'Widowed')]
    EMPLOYMENT_TYPE_CHOICES = [('full_time', 'Full Time'), ('part_time', 'Part Time'), ('contract', 'Contract'), ('intern', 'Intern')]
    STATUS_CHOICES = [('active', 'Active'), ('inactive', 'Inactive')]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES, null=True, blank=True)
    employee_code = models.CharField(max_length=20, unique=True, editable=False)
    date_of_joining = models.DateField(null=True, blank=True)
    employment_type = models.CharField(max_length=15, choices=EMPLOYMENT_TYPE_CHOICES, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    business_unit = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    reporting_manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subordinates')
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\+?\d{10,15}$', message='Enter a valid phone number.')], null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    pan = models.CharField(max_length=10, null=True, blank=True)
    aadhaar = models.CharField(max_length=12, null=True, blank=True)
    pf_number = models.CharField(max_length=20, null=True, blank=True)
    esi_number = models.CharField(max_length=20, null=True, blank=True)
    ctc = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    pay_grade = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # warnings.warn("user_management.Employee is a Legacy/Duplicate model.", DeprecationWarning)

    class Meta:
        app_label = "user_management"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.employee_code})"


# -----------------------------------------------------------------------------
# NEW PERMISSION MODELS (Parity with 02practice)
# -----------------------------------------------------------------------------

class Role(models.Model):
    """Role definitions for the permission system"""
    role_key = models.CharField(max_length=50, unique=True)
    role_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    is_system_role = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'roles'
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.role_name


class UserProfile(models.Model):
    """
    Extends Django User to include additional profile information.
    Replaces custom User model fields from 02practice.
    """
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    employee_code = models.CharField(max_length=20, unique=True, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_profiles'
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return f"{self.user.username} Profile"


class UserCompanyMapping(models.Model):
    """
    Maps Users to Companies they can access.
    Replaces UserOperatingCompanyMapping (Company concept removed).
    """
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='company_mappings')
    company = models.ForeignKey('business_entities.Company', on_delete=models.CASCADE, related_name='user_mappings')
    is_active = models.BooleanField(default=True)
    is_default = models.BooleanField(default=False, help_text="Default company for this user")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_company_mapping'
        unique_together = ('user', 'company')
        verbose_name = 'User Company Mapping'
        verbose_name_plural = 'User Company Mappings'

    def __str__(self):
        return f"{self.user.username} → {self.company.code}"


class ERPToolbarControl(models.Model):
    """
    Master Control Strings for Toolbars per Module.
    Defines the superset of ALL available actions for a module.
    """
    module_name = models.CharField(max_length=50, unique=True, choices=[
        ('RETAIL', 'Retail Operations'),
        ('FMS', 'Financial Management'),
        ('HRM', 'Human Resources'),
        ('CRM', 'Customer Relationship Management'),
        ('ADMIN', 'Administration'),
        ('SETUP', 'System Setup'),
        ('SYSTEM', 'System Infrastructure')
    ])
    master_toolbar_string = models.CharField(
        max_length=100,
        help_text="Master string of all permitted action codes (e.g., 'NESCAZ...')"
    )
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'erp_toolbar_controls'
        verbose_name = "ERP Toolbar Control"
        verbose_name_plural = "ERP Toolbar Controls"

    def __str__(self):
        return f"{self.module_name} Control"


class ERPMenuItem(models.Model):
    """ERP Menu Item Registry with Toolbar Configuration"""
    
    # Identification
    menu_id = models.CharField(max_length=100, unique=True, db_index=True)
    menu_name = models.CharField(max_length=200)
    parent_menu = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    
    # Module & Type
    module_name = models.CharField(
        max_length=50,
        choices=[
            ('RETAIL', 'Retail Operations'),
            ('FMS', 'Financial Management'),
            ('HRM', 'Human Resources'),
            ('CRM', 'Customer Relationship Management'),
            ('ADMIN', 'Administration'),
            ('SETUP', 'System Setup'),
            ('SYSTEM', 'System Infrastructure')
        ]
    )
    submodule = models.CharField(max_length=50, null=True, blank=True, help_text='e.g., INVENTORY, SALES, PROCUREMENT')
    view_type = models.CharField(
        max_length=20,
        choices=[
            ('MASTER', 'Master Data'),
            ('TRANSACTION', 'Transaction'),
            ('REPORT', 'Report'),
            ('DASHBOARD', 'Dashboard'),
            ('CONFIGURATION', 'Configuration/Settings')
        ],
        default='TRANSACTION'
    )
    
    # Toolbar Configuration (Legacy & New)
    toolbar_config = models.CharField(
        max_length=50,
        default='1,1,1,1,1,1,1,1,1,1,1,1,1,1,1',
        help_text='[DEPRECATED] 15-button config'
    )
    # New String-Based Config
    original_toolbar_string = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="DerivedSuperset from ERPToolbarControl (Read Only logic)"
    )
    applicable_toolbar_config = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Effective toolbar string for this specific menu item (e.g. 'NESC')"
    )
    toolbar_config_backup = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text='Backup config for license restoration'
    )
    # Mode-Specific Toolbar Configuration (SCCB Compliance)
    toolbar_list = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Toolbar config for LIST mode (e.g., 'NRQFVIOX')"
    )
    toolbar_view = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Toolbar config for VIEW mode (e.g., 'X')"
    )
    toolbar_edit = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Toolbar config for EDIT mode (e.g., 'SCX')"
    )
    toolbar_create = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Toolbar config for CREATE mode (e.g., 'SCX')"
    )
    is_license_controlled = models.BooleanField(
        default=True,
        help_text='If True, toolbar is disabled when license expires'
    )
    
    # Metadata
    route_path = models.CharField(max_length=200, null=True, blank=True, help_text='Frontend route path')
    component_name = models.CharField(max_length=100, null=True, blank=True, help_text='React component name')
    description = models.TextField(null=True, blank=True)
    menu_order = models.IntegerField(default=0)
    display_order = models.IntegerField(default=0)
    
    # Status
    is_active = models.BooleanField(default=True)
    is_system_menu = models.BooleanField(default=False, help_text='System menus cannot be deleted')
    
    # Audit
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        'auth.User',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='created_menu_items'
    )
    updated_by = models.ForeignKey(
        'auth.User',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='updated_menu_items'
    )

    class Meta:
        db_table = 'erp_menu_items'
        verbose_name = "ERP Menu Item"
        verbose_name_plural = "ERP Menu Items"
        ordering = ['module_name', 'submodule', 'menu_order', 'menu_name']

    def __str__(self):
        return f"{self.menu_name} ({self.module_name})"


# Backward compatibility alias
MenuItemType = ERPMenuItem


class RolePermission(models.Model):
    """Permission Matrix - Role to Menu Item permissions"""
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(ERPMenuItem, on_delete=models.CASCADE, related_name='role_permissions')
    
    # Original CRUD permissions
    can_access = models.BooleanField(default=False)
    can_view = models.BooleanField(default=False)
    can_create = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)
    
    # Toolbar Override
    toolbar_override = models.CharField(
        max_length=100,  # Increased length to support full string
        null=True,
        blank=True,
        help_text='String override (e.g. "NESC"). If NULL, inherits from ERPMenuItem.'
    )
    override_enabled = models.BooleanField(
        default=False,
        help_text='If TRUE, toolbar_override is applied; if FALSE, uses ERPMenuItem.toolbar_config'
    )
    
    # NEW: Character-Based Toolbar Permission System
    toolbar_string = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='Toolbar capability string from ERPMenuItem (e.g., "NESCKZTJAVPMRDX1234QF")'
    )
    toolbar_permissions = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='Permission mask: 1=allowed, 0=denied (e.g., "110111010011011110011"). Each position maps to toolbar_string character.'
    )
    
    # Audit
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        'auth.User',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='created_role_permissions'
    )
    updated_by = models.ForeignKey(
        'auth.User',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='updated_role_permissions'
    )

    class Meta:
        db_table = 'role_permissions'
        unique_together = ('role', 'menu_item')
        verbose_name = 'Role Permission'
        verbose_name_plural = 'Role Permissions'

    def __str__(self):
        return f"{self.role.role_name} - {self.menu_item.menu_name}"


class UserRole(models.Model):
    """User-Role Mapping with audit trail"""
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    assigned_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='assigned_roles')
    assigned_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'user_roles'
        unique_together = ('user', 'role')
        verbose_name = 'User Role'
        verbose_name_plural = 'User Roles'

    def __str__(self):
        return f"{self.user.username} - {self.role.role_name}"


class UserPermission(models.Model):
    """Fine-grained user permissions per menu item"""
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='permissions')
    menu_item = models.ForeignKey(ERPMenuItem, on_delete=models.CASCADE, related_name='user_permissions')
    
    # Original CRUD permissions
    can_access = models.BooleanField(default=False)
    can_view = models.BooleanField(default=False)
    can_create = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)
    override = models.BooleanField(default=False)
    
    # Toolbar Override
    toolbar_override = models.CharField(
        max_length=100, # Increased length
        null=True,
        blank=True,
        help_text='User-specific string override. If NULL, inherits from Role or ERPMenuItem'
    )
    
    # Audit
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        'auth.User',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='created_user_permissions'
    )
    updated_by = models.ForeignKey(
        'auth.User',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='updated_user_permissions'
    )

    class Meta:
        db_table = 'user_permissions'
        unique_together = ['user', 'menu_item']
        verbose_name = 'User Permission'
        verbose_name_plural = 'User Permissions'

    def __str__(self):
        return f"{self.user.username} - {self.menu_item.menu_name}"


class GroupPermission(models.Model):
    """Role/Group default permissions"""
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='menu_permissions')
    role_key = models.CharField(max_length=50) # e.g. 'posmanager'
    menu_item = models.ForeignKey(ERPMenuItem, on_delete=models.CASCADE, related_name='group_permissions')
    
    can_access = models.BooleanField(default=False)
    can_view = models.BooleanField(default=False)
    can_create = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'group_permissions'
        unique_together = ['group', 'menu_item']

    def __str__(self):
        return f"{self.group.name} - {self.menu_item.menu_name}"


class POSFunction(models.Model):
    """POS Function Master"""
    FUNCTION_CATEGORY_CHOICES = [('BASIC', 'Basic'), ('DISCOUNT', 'Discount'), ('PAYMENT', 'Payment'), ('TRANSACTION', 'Transaction'), ('ADMIN', 'Administrative')]
    
    function_code = models.CharField(max_length=50, unique=True, db_index=True)
    function_name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=FUNCTION_CATEGORY_CHOICES)
    keyboard_shortcut = models.CharField(max_length=20)
    is_critical = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'pos_functions'

    def __str__(self):
        return self.function_name


class RolePOSFunctionMapping(models.Model):
    """Role to POS Function Mapping"""
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('posmanager', 'POS Manager'),
        ('posuser', 'POS User'),
        ('backofficemanager', 'Back Office Manager'),
        ('backofficeuser', 'Back Office User'),
    ]
    
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)
    function = models.ForeignKey(POSFunction, on_delete=models.CASCADE, related_name='role_mappings')
    is_allowed = models.BooleanField(default=True)
    requires_approval = models.BooleanField(default=False)
    created_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'role_pos_function_mappings'
        unique_together = ['role', 'function']





from core.licensing.backend.business_entities.models import Company
# Location is now in Retail.backend.domain (Retail-exclusive)
# from core.org_structure.backend.company.models import Location as BELocation

# UserOperatingCompanyMapping REMOVED - Using UserCompanyMapping at Line 112 instead.


# UserLocationMapping model removed - Location is Retail-only model
# This functionality is not available in HRM-only setup

# ... Audits follow



# -----------------------------------------------------------------------------
# AUDIT MODELS
# -----------------------------------------------------------------------------

class PermissionAudit(models.Model):
    """Audit trail for permission changes"""
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    menu_item = models.ForeignKey(ERPMenuItem, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=20)  # CREATE, UPDATE, DELETE
    old_permissions = models.JSONField(null=True, blank=True)
    new_permissions = models.JSONField(null=True, blank=True)
    changed_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='permission_changes')
    changed_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'permission_audits'
        verbose_name = 'Permission Audit'
        verbose_name_plural = 'Permission Audits'

    def __str__(self):
        return f"{self.action} - {self.changed_by} - {self.changed_at}"


class RoleAssignmentAudit(models.Model):
    """Audit trail for role assignments"""
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=20)  # ASSIGN, REMOVE
    assigned_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='role_assignments')
    assigned_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        db_table = 'role_assignment_audits'
        verbose_name = 'Role Assignment Audit'
        verbose_name_plural = 'Role Assignment Audits'

    def __str__(self):
        return f"{self.action} - {self.assigned_by} - {self.assigned_at}"
