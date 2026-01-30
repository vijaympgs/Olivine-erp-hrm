"""
Employee Self-Service Models - Following BBP 1.3 Employee Self-Service specifications
Comprehensive self-service functionality with approval workflows and audit trails
"""
import uuid
import json
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from ..tenancy import DEFAULT_COMPANY_CODE


class EmployeeChangeRequest(models.Model):
    """
    Employee change request model for self-service updates
    Following BBP 1.3.3 Change Request Schema
    """
    REQUEST_TYPE_CHOICES = [
        ('Personal Info', 'Personal Info'),
        ('Contact Info', 'Contact Info'),
        ('Bank Details', 'Bank Details'),
        ('Emergency Contact', 'Emergency Contact'),
        ('Tax Info', 'Tax Info'),
        ('Address', 'Address'),
    ]
    
    STATUS_CHOICES = [
        ('Draft', 'Draft'),
        ('Submitted', 'Submitted'),
        ('Pending Approval', 'Pending Approval'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Completed', 'Completed'),
    ]
    
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Urgent', 'Urgent'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_code = models.CharField(max_length=10, db_index=True, default=DEFAULT_COMPANY_CODE)
    employee = models.ForeignKey('EmployeeRecord', on_delete=models.CASCADE, related_name='change_requests')
    request_type = models.CharField(max_length=50, choices=REQUEST_TYPE_CHOICES, db_index=True)
    field_name = models.CharField(max_length=100, db_index=True)
    old_value = models.TextField(null=True, blank=True)
    new_value = models.TextField()
    change_reason = models.TextField()
    supporting_document = models.ForeignKey('EmployeeDocument', on_delete=models.SET_NULL, null=True, blank=True, related_name='related_change_requests')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Draft', db_index=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium', db_index=True)
    submitted_at = models.DateTimeField(null=True, blank=True, db_index=True)
    approved_by_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_change_requests')
    approved_at = models.DateTimeField(null=True, blank=True)
    rejection_reason = models.TextField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'employee_change_request'
        verbose_name = 'Employee Change Request'
        verbose_name_plural = 'Employee Change Requests'
        indexes = [
            models.Index(fields=['company_code', 'employee'], name='idx_ess_change_comp_emp'),
            models.Index(fields=['request_type'], name='idx_ess_change_req_type'),
            models.Index(fields=['status'], name='idx_ess_change_status'),
            models.Index(fields=['priority'], name='idx_ess_change_priority'),
            models.Index(fields=['submitted_at'], name='idx_ess_change_submitted'),
            models.Index(fields=['approved_by_user'], name='idx_ess_change_approver'),
        ]

    def __str__(self):
        return f'{self.request_type} - {self.field_name} for {self.employee.first_name} {self.employee.last_name}'


class ApprovalMatrix(models.Model):
    """
    Approval matrix configuration for change requests
    Following BBP 1.3.4 Approval Matrix Schema
    """
    REQUEST_TYPE_CHOICES = [
        ('Personal Info', 'Personal Info'),
        ('Contact Info', 'Contact Info'),
        ('Bank Details', 'Bank Details'),
        ('Emergency Contact', 'Emergency Contact'),
        ('Tax Info', 'Tax Info'),
        ('Address', 'Address'),
    ]
    
    EMPLOYEE_CATEGORY_CHOICES = [
        ('All', 'All'),
        ('Staff', 'Staff'),
        ('Worker', 'Worker'),
        ('Executive', 'Executive'),
        ('Management', 'Management'),
    ]
    
    APPROVER_TYPE_CHOICES = [
        ('Manager', 'Manager'),
        ('HR Admin', 'HR Admin'),
        ('Department Head', 'Department Head'),
        ('Specific User', 'Specific User'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='approval_matrices')
    request_type = models.CharField(max_length=50, choices=REQUEST_TYPE_CHOICES, db_index=True)
    employee_category = models.CharField(max_length=20, choices=EMPLOYEE_CATEGORY_CHOICES, default='All', db_index=True)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True, related_name='approval_matrices')
    location = models.ForeignKey('OrganizationalUnit', on_delete=models.SET_NULL, null=True, blank=True, related_name='approval_matrices')
    approval_level = models.IntegerField(validators=[MinValueValidator(1)])
    approver_type = models.CharField(max_length=20, choices=APPROVER_TYPE_CHOICES, db_index=True)
    approver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='approval_matrix_entries')
    is_required = models.BooleanField(default=True)
    is_parallel = models.BooleanField(default=False)
    time_limit_hours = models.IntegerField(default=48)
    auto_approve = models.BooleanField(default=False)
    conditions = models.JSONField(default=dict, help_text="Approval conditions")
    is_active = models.BooleanField(default=True, db_index=True)
    effective_from = models.DateField()
    effective_to = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'approval_matrix'
        verbose_name = 'Approval Matrix'
        verbose_name_plural = 'Approval Matrices'
        indexes = [
            models.Index(fields=['company', 'request_type'], name='idx_ess_matrix_company_request'),
            models.Index(fields=['employee_category'], name='idx_ess_matrix_category'),
            models.Index(fields=['department'], name='idx_ess_matrix_department'),
            models.Index(fields=['location'], name='idx_ess_matrix_location'),
            models.Index(fields=['approval_level'], name='idx_ess_matrix_level'),
            models.Index(fields=['approver_type'], name='idx_ess_matrix_approver_type'),
            models.Index(fields=['approver'], name='idx_ess_matrix_approver'),
            models.Index(fields=['is_active'], name='idx_ess_matrix_active'),
        ]

    def __str__(self):
        return f'{self.request_type} - Level {self.approval_level} for {self.company.name}'


