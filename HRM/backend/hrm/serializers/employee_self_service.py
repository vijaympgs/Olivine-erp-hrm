"""
Employee Self-Service Serializers - Following BBP 1.3 Employee Self-Service specifications
API serializers for ESS functionality with proper validation and company scoping
"""
from rest_framework import serializers
from django.contrib.auth.models import User
from ..models.employee_self_service import (
    EmployeeChangeRequest, ApprovalMatrix, ApprovalWorkflow, ESSConfiguration,
    ESSServiceCatalog, ESSServiceRequest, ESSAnalytics, ESSAuditLog
)
from ..models.employee import EmployeeRecord
from ..models.document import EmployeeDocument


class EmployeeChangeRequestSerializer(serializers.ModelSerializer):
    """
    Serializer for employee change requests
    Following BBP 1.3.3 Change Request Schema
    """
    employee_name = serializers.CharField(source='employee.get_full_name', read_only=True)
    employee_number = serializers.CharField(source='employee.employee_number', read_only=True)
    supporting_document_name = serializers.CharField(source='supporting_document.document_name', read_only=True)
    approved_by_name = serializers.CharField(source='approved_by_user.get_full_name', read_only=True)
    
    class Meta:
        model = EmployeeChangeRequest
        fields = [
            'id', 'company_code', 'employee', 'employee_name', 'employee_number',
            'request_type', 'field_name', 'old_value', 'new_value', 'change_reason',
            'supporting_document', 'supporting_document_name', 'status', 'priority',
            'submitted_at', 'approved_by_user', 'approved_by_name', 'approved_at',
            'rejection_reason', 'completed_at', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'company_code', 'employee', 'submitted_at', 'approved_by_user', 'approved_at', 'completed_at', 'created_at', 'updated_at']

    def validate_new_value(self, value):
        """Validate that new value is not empty"""
        if not value or not value.strip():
            raise serializers.ValidationError("New value cannot be empty")
        return value.strip()

    def validate_change_reason(self, value):
        """Validate that change reason is provided"""
        if not value or not value.strip():
            raise serializers.ValidationError("Change reason is required")
        if len(value.strip()) < 10:
            raise serializers.ValidationError("Change reason must be at least 10 characters long")
        return value.strip()


