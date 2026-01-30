"""
Employee Lifecycle Management Models

This module implements comprehensive employee lifecycle management including:
- State machine framework for employee status transitions
- Event logging and audit trails
- Onboarding and offboarding workflows
- Compliance monitoring and analytics
- Automated workflow triggers
"""

import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models import Company

User = get_user_model()


class LifecycleStateMachine(models.Model):
    """
    Defines the state machine for employee lifecycle transitions
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='lifecycle_state_machines')
    state_machine_name = models.CharField(max_length=200)
    current_state = models.CharField(max_length=100)
    previous_state = models.CharField(max_length=100, blank=True, null=True)
    target_state = models.CharField(max_length=100)
    transition_event = models.CharField(max_length=100)
    transition_condition = models.JSONField(default=dict, blank=True)
    action_required = models.BooleanField(default=True)
    auto_transition = models.BooleanField(default=False)
    transition_timeout_hours = models.IntegerField(validators=[MinValueValidator(1)], blank=True, null=True)
    approval_required = models.BooleanField(default=False)
    approver_type = models.CharField(
        max_length=20,
        choices=[
            ('Manager', 'Manager'),
            ('HR Admin', 'HR Admin'),
            ('Department Head', 'Department Head'),
            ('Specific User', 'Specific User'),
        ],
        blank=True,
        null=True
    )
    approver = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='lifecycle_approvals')
    notification_template = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    effective_from = models.DateField()
    effective_to = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='lifecycle_state_machines_created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'hrm_lifecycle_state_machine'
        indexes = [
            models.Index(fields=['company']),
            models.Index(fields=['current_state']),
            models.Index(fields=['transition_event']),
            models.Index(fields=['target_state']),
            models.Index(fields=['is_active']),
            models.Index(fields=['effective_from']),
        ]

    def __str__(self):
        return f"{self.state_machine_name} - {self.current_state} → {self.target_state}"


class LifecycleEventLog(models.Model):
    """
    Logs all employee lifecycle events with complete audit trail
    """
    EVENT_TYPES = [
        ('Hire', 'Hire'),
        ('Onboarding', 'Onboarding'),
        ('Confirmation', 'Confirmation'),
        ('Promotion', 'Promotion'),
        ('Transfer', 'Transfer'),
        ('Department Change', 'Department Change'),
        ('Position Change', 'Position Change'),
        ('Leave', 'Leave'),
        ('Return from Leave', 'Return from Leave'),
        ('Suspension', 'Suspension'),
        ('Termination', 'Termination'),
        ('Retirement', 'Retirement'),
        ('Resignation', 'Resignation'),
        ('Contract End', 'Contract End'),
        ('Death', 'Death'),
    ]

    STATUSES = [
        ('Draft', 'Draft'),
        ('Submitted', 'Submitted'),
        ('Pending Approval', 'Pending Approval'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    PRIORITIES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Urgent', 'Urgent'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee = models.ForeignKey('EmployeeRecord', on_delete=models.CASCADE, related_name='lifecycle_events')
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
    event_sub_type = models.CharField(max_length=100, blank=True, null=True)
    previous_status = models.CharField(max_length=100, blank=True, null=True)
    new_status = models.CharField(max_length=100, blank=True, null=True)
    event_date = models.DateField()
    effective_date = models.DateField()
    reason_code = models.CharField(max_length=100, blank=True, null=True)
    event_description = models.TextField(blank=True, null=True)
    initiated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='lifecycle_events_initiated')
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='lifecycle_events_approved')
    approved_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUSES, default='Draft')
    priority = models.CharField(max_length=10, choices=PRIORITIES, default='Medium')
    workflow_instance_id = models.UUIDField(blank=True, null=True)
    supporting_documents = models.JSONField(default=list, blank=True)
    system_generated = models.BooleanField(default=False)
    batch_reference = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'hrm_lifecycle_event_log'
        indexes = [
            models.Index(fields=['employee']),
            models.Index(fields=['event_type']),
            models.Index(fields=['event_date']),
            models.Index(fields=['effective_date']),
            models.Index(fields=['status']),
            models.Index(fields=['initiated_by']),
            models.Index(fields=['approved_by']),
        ]

    def __str__(self):
        return f"{self.employee} - {self.event_type} ({self.event_date})"


class EmployeeLifecycle(models.Model):
    """
    Main employee lifecycle management model that consolidates all lifecycle information
    """
    EMPLOYMENT_STATUSES = [
        ('Active', 'Active'),
        ('On Leave', 'On Leave'),
        ('Probation', 'Probation'),
        ('Notice Period', 'Notice Period'),
        ('Terminated', 'Terminated'),
        ('Retired', 'Retired'),
        ('Resigned', 'Resigned'),
        ('Contract Ended', 'Contract Ended'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee = models.OneToOneField('EmployeeRecord', on_delete=models.CASCADE, related_name='lifecycle')
    hire_date = models.DateField()
    confirmation_date = models.DateField(blank=True, null=True)
    employment_status = models.CharField(max_length=20, choices=EMPLOYMENT_STATUSES, default='Active')
    probation_end_date = models.DateField(blank=True, null=True)
    contract_start_date = models.DateField(blank=True, null=True)
    contract_end_date = models.DateField(blank=True, null=True)
    notice_period_days = models.IntegerField(default=30)
    last_working_day = models.DateField(blank=True, null=True)
    separation_reason = models.CharField(max_length=200, blank=True, null=True)
    separation_type = models.CharField(
        max_length=20,
        choices=[
            ('Resignation', 'Resignation'),
            ('Termination', 'Termination'),
            ('Retirement', 'Retirement'),
            ('Contract End', 'Contract End'),
            ('Death', 'Death'),
            ('Layoff', 'Layoff'),
        ],
        blank=True,
        null=True
    )
    is_rehireable = models.BooleanField(default=True)
    exit_interview_completed = models.BooleanField(default=False)
    final_payroll_processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'hrm_employee_lifecycle'
        indexes = [
            models.Index(fields=['employee']),
            models.Index(fields=['employment_status']),
            models.Index(fields=['hire_date']),
            models.Index(fields=['confirmation_date']),
            models.Index(fields=['contract_end_date']),
            models.Index(fields=['last_working_day']),
        ]

    def __str__(self):
        return f"{self.employee} - {self.employment_status}"

    @property
    def years_of_service(self):
        """Calculate years of service based on hire date"""
        from datetime import date
        today = date.today()
        hire_date = self.hire_date
        years = today.year - hire_date.year - ((today.month, today.day) < (hire_date.month, hire_date.day))
        return years

    @property
    def is_probation_complete(self):
        """Check if probation period is complete"""
        if self.probation_end_date:
            from datetime import date
            return date.today() > self.probation_end_date
        return False

    @property
    def days_to_contract_end(self):
        """Calculate days until contract ends"""
        if self.contract_end_date:
            from datetime import date
            delta = self.contract_end_date - date.today()
            return delta.days if delta.days > 0 else 0
        return None


class LifecycleAnalytics(models.Model):
    """
    Analytics and metrics for employee lifecycle events
    """
    EVENT_TYPES = [
        ('Hire', 'Hire'),
        ('Onboarding', 'Onboarding'),
        ('Confirmation', 'Confirmation'),
        ('Promotion', 'Promotion'),
        ('Transfer', 'Transfer'),
        ('Leave', 'Leave'),
        ('Termination', 'Termination'),
        ('Retirement', 'Retirement'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='lifecycle_analytics')
    employee = models.ForeignKey('EmployeeRecord', on_delete=models.CASCADE, related_name='lifecycle_analytics')
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    event_date = models.DateField()
    processing_time_days = models.IntegerField(blank=True, null=True)
    workflow_completion_time_hours = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    satisfaction_rating = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    feedback_score = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(10)])
    cost_impact = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, blank=True, null=True)
    location = models.ForeignKey('OrganizationalUnit', on_delete=models.SET_NULL, blank=True, null=True)
    manager = models.ForeignKey('EmployeeRecord', on_delete=models.SET_NULL, blank=True, null=True, related_name='team_lifecycle_analytics')
    hr_rep = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='hr_lifecycle_analytics')
    metrics_data = models.JSONField(default=dict, blank=True)
    benchmark_comparison = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'hrm_lifecycle_analytics'
        indexes = [
            models.Index(fields=['company']),
            models.Index(fields=['employee']),
            models.Index(fields=['event_type']),
            models.Index(fields=['event_date']),
            models.Index(fields=['processing_time_days']),
            models.Index(fields=['satisfaction_rating']),
            models.Index(fields=['department']),
            models.Index(fields=['location']),
        ]

    def __str__(self):
        return f"{self.employee} - {self.event_type} Analytics"


class LifecycleComplianceMonitoring(models.Model):
    """
    Monitors compliance for lifecycle events
    """
    COMPLIANCE_TYPES = [
        ('Legal', 'Legal'),
        ('Policy', 'Policy'),
        ('Regulatory', 'Regulatory'),
        ('Contractual', 'Contractual'),
        ('Safety', 'Safety'),
    ]

    CHECK_FREQUENCIES = [
        ('One Time', 'One Time'),
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
        ('Quarterly', 'Quarterly'),
        ('Annually', 'Annually'),
    ]

    RESPONSIBLE_ROLES = [
        ('HR Admin', 'HR Admin'),
        ('Manager', 'Manager'),
        ('Compliance Officer', 'Compliance Officer'),
        ('Legal', 'Legal'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='lifecycle_compliance_monitoring')
    compliance_rule_name = models.CharField(max_length=200)
    compliance_type = models.CharField(max_length=20, choices=COMPLIANCE_TYPES)
    lifecycle_event = models.CharField(max_length=100)
    check_frequency = models.CharField(max_length=20, choices=CHECK_FREQUENCIES)
    compliance_check = models.TextField()
    threshold_value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tolerance_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    notification_threshold = models.DecimalField(max_digits=5, decimal_places=2, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    escalation_threshold = models.DecimalField(max_digits=5, decimal_places=2, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    responsible_role = models.CharField(max_length=20, choices=RESPONSIBLE_ROLES)
    responsible_user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='compliance_responsibilities')
    notification_template = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    last_check_date = models.DateField(blank=True, null=True)
    next_check_date = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='compliance_rules_created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'hrm_lifecycle_compliance_monitoring'
        indexes = [
            models.Index(fields=['company']),
            models.Index(fields=['compliance_type']),
            models.Index(fields=['lifecycle_event']),
            models.Index(fields=['check_frequency']),
            models.Index(fields=['is_active']),
            models.Index(fields=['last_check_date']),
            models.Index(fields=['next_check_date']),
        ]

    def __str__(self):
        return f"{self.compliance_rule_name} - {self.compliance_type}"


class AutomatedWorkflowTrigger(models.Model):
    """
    Defines automated workflow triggers for lifecycle events
    """
    TRIGGER_EVENTS = [
        ('Employee Hire', 'Employee Hire'),
        ('Status Change', 'Status Change'),
        ('Anniversary', 'Anniversary'),
        ('Probation End', 'Probation End'),
        ('Document Expiry', 'Document Expiry'),
        ('Leave Start', 'Leave Start'),
        ('Leave End', 'Leave End'),
        ('Termination', 'Termination'),
    ]

    TRIGGER_TIMINGS = [
        ('Immediate', 'Immediate'),
        ('Scheduled', 'Scheduled'),
        ('Delayed', 'Delayed'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='automated_workflow_triggers')
    trigger_name = models.CharField(max_length=200)
    trigger_event = models.CharField(max_length=20, choices=TRIGGER_EVENTS)
    trigger_condition = models.JSONField(default=dict, blank=True)
    workflow_template_id = models.UUIDField(blank=True, null=True)
    trigger_timing = models.CharField(max_length=20, choices=TRIGGER_TIMINGS, default='Immediate')
    delay_minutes = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    schedule_pattern = models.CharField(max_length=200, blank=True, null=True)  # Cron expression
    is_active = models.BooleanField(default=True)
    execution_count = models.IntegerField(default=0)
    last_executed_at = models.DateTimeField(blank=True, null=True)
    next_execution_at = models.DateTimeField(blank=True, null=True)
    success_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    error_count = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='workflow_triggers_created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'hrm_automated_workflow_trigger'
        indexes = [
            models.Index(fields=['company']),
            models.Index(fields=['trigger_event']),
            models.Index(fields=['workflow_template_id']),
            models.Index(fields=['trigger_timing']),
            models.Index(fields=['is_active']),
            models.Index(fields=['last_executed_at']),
            models.Index(fields=['next_execution_at']),
        ]

    def __str__(self):
        return f"{self.trigger_name} - {self.trigger_event}"


class LifecycleReporting(models.Model):
    """
    Configuration for lifecycle-related reports
    """
    REPORT_TYPES = [
        ('Headcount', 'Headcount'),
        ('Turnover', 'Turnover'),
        ('Hiring', 'Hiring'),
        ('Onboarding', 'Onboarding'),
        ('Offboarding', 'Offboarding'),
        ('Lifecycle Events', 'Lifecycle Events'),
        ('Compliance', 'Compliance'),
        ('Performance', 'Performance'),
    ]

    REPORT_FREQUENCIES = [
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
        ('Quarterly', 'Quarterly'),
        ('Annually', 'Annually'),
        ('On Demand', 'On Demand'),
    ]

    OUTPUT_FORMATS = [
        ('PDF', 'PDF'),
        ('Excel', 'Excel'),
        ('CSV', 'CSV'),
        ('HTML', 'HTML'),
        ('Dashboard', 'Dashboard'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='lifecycle_reporting')
    report_name = models.CharField(max_length=200)
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    report_frequency = models.CharField(max_length=20, choices=REPORT_FREQUENCIES)
    report_parameters = models.JSONField(default=dict, blank=True)
    data_sources = models.JSONField(default=list, blank=True)
    calculation_logic = models.JSONField(default=dict, blank=True)
    output_format = models.CharField(max_length=20, choices=OUTPUT_FORMATS, default='PDF')
    distribution_list = models.JSONField(default=list, blank=True)
    is_scheduled = models.BooleanField(default=False)
    schedule_pattern = models.CharField(max_length=200, blank=True, null=True)  # Cron expression
    last_generated_at = models.DateTimeField(blank=True, null=True)
    next_generation_at = models.DateTimeField(blank=True, null=True)
    generated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='reports_generated')
    file_path = models.CharField(max_length=1000, blank=True, null=True)
    file_size = models.BigInteger(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='reports_created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'hrm_lifecycle_reporting'
        indexes = [
            models.Index(fields=['company']),
            models.Index(fields=['report_type']),
            models.Index(fields=['report_frequency']),
            models.Index(fields=['is_scheduled']),
            models.Index(fields=['last_generated_at']),
            models.Index(fields=['next_generation_at']),
            models.Index(fields=['is_active']),
        ]

    def __str__(self):
        return f"{self.report_name} - {self.report_type}"
