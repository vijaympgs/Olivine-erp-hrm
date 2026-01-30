"""
Document Management Views - Following BBP 1.4 Document Management specifications
Comprehensive document storage, versioning, verification, and access control APIs
"""
import os
import uuid
import hashlib
from datetime import datetime, timedelta
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.db.models import Q, F, Sum
from django.http import HttpResponse, Http404, JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.pagination import PageNumberPagination

from ..models.document import (
    DocumentTypeMaster, EmployeeDocument, DocumentVersion,
    DocumentVerification, DocumentAccessControl, DocumentAnalytics
)
from ..models.employee import EmployeeRecord
from ..serializers.document import (
    DocumentTypeMasterSerializer, DocumentTypeListSerializer,
    EmployeeDocumentSerializer, EmployeeDocumentListSerializer,
    EmployeeDocumentCreateSerializer, EmployeeDocumentUpdateSerializer,
    DocumentVersionSerializer, DocumentVerificationSerializer,
    DocumentVerificationCreateSerializer, DocumentAccessControlSerializer,
    DocumentAccessControlCreateSerializer, DocumentAnalyticsSerializer,
    DocumentUploadSerializer, DocumentSearchSerializer
)


class StandardResultsSetPagination(PageNumberPagination):
    """Standard pagination for document views"""
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000


