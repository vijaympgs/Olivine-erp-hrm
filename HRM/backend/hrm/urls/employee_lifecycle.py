"""
Employee Lifecycle Management URLs

This module defines URL patterns for all employee lifecycle management API endpoints including:
- State machine transitions
- Event logging and audit trails
- Employee lifecycle status management
- Analytics and compliance monitoring
- Workflow triggers and reporting
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from ..views.employee_lifecycle import (
    LifecycleStateMachineViewSet,
    LifecycleEventLogViewSet,
    EmployeeLifecycleViewSet,
    LifecycleAnalyticsViewSet,
    LifecycleComplianceMonitoringViewSet,
    AutomatedWorkflowTriggerViewSet,
    LifecycleReportingViewSet
)

router = DefaultRouter()
router.register(r'state-machines', LifecycleStateMachineViewSet, basename='lifecycle-state-machine')
router.register(r'event-logs', LifecycleEventLogViewSet, basename='lifecycle-event-log')
router.register(r'employee-lifecycles', EmployeeLifecycleViewSet, basename='employee-lifecycle')
router.register(r'analytics', LifecycleAnalyticsViewSet, basename='lifecycle-analytics')
router.register(r'compliance-monitoring', LifecycleComplianceMonitoringViewSet, basename='lifecycle-compliance-monitoring')
router.register(r'workflow-triggers', AutomatedWorkflowTriggerViewSet, basename='automated-workflow-trigger')
router.register(r'reporting', LifecycleReportingViewSet, basename='lifecycle-reporting')

app_name = 'hrm_lifecycle'

urlpatterns = [
    path('lifecycle/', include(router.urls)),
]
