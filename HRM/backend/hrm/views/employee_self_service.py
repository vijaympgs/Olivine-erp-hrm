"""
Employee Self-Service Views - Following BBP 1.3 Employee Self-Service specifications
API views for ESS functionality with proper permissions and company scoping
"""
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from django.db.models import Q, Count, Avg
from django.contrib.auth.models import User
from ..models.employee_self_service import (
    EmployeeChangeRequest, ApprovalMatrix, ApprovalWorkflow, ESSConfiguration,
    ESSServiceCatalog, ESSServiceRequest, ESSAnalytics, ESSAuditLog
)
from ..models.employee import EmployeeRecord
from ..serializers.employee_self_service import (
    EmployeeChangeRequestSerializer, ApprovalMatrixSerializer, ApprovalWorkflowSerializer,
    ESSConfigurationSerializer, ESSServiceCatalogSerializer, ESSServiceRequestSerializer,
    ESSAnalyticsSerializer, ESSAuditLogSerializer, ESSDashboardSerializer,
    ESSServiceCatalogListSerializer, ESSChangeRequestListSerializer, ESSServiceRequestListSerializer
)
from core.auth_access.backend.user_management.permissions import IsHRAdmin, IsEmployeeSelf, IsManager
from core.auth_access.backend.user_management.utils import get_current_company_code
import uuid
import logging

logger = logging.getLogger(__name__)


