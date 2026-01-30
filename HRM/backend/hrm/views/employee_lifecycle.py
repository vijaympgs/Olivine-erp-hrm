"""
Employee Lifecycle Management Views

This module provides API views for all employee lifecycle management operations including:
- State machine transitions
- Event logging and audit trails
- Employee lifecycle status management
- Analytics and compliance monitoring
- Workflow triggers and reporting
"""

from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.db import models

from ..models.employee_lifecycle import (
    LifecycleStateMachine, LifecycleEventLog, EmployeeLifecycle, LifecycleAnalytics,
    LifecycleComplianceMonitoring, AutomatedWorkflowTrigger, LifecycleReporting
)
from ..serializers.employee_lifecycle import (
    LifecycleStateMachineSerializer, LifecycleEventLogSerializer, EmployeeLifecycleSerializer,
    LifecycleAnalyticsSerializer, LifecycleComplianceMonitoringSerializer,
    AutomatedWorkflowTriggerSerializer, LifecycleReportingSerializer,
    EmployeeLifecycleDetailSerializer, LifecycleEventLogCreateSerializer,
    LifecycleEventLogUpdateSerializer, EmployeeLifecycleCreateSerializer,
    EmployeeLifecycleUpdateSerializer
)

User = get_user_model()


class LifecycleStateMachineViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Lifecycle State Machine configurations
    """
    queryset = LifecycleStateMachine.objects.all()
    serializer_class = LifecycleStateMachineSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['company', 'current_state', 'target_state', 'transition_event', 'is_active']
    search_fields = ['state_machine_name', 'current_state', 'target_state', 'transition_event']
    ordering_fields = ['created_at', 'effective_from', 'state_machine_name']
    ordering = ['-created_at']

    def get_queryset(self):
        """Filter by company based on user permissions"""
        user = self.request.user
        queryset = super().get_queryset()
        
        # Filter by user's company
        if hasattr(user, 'company') and user.company:
            queryset = queryset.filter(company=user.company)
        
        return queryset

    @action(detail=False, methods=['get'])
    def active_transitions(self, request):
        """Get all active state machine transitions"""
        queryset = self.get_queryset().filter(is_active=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class LifecycleEventLogViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Lifecycle Event Log entries
    """
    queryset = LifecycleEventLog.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['employee', 'event_type', 'status', 'priority', 'initiated_by']
    search_fields = ['employee__employee_name', 'employee__employee_number', 'event_type', 'reason_code']
    ordering_fields = ['created_at', 'event_date', 'effective_date']
    ordering = ['-created_at']

    def get_serializer_class(self):
        """Return appropriate serializer based on action"""
        if self.action == 'create':
            return LifecycleEventLogCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return LifecycleEventLogUpdateSerializer
        return LifecycleEventLogSerializer

    def get_queryset(self):
        """Filter by company based on user permissions"""
        user = self.request.user
        queryset = super().get_queryset()
        
        # Filter by user's company through employee relationship
        if hasattr(user, 'company') and user.company:
            queryset = queryset.filter(employee__company=user.company)
        
        return queryset

    def perform_create(self, serializer):
        """Set initiated_by to current user"""
        serializer.save(initiated_by=self.request.user)

    @action(detail=False, methods=['get'])
    def pending_approval(self, request):
        """Get events pending approval"""
        queryset = self.get_queryset().filter(status='Pending Approval')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        """Approve a lifecycle event"""
        event = self.get_object()
        
        if event.status != 'Pending Approval':
            return Response(
                {'error': 'Only pending approval events can be approved'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        event.status = 'Approved'
        event.approved_by = request.user
        event.save()
        
        serializer = self.get_serializer(event)
        return Response(serializer.data)


class EmployeeLifecycleViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Employee Lifecycle records
    """
    queryset = EmployeeLifecycle.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['employment_status', 'separation_type']
    search_fields = ['employee__employee_name', 'employee__employee_number']
    ordering_fields = ['created_at', 'hire_date', 'confirmation_date']
    ordering = ['-created_at']

    def get_serializer_class(self):
        """Return appropriate serializer based on action"""
        if self.action == 'create':
            return EmployeeLifecycleCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return EmployeeLifecycleUpdateSerializer
        return EmployeeLifecycleSerializer

    def get_queryset(self):
        """Filter by company based on user permissions"""
        user = self.request.user
        queryset = super().get_queryset()
        
        # Filter by user's company through employee relationship
        if hasattr(user, 'company') and user.company:
            queryset = queryset.filter(employee__company=user.company)
        
        return queryset

    @action(detail=False, methods=['get'])
    def active_employees(self, request):
        """Get all active employee lifecycles"""
        queryset = self.get_queryset().filter(employment_status='Active')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def on_probation(self, request):
        """Get employees on probation"""
        queryset = self.get_queryset().filter(employment_status='Probation')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def details(self, request, pk=None):
        """Get detailed employee lifecycle information with related events"""
        lifecycle = self.get_object()
        serializer = EmployeeLifecycleDetailSerializer(lifecycle)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def confirm_employment(self, request, pk=None):
        """Confirm employee employment"""
        lifecycle = self.get_object()
        
        if lifecycle.employment_status != 'Probation':
            return Response(
                {'error': 'Only probation employees can be confirmed'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        lifecycle.employment_status = 'Active'
        lifecycle.confirmation_date = request.data.get('confirmation_date')
        lifecycle.save()
        
        # Create confirmation event log
        LifecycleEventLog.objects.create(
            employee=lifecycle.employee,
            event_type='Confirmation',
            previous_status='Probation',
            new_status='Active',
            event_date=request.data.get('confirmation_date'),
            effective_date=request.data.get('confirmation_date'),
            initiated_by=request.user,
            status='Completed',
            system_generated=True
        )
        
        serializer = self.get_serializer(lifecycle)
        return Response(serializer.data)


class LifecycleAnalyticsViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Lifecycle Analytics
    """
    queryset = LifecycleAnalytics.objects.all()
    serializer_class = LifecycleAnalyticsSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['company', 'event_type', 'department', 'location']
    search_fields = ['employee__employee_name', 'employee__employee_number', 'event_type']
    ordering_fields = ['created_at', 'event_date', 'processing_time_days']
    ordering = ['-created_at']

    def get_queryset(self):
        """Filter by company based on user permissions"""
        user = self.request.user
        queryset = super().get_queryset()
        
        # Filter by user's company
        if hasattr(user, 'company') and user.company:
            queryset = queryset.filter(company=user.company)
        
        return queryset

    @action(detail=False, methods=['get'])
    def turnover_analytics(self, request):
        """Get turnover analytics"""
        queryset = self.get_queryset().filter(event_type='Termination')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def hiring_analytics(self, request):
        """Get hiring analytics"""
        queryset = self.get_queryset().filter(event_type='Hire')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def summary_stats(self, request):
        """Get summary statistics for lifecycle events"""
        queryset = self.get_queryset()
        
        stats = {
            'total_events': queryset.count(),
            'avg_processing_time': queryset.aggregate(
                avg_time=models.Avg('processing_time_days')
            )['avg_time'] or 0,
            'avg_satisfaction': queryset.aggregate(
                avg_satisfaction=models.Avg('satisfaction_rating')
            )['avg_satisfaction'] or 0,
        }
        
        return Response(stats)


class LifecycleComplianceMonitoringViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Lifecycle Compliance Monitoring
    """
    queryset = LifecycleComplianceMonitoring.objects.all()
    serializer_class = LifecycleComplianceMonitoringSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['company', 'compliance_type', 'lifecycle_event', 'responsible_role']
    search_fields = ['compliance_rule_name', 'lifecycle_event']
    ordering_fields = ['created_at', 'compliance_rule_name']
    ordering = ['-created_at']

    def get_queryset(self):
        """Filter by company based on user permissions"""
        user = self.request.user
        queryset = super().get_queryset()
        
        # Filter by user's company
        if hasattr(user, 'company') and user.company:
            queryset = queryset.filter(company=user.company)
        
        return queryset

    @action(detail=False, methods=['get'])
    def active_rules(self, request):
        """Get all active compliance rules"""
        queryset = self.get_queryset().filter(is_active=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class AutomatedWorkflowTriggerViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Automated Workflow Triggers
    """
    queryset = AutomatedWorkflowTrigger.objects.all()
    serializer_class = AutomatedWorkflowTriggerSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['company', 'trigger_event', 'trigger_timing', 'is_active']
    search_fields = ['trigger_name', 'trigger_event']
    ordering_fields = ['created_at', 'trigger_name']
    ordering = ['-created_at']

    def get_queryset(self):
        """Filter by company based on user permissions"""
        user = self.request.user
        queryset = super().get_queryset()
        
        # Filter by user's company
        if hasattr(user, 'company') and user.company:
            queryset = queryset.filter(company=user.company)
        
        return queryset

    @action(detail=False, methods=['get'])
    def active_triggers(self, request):
        """Get all active workflow triggers"""
        queryset = self.get_queryset().filter(is_active=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class LifecycleReportingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Lifecycle Reporting
    """
    queryset = LifecycleReporting.objects.all()
    serializer_class = LifecycleReportingSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['company', 'report_type', 'report_frequency', 'is_active']
    search_fields = ['report_name', 'report_type']
    ordering_fields = ['created_at', 'report_name']
    ordering = ['-created_at']

    def get_queryset(self):
        """Filter by company based on user permissions"""
        user = self.request.user
        queryset = super().get_queryset()
        
        # Filter by user's company
        if hasattr(user, 'company') and user.company:
            queryset = queryset.filter(company=user.company)
        
        return queryset

    @action(detail=False, methods=['get'])
    def scheduled_reports(self, request):
        """Get all scheduled reports"""
        queryset = self.get_queryset().filter(is_scheduled=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def generate_report(self, request, pk=None):
        """Generate a report"""
        report = self.get_object()
        
        # Here you would implement the actual report generation logic
        # For now, just update the last_generated_at timestamp
        
        from django.utils import timezone
        report.last_generated_at = timezone.now()
        report.save()
        
        serializer = self.get_serializer(report)
        return Response(serializer.data)