class DocumentTypeMasterViewSet(viewsets.ModelViewSet):
    """
    ViewSet for DocumentTypeMaster model
    Following T1 Complex Master Template specifications
    """
    serializer_class = DocumentTypeMasterSerializer
    permission_classes = [permissions.AllowAny]  # Allow access for development
    pagination_class = StandardResultsSetPagination
    
    # Enable filtering, searching, and ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    
    # Define filterable fields
    filterset_fields = [
        'company_code',
        'category',
        'is_required',
        'is_active'
    ]
    
    # Define searchable fields
    search_fields = [
        'type_code',
        'type_name',
        'description'
    ]
    
    # Define orderable fields
    ordering_fields = [
        'type_code',
        'type_name',
        'category',
        'display_order',
        'created_at'
    ]
    
    # Default ordering
    ordering = ['display_order', 'type_name']
    
    def get_queryset(self):
        """Get queryset with company scoping"""
        user = self.request.user
        company_code = getattr(user, 'company_code', 'MINDRA')
        
        return DocumentTypeMaster.objects.filter(
            company_code=company_code
        ).select_related('created_by_user')
    
    def get_serializer_class(self):
        """Return appropriate serializer based on action"""
        if self.action == 'list':
            return DocumentTypeListSerializer
        return DocumentTypeMasterSerializer
    
    @action(detail=False, methods=['get'])
    def active(self, request):
        """Get only active document types"""
        queryset = self.get_queryset().filter(is_active=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def by_category(self, request):
        """Filter document types by category"""
        category = request.query_params.get('category')
        if not category:
            return Response(
                {"error": "Category parameter is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        queryset = self.get_queryset().filter(category=category, is_active=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class EmployeeDocumentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for EmployeeDocument model
    Following T1 Complex Master Template specifications with file handling
    """
    serializer_class = EmployeeDocumentListSerializer
    permission_classes = [permissions.AllowAny]  # Allow access for development
    pagination_class = StandardResultsSetPagination
    parser_classes = [MultiPartParser, FormParser]
    
    # Enable filtering, searching, and ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    
    # Define filterable fields
    filterset_fields = [
        'company_code',
        'employee',
        'document_type',
        'status',
        'is_current',
        'storage_location'
    ]
    
    # Define searchable fields
    search_fields = [
        'document_name',
        'document_description',
        'file_name',
        'tags'
    ]
    
    # Define orderable fields
    ordering_fields = [
        'document_name',
        'upload_date',
        'expiry_date',
        'created_at',
        'updated_at'
    ]
    
    # Default ordering
    ordering = ['-created_at']
    
    def get_queryset(self):
        """Get queryset with company scoping and optimizations"""
        user = self.request.user
        company_code = getattr(user, 'company_code', 'MINDRA')
        
        queryset = EmployeeDocument.objects.filter(
            company_code=company_code
        ).select_related(
            'employee',
            'document_type',
            'uploaded_by_user',
            'verified_by_user'
        ).prefetch_related(
            'versions',
            'verifications',
            'access_controls'
        )
        
        # Filter by employee if provided
        employee_id = self.request.query_params.get('employee_id')
        if employee_id:
            queryset = queryset.filter(employee_id=employee_id)
        
        return queryset
    
    def get_serializer_class(self):
        """Return appropriate serializer based on action"""
        if self.action == 'create':
            return EmployeeDocumentCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return EmployeeDocumentUpdateSerializer
        elif self.action == 'retrieve':
            return EmployeeDocumentSerializer
        elif self.action == 'list':
            return EmployeeDocumentListSerializer
        
        return EmployeeDocumentSerializer
    
    def perform_create(self, serializer):
        """Handle document creation with file processing"""
        user = self.request.user
        company_code = getattr(user, 'company_code', 'MINDRA')
        
        serializer.save(
            company_code=company_code,
            uploaded_by_user=user if user.is_authenticated else None
        )
    
    @action(detail=False, methods=['post'])
    def upload(self, request):
        """
        Upload a new document
        Following BBP specifications for file upload with validation
        """
        upload_serializer = DocumentUploadSerializer(data=request.data)
        if not upload_serializer.is_valid():
            return Response(upload_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Get validated data
            file = upload_serializer.validated_data['file']
            document_type_id = upload_serializer.validated_data['document_type']
            document_name = upload_serializer.validated_data['document_name']
            document_description = upload_serializer.validated_data.get('document_description', '')
            expiry_date = upload_serializer.validated_data.get('expiry_date')
            tags = upload_serializer.validated_data.get('tags', [])
            metadata = upload_serializer.validated_data.get('metadata', {})
            
            # Get employee ID from request
            employee_id = request.data.get('employee_id')
            if not employee_id:
                return Response(
                    {"error": "employee_id is required"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Validate employee exists and belongs to company
            user = request.user
            company_code = getattr(user, 'company_code', 'MINDRA')
            try:
                employee = EmployeeRecord.objects.get(
                    id=employee_id,
                    company_code=company_code
                )
            except EmployeeRecord.DoesNotExist:
                return Response(
                    {"error": "Employee not found"},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # Validate document type
            try:
                document_type = DocumentTypeMaster.objects.get(
                    id=document_type_id,
                    company_code=company_code,
                    is_active=True
                )
            except DocumentTypeMaster.DoesNotExist:
                return Response(
                    {"error": "Document type not found or inactive"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Validate file size against document type limits
            if file.size > document_type.max_file_size_mb * 1024 * 1024:
                return Response(
                    {"error": f"File size exceeds maximum limit of {document_type.max_file_size_mb}MB"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Validate file type
            file_extension = os.path.splitext(file.name)[1].lower()
            if document_type.allowed_file_types and file_extension not in document_type.allowed_file_types:
                return Response(
                    {"error": f"File type {file_extension} not allowed. Allowed types: {document_type.allowed_file_types}"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Generate unique file path
            file_extension = os.path.splitext(file.name)[1]
            unique_filename = f"{uuid.uuid4()}{file_extension}"
            file_path = f"documents/{company_code}/{employee_id}/{unique_filename}"
            
            # Save file to storage
            file_path = default_storage.save(file_path, file)
            
            # Calculate file hash
            file_hash = hashlib.sha256()
            for chunk in file.chunks():
                file_hash.update(chunk)
            file_hash = file_hash.hexdigest()
            
            # Create document record
            document = EmployeeDocument.objects.create(
                company_code=company_code,
                employee=employee,
                document_type=document_type,
                document_name=document_name,
                document_description=document_description,
                file_name=file.name,
                file_path=file_path,
                file_size=file.size,
                file_type=file_extension,
                mime_type=file.content_type or 'application/octet-stream',
                file_hash=file_hash,
                expiry_date=expiry_date,
                tags=tags,
                metadata=metadata,
                uploaded_by_user=user if user.is_authenticated else None
            )
            
            # Log analytics
            self._log_analytics(
                employee=employee,
                document=document,
                action='Upload',
                user=user,
                file_size=file.size,
                success_flag=True
            )
            
            # Return full document details
            serializer = EmployeeDocumentSerializer(document)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response(
                {"error": f"Upload failed: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        """
        Download document file
        Following BBP specifications for secure file access
        """
        document = self.get_object()
        
        # Check access permissions (simplified for development)
        # In production, implement proper access control checking
        
        try:
            if default_storage.exists(document.file_path):
                # Open file for reading
                file = default_storage.open(document.file_path, 'rb')
                response = HttpResponse(file, content_type=document.mime_type)
                response['Content-Disposition'] = f'attachment; filename="{document.file_name}"'
                response['Content-Length'] = document.file_size
                
                # Log analytics
                self._log_analytics(
                    employee=document.employee,
                    document=document,
                    action='Download',
                    user=request.user,
                    file_size=document.file_size,
                    success_flag=True
                )
                
                return response
            else:
                return Response(
                    {"error": "File not found"},
                    status=status.HTTP_404_NOT_FOUND
                )
        except Exception as e:
            return Response(
                {"error": f"Download failed: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=True, methods=['get'])
    def preview(self, request, pk=None):
        """
        Preview document (for supported file types)
        Following BBP specifications for document viewing
        """
        document = self.get_object()
        
        # Check if file type supports preview
        previewable_types = ['.pdf', '.jpg', '.jpeg', '.png', '.gif', '.txt']
        file_extension = os.path.splitext(document.file_name)[1].lower()
        
        if file_extension not in previewable_types:
            return Response(
                {"error": f"Preview not supported for {file_extension} files"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            if default_storage.exists(document.file_path):
                # Open file for reading
                file = default_storage.open(document.file_path, 'rb')
                response = HttpResponse(file, content_type=document.mime_type)
                response['Content-Disposition'] = f'inline; filename="{document.file_name}"'
                response['Content-Length'] = document.file_size
                
                # Log analytics
                self._log_analytics(
                    employee=document.employee,
                    document=document,
                    action='View',
                    user=request.user,
                    file_size=document.file_size,
                    success_flag=True
                )
                
                return response
            else:
                return Response(
                    {"error": "File not found"},
                    status=status.HTTP_404_NOT_FOUND
                )
        except Exception as e:
            return Response(
                {"error": f"Preview failed: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=True, methods=['post'])
    def verify(self, request, pk=None):
        """
        Verify document
        Following BBP specifications for document verification
        """
        document = self.get_object()
        
        verification_serializer = DocumentVerificationCreateSerializer(
            data=request.data,
            context={'document_id': document.id, 'request': request}
        )
        
        if not verification_serializer.is_valid():
            return Response(verification_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            verification = verification_serializer.save()
            
            # Update document verification status
            if verification.verification_status == 'Verified':
                document.status = 'Verified'
                document.verification_date = datetime.now().date()
                document.verified_by_user = request.user if request.user.is_authenticated else None
                document.verification_notes = verification.verification_notes
                document.save(update_fields=['status', 'verification_date', 'verified_by_user', 'verification_notes'])
            
            # Log analytics
            self._log_analytics(
                employee=document.employee,
                document=document,
                action='Verify',
                user=request.user,
                success_flag=True
            )
            
            serializer = DocumentVerificationSerializer(verification)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response(
                {"error": f"Verification failed: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=True, methods=['get', 'post'])
    def access_control(self, request, pk=None):
        """
        Manage document access control
        Following BBP specifications for access management
        """
        document = self.get_object()
        
        if request.method == 'GET':
            # List access controls
            access_controls = document.access_controls.filter(is_active=True)
            serializer = DocumentAccessControlSerializer(access_controls, many=True)
            return Response(serializer.data)
        
        elif request.method == 'POST':
            # Create new access control
            access_serializer = DocumentAccessControlCreateSerializer(
                data=request.data,
                context={'document_id': document.id, 'request': request}
            )
            
            if not access_serializer.is_valid():
                return Response(access_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            try:
                access_control = access_serializer.save()
                serializer = DocumentAccessControlSerializer(access_control)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
                
            except Exception as e:
                return Response(
                    {"error": f"Access control creation failed: {str(e)}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
    
    @action(detail=True, methods=['get'])
    def versions(self, request, pk=None):
        """
        Get document versions
        Following BBP specifications for version control
        """
        document = self.get_object()
        versions = document.versions.all().order_by('-version_number')
        serializer = DocumentVersionSerializer(versions, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def analytics(self, request, pk=None):
        """
        Get document analytics
        Following BBP specifications for analytics tracking
        """
        document = self.get_object()
        analytics = document.analytics.all().order_by('-action_timestamp')
        serializer = DocumentAnalyticsSerializer(analytics, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def search(self, request):
        """
        Advanced document search
        Following BBP specifications for complex filtering
        """
        search_serializer = DocumentSearchSerializer(data=request.data)
        if not search_serializer.is_valid():
            return Response(search_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = self.get_queryset()
        
        # Apply filters
        document_type = search_serializer.validated_data.get('document_type')
        if document_type:
            queryset = queryset.filter(document_type_id=document_type)
        
        status_filter = search_serializer.validated_data.get('status')
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        
        category = search_serializer.validated_data.get('category')
        if category:
            queryset = queryset.filter(document_type__category=category)
        
        date_from = search_serializer.validated_data.get('date_from')
        if date_from:
            queryset = queryset.filter(upload_date__gte=date_from)
        
        date_to = search_serializer.validated_data.get('date_to')
        if date_to:
            queryset = queryset.filter(upload_date__lte=date_to)
        
        search_term = search_serializer.validated_data.get('search')
        if search_term:
            queryset = queryset.filter(
                Q(document_name__icontains=search_term) |
                Q(document_description__icontains=search_term) |
                Q(file_name__icontains=search_term) |
                Q(tags__icontains=search_term)
            )
        
        tags = search_serializer.validated_data.get('tags')
        if tags:
            queryset = queryset.filter(tags__overlap=tags)
        
        expiry_soon = search_serializer.validated_data.get('expiry_soon')
        if expiry_soon:
            # Documents expiring in next 30 days
            expiry_date = datetime.now().date() + timedelta(days=30)
            queryset = queryset.filter(expiry_date__lte=expiry_date, expiry_date__gte=datetime.now().date())
        
        requires_verification = search_serializer.validated_data.get('requires_verification')
        if requires_verification:
            queryset = queryset.filter(status='Uploaded', document_type__requires_verification=True)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def statistics(self, request):
        """
        Get document statistics
        Following BBP specifications for analytics
        """
        queryset = self.get_queryset()
        
        stats = {
            'total_documents': queryset.count(),
            'by_status': {},
            'by_type': {},
            'by_category': {},
            'by_storage_location': {},
            'total_file_size': queryset.aggregate(total=Sum('file_size'))['total'] or 0,
            'documents_expiring_soon': 0,
            'documents_requiring_verification': 0
        }
        
        # Status statistics
        for status in queryset.values_list('status', flat=True).distinct():
            stats['by_status'][status] = queryset.filter(status=status).count()
        
        # Type statistics
        for doc_type in queryset.values_list('document_type__type_name', flat=True).distinct():
            stats['by_type'][doc_type] = queryset.filter(document_type__type_name=doc_type).count()
        
        # Category statistics
        for category in queryset.values_list('document_type__category', flat=True).distinct():
            stats['by_category'][category] = queryset.filter(document_type__category=category).count()
        
        # Storage location statistics
        for location in queryset.values_list('storage_location', flat=True).distinct():
            stats['by_storage_location'][location] = queryset.filter(storage_location=location).count()
        
        # Documents expiring soon (next 30 days)
        expiry_date = datetime.now().date() + timedelta(days=30)
        stats['documents_expiring_soon'] = queryset.filter(
            expiry_date__lte=expiry_date,
            expiry_date__gte=datetime.now().date()
        ).count()
        
        # Documents requiring verification
        stats['documents_requiring_verification'] = queryset.filter(
            status='Uploaded',
            document_type__requires_verification=True
        ).count()
        
        return Response(stats)
    
    def _log_analytics(self, employee, document, action, user, file_size=None, success_flag=True, error_message=None):
        """
        Log document analytics
        Following BBP specifications for analytics tracking
        """
        try:
            # Get request context
            request = self.request if hasattr(self, 'request') else None
            
            DocumentAnalytics.objects.create(
                company_code=document.company_code,
                document=document,
                employee=employee,
                action=action,
                user=user if user and user.is_authenticated else None,
                session_id=getattr(request, 'session', {}).get('session_key', ''),
                ip_address=self._get_client_ip(request) if request else None,
                user_agent=request.META.get('HTTP_USER_AGENT', '') if request else '',
                device_type=self._get_device_type(request) if request else 'Desktop',
                browser=self._get_browser(request) if request else None,
                file_size=file_size,
                success_flag=success_flag,
                error_message=error_message
            )
        except Exception as e:
            # Log error but don't fail the main operation
            print(f"Analytics logging failed: {str(e)}")
    
    def _get_client_ip(self, request):
        """Get client IP address"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
    def _get_device_type(self, request):
        """Get device type from user agent"""
        user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
        if 'mobile' in user_agent or 'android' in user_agent:
            return 'Mobile'
        elif 'tablet' in user_agent or 'ipad' in user_agent:
            return 'Tablet'
        return 'Desktop'
    
    def _get_browser(self, request):
        """Get browser from user agent"""
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        if 'Chrome' in user_agent:
            return 'Chrome'
        elif 'Firefox' in user_agent:
            return 'Firefox'
        elif 'Safari' in user_agent:
            return 'Safari'
        elif 'Edge' in user_agent:
            return 'Edge'
        return None