class EmployeeChangeRequestViewSet(viewsets.ModelViewSet):
    """
    ViewSet for employee change requests
    Following BBP 1.3.3 Change Request Schema
    """
    serializer_class = EmployeeChangeRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        """Filter by company and employee permissions"""
        company_code = get_current_company_code(self.request)
        user = self.request.user
        
        if user.is_staff or user.groups.filter(name='HR Admin').exists():
            # HR can see all change requests
            return EmployeeChangeRequest.objects.filter(company_code=company_code)
        else:
            # Employees can only see their own change requests
            try:
                employee = EmployeeRecord.objects.get(user=user, company_code=company_code)
                return EmployeeChangeRequest.objects.filter(company_code=company_code, employee=employee)
            except EmployeeRecord.DoesNotExist:
                return EmployeeChangeRequest.objects.none()
    
    def perform_create(self, serializer):
        """Set company code and employee on create"""
        company_code = get_current_company_code(self.request)
        user = self.request.user
        
        try:
            employee = EmployeeRecord.objects.get(user=user, company_code=company_code)
            serializer.save(company_code=company_code, employee=employee)
            
            # Log the action
            self._log_audit_action('Create', 'Change Request', serializer.instance.id, {}, serializer.validated_data)
            
        except EmployeeRecord.DoesNotExist:
            raise permissions.PermissionDenied("Employee record not found")
    
    def perform_update(self, serializer):
        """Log update action"""
        old_values = self.get_object().__dict__
        serializer.save()
        new_values = serializer.instance.__dict__
        
        # Log the action
        self._log_audit_action('Update', 'Change Request', serializer.instance.id, old_values, new_values)
    
    @action(detail=False, methods=['get'])
    def my_requests(self, request):
        """Get current user's change requests"""
        company_code = get_current_company_code(request)
        user = request.user
        
        try:
            employee = EmployeeRecord.objects.get(user=user, company_code=company_code)
            requests = EmployeeChangeRequest.objects.filter(company_code=company_code, employee=employee)
            serializer = self.get_serializer(requests, many=True)
            return Response(serializer.data)
        except EmployeeRecord.DoesNotExist:
            return Response({"error": "Employee record not found"}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['post'])
    def submit(self, request, pk=None):
        """Submit change request for approval"""
        change_request = self.get_object()
        
        if change_request.status != 'Draft':
            return Response({"error": "Only draft requests can be submitted"}, status=status.HTTP_400_BAD_REQUEST)
        
        change_request.status = 'Submitted'
        change_request.submitted_at = timezone.now()
        change_request.save()
        
        # Create approval workflow if needed
        self._create_approval_workflow(change_request)
        
        # Log the action
        self._log_audit_action('Submit', 'Change Request', change_request.id, {}, {'status': 'Submitted'})
        
        return Response({"message": "Change request submitted successfully"})
    
    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        """Approve change request"""
        change_request = self.get_object()
        
        if not request.user.groups.filter(name='HR Admin').exists():
            return Response({"error": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)
        
        if change_request.status not in ['Submitted', 'Pending Approval']:
            return Response({"error": "Request cannot be approved in current status"}, status=status.HTTP_400_BAD_REQUEST)
        
        change_request.status = 'Approved'
        change_request.approved_by_user = request.user
        change_request.approved_at = timezone.now()
        change_request.save()
        
        # Log the action
        self._log_audit_action('Approve', 'Change Request', change_request.id, {}, {'status': 'Approved'})
        
        return Response({"message": "Change request approved successfully"})
    
    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        """Reject change request"""
        change_request = self.get_object()
        rejection_reason = request.data.get('rejection_reason', '')
        
        if not request.user.groups.filter(name='HR Admin').exists():
            return Response({"error": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)
        
        if change_request.status not in ['Submitted', 'Pending Approval']:
            return Response({"error": "Request cannot be rejected in current status"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not rejection_reason:
            return Response({"error": "Rejection reason is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        change_request.status = 'Rejected'
        change_request.approved_by_user = request.user
        change_request.approved_at = timezone.now()
        change_request.rejection_reason = rejection_reason
        change_request.save()
        
        # Log the action
        self._log_audit_action('Reject', 'Change Request', change_request.id, {}, {'status': 'Rejected', 'rejection_reason': rejection_reason})
        
        return Response({"message": "Change request rejected successfully"})
    
    def _create_approval_workflow(self, change_request):
        """Create approval workflow for change request"""
        # Check if approval is required based on configuration
        try:
            config = ESSConfiguration.objects.get(
                company_code=change_request.company_code,
                module_name='ESS',
                feature_name=change_request.request_type,
                is_enabled=True
            )
            
            if not config.approval_required:
                # Auto-approve if no approval required
                change_request.status = 'Approved'
                change_request.approved_at = timezone.now()
                change_request.save()
                return
                
        except ESSConfiguration.DoesNotExist:
            # Default to requiring approval
            pass
        
        # Create approval workflow based on approval matrix
        approval_matrices = ApprovalMatrix.objects.filter(
            company__company_code=change_request.company_code,
            request_type=change_request.request_type,
            is_active=True
        ).order_by('approval_level')
        
        for matrix in approval_matrices:
            ApprovalWorkflow.objects.create(
                request=change_request,
                matrix=matrix,
                approver=matrix.approver,
                approval_level=matrix.approval_level,
                due_date=timezone.now() + timezone.timedelta(hours=matrix.time_limit_hours)
            )
    
    def _log_audit_action(self, action, entity_type, entity_id, old_values, new_values):
        """Log audit action"""
        ESSAuditLog.objects.create(
            company_code=get_current_company_code(self.request),
            employee=self.get_employee(),
            action=action,
            entity_type=entity_type,
            entity_id=entity_id,
            old_values=old_values,
            new_values=new_values,
            ip_address=self._get_client_ip(),
            user_agent=self.request.META.get('HTTP_USER_AGENT', ''),
            session_id=self.request.session.session_key
        )
    
    def _get_client_ip(self):
        """Get client IP address"""
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip
    
    def get_employee(self):
        """Get current employee"""
        try:
            company_code = get_current_company_code(self.request)
            return EmployeeRecord.objects.get(user=self.request.user, company_code=company_code)
        except EmployeeRecord.DoesNotExist:
            return None


class ESSServiceCatalogViewSet(viewsets.ModelViewSet):
    """
    ViewSet for ESS service catalog
    Following BBP 1.3.8 Service Catalog Schema
    """
    serializer_class = ESSServiceCatalogSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        """Filter by company and active status"""
        company_code = get_current_company_code(self.request)
        return ESSServiceCatalog.objects.filter(company__company_code=company_code, is_active=True)
    
    def get_serializer_class(self):
        """Use list serializer for list view"""
        if self.action == 'list':
            return ESSServiceCatalogListSerializer
        return ESSServiceCatalogSerializer
    
    @action(detail=False, methods=['get'])
    def by_category(self, request):
        """Get services grouped by category"""
        company_code = get_current_company_code(request)
        services = ESSServiceCatalog.objects.filter(company__company_code=company_code, is_active=True)
        
        categorized_services = {}
        for service in services:
            category = service.service_category
            if category not in categorized_services:
                categorized_services[category] = []
            categorized_services[category].append(ESSServiceCatalogListSerializer(service).data)
        
        return Response(categorized_services)
    
    @action(detail=True, methods=['get'])
    def details(self, request, pk=None):
        """Get detailed service information"""
        service = self.get_object()
        serializer = ESSServiceCatalogSerializer(service)
        return Response(serializer.data)


class ESSServiceRequestViewSet(viewsets.ModelViewSet):
    """
    ViewSet for ESS service requests
    Following BBP 1.3.9 Service Request Schema
    """
    serializer_class = ESSServiceRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        """Filter by company and employee permissions"""
        company_code = get_current_company_code(self.request)
        user = self.request.user
        
        if user.is_staff or user.groups.filter(name='HR Admin').exists():
            # HR can see all service requests
            return ESSServiceRequest.objects.filter(service__company__company_code=company_code)
        else:
            # Employees can only see their own service requests
            try:
                employee = EmployeeRecord.objects.get(user=user, company_code=company_code)
                return ESSServiceRequest.objects.filter(service__company__company_code=company_code, employee=employee)
            except EmployeeRecord.DoesNotExist:
                return ESSServiceRequest.objects.none()
    
    def get_serializer_class(self):
        """Use list serializer for list view"""
        if self.action == 'list':
            return ESSServiceRequestListSerializer
        return ESSServiceRequestSerializer
    
    def perform_create(self, serializer):
        """Set company code, employee, and request number on create"""
        company_code = get_current_company_code(self.request)
        user = self.request.user
        
        try:
            employee = EmployeeRecord.objects.get(user=user, company_code=company_code)
            
            # Generate unique request number
            request_number = f"SR-{timezone.now().strftime('%Y%m%d')}-{uuid.uuid4().hex[:8].upper()}"
            
            serializer.save(
                employee=employee,
                request_number=request_number
            )
            
            # Log the action
            self._log_audit_action('Create', 'Service Request', serializer.instance.id, {}, serializer.validated_data)
            
        except EmployeeRecord.DoesNotExist:
            raise permissions.PermissionDenied("Employee record not found")
    
    @action(detail=False, methods=['get'])
    def my_requests(self, request):
        """Get current user's service requests"""
        company_code = get_current_company_code(request)
        user = request.user
        
        try:
            employee = EmployeeRecord.objects.get(user=user, company_code=company_code)
            requests = ESSServiceRequest.objects.filter(service__company__company_code=company_code, employee=employee)
            serializer = ESSServiceRequestListSerializer(requests, many=True)
            return Response(serializer.data)
        except EmployeeRecord.DoesNotExist:
            return Response({"error": "Employee record not found"}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['post'])
    def submit(self, request, pk=None):
        """Submit service request"""
        service_request = self.get_object()
        
        if service_request.status != 'Draft':
            return Response({"error": "Only draft requests can be submitted"}, status=status.HTTP_400_BAD_REQUEST)
        
        service_request.status = 'Submitted'
        service_request.submitted_at = timezone.now()
        
        # Set due date based on SLA
        if service_request.service.sla_hours:
            service_request.due_date = timezone.now() + timezone.timedelta(hours=service_request.service.sla_hours)
        
        service_request.save()
        
        # Log the action
        self._log_audit_action('Submit', 'Service Request', service_request.id, {}, {'status': 'Submitted'})
        
        return Response({"message": "Service request submitted successfully"})
    
    @action(detail=True, methods=['post'])
    def rate(self, request, pk=None):
        """Rate completed service request"""
        service_request = self.get_object()
        rating = request.data.get('rating')
        feedback = request.data.get('feedback', '')
        
        if service_request.status != 'Completed':
            return Response({"error": "Only completed requests can be rated"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not rating:
            return Response({"error": "Rating is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        service_request.employee_rating = rating
        service_request.employee_feedback = feedback
        service_request.save()
        
        # Log the action
        self._log_audit_action('Update', 'Service Request', service_request.id, {}, {'rating': rating, 'feedback': feedback})
        
        return Response({"message": "Service request rated successfully"})
    
    def _log_audit_action(self, action, entity_type, entity_id, old_values, new_values):
        """Log audit action"""
        ESSAuditLog.objects.create(
            company_code=get_current_company_code(self.request),
            employee=self.get_employee(),
            action=action,
            entity_type=entity_type,
            entity_id=entity_id,
            old_values=old_values,
            new_values=new_values,
            ip_address=self._get_client_ip(),
            user_agent=self.request.META.get('HTTP_USER_AGENT', ''),
            session_id=self.request.session.session_key
        )
    
    def _get_client_ip(self):
        """Get client IP address"""
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip
    
    def get_employee(self):
        """Get current employee"""
        try:
            company_code = get_current_company_code(self.request)
            return EmployeeRecord.objects.get(user=self.request.user, company_code=company_code)
        except EmployeeRecord.DoesNotExist:
            return None


class ESSDashboardViewSet(viewsets.ViewSet):
    """
    ViewSet for ESS dashboard
    Provides summary statistics and analytics
    """
    permission_classes = [permissions.IsAuthenticated]
    
    @action(detail=False, methods=['get'])
    def summary(self, request):
        """Get ESS dashboard summary"""
        company_code = get_current_company_code(request)
        user = request.user
        
        try:
            employee = EmployeeRecord.objects.get(user=user, company_code=company_code)
            
            # Get statistics
            total_change_requests = EmployeeChangeRequest.objects.filter(
                company_code=company_code, employee=employee
            ).count()
            
            pending_change_requests = EmployeeChangeRequest.objects.filter(
                company_code=company_code, employee=employee, status__in=['Submitted', 'Pending Approval']
            ).count()
            
            total_service_requests = ESSServiceRequest.objects.filter(
                service__company__company_code=company_code, employee=employee
            ).count()
            
            pending_service_requests = ESSServiceRequest.objects.filter(
                service__company__company_code=company_code, employee=employee, status__in=['Submitted', 'In Progress']
            ).count()
            
            # Get recent activities
            recent_activities = ESSAnalytics.objects.filter(
                company_code=company_code, employee=employee
            ).order_by('-action_timestamp')[:10]
            
            # Quick actions based on available services
            quick_actions = [
                {'id': 'personal_info', 'name': 'Update Personal Information', 'icon': 'User'},
                {'id': 'contact_info', 'name': 'Update Contact Information', 'icon': 'Phone'},
                {'id': 'documents', 'name': 'Request Documents', 'icon': 'FileText'},
                {'id': 'leave', 'name': 'Apply for Leave', 'icon': 'Calendar'},
            ]
            
            data = {
                'total_change_requests': total_change_requests,
                'pending_change_requests': pending_change_requests,
                'total_service_requests': total_service_requests,
                'pending_service_requests': pending_service_requests,
                'recent_activities': ESSAnalyticsSerializer(recent_activities, many=True).data,
                'quick_actions': quick_actions
            }
            
            serializer = ESSDashboardSerializer(data)
            return Response(serializer.data)
            
        except EmployeeRecord.DoesNotExist:
            return Response({"error": "Employee record not found"}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=False, methods=['get'])
    def analytics(self, request):
        """Get ESS analytics data"""
        company_code = get_current_company_code(request)
        
        # Get analytics by action type
        analytics_by_action = ESSAnalytics.objects.filter(
            company_code=company_code
        ).values('action_type').annotate(count=Count('id')).order_by('-count')
        
        # Get analytics by service category
        analytics_by_category = ESSAnalytics.objects.filter(
            company_code=company_code
        ).values('service_category').annotate(count=Count('id')).order_by('-count')
        
        # Get device type statistics
        device_stats = ESSAnalytics.objects.filter(
            company_code=company_code
        ).values('device_type').annotate(count=Count('id')).order_by('-count')
        
        return Response({
            'by_action': list(analytics_by_action),
            'by_category': list(analytics_by_category),
            'by_device': list(device_stats)
        })


class ESSAnalyticsViewSet(viewsets.ModelViewSet):
    """
    ViewSet for ESS analytics tracking
    Following BBP 1.3.10 ESS Analytics Schema
    """
    serializer_class = ESSAnalyticsSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        """Filter by company and employee permissions"""
        company_code = get_current_company_code(self.request)
        user = self.request.user
        
        if user.is_staff or user.groups.filter(name='HR Admin').exists():
            # HR can see all analytics
            return ESSAnalytics.objects.filter(company_code=company_code)
        else:
            # Employees can only see their own analytics
            try:
                employee = EmployeeRecord.objects.get(user=user, company_code=company_code)
                return ESSAnalytics.objects.filter(company_code=company_code, employee=employee)
            except EmployeeRecord.DoesNotExist:
                return ESSAnalytics.objects.none()
    
    @action(detail=False, methods=['post'])
    def track(self, request):
        """Track user action"""
        company_code = get_current_company_code(request)
        user = request.user
        
        try:
            employee = EmployeeRecord.objects.get(user=user, company_code=company_code)
            
            action_data = {
                'company_code': company_code,
                'employee': employee,
                'action_type': request.data.get('action_type'),
                'service_category': request.data.get('service_category'),
                'service_id': request.data.get('service_id'),
                'service_request_id': request.data.get('service_request_id'),
                'session_id': request.session.session_key,
                'ip_address': self._get_client_ip(),
                'user_agent': request.META.get('HTTP_USER_AGENT', ''),
                'device_type': request.data.get('device_type'),
                'browser': request.data.get('browser'),
                'processing_time_ms': request.data.get('processing_time_ms'),
                'success_flag': request.data.get('success_flag', True),
                'error_message': request.data.get('error_message')
            }
            
            # Remove None values
            action_data = {k: v for k, v in action_data.items() if v is not None}
            
            analytics = ESSAnalytics.objects.create(**action_data)
            serializer = ESSAnalyticsSerializer(analytics)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        except EmployeeRecord.DoesNotExist:
            return Response({"error": "Employee record not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def _get_client_ip(self):
        """Get client IP address"""
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip
