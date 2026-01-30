"""
Employee Lifecycle Management Serializers

This module provides serializers for all employee lifecycle management models including:
- State machine transitions
- Event logging and audit trails
- Employee lifecycle status management
- Analytics and compliance monitoring
- Workflow triggers and reporting
"""

from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models.employee_lifecycle import (
    LifecycleStateMachine, LifecycleEventLog, EmployeeLifecycle, LifecycleAnalytics,
    LifecycleComplianceMonitoring, AutomatedWorkflowTrigger, LifecycleReporting
)

User = get_user_model()


class LifecycleStateMachineSerializer(serializers.ModelSerializer):
    """Serializer for Lifecycle State Machine model"""
    
    approver_name = serializers.CharField(source='approver.get_full_name', read_only=True)
    created_by_name = serializers.CharField(source='created_by.get_full_name', read_only=True)
    
    class Meta:
        model = LifecycleStateMachine
        fields = [
            'id', 'company', 'state_machine_name', 'current_state', 'previous_state',
            'target_state', 'transition_event', 'transition_condition', 'action_required',
            'auto_transition', 'transition_timeout_hours', 'approval_required',
            'approver_type', 'approver', 'approver_name', 'notification_template',
            'is_active', 'effective_from', 'effective_to', 'created_by', 'created_by_name',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class LifecycleEventLogSerializer(serializers.ModelSerializer):
    """Serializer for Lifecycle Event Log model"""
    
    employee_name = serializers.CharField(source='employee.employee_name', read_only=True)
    employee_number = serializers.CharField(source='employee.employee_number', read_only=True)
    initiated_by_name = serializers.CharField(source='initiated_by.get_full_name', read_only=True)
    approved_by_name = serializers.CharField(source='approved_by.get_full_name', read_only=True)
    
    class Meta:
        model = LifecycleEventLog
        fields = [
            'id', 'employee', 'employee_name', 'employee_number', 'event_type',
            'event_sub_type', 'previous_status', 'new_status', 'event_date',
            'effective_date', 'reason_code', 'event_description', 'initiated_by',
            'initiated_by_name', 'approved_by', 'approved_by_name', 'approved_at',
            'status', 'priority', 'workflow_instance_id', 'supporting_documents',
            'system_generated', 'batch_reference', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class EmployeeLifecycleSerializer(serializers.ModelSerializer):
    """Serializer for Employee Lifecycle model"""
    
    employee_name = serializers.CharField(source='employee.employee_name', read_only=True)
    employee_number = serializers.CharField(source='employee.employee_number', read_only=True)
    years_of_service = serializers.ReadOnlyField()
    is_probation_complete = serializers.ReadOnlyField()
    days_to_contract_end = serializers.ReadOnlyField()
    
    class Meta:
        model = EmployeeLifecycle
        fields = [
            'id', 'employee', 'employee_name', 'employee_number', 'hire_date',
            'confirmation_date', 'employment_status', 'probation_end_date',
            'contract_start_date', 'contract_end_date', 'notice_period_days',
            'last_working_day', 'separation_reason', 'separation_type',
            'is_rehireable', 'exit_interview_completed', 'final_payroll_processed',
            'years_of_service', 'is_probation_complete', 'days_to_contract_end',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class LifecycleAnalyticsSerializer(serializers.ModelSerializer):
    """Serializer for Lifecycle Analytics model"""
    
    employee_name = serializers.CharField(source='employee.employee_name', read_only=True)
    employee_number = serializers.CharField(source='employee.employee_number', read_only=True)
    department_name = serializers.CharField(source='department.department_name', read_only=True)
    location_name = serializers.CharField(source='location.unit_name', read_only=True)
    manager_name = serializers.CharField(source='manager.employee_name', read_only=True)
    hr_rep_name = serializers.CharField(source='hr_rep.get_full_name', read_only=True)
    
    class Meta:
        model = LifecycleAnalytics
        fields = [
            'id', 'company', 'employee', 'employee_name', 'employee_number',
            'event_type', 'event_date', 'processing_time_days',
            'workflow_completion_time_hours', 'satisfaction_rating', 'feedback_score',
            'cost_impact', 'department', 'department_name', 'location',
            'location_name', 'manager', 'manager_name', 'hr_rep', 'hr_rep_name',
            'metrics_data', 'benchmark_comparison', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']


class LifecycleComplianceMonitoringSerializer(serializers.ModelSerializer):
    """Serializer for Lifecycle Compliance Monitoring model"""
    
    created_by_name = serializers.CharField(source='created_by.get_full_name', read_only=True)
    responsible_user_name = serializers.CharField(source='responsible_user.get_full_name', read_only=True)
    
    class Meta:
        model = LifecycleComplianceMonitoring
        fields = [
            'id', 'company', 'compliance_rule_name', 'compliance_type',
            'lifecycle_event', 'check_frequency', 'compliance_check',
            'threshold_value', 'tolerance_percentage', 'notification_threshold',
            'escalation_threshold', 'responsible_role', 'responsible_user',
            'responsible_user_name', 'notification_template', 'is_active',
            'last_check_date', 'next_check_date', 'created_by', 'created_by_name',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class AutomatedWorkflowTriggerSerializer(serializers.ModelSerializer):
    """Serializer for Automated Workflow Trigger model"""
    
    created_by_name = serializers.CharField(source='created_by.get_full_name', read_only=True)
    
    class Meta:
        model = AutomatedWorkflowTrigger
        fields = [
            'id', 'company', 'trigger_name', 'trigger_event', 'trigger_condition',
            'workflow_template_id', 'trigger_timing', 'delay_minutes',
            'schedule_pattern', 'is_active', 'execution_count', 'last_executed_at',
            'next_execution_at', 'success_rate', 'error_count', 'created_by',
            'created_by_name', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class LifecycleReportingSerializer(serializers.ModelSerializer):
    """Serializer for Lifecycle Reporting model"""
    
    created_by_name = serializers.CharField(source='created_by.get_full_name', read_only=True)
    generated_by_name = serializers.CharField(source='generated_by.get_full_name', read_only=True)
    
    class Meta:
        model = LifecycleReporting
        fields = [
            'id', 'company', 'report_name', 'report_type', 'report_frequency',
            'report_parameters', 'data_sources', 'calculation_logic', 'output_format',
            'distribution_list', 'is_scheduled', 'schedule_pattern', 'last_generated_at',
            'next_generation_at', 'generated_by', 'generated_by_name', 'file_path',
            'file_size', 'is_active', 'created_by', 'created_by_name',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class EmployeeLifecycleDetailSerializer(serializers.ModelSerializer):
    """Detailed serializer for Employee Lifecycle with related data"""
    
    employee_name = serializers.CharField(source='employee.employee_name', read_only=True)
    employee_number = serializers.CharField(source='employee.employee_number', read_only=True)
    department = serializers.CharField(source='employee.department.department_name', read_only=True)
    position = serializers.CharField(source='employee.position.position_title', read_only=True)
    years_of_service = serializers.ReadOnlyField()
    is_probation_complete = serializers.ReadOnlyField()
    days_to_contract_end = serializers.ReadOnlyField()
    recent_events = LifecycleEventLogSerializer(
        source='lifecycle_events',
        many=True,
        read_only=True
    )
    
    class Meta:
        model = EmployeeLifecycle
        fields = [
            'id', 'employee', 'employee_name', 'employee_number', 'department',
            'position', 'hire_date', 'confirmation_date', 'employment_status',
            'probation_end_date', 'contract_start_date', 'contract_end_date',
            'notice_period_days', 'last_working_day', 'separation_reason',
            'separation_type', 'is_rehireable', 'exit_interview_completed',
            'final_payroll_processed', 'years_of_service', 'is_probation_complete',
            'days_to_contract_end', 'recent_events', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class LifecycleEventLogCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating Lifecycle Event Log entries"""
    
    class Meta:
        model = LifecycleEventLog
        fields = [
            'employee', 'event_type', 'event_sub_type', 'previous_status',
            'new_status', 'event_date', 'effective_date', 'reason_code',
            'event_description', 'priority', 'workflow_instance_id',
            'supporting_documents', 'system_generated', 'batch_reference'
        ]


class LifecycleEventLogUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating Lifecycle Event Log entries"""
    
    class Meta:
        model = LifecycleEventLog
        fields = [
            'event_sub_type', 'previous_status', 'new_status', 'event_date',
            'effective_date', 'reason_code', 'event_description', 'status',
            'priority', 'workflow_instance_id', 'supporting_documents',
            'approved_by', 'approved_at'
        ]


class EmployeeLifecycleCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating Employee Lifecycle entries"""
    
    class Meta:
        model = EmployeeLifecycle
        fields = [
            'employee', 'hire_date', 'confirmation_date', 'employment_status',
            'probation_end_date', 'contract_start_date', 'contract_end_date',
            'notice_period_days', 'last_working_day', 'separation_reason',
            'separation_type', 'is_rehireable', 'exit_interview_completed',
            'final_payroll_processed'
        ]


class EmployeeLifecycleUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating Employee Lifecycle entries"""
    
    class Meta:
        model = EmployeeLifecycle
        fields = [
            'confirmation_date', 'employment_status', 'probation_end_date',
            'contract_start_date', 'contract_end_date', 'notice_period_days',
            'last_working_day', 'separation_reason', 'separation_type',
            'is_rehireable', 'exit_interview_completed', 'final_payroll_processed'
        ]


class LifecycleAnalyticsCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating Lifecycle Analytics entries"""
    
    class Meta:
        model = LifecycleAnalytics
        fields = [
            'company', 'employee', 'event_type', 'event_date',
            'processing_time_days', 'workflow_completion_time_hours',
            'satisfaction_rating', 'feedback_score', 'cost_impact',
            'department', 'location', 'manager', 'hr_rep',
            'metrics_data', 'benchmark_comparison'
        ]


class LifecycleComplianceMonitoringCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating Lifecycle Compliance Monitoring entries"""
    
    class Meta:
        model = LifecycleComplianceMonitoring
        fields = [
            'company', 'compliance_rule_name', 'compliance_type',
            'lifecycle_event', 'check_frequency', 'compliance_check',
            'threshold_value', 'tolerance_percentage', 'notification_threshold',
            'escalation_threshold', 'responsible_role', 'responsible_user',
            'notification_template', 'is_active', 'last_check_date',
            'next_check_date'
        ]


class AutomatedWorkflowTriggerCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating Automated Workflow Trigger entries"""
    
    class Meta:
        model = AutomatedWorkflowTrigger
        fields = [
            'company', 'trigger_name', 'trigger_event', 'trigger_condition',
            'workflow_template_id', 'trigger_timing', 'delay_minutes',
            'schedule_pattern', 'is_active'
        ]


class LifecycleReportingCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating Lifecycle Reporting entries"""
    
    class Meta:
        model = LifecycleReporting
        fields = [
            'company', 'report_name', 'report_type', 'report_frequency',
            'report_parameters', 'data_sources', 'calculation_logic',
            'output_format', 'distribution_list', 'is_scheduled',
            'schedule_pattern', 'is_active'
        ]