class ApprovalWorkflow(models.Model):
    """
    Approval workflow tracking for change requests
    Following BBP 1.3.5 Approval Workflow Schema
    """
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Delegated', 'Delegated'),
        ('Escalated', 'Escalated'),
    ]
    
    DECISION_CHOICES = [
        ('Approve', 'Approve'),
        ('Reject', 'Reject'),
        ('Request More Info', 'Request More Info'),
        ('Delegate', 'Delegate'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    request = models.ForeignKey('EmployeeChangeRequest', on_delete=models.CASCADE, related_name='approval_workflows')
    matrix = models.ForeignKey('ApprovalMatrix', on_delete=models.CASCADE, related_name='workflows')
    approver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='approval_workflow_actions')
    approval_level = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending', db_index=True)
    decision = models.CharField(max_length=20, choices=DECISION_CHOICES, null=True, blank=True, db_index=True)
    comments = models.TextField(null=True, blank=True)
    attachments = models.JSONField(default=list, help_text="Array of document IDs")
    delegated_to_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='delegated_approvals')
    escalated_to_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='escalated_approvals')
    due_date = models.DateTimeField(db_index=True)
    action_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'approval_workflow'
        verbose_name = 'Approval Workflow'
        verbose_name_plural = 'Approval Workflows'
        indexes = [
            models.Index(fields=['request', 'matrix'], name='idx_ess_workflow_req_matrix'),
            models.Index(fields=['approver'], name='idx_ess_workflow_approver'),
            models.Index(fields=['approval_level'], name='idx_ess_workflow_level'),
            models.Index(fields=['status'], name='idx_ess_workflow_status'),
            models.Index(fields=['decision'], name='idx_ess_workflow_decision'),
            models.Index(fields=['due_date'], name='idx_ess_workflow_due'),
        ]

    def __str__(self):
        return f'Workflow for {self.request.request_type} - Level {self.approval_level}'


