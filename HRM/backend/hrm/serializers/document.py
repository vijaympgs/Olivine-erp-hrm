"""
Document Management Serializers - Following BBP 1.4 Document Management specifications
Handles serialization of all document-related models
"""
from rest_framework import serializers
from django.contrib.auth.models import User
from ..models.document import (
    DocumentTypeMaster, EmployeeDocument, DocumentVersion, 
    DocumentVerification, DocumentAccessControl, DocumentAnalytics
)
from ..models.employee import EmployeeRecord


class DocumentTypeMasterSerializer(serializers.ModelSerializer):
    """Serializer for DocumentTypeMaster model"""
    
    class Meta:
        model = DocumentTypeMaster
        fields = [
            'id', 'company_code', 'type_code', 'type_name', 'category', 'description',
            'is_required', 'is_mandatory_for_onboarding', 'is_mandatory_for_exit',
            'requires_verification', 'expiry_required', 'expiry_days', 'max_file_size_mb',
            'allowed_file_types', 'access_level', 'retention_years', 'auto_archive',
            'is_active', 'display_order', 'created_by_user', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'company_code', 'created_by_user', 'created_at', 'updated_at']


class DocumentTypeListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for document type lists"""
    
    class Meta:
        model = DocumentTypeMaster
        fields = ['id', 'type_code', 'type_name', 'category', 'is_required', 'is_active']


class EmployeeDocumentSerializer(serializers.ModelSerializer):
    """Full serializer for EmployeeDocument model"""
    document_type_name = serializers.CharField(source='document_type.type_name', read_only=True)
    document_type_category = serializers.CharField(source='document_type.category', read_only=True)
    employee_name = serializers.CharField(source='employee.full_name', read_only=True)
    employee_number = serializers.CharField(source='employee.employee_number', read_only=True)
    uploaded_by_username = serializers.CharField(source='uploaded_by_user.username', read_only=True)
    verified_by_username = serializers.CharField(source='verified_by_user.username', read_only=True)
    file_url = serializers.SerializerMethodField()
    file_size_display = serializers.SerializerMethodField()
    
    class Meta:
        model = EmployeeDocument
        fields = [
            'id', 'company_code', 'employee', 'document_type', 'document_type_name', 
            'document_type_category', 'document_name', 'document_description', 'file_name',
            'file_path', 'file_size', 'file_size_display', 'file_type', 'mime_type',
            'file_hash', 'version', 'is_current', 'status', 'upload_date', 'expiry_date',
            'verification_date', 'verified_by_user', 'verified_by_username', 'verification_notes',
            'is_public', 'is_encrypted', 'storage_location', 'backup_location', 'tags',
            'metadata', 'uploaded_by_user', 'uploaded_by_username', 'employee_name',
            'employee_number', 'file_url', 'created_at', 'updated_at'
        ]
        read_only_fields = [
            'id', 'company_code', 'file_hash', 'version', 'upload_date', 'verification_date',
            'uploaded_by_user', 'created_at', 'updated_at'
        ]
    
    def get_file_url(self, obj):
        """Get the file URL for download"""
        return obj.get_file_url()
    
    def get_file_size_display(self, obj):
        """Get human-readable file size"""
        if not obj.file_size:
            return '0 bytes'
        
        for unit in ['bytes', 'KB', 'MB', 'GB']:
            if obj.file_size < 1024.0:
                return f"{obj.file_size:.1f} {unit}"
            obj.file_size /= 1024.0
        return f"{obj.file_size:.1f} TB"


class EmployeeDocumentListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for document lists"""
    document_type_name = serializers.CharField(source='document_type.type_name', read_only=True)
    document_type_category = serializers.CharField(source='document_type.category', read_only=True)
    employee_name = serializers.CharField(source='employee.full_name', read_only=True)
    file_size_display = serializers.SerializerMethodField()
    
    class Meta:
        model = EmployeeDocument
        fields = [
            'id', 'document_type', 'document_type_name', 'document_type_category',
            'document_name', 'file_name', 'file_size_display', 'file_type', 'status',
            'upload_date', 'expiry_date', 'is_current', 'version', 'employee_name'
        ]
    
    def get_file_size_display(self, obj):
        """Get human-readable file size"""
        if not obj.file_size:
            return '0 bytes'
        
        size = obj.file_size
        for unit in ['bytes', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.1f} {unit}"
            size /= 1024.0
        return f"{size:.1f} TB"


class EmployeeDocumentCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating new documents"""
    
    class Meta:
        model = EmployeeDocument
        fields = [
            'employee', 'document_type', 'document_name', 'document_description',
            'file_name', 'file_path', 'file_size', 'file_type', 'mime_type',
            'expiry_date', 'is_public', 'is_encrypted', 'storage_location',
            'backup_location', 'tags', 'metadata'
        ]
    
    def create(self, validated_data):
        """Create document with automatic hash calculation"""
        user = self.context['request'].user
        company_code = getattr(user, 'company_code', 'MINDRA')
        
        document = EmployeeDocument.objects.create(
            company_code=company_code,
            uploaded_by_user=user if user.is_authenticated else None,
            **validated_data
        )
        
        # Calculate file hash
        document.calculate_file_hash()
        
        return document


class EmployeeDocumentUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating documents"""
    
    class Meta:
        model = EmployeeDocument
        fields = [
            'document_name', 'document_description', 'expiry_date', 'status',
            'verification_notes', 'is_public', 'is_encrypted', 'storage_location',
            'backup_location', 'tags', 'metadata'
        ]


class DocumentVersionSerializer(serializers.ModelSerializer):
    """Serializer for DocumentVersion model"""
    document_name = serializers.CharField(source='document.document_name', read_only=True)
    uploaded_by_username = serializers.CharField(source='uploaded_by_user.username', read_only=True)
    approved_by_username = serializers.CharField(source='approved_by_user.username', read_only=True)
    file_size_display = serializers.SerializerMethodField()
    
    class Meta:
        model = DocumentVersion
        fields = [
            'id', 'document', 'document_name', 'version_number', 'file_name',
            'file_path', 'file_size', 'file_size_display', 'file_type', 'file_hash',
            'change_summary', 'change_reason', 'status', 'effective_date',
            'uploaded_by_user', 'uploaded_by_username', 'approved_by_user',
            'approved_by_username', 'approved_at', 'created_at'
        ]
        read_only_fields = [
            'id', 'document', 'version_number', 'file_hash', 'uploaded_by_user',
            'approved_by_user', 'approved_at', 'created_at'
        ]
    
    def get_file_size_display(self, obj):
        """Get human-readable file size"""
        if not obj.file_size:
            return '0 bytes'
        
        size = obj.file_size
        for unit in ['bytes', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.1f} {unit}"
            size /= 1024.0
        return f"{size:.1f} TB"


class DocumentVerificationSerializer(serializers.ModelSerializer):
    """Serializer for DocumentVerification model"""
    document_name = serializers.CharField(source='document.document_name', read_only=True)
    verifier_username = serializers.CharField(source='verifier.username', read_only=True)
    
    class Meta:
        model = DocumentVerification
        fields = [
            'id', 'document', 'document_name', 'verification_type', 'verifier',
            'verifier_username', 'verification_status', 'verification_method',
            'verification_result', 'verification_notes', 'verification_score',
            'verification_date', 'expiry_date', 'next_verification_date',
            'supporting_documents', 'verification_checklist', 'automated_checks',
            'third_party_reference', 'created_at', 'updated_at'
        ]
        read_only_fields = [
            'id', 'document', 'verification_date', 'created_at', 'updated_at'
        ]


class DocumentVerificationCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating document verifications"""
    
    class Meta:
        model = DocumentVerification
        fields = [
            'verification_type', 'verification_method', 'verification_result',
            'verification_notes', 'verification_score', 'expiry_date',
            'next_verification_date', 'supporting_documents',
            'verification_checklist', 'automated_checks', 'third_party_reference'
        ]
    
    def create(self, validated_data):
        """Create verification with user and document"""
        user = self.context['request'].user
        document_id = self.context['document_id']
        
        return DocumentVerification.objects.create(
            document_id=document_id,
            verifier=user if user.is_authenticated else None,
            **validated_data
        )


class DocumentAccessControlSerializer(serializers.ModelSerializer):
    """Serializer for DocumentAccessControl model"""
    document_name = serializers.CharField(source='document.document_name', read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)
    granted_by_username = serializers.CharField(source='granted_by_user.username', read_only=True)
    
    class Meta:
        model = DocumentAccessControl
        fields = [
            'id', 'document', 'document_name', 'user', 'user_username',
            'access_type', 'permission_level', 'granted_by_user',
            'granted_by_username', 'granted_at', 'expires_at', 'access_reason',
            'ip_restriction', 'time_restriction', 'download_limit',
            'download_count', 'is_active', 'last_accessed_at', 'access_count',
            'created_at', 'updated_at'
        ]
        read_only_fields = [
            'id', 'document', 'granted_by_user', 'granted_at', 'download_count',
            'last_accessed_at', 'access_count', 'created_at', 'updated_at'
        ]


class DocumentAccessControlCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating document access controls"""
    
    class Meta:
        model = DocumentAccessControl
        fields = [
            'user', 'access_type', 'permission_level', 'expires_at',
            'access_reason', 'ip_restriction', 'time_restriction', 'download_limit'
        ]
    
    def create(self, validated_data):
        """Create access control with user and document"""
        user = self.context['request'].user
        document_id = self.context['document_id']
        
        return DocumentAccessControl.objects.create(
            document_id=document_id,
            granted_by_user=user if user.is_authenticated else None,
            **validated_data
        )


class DocumentAnalyticsSerializer(serializers.ModelSerializer):
    """Serializer for DocumentAnalytics model"""
    document_name = serializers.CharField(source='document.document_name', read_only=True)
    employee_name = serializers.CharField(source='employee.full_name', read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = DocumentAnalytics
        fields = [
            'id', 'company_code', 'document', 'document_name', 'employee',
            'employee_name', 'action', 'user', 'user_username', 'session_id',
            'ip_address', 'user_agent', 'device_type', 'browser',
            'action_timestamp', 'processing_time_ms', 'file_size',
            'success_flag', 'error_message', 'additional_context'
        ]
        read_only_fields = [
            'id', 'company_code', 'document', 'employee', 'action_timestamp'
        ]


class DocumentUploadSerializer(serializers.Serializer):
    """Serializer for document upload operations"""
    file = serializers.FileField()
    document_type = serializers.UUIDField()
    document_name = serializers.CharField(max_length=200)
    document_description = serializers.CharField(required=False, allow_blank=True)
    expiry_date = serializers.DateField(required=False, allow_null=True)
    tags = serializers.ListField(child=serializers.CharField(), required=False)
    metadata = serializers.JSONField(required=False)
    
    def validate_file(self, value):
        """Validate uploaded file"""
        # Check file size (default 10MB limit)
        max_size = 10 * 1024 * 1024  # 10MB
        if value.size > max_size:
            raise serializers.ValidationError(f"File size exceeds maximum limit of {max_size // (1024*1024)}MB")
        
        return value


class DocumentSearchSerializer(serializers.Serializer):
    """Serializer for document search parameters"""
    document_type = serializers.UUIDField(required=False)
    status = serializers.CharField(required=False)
    category = serializers.CharField(required=False)
    date_from = serializers.DateField(required=False)
    date_to = serializers.DateField(required=False)
    search = serializers.CharField(required=False)
    tags = serializers.ListField(child=serializers.CharField(), required=False)
    expiry_soon = serializers.BooleanField(required=False)
    requires_verification = serializers.BooleanField(required=False)
