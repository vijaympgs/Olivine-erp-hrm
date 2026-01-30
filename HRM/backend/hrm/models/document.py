"""
Document Management Models - Following BBP 1.4 Document Management specifications
Comprehensive document storage, versioning, verification, and access control
"""
import uuid
import hashlib
import os
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from ..tenancy import DEFAULT_COMPANY_CODE


class DocumentTypeMaster(models.Model):
    """
    Master table for document types with company-specific configurations
    Following BBP 1.4.4 Document Type Master Schema
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_code = models.CharField(max_length=10, db_index=True, default=DEFAULT_COMPANY_CODE)
    type_code = models.CharField(max_length=50, db_index=True)
    type_name = models.CharField(max_length=200)
    category = models.CharField(
        max_length=20,
        choices=[
            ('Personal', 'Personal'),
            ('Employment', 'Employment'),
            ('Education', 'Education'),
            ('Professional', 'Professional'),
            ('Legal', 'Legal'),
            ('Medical', 'Medical'),
            ('Financial', 'Financial'),
            ('Training', 'Training'),
            ('Performance', 'Performance'),
            ('Compliance', 'Compliance')
        ]
    )
    description = models.TextField(null=True, blank=True)
    is_required = models.BooleanField(default=False)
    is_mandatory_for_onboarding = models.BooleanField(default=False)
    is_mandatory_for_exit = models.BooleanField(default=False)
    requires_verification = models.BooleanField(default=True)
    expiry_required = models.BooleanField(default=False)
    expiry_days = models.IntegerField(default=365)
    max_file_size_mb = models.IntegerField(default=10)
    allowed_file_types = models.JSONField(default=list, help_text="Array of allowed file extensions")
    access_level = models.CharField(
        max_length=20,
        choices=[
            ('Public', 'Public'),
            ('HR Only', 'HR Only'),
            ('Manager', 'Manager'),
            ('Employee', 'Employee'),
            ('Restricted', 'Restricted')
        ],
        default='HR Only'
    )
    retention_years = models.IntegerField(default=7)
    auto_archive = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)
    created_by_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='doctype_created_by_user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'document_type_master'
        verbose_name = 'Document Type Master'
        verbose_name_plural = 'Document Type Masters'
        unique_together = ['company_code', 'type_code']
        indexes = [
            models.Index(fields=['company_code', 'type_code'], name='idx_doctype_company_code'),
            models.Index(fields=['category'], name='idx_doctype_category'),
            models.Index(fields=['is_required'], name='idx_doctype_required'),
            models.Index(fields=['is_active'], name='idx_doctype_active'),
            models.Index(fields=['display_order'], name='idx_doctype_display_order'),
        ]

    def __str__(self):
        return f'{self.type_name} ({self.type_code})'


class EmployeeDocument(models.Model):
    """
    Main document storage model for employee documents
    Following BBP 1.4.3 Employee Document Schema
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_code = models.CharField(max_length=10, db_index=True, default=DEFAULT_COMPANY_CODE)
    employee = models.ForeignKey('hrm.EmployeeRecord', on_delete=models.CASCADE, related_name='documents')
    document_type = models.ForeignKey(DocumentTypeMaster, on_delete=models.PROTECT, related_name='documents')
    document_name = models.CharField(max_length=200)
    document_description = models.TextField(null=True, blank=True)
    file_name = models.CharField(max_length=500, null=True, blank=True)
    file_path = models.CharField(max_length=1000, null=True, blank=True)
    file_size = models.BigIntegerField()
    file_type = models.CharField(max_length=100)
    mime_type = models.CharField(max_length=200, null=True, blank=True)
    file_hash = models.CharField(max_length=256, help_text="SHA-256 hash", null=True, blank=True)
    version = models.IntegerField(default=1)
    is_current = models.BooleanField(default=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('Draft', 'Draft'),
            ('Uploaded', 'Uploaded'),
            ('Verified', 'Verified'),
            ('Rejected', 'Rejected'),
            ('Expired', 'Expired'),
            ('Archived', 'Archived')
        ],
        default='Uploaded'
    )
    upload_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField(null=True, blank=True)
    verification_date = models.DateField(null=True, blank=True)
    verified_by_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='verified_documents')
    verification_notes = models.TextField(null=True, blank=True)
    is_public = models.BooleanField(default=False)
    is_encrypted = models.BooleanField(default=False)
    storage_location = models.CharField(
        max_length=20,
        choices=[
            ('Local', 'Local'),
            ('Cloud', 'Cloud'),
            ('Hybrid', 'Hybrid')
        ],
        default='Local'
    )
    backup_location = models.CharField(max_length=500, null=True, blank=True)
    tags = models.JSONField(default=list, help_text="Array of tags")
    metadata = models.JSONField(default=dict, help_text="Document metadata")
    uploaded_by_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='uploaded_documents')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'employee_document'
        verbose_name = 'Employee Document'
        verbose_name_plural = 'Employee Documents'
        indexes = [
            models.Index(fields=['employee', 'document_type'], name='idx_doc_employee_type'),
            models.Index(fields=['document_name'], name='idx_doc_name'),
            models.Index(fields=['status'], name='idx_doc_status'),
            models.Index(fields=['upload_date'], name='idx_doc_upload_date'),
            models.Index(fields=['expiry_date'], name='idx_doc_expiry_date'),
            models.Index(fields=['is_current'], name='idx_doc_current'),
            models.Index(fields=['file_hash'], name='idx_doc_hash'),
            models.Index(fields=['uploaded_by_user'], name='idx_doc_uploader'),
        ]

    def __str__(self):
        return f'{self.document_name} - {self.employee.first_name} {self.employee.last_name}'

    def calculate_file_hash(self):
        """Calculate SHA-256 hash of the uploaded file"""
        if self.file_path and default_storage.exists(self.file_path):
            with default_storage.open(self.file_path, 'rb') as f:
                hash_sha256 = hashlib.sha256()
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_sha256.update(chunk)
                self.file_hash = hash_sha256.hexdigest()
                self.save(update_fields=['file_hash'])

    def get_file_url(self):
        """Get the URL for downloading the file"""
        if self.file_path:
            return default_storage.url(self.file_path)
        return None