class ESSConfiguration(models.Model):
    """
    ESS configuration settings
    Following BBP 1.3.6 Self-Service Configuration Schema
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='ess_configurations')
    module_name = models.CharField(max_length=100, db_index=True)
    feature_name = models.CharField(max_length=100, db_index=True)
    is_enabled = models.BooleanField(default=True, db_index=True)
    configuration = models.JSONField(default=dict, help_text="Feature-specific settings")
    access_roles = models.JSONField(default=list, help_text="Array of role IDs")
    employee_categories = models.JSONField(default=list, help_text="Array of categories")
    departments = models.JSONField(default=list, help_text="Array of department IDs")
    locations = models.JSONField(default=list, help_text="Array of location IDs")
    validation_rules = models.JSONField(default=dict, help_text="Field validation rules")
    notification_settings = models.JSONField(default=dict, help_text="Email/SMS templates")
    approval_required = models.BooleanField(default=False)
    auto_approve_conditions = models.JSONField(default=dict, help_text="Auto-approval rules")
    effective_from = models.DateField()
    effective_to = models.DateField(null=True, blank=True)
    created_by_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='ess_config_created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ess_configuration'
        verbose_name = 'ESS Configuration'
        verbose_name_plural = 'ESS Configurations'
        unique_together = ['company', 'module_name', 'feature_name']
        indexes = [
            models.Index(fields=['company', 'module_name'], name='idx_ess_config_company_module'),
            models.Index(fields=['feature_name'], name='idx_ess_config_feature'),
            models.Index(fields=['is_enabled'], name='idx_ess_config_enabled'),
        ]

    def __str__(self):
        return f'{self.module_name} - {self.feature_name} for {self.company.name}'


class ESSServiceCatalog(models.Model):
    """
    ESS service catalog for available services
    Following BBP 1.3.8 Service Catalog Schema
    """
    SERVICE_CATEGORY_CHOICES = [
        ('Personal Info', 'Personal Info'),
        ('Benefits', 'Benefits'),
        ('Payroll', 'Payroll'),
        ('Leave', 'Leave'),
        ('Documents', 'Documents'),
        ('Training', 'Training'),
        ('IT Support', 'IT Support'),
    ]
    
    SERVICE_TYPE_CHOICES = [
        ('Form', 'Form'),
        ('Document Request', 'Document Request'),
        ('Information', 'Information'),
        ('Approval Request', 'Approval Request'),
        ('Automated Process', 'Automated Process'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='ess_services')
    service_code = models.CharField(max_length=50, db_index=True)
    service_name = models.CharField(max_length=200)
    service_category = models.CharField(max_length=20, choices=SERVICE_CATEGORY_CHOICES, db_index=True)
    service_description = models.TextField(null=True, blank=True)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPE_CHOICES, db_index=True)
    target_audience = models.JSONField(default=dict, help_text="Employee categories, roles, departments")
    prerequisites = models.JSONField(default=dict, help_text="Required conditions")
    process_steps = models.JSONField(default=list, help_text="Step-by-step process")
    sla_hours = models.IntegerField(default=48)
    auto_approve = models.BooleanField(default=False)
    fee_applicable = models.BooleanField(default=False)
    fee_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True, db_index=True)
    display_order = models.IntegerField(default=0)
    icon_name = models.CharField(max_length=100, null=True, blank=True)
    help_text = models.TextField(null=True, blank=True)
    created_by_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='ess_services_created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ess_service_catalog'
        verbose_name = 'ESS Service Catalog'
        verbose_name_plural = 'ESS Service Catalog'
        unique_together = ['company', 'service_code']
        indexes = [
            models.Index(fields=['company', 'service_code'], name='idx_ess_service_company_code'),
            models.Index(fields=['service_category'], name='idx_ess_service_category'),
            models.Index(fields=['service_type'], name='idx_ess_service_type'),
            models.Index(fields=['is_active'], name='idx_ess_service_active'),
            models.Index(fields=['display_order'], name='idx_ess_service_order'),
        ]

    def __str__(self):
        return f'{self.service_name} ({self.service_code})'


class ESSServiceRequest(models.Model):
    """
    ESS service requests from employees
    Following BBP 1.3.9 Service Request Schema
    """
    STATUS_CHOICES = [
        ('Draft', 'Draft'),
        ('Submitted', 'Submitted'),
        ('In Progress', 'In Progress'),
        ('Pending Info', 'Pending Info'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
        ('Rejected', 'Rejected'),
    ]
    
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Urgent', 'Urgent'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    request_number = models.CharField(max_length=50, unique=True, db_index=True)
    employee = models.ForeignKey('EmployeeRecord', on_delete=models.CASCADE, related_name='service_requests')
    service = models.ForeignKey('ESSServiceCatalog', on_delete=models.CASCADE, related_name='requests')
    request_data = models.JSONField(default=dict, help_text="Form data and attachments")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Draft', db_index=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium', db_index=True)
    assigned_to_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_service_requests')
    submitted_at = models.DateTimeField(null=True, blank=True, db_index=True)
    due_date = models.DateTimeField(null=True, blank=True, db_index=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    completion_notes = models.TextField(null=True, blank=True)
    employee_rating = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    employee_feedback = models.TextField(null=True, blank=True)
    processing_time_hours = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ess_service_request'
        verbose_name = 'ESS Service Request'
        verbose_name_plural = 'ESS Service Requests'
        indexes = [
            models.Index(fields=['employee', 'service'], name='idx_ess_req_employee_service'),
            models.Index(fields=['status'], name='idx_ess_req_status'),
            models.Index(fields=['priority'], name='idx_ess_req_priority'),
            models.Index(fields=['assigned_to_user'], name='idx_ess_req_assigned'),
            models.Index(fields=['submitted_at'], name='idx_ess_req_submitted'),
            models.Index(fields=['due_date'], name='idx_ess_req_due'),
        ]

    def __str__(self):
        return f'{self.request_number} - {self.service.service_name}'


class ESSAnalytics(models.Model):
    """
    ESS analytics tracking
    Following BBP 1.3.10 ESS Analytics Schema
    """
    ACTION_TYPE_CHOICES = [
        ('Login', 'Login'),
        ('View Service', 'View Service'),
        ('Submit Request', 'Submit Request'),
        ('Update Profile', 'Update Profile'),
        ('Download Document', 'Download Document'),
        ('Track Request', 'Track Request'),
    ]
    
    DEVICE_TYPE_CHOICES = [
        ('Desktop', 'Desktop'),
        ('Mobile', 'Mobile'),
        ('Tablet', 'Tablet'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_code = models.CharField(max_length=10, db_index=True, default=DEFAULT_COMPANY_CODE)
    employee = models.ForeignKey('EmployeeRecord', on_delete=models.CASCADE, related_name='ess_analytics')
    action_type = models.CharField(max_length=20, choices=ACTION_TYPE_CHOICES, db_index=True)
    service_category = models.CharField(max_length=100, null=True, blank=True, db_index=True)
    service = models.ForeignKey('ESSServiceCatalog', on_delete=models.SET_NULL, null=True, blank=True, related_name='analytics')
    service_request = models.ForeignKey('ESSServiceRequest', on_delete=models.SET_NULL, null=True, blank=True, related_name='analytics')
    session_id = models.CharField(max_length=100, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
    device_type = models.CharField(max_length=20, choices=DEVICE_TYPE_CHOICES, null=True, blank=True, db_index=True)
    browser = models.CharField(max_length=100, null=True, blank=True)
    action_timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    processing_time_ms = models.IntegerField(null=True, blank=True)
    success_flag = models.BooleanField(default=True)
    error_message = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'ess_analytics'
        verbose_name = 'ESS Analytics'
        verbose_name_plural = 'ESS Analytics'
        indexes = [
            models.Index(fields=['company_code', 'employee'], name='idx_ess_analytics_comp_emp'),
            models.Index(fields=['action_type'], name='idx_ess_analytics_action'),
            models.Index(fields=['service_category'], name='idx_ess_analytics_category'),
            models.Index(fields=['service'], name='idx_ess_analytics_service'),
            models.Index(fields=['service_request'], name='idx_ess_analytics_request'),
            models.Index(fields=['action_timestamp'], name='idx_ess_analytics_timestamp'),
            models.Index(fields=['device_type'], name='idx_ess_analytics_device'),
        ]

    def __str__(self):
        return f'{self.action_type} by {self.employee.first_name} {self.employee.last_name}'


class ESSAuditLog(models.Model):
    """
    ESS audit log for compliance
    Following BBP 1.3.11 ESS Audit Log Schema
    """
    ACTION_CHOICES = [
        ('Create', 'Create'),
        ('Update', 'Update'),
        ('Delete', 'Delete'),
        ('Submit', 'Submit'),
        ('Approve', 'Approve'),
        ('Reject', 'Reject'),
        ('View', 'View'),
        ('Download', 'Download'),
    ]
    
    ENTITY_TYPE_CHOICES = [
        ('Change Request', 'Change Request'),
        ('Service Request', 'Service Request'),
        ('Personal Info', 'Personal Info'),
        ('Document', 'Document'),
        ('Approval Workflow', 'Approval Workflow'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_code = models.CharField(max_length=10, db_index=True, default=DEFAULT_COMPANY_CODE)
    employee = models.ForeignKey('EmployeeRecord', on_delete=models.CASCADE, related_name='ess_audit_logs')
    action = models.CharField(max_length=20, choices=ACTION_CHOICES, db_index=True)
    entity_type = models.CharField(max_length=20, choices=ENTITY_TYPE_CHOICES, db_index=True)
    entity_id = models.UUIDField(null=True, blank=True, db_index=True)
    old_values = models.JSONField(default=dict, help_text="Previous values")
    new_values = models.JSONField(default=dict, help_text="Updated values")
    field_changes = models.JSONField(default=dict, help_text="Specific field changes")
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
    session_id = models.CharField(max_length=100, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    additional_context = models.JSONField(default=dict, help_text="Extra context information")

    class Meta:
        db_table = 'ess_audit_log'
        verbose_name = 'ESS Audit Log'
        verbose_name_plural = 'ESS Audit Logs'
        indexes = [
            models.Index(fields=['company_code', 'employee'], name='idx_ess_audit_company_employee'),
            models.Index(fields=['action'], name='idx_ess_audit_action'),
            models.Index(fields=['entity_type'], name='idx_ess_audit_entity_type'),
            models.Index(fields=['entity_id'], name='idx_ess_audit_entity_id'),
            models.Index(fields=['timestamp'], name='idx_ess_audit_timestamp'),
        ]

    def __str__(self):
        return f'{self.action} {self.entity_type} by {self.employee.first_name} {self.employee.last_name}'