class ApprovalMatrixSerializer(serializers.ModelSerializer):
    """
    Serializer for approval matrix configuration
    Following BBP 1.3.4 Approval Matrix Schema
    """
    company_name = serializers.CharField(source='company.name', read_only=True)
    department_name = serializers.CharField(source='department.name', read_only=True)
    location_name = serializers.CharField(source='location.name', read_only=True)
    approver_name = serializers.CharField(source='approver.get_full_name', read_only=True)
    
    class Meta:
        model = ApprovalMatrix
        fields = [
            'id', 'company', 'company_name', 'request_type', 'employee_category',
            'department', 'department_name', 'location', 'location_name',
            'approval_level', 'approver_type', 'approver', 'approver_name',
            'is_required', 'is_parallel', 'time_limit_hours', 'auto_approve',
            'conditions', 'is_active', 'effective_from', 'effective_to',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_approval_level(self, value):
        """Validate approval level is positive"""
        if value <= 0:
            raise serializers.ValidationError("Approval level must be greater than 0")
        return value

    def validate_time_limit_hours(self, value):
        """Validate time limit is reasonable"""
        if value <= 0:
            raise serializers.ValidationError("Time limit must be greater than 0")
        if value > 168:  # 1 week
            raise serializers.ValidationError("Time limit cannot exceed 168 hours (1 week)")
        return value


class ApprovalWorkflowSerializer(serializers.ModelSerializer):
    """
    Serializer for approval workflow tracking
    Following BBP 1.3.5 Approval Workflow Schema
    """
    request_details = serializers.CharField(source='request.get_change_summary', read_only=True)
    approver_name = serializers.CharField(source='approver.get_full_name', read_only=True)
    delegated_to_name = serializers.CharField(source='delegated_to_user.get_full_name', read_only=True)
    escalated_to_name = serializers.CharField(source='escalated_to_user.get_full_name', read_only=True)
    
    class Meta:
        model = ApprovalWorkflow
        fields = [
            'id', 'request', 'request_details', 'matrix', 'approver', 'approver_name',
            'approval_level', 'status', 'decision', 'comments', 'attachments',
            'delegated_to_user', 'delegated_to_name', 'escalated_to_user', 'escalated_to_name',
            'due_date', 'action_date', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'request', 'matrix', 'approver', 'created_at', 'updated_at']

    def validate_decision(self, value):
        """Validate decision is valid for current status"""
        if self.instance and self.instance.status == 'Pending' and value not in ['Approve', 'Reject', 'Request More Info', 'Delegate']:
            raise serializers.ValidationError("Invalid decision for pending workflow")
        return value


class ESSConfigurationSerializer(serializers.ModelSerializer):
    """
    Serializer for ESS configuration settings
    Following BBP 1.3.6 Self-Service Configuration Schema
    """
    company_name = serializers.CharField(source='company.name', read_only=True)
    created_by_name = serializers.CharField(source='created_by_user.get_full_name', read_only=True)
    
    class Meta:
        model = ESSConfiguration
        fields = [
            'id', 'company', 'company_name', 'module_name', 'feature_name',
            'is_enabled', 'configuration', 'access_roles', 'employee_categories',
            'departments', 'locations', 'validation_rules', 'notification_settings',
            'approval_required', 'auto_approve_conditions', 'effective_from',
            'effective_to', 'created_by_user', 'created_by_name', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_by_user', 'created_at', 'updated_at']

    def validate_effective_to(self, value):
        """Validate effective dates"""
        if value and self.initial_data.get('effective_from') and value < self.initial_data['effective_from']:
            raise serializers.ValidationError("Effective to date cannot be before effective from date")
        return value


class ESSServiceCatalogSerializer(serializers.ModelSerializer):
    """
    Serializer for ESS service catalog
    Following BBP 1.3.8 Service Catalog Schema
    """
    company_name = serializers.CharField(source='company.name', read_only=True)
    created_by_name = serializers.CharField(source='created_by_user.get_full_name', read_only=True)
    
    class Meta:
        model = ESSServiceCatalog
        fields = [
            'id', 'company', 'company_name', 'service_code', 'service_name',
            'service_category', 'service_description', 'service_type', 'target_audience',
            'prerequisites', 'process_steps', 'sla_hours', 'auto_approve',
            'fee_applicable', 'fee_amount', 'is_active', 'display_order',
            'icon_name', 'help_text', 'created_by_user', 'created_by_name',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_by_user', 'created_at', 'updated_at']

    def validate_service_code(self, value):
        """Validate service code format"""
        if not value or not value.strip():
            raise serializers.ValidationError("Service code is required")
        if not value.replace('_', '').replace('-', '').isalnum():
            raise serializers.ValidationError("Service code can only contain letters, numbers, underscores, and hyphens")
        return value.upper().strip()

    def validate_sla_hours(self, value):
        """Validate SLA hours"""
        if value <= 0:
            raise serializers.ValidationError("SLA hours must be greater than 0")
        if value > 720:  # 30 days
            raise serializers.ValidationError("SLA hours cannot exceed 720 hours (30 days)")
        return value

    def validate_fee_amount(self, value):
        """Validate fee amount"""
        if value < 0:
            raise serializers.ValidationError("Fee amount cannot be negative")
        return value


class ESSServiceRequestSerializer(serializers.ModelSerializer):
    """
    Serializer for ESS service requests
    Following BBP 1.3.9 Service Request Schema
    """
    employee_name = serializers.CharField(source='employee.get_full_name', read_only=True)
    employee_number = serializers.CharField(source='employee.employee_number', read_only=True)
    service_name = serializers.CharField(source='service.service_name', read_only=True)
    service_code = serializers.CharField(source='service.service_code', read_only=True)
    assigned_to_name = serializers.CharField(source='assigned_to_user.get_full_name', read_only=True)
    
    class Meta:
        model = ESSServiceRequest
        fields = [
            'id', 'request_number', 'employee', 'employee_name', 'employee_number',
            'service', 'service_name', 'service_code', 'request_data', 'status',
            'priority', 'assigned_to_user', 'assigned_to_name', 'submitted_at',
            'due_date', 'completed_at', 'completion_notes', 'employee_rating',
            'employee_feedback', 'processing_time_hours', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'request_number', 'employee', 'service', 'submitted_at', 'completed_at', 'processing_time_hours', 'created_at', 'updated_at']

    def validate_employee_rating(self, value):
        """Validate employee rating"""
        if value is not None and (value < 1 or value > 5):
            raise serializers.ValidationError("Employee rating must be between 1 and 5")
        return value

    def validate_request_data(self, value):
        """Validate request data is not empty"""
        if not value or not isinstance(value, dict):
            raise serializers.ValidationError("Request data must be a valid JSON object")
        return value


class ESSAnalyticsSerializer(serializers.ModelSerializer):
    """
    Serializer for ESS analytics tracking
    Following BBP 1.3.10 ESS Analytics Schema
    """
    employee_name = serializers.CharField(source='employee.get_full_name', read_only=True)
    employee_number = serializers.CharField(source='employee.employee_number', read_only=True)
    service_name = serializers.CharField(source='service.service_name', read_only=True)
    service_request_number = serializers.CharField(source='service_request.request_number', read_only=True)
    
    class Meta:
        model = ESSAnalytics
        fields = [
            'id', 'company_code', 'employee', 'employee_name', 'employee_number',
            'action_type', 'service_category', 'service', 'service_name',
            'service_request', 'service_request_number', 'session_id', 'ip_address',
            'user_agent', 'device_type', 'browser', 'action_timestamp',
            'processing_time_ms', 'success_flag', 'error_message'
        ]
        read_only_fields = ['id', 'company_code', 'employee', 'action_timestamp']

    def validate_processing_time_ms(self, value):
        """Validate processing time"""
        if value is not None and value < 0:
            raise serializers.ValidationError("Processing time cannot be negative")
        return value


class ESSAuditLogSerializer(serializers.ModelSerializer):
    """
    Serializer for ESS audit log
    Following BBP 1.3.11 ESS Audit Log Schema
    """
    employee_name = serializers.CharField(source='employee.get_full_name', read_only=True)
    employee_number = serializers.CharField(source='employee.employee_number', read_only=True)
    
    class Meta:
        model = ESSAuditLog
        fields = [
            'id', 'company_code', 'employee', 'employee_name', 'employee_number',
            'action', 'entity_type', 'entity_id', 'old_values', 'new_values',
            'field_changes', 'ip_address', 'user_agent', 'session_id',
            'timestamp', 'additional_context'
        ]
        read_only_fields = ['id', 'company_code', 'employee', 'timestamp']

    def validate_old_values(self, value):
        """Validate old values is valid JSON"""
        if value is not None and not isinstance(value, dict):
            raise serializers.ValidationError("Old values must be a valid JSON object")
        return value

    def validate_new_values(self, value):
        """Validate new values is valid JSON"""
        if value is not None and not isinstance(value, dict):
            raise serializers.ValidationError("New values must be a valid JSON object")
        return value

    def validate_field_changes(self, value):
        """Validate field changes is valid JSON"""
        if value is not None and not isinstance(value, dict):
            raise serializers.ValidationError("Field changes must be a valid JSON object")
        return value


# Summary Serializers for Dashboard and List Views
class ESSDashboardSerializer(serializers.Serializer):
    """
    Summary serializer for ESS dashboard
    """
    total_change_requests = serializers.IntegerField()
    pending_change_requests = serializers.IntegerField()
    total_service_requests = serializers.IntegerField()
    pending_service_requests = serializers.IntegerField()
    recent_activities = ESSAnalyticsSerializer(many=True)
    quick_actions = serializers.ListField()


class ESSServiceCatalogListSerializer(serializers.ModelSerializer):
    """
    Lightweight serializer for service catalog list
    """
    class Meta:
        model = ESSServiceCatalog
        fields = ['id', 'service_code', 'service_name', 'service_category', 'service_description', 'icon_name', 'is_active']


class ESSChangeRequestListSerializer(serializers.ModelSerializer):
    """
    Lightweight serializer for change request list
    """
    employee_name = serializers.CharField(source='employee.get_full_name', read_only=True)
    employee_number = serializers.CharField(source='employee.employee_number', read_only=True)
    
    class Meta:
        model = EmployeeChangeRequest
        fields = ['id', 'request_type', 'field_name', 'status', 'priority', 'submitted_at', 'employee_name', 'employee_number']


class ESSServiceRequestListSerializer(serializers.ModelSerializer):
    """
    Lightweight serializer for service request list
    """
    employee_name = serializers.CharField(source='employee.get_full_name', read_only=True)
    employee_number = serializers.CharField(source='employee.employee_number', read_only=True)
    service_name = serializers.CharField(source='service.service_name', read_only=True)
    
    class Meta:
        model = ESSServiceRequest
        fields = ['id', 'request_number', 'service_name', 'status', 'priority', 'submitted_at', 'employee_name', 'employee_number']
