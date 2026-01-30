from django.contrib import admin
from .models import (
    # Toolbar Configuration Models
    ERPToolbarControl, ERPMenuItem, Role, RolePermission, UserRole,
    
    # Employee Management Models
    EmployeeRecord, EmployeeAddress, EmployeeProfile, EmployeeSkill, SkillCategory,
)

# ============================================================================
# TOOLBAR CONFIGURATION ADMIN CLASSES
# ============================================================================
# Import unified admin classes from Core Platform
from core.auth_access.backend.user_management.admin import (
    ERPToolbarControlAdmin, ERPMenuItemAdmin, RoleAdmin,
    RolePermissionAdmin, UserRoleAdmin
)
# EMPLOYEE MANAGEMENT ADMIN CLASSES
# ============================================================================

class EmployeeRecordAdmin(admin.ModelAdmin):
    list_display = ['company_code', 'employee_number', 'first_name', 'last_name', 'work_email', 'department_name', 'employment_status', 'is_active']
    list_filter = ['employment_status', 'employment_type', 'is_active', 'department_name']
    search_fields = ['employee_number', 'first_name', 'last_name', 'work_email']
    list_editable = ['is_active', 'employment_status']
    ordering = ['employee_number']
    
    fieldsets = (
        ('Employee Information', {
            'fields': ('employee_number', 'first_name', 'last_name', 'middle_name', 'preferred_name')
        }),
        ('Contact Information', {
            'fields': ('work_email', 'personal_email', 'work_phone', 'mobile_phone', 'home_phone')
        }),
        ('Employment Details', {
            'fields': ('employment_status', 'employment_type', 'hire_date', 'termination_date', 'termination_reason')
        }),
        ('Job Information', {
            'fields': ('department_name', 'position_title', 'job_category', 'job_level', 'manager_name')
        }),
        ('Personal Information', {
            'fields': ('date_of_birth', 'gender', 'marital_status', 'national_id', 'social_security_number')
        }),
        ('System Information', {
            'fields': ('is_active', 'is_confidential', 'is_key_employee', 'username', 'role')
        }),
    )

class EmployeeAddressAdmin(admin.ModelAdmin):
    list_display = ['employee', 'address_type', 'city', 'state', 'country', 'is_primary', 'is_active']
    list_filter = ['address_type', 'is_primary', 'is_active', 'country']
    search_fields = ['employee__first_name', 'employee__last_name', 'city', 'state']
    ordering = ['employee', '-is_primary', 'address_type']
    
    fieldsets = (
        ('Address Information', {
            'fields': ('employee', 'address_type', 'is_primary', 'is_active')
        }),
        ('Address Details', {
            'fields': ('address_line_1', 'address_line_2', 'city', 'state', 'postal_code', 'country')
        }),
    )

class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ['employee', 'preferred_name', 'gender', 'marital_status', 'profile_visibility', 'is_active']
    list_filter = ['gender', 'marital_status', 'profile_visibility', 'is_active']
    search_fields = ['employee__first_name', 'employee__last_name', 'preferred_name']
    ordering = ['employee']
    
    fieldsets = (
        ('Profile Information', {
            'fields': ('employee', 'preferred_name', 'middle_name', 'nickname', 'gender', 'date_of_birth')
        }),
        ('Contact Information', {
            'fields': ('personal_email', 'personal_phone', 'work_phone_extension')
        }),
        ('Address Information', {
            'fields': ('home_address_line_1', 'home_address_line_2', 'home_city', 'home_state', 'home_postal_code', 'home_country')
        }),
        ('Emergency Contact', {
            'fields': ('emergency_contact_name', 'emergency_contact_relationship', 'emergency_contact_phone', 'emergency_contact_email')
        }),
        ('Profile Settings', {
            'fields': ('profile_visibility', 'profile_photo_url', 'bio', 'linkedin_url', 'twitter_url')
        }),
        ('Preferences', {
            'fields': ('preferred_language', 'timezone', 'email_notifications', 'sms_notifications')
        }),
        ('Status', {
            'fields': ('is_active', 'is_verified', 'verification_date')
        }),
    )

class EmployeeSkillAdmin(admin.ModelAdmin):
    list_display = ['employee', 'skill_name', 'skill_category', 'proficiency_level', 'years_experience', 'is_verified']
    list_filter = ['skill_category', 'proficiency_level', 'is_verified']
    search_fields = ['employee__employee__first_name', 'employee__employee_number', 'skill_name', 'skill_category']
    ordering = ['employee', 'skill_category', 'skill_name']
    
    fieldsets = (
        ('Skill Information', {
            'fields': ('employee', 'skill_name', 'skill_category', 'proficiency_level', 'years_experience', 'last_used', 'is_verified')
        }),
        ('Skill Details', {
            'fields': ('description', 'verified_by', 'verified_date')
        }),
    )