class DocumentVersion(models.Model):
    """
    Version control for documents
    Following BBP 1.4.5 Document Version Schema
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    document = models.ForeignKey(EmployeeDocument, on_delete=models.CASCADE, related_name='versions')
    version_number = models.IntegerField()
    file_name = models.CharField(max_length=500)
    file_path = models.CharField(max_length=1000)
    file_size = models.BigIntegerField()
    file_type = models.CharField(max_length=100)
    file_hash = models.CharField(max_length=256, help_text="SHA-256 hash")
    change_summary = models.TextField(null=True, blank=True)
    change_reason = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('Draft', 'Draft'),
            ('Active', 'Active'),
            ('Superseded', 'Superseded'),
            ('Archived', 'Archived')
        ],
        default='Active'
    )
    effective_date = models.DateField(null=True, blank=True)
    uploaded_by_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='doc_versions_uploaded')
    approved_by_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='doc_versions_approved')
    approved_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'document_version'
        verbose_name = 'Document Version'
        verbose_name_plural = 'Document Versions'
        unique_together = ['document', 'version_number']
        indexes = [
            models.Index(fields=['document', 'version_number'], name='idx_version_doc_number'),
            models.Index(fields=['status'], name='idx_version_status'),
            models.Index(fields=['effective_date'], name='idx_version_effective'),
            models.Index(fields=['uploaded_by_user'], name='idx_version_uploader'),
            models.Index(fields=['approved_by_user'], name='idx_version_approver'),
        ]

    def __str__(self):
        return f'Version {self.version_number} of {self.document.document_name}'


class DocumentVerification(models.Model):
    """
    Document verification tracking
    Following BBP 1.4.6 Document Verification Schema
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    document = models.ForeignKey(EmployeeDocument, on_delete=models.CASCADE, related_name='verifications')
    verification_type = models.CharField(
        max_length=20,
        choices=[
            ('Manual', 'Manual'),
            ('Automated', 'Automated'),
            ('Third Party', 'Third Party'),
            ('E-Signature', 'E-Signature')
        ],
        default='Manual'
    )
    verifier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='document_verifications')
    verification_status = models.CharField(
        max_length=30,
        choices=[
            ('Pending', 'Pending'),
            ('In Progress', 'In Progress'),
            ('Verified', 'Verified'),
            ('Rejected', 'Rejected'),
            ('Requires Additional Info', 'Requires Additional Info')
        ],
        default='Pending'
    )
    verification_method = models.CharField(max_length=100, null=True, blank=True)
    verification_result = models.TextField(null=True, blank=True)
    verification_notes = models.TextField(null=True, blank=True)
    verification_score = models.IntegerField(null=True, blank=True, help_text="0-100")
    verification_date = models.DateTimeField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    next_verification_date = models.DateField(null=True, blank=True)
    supporting_documents = models.JSONField(default=list, help_text="Array of supporting document IDs")
    verification_checklist = models.JSONField(default=dict, help_text="Checklist items and results")
    automated_checks = models.JSONField(default=dict, help_text="Automated validation results")
    third_party_reference = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'document_verification'
        verbose_name = 'Document Verification'
        verbose_name_plural = 'Document Verifications'
        indexes = [
            models.Index(fields=['document', 'verification_type'], name='idx_verify_doc_type'),
            models.Index(fields=['verifier'], name='idx_verify_verifier'),
            models.Index(fields=['verification_status'], name='idx_verify_status'),
            models.Index(fields=['verification_date'], name='idx_verify_date'),
            models.Index(fields=['expiry_date'], name='idx_verify_expiry'),
        ]

    def __str__(self):
        return f'{self.verification_status} - {self.document.document_name}'


class DocumentAccessControl(models.Model):
    """
    Access control for documents
    Following BBP 1.4.9 Document Access Control Schema
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    document = models.ForeignKey(EmployeeDocument, on_delete=models.CASCADE, related_name='access_controls')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='document_access')
    access_type = models.CharField(
        max_length=20,
        choices=[
            ('View', 'View'),
            ('Download', 'Download'),
            ('Print', 'Print'),
            ('Share', 'Share'),
            ('Edit', 'Edit'),
            ('Delete', 'Delete')
        ],
        default='View'
    )
    permission_level = models.CharField(
        max_length=20,
        choices=[
            ('Owner', 'Owner'),
            ('Full Access', 'Full Access'),
            ('Read Only', 'Read Only'),
            ('Restricted', 'Restricted')
        ],
        default='Read Only'
    )
    granted_by_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='granted_document_access')
    granted_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    access_reason = models.CharField(max_length=500, null=True, blank=True)
    ip_restriction = models.CharField(max_length=45, null=True, blank=True)
    time_restriction = models.JSONField(default=dict, help_text="Allowed time windows")
    download_limit = models.IntegerField(null=True, blank=True)
    download_count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    last_accessed_at = models.DateTimeField(null=True, blank=True)
    access_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'document_access_control'
        verbose_name = 'Document Access Control'
        verbose_name_plural = 'Document Access Controls'
        unique_together = ['document', 'user', 'access_type']
        indexes = [
            models.Index(fields=['document', 'user'], name='idx_access_doc_user'),
            models.Index(fields=['access_type'], name='idx_access_type'),
            models.Index(fields=['permission_level'], name='idx_access_permission'),
            models.Index(fields=['granted_by_user'], name='idx_access_granter'),
            models.Index(fields=['expires_at'], name='idx_access_expires'),
            models.Index(fields=['is_active'], name='idx_access_active'),
        ]

    def __str__(self):
        return f'{self.permission_level} access for {self.user.username} on {self.document.document_name}'


class DocumentAnalytics(models.Model):
    """
    Analytics tracking for document operations
    Following BBP 1.4.10 Document Analytics Schema
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_code = models.CharField(max_length=10, db_index=True, default=DEFAULT_COMPANY_CODE)
    document = models.ForeignKey(EmployeeDocument, on_delete=models.CASCADE, related_name='analytics')
    employee = models.ForeignKey('hrm.EmployeeRecord', on_delete=models.CASCADE, related_name='document_analytics')
    action = models.CharField(
        max_length=20,
        choices=[
            ('Upload', 'Upload'),
            ('View', 'View'),
            ('Download', 'Download'),
            ('Print', 'Print'),
            ('Share', 'Share'),
            ('Delete', 'Delete'),
            ('Verify', 'Verify'),
            ('Archive', 'Archive')
        ]
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='document_actions')
    session_id = models.CharField(max_length=100, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
    device_type = models.CharField(
        max_length=20,
        choices=[
            ('Desktop', 'Desktop'),
            ('Mobile', 'Mobile'),
            ('Tablet', 'Tablet')
        ]
    )
    browser = models.CharField(max_length=100, null=True, blank=True)
    action_timestamp = models.DateTimeField(auto_now_add=True)
    processing_time_ms = models.IntegerField(null=True, blank=True)
    file_size = models.BigIntegerField(null=True, blank=True)
    success_flag = models.BooleanField(default=True)
    error_message = models.TextField(null=True, blank=True)
    additional_context = models.JSONField(default=dict, help_text="Extra context information")

    class Meta:
        db_table = 'document_analytics'
        verbose_name = 'Document Analytics'
        verbose_name_plural = 'Document Analytics'
        indexes = [
            models.Index(fields=['company_code', 'document'], name='idx_analytics_company_doc'),
            models.Index(fields=['employee', 'action'], name='idx_analytics_employee_action'),
            models.Index(fields=['user', 'action_timestamp'], name='idx_analytics_user_time'),
            models.Index(fields=['action', 'action_timestamp'], name='idx_analytics_action_time'),
            models.Index(fields=['device_type'], name='idx_analytics_device'),
        ]

    def __str__(self):
        return f'{self.action} on {self.document.document_name} by {self.user.username if self.user else "Anonymous"}'
