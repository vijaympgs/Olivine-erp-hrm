import React, { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import {
  FileText,
  Upload,
  Download,
  Eye,
  Edit3,
  Trash2,
  Search,
  Filter,
  Plus,
  RefreshCw,
  AlertCircle,
  CheckCircle,
  Clock,
  Calendar,
  User,
  Folder,
  Tag,
  Shield,
  Lock,
  Unlock
} from 'lucide-react';
import { MasterToolbar, MasterMode } from "../components/ui/MasterToolbar";

interface EmployeeDocument {
  id: string;
  employee_id: string;
  employee_name: string;
  employee_number: string;
  document_type: string;
  document_name: string;
  description: string;
  file_name: string;
  file_path: string;
  file_size: number;
  file_type: string;
  mime_type: string;
  file_hash: string;
  version: number;
  is_current: boolean;
  status: string;
  upload_date: string;
  expiry_date: string | null;
  verification_date: string | null;
  verified_by_name: string | null;
  verification_notes: string;
  is_public: boolean;
  is_encrypted: boolean;
  storage_location: string;
  tags: string[];
  metadata: any;
  uploaded_by_name: string;
  created_at: string;
  updated_at: string;
}

interface DocumentType {
  id: string;
  type_code: string;
  type_name: string;
  category: string;
  description: string;
  is_required: boolean;
  is_mandatory_for_onboarding: boolean;
  is_mandatory_for_exit: boolean;
  requires_verification: boolean;
  expiry_required: boolean;
  expiry_days: number;
  max_file_size_mb: number;
  allowed_file_types: string[];
  access_level: string;
  retention_years: number;
  auto_archive: boolean;
  is_active: boolean;
}

const DocumentManagement: React.FC = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Data states
  const [documents, setDocuments] = useState<EmployeeDocument[]>([]);
  const [documentTypes, setDocumentTypes] = useState<DocumentType[]>([]);

  // UI states
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedType, setSelectedType] = useState('all');
  const [selectedStatus, setSelectedStatus] = useState('all');
  const [selectedCategory, setSelectedCategory] = useState('all');

  // Selection and mode states
  const [selectedItems, setSelectedItems] = useState<string[]>([]);
  const [isEditing, setIsEditing] = useState(false);
  const [showUploadModal, setShowUploadModal] = useState(false);

  // Determine toolbar mode
  const getMode = (): MasterMode => {
    const isForm = location.pathname.includes('/documents/new') || location.pathname.includes('/documents/edit');
    
    if (isForm) {
      if (location.pathname.includes('/new')) {
        return 'CREATE';
      }
      return 'EDIT';
    }
    
    if (isEditing) return 'EDIT';
    return 'LIST';
  };

  // Load all data
  const loadAllData = async () => {
    try {
      setLoading(true);

      // Load documents
      const mockDocuments: EmployeeDocument[] = [
        {
          id: '1',
          employee_id: 'emp-001',
          employee_name: 'John Doe',
          employee_number: 'EMP001',
          document_type: 'Resume',
          document_name: 'John Doe - Resume',
          description: 'Professional resume for John Doe',
          file_name: 'john_doe_resume.pdf',
          file_path: '/documents/emp-001/resume.pdf',
          file_size: 245760,
          file_type: 'pdf',
          mime_type: 'application/pdf',
          file_hash: 'abc123def456',
          version: 1,
          is_current: true,
          status: 'Verified',
          upload_date: '2024-01-15T10:30:00Z',
          expiry_date: null,
          verification_date: '2024-01-16T14:20:00Z',
          verified_by_name: 'HR Manager',
          verification_notes: 'Document verified and approved',
          is_public: false,
          is_encrypted: false,
          storage_location: 'Local',
          tags: ['resume', 'professional'],
          metadata: {},
          uploaded_by_name: 'John Doe',
          created_at: '2024-01-15T10:30:00Z',
          updated_at: '2024-01-16T14:20:00Z'
        },
        {
          id: '2',
          employee_id: 'emp-001',
          employee_name: 'John Doe',
          employee_number: 'EMP001',
          document_type: 'Contract',
          document_name: 'Employment Contract',
          description: 'Employment contract for John Doe',
          file_name: 'john_doe_contract.pdf',
          file_path: '/documents/emp-001/contract.pdf',
          file_size: 524288,
          file_type: 'pdf',
          mime_type: 'application/pdf',
          file_hash: 'def456ghi789',
          version: 1,
          is_current: true,
          status: 'Verified',
          upload_date: '2024-01-15T10:30:00Z',
          expiry_date: '2025-01-15',
          verification_date: '2024-01-16T14:20:00Z',
          verified_by_name: 'HR Manager',
          verification_notes: 'Contract verified and signed',
          is_public: false,
          is_encrypted: true,
          storage_location: 'Local',
          tags: ['contract', 'employment'],
          metadata: {},
          uploaded_by_name: 'HR Manager',
          created_at: '2024-01-15T10:30:00Z',
          updated_at: '2024-01-16T14:20:00Z'
        },
        {
          id: '3',
          employee_id: 'emp-002',
          employee_name: 'Jane Smith',
          employee_number: 'EMP002',
          document_type: 'ID Proof',
          document_name: 'Passport Copy',
          description: 'Passport copy for Jane Smith',
          file_name: 'jane_smith_passport.pdf',
          file_path: '/documents/emp-002/passport.pdf',
          file_size: 163840,
          file_type: 'pdf',
          mime_type: 'application/pdf',
          file_hash: 'ghi789jkl012',
          version: 1,
          is_current: true,
          status: 'Verified',
          upload_date: '2024-01-20T09:00:00Z',
          expiry_date: '2029-01-20',
          verification_date: '2024-01-21T11:00:00Z',
          verified_by_name: 'HR Manager',
          verification_notes: 'Passport verified',
          is_public: false,
          is_encrypted: true,
          storage_location: 'Local',
          tags: ['id-proof', 'passport'],
          metadata: {},
          uploaded_by_name: 'Jane Smith',
          created_at: '2024-01-20T09:00:00Z',
          updated_at: '2024-01-21T11:00:00Z'
        }
      ];
      setDocuments(mockDocuments);

      // Load document types
      const mockDocumentTypes: DocumentType[] = [
        {
          id: '1',
          type_code: 'RESUME',
          type_name: 'Resume',
          category: 'Employment',
          description: 'Professional resume',
          is_required: true,
          is_mandatory_for_onboarding: true,
          is_mandatory_for_exit: false,
          requires_verification: true,
          expiry_required: false,
          expiry_days: 0,
          max_file_size_mb: 5,
          allowed_file_types: ['pdf', 'doc', 'docx'],
          access_level: 'HR Only',
          retention_years: 7,
          auto_archive: true,
          is_active: true
        },
        {
          id: '2',
          type_code: 'CONTRACT',
          type_name: 'Contract',
          category: 'Employment',
          description: 'Employment contract',
          is_required: true,
          is_mandatory_for_onboarding: true,
          is_mandatory_for_exit: false,
          requires_verification: true,
          expiry_required: true,
          expiry_days: 365,
          max_file_size_mb: 10,
          allowed_file_types: ['pdf'],
          access_level: 'HR Only',
          retention_years: 7,
          auto_archive: true,
          is_active: true
        },
        {
          id: '3',
          type_code: 'ID_PROOF',
          type_name: 'ID Proof',
          category: 'Legal',
          description: 'Government ID proof',
          is_required: true,
          is_mandatory_for_onboarding: true,
          is_mandatory_for_exit: false,
          requires_verification: true,
          expiry_required: true,
          expiry_days: 1825,
          max_file_size_mb: 5,
          allowed_file_types: ['pdf', 'jpg', 'jpeg', 'png'],
          access_level: 'HR Only',
          retention_years: 7,
          auto_archive: true,
          is_active: true
        }
      ];
      setDocumentTypes(mockDocumentTypes);
    } catch (err: any) {
      setError(err.message || 'Failed to load data');
    } finally {
      setLoading(false);
    }
  };

  // Calculate summary statistics
  const summaryStats = {
    totalDocuments: documents.length,
    verifiedDocuments: documents.filter(doc => doc.status === 'Verified').length,
    pendingDocuments: documents.filter(doc => doc.status === 'Uploaded').length,
    expiredDocuments: documents.filter(doc => {
      if (!doc.expiry_date) return false;
      return new Date(doc.expiry_date) < new Date();
    }).length,
    expiringSoonDocuments: documents.filter(doc => {
      if (!doc.expiry_date) return false;
      const expiryDate = new Date(doc.expiry_date);
      const today = new Date();
      const daysUntilExpiry = Math.ceil((expiryDate.getTime() - today.getTime()) / (1000 * 60 * 60 * 24));
      return daysUntilExpiry > 0 && daysUntilExpiry <= 30;
    }).length,
    encryptedDocuments: documents.filter(doc => doc.is_encrypted).length,
    publicDocuments: documents.filter(doc => doc.is_public).length
  };

  // Handle toolbar actions
  const handleToolbarAction = (action: string) => {
    switch (action) {
      case 'new':
        setShowUploadModal(true);
        break;
      case 'edit':
        handleEdit();
        break;
      case 'delete':
        handleDelete();
        break;
      case 'refresh':
        handleRefresh();
        break;
      case 'search':
        document.getElementById('doc-search')?.focus();
        break;
      case 'filter':
        document.getElementById('type-filter')?.focus();
        break;
      case 'export':
        handleExport();
        break;
      case 'print':
        window.print();
        break;
      case 'save':
        // Handle save action
        break;
      case 'cancel':
        setShowUploadModal(false);
        setIsEditing(false);
        break;
      case 'clear':
        setSearchTerm('');
        setSelectedType('all');
        setSelectedStatus('all');
        setSelectedCategory('all');
        break;
      default:
        console.log('Action:', action);
    }
  };

  const handleEdit = () => {
    if (selectedItems.length > 0) {
      setIsEditing(true);
      const itemId = selectedItems[0];
      navigate(`/hr/employees/documents/${itemId}/edit`);
    }
  };

  const handleDelete = () => {
    if (selectedItems.length > 0) {
      const confirmDelete = window.confirm(
        `Are you sure you want to delete ${selectedItems.length} document(s)?`
      );
      if (confirmDelete) {
        console.log('Deleting documents:', selectedItems);
        setSelectedItems([]);
      }
    }
  };

  const handleRefresh = () => {
    loadAllData();
  };

  const handleExport = () => {
    const allData = documents.map(doc => ({
      'Employee Name': doc.employee_name,
      'Employee Number': doc.employee_number,
      'Document Type': doc.document_type,
      'Document Name': doc.document_name,
      'File Name': doc.file_name,
      'File Size': `${(doc.file_size / 1024).toFixed(2)} KB`,
      'Status': doc.status,
      'Upload Date': new Date(doc.upload_date).toLocaleDateString(),
      'Expiry Date': doc.expiry_date ? new Date(doc.expiry_date).toLocaleDateString() : 'N/A',
      'Encrypted': doc.is_encrypted ? 'Yes' : 'No',
      'Public': doc.is_public ? 'Yes' : 'No'
    }));

    if (allData.length > 0) {
      const csv = convertToCSV(allData);
      downloadCSV(csv, 'document-management-export.csv');
    }
  };

  // Helper functions
  const convertToCSV = (data: any[]): string => {
    if (data.length === 0) return '';

    const headers = Object.keys(data[0]);
    const csvHeaders = headers.join(',');

    const csvRows = data.map(row => {
      return headers.map(header => {
        const value = row[header];
        const escapedValue = String(value).replace(/"/g, '""');
        return `"${escapedValue}"`;
      }).join(',');
    });

    return [csvHeaders, ...csvRows].join('\n');
  };

  const downloadCSV = (csv: string, filename: string) => {
    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
    const url = URL.createObjectURL(blob);
    link.setAttribute('href', url);
    link.setAttribute('download', filename);
    link.style.visibility = 'hidden';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
  };

  // Get status badge styling
  const getStatusBadge = (status: string) => {
    const styles: Record<string, string> = {
      'Draft': 'bg-gray-100 text-gray-800',
      'Uploaded': 'bg-blue-100 text-blue-800',
      'Verified': 'bg-green-100 text-green-800',
      'Rejected': 'bg-red-100 text-red-800',
      'Expired': 'bg-red-100 text-red-800',
      'Archived': 'bg-gray-100 text-gray-800'
    };
    return (
      <span className={`inline-flex items-center px-2.5 py-0.5 text-xs font-medium ${styles[status] || 'bg-gray-100 text-gray-800'}`}>
        {status}
      </span>
    );
  };

  // Get category badge styling
  const getCategoryBadge = (category: string) => {
    const styles: Record<string, string> = {
      'Personal': 'bg-purple-100 text-purple-800',
      'Employment': 'bg-blue-100 text-blue-800',
      'Education': 'bg-green-100 text-green-800',
      'Professional': 'bg-indigo-100 text-indigo-800',
      'Legal': 'bg-red-100 text-red-800',
      'Medical': 'bg-pink-100 text-pink-800',
      'Financial': 'bg-yellow-100 text-yellow-800',
      'Training': 'bg-teal-100 text-teal-800',
      'Performance': 'bg-orange-100 text-orange-800',
      'Compliance': 'bg-cyan-100 text-cyan-800'
    };
    return (
      <span className={`inline-flex items-center px-2.5 py-0.5 text-xs font-medium ${styles[category] || 'bg-gray-100 text-gray-800'}`}>
        {category}
      </span>
    );
  };

  // Format file size
  const formatFileSize = (bytes: number): string => {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i];
  };

  // Filter data based on search and filters
  const filteredDocuments = documents.filter(doc => {
    const matchesSearch = doc.document_name.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         doc.employee_name.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         doc.employee_number.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         doc.document_type.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesType = selectedType === 'all' || doc.document_type === selectedType;
    const matchesStatus = selectedStatus === 'all' || doc.status === selectedStatus;
    return matchesSearch && matchesType && matchesStatus;
  });

  // Check if we're in form mode
  const isFormMode = location.pathname.includes('/documents/new') || location.pathname.includes('/documents/edit');

  // Load data on component mount
  useEffect(() => {
    if (!isFormMode) {
      loadAllData();
    }
  }, [isFormMode]);

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="bg-red-50 border border-red-200 rounded-md p-4">
        <div className="text-sm text-red-600">{error}</div>
      </div>
    );
  }

  return (
    <div className="h-screen flex flex-col">
      {/* Stagnant Toolbar */}
      <div className="flex-shrink-0">
        <MasterToolbar
          viewId="HRM_DOCUMENT_MANAGEMENT"
          mode={getMode()}
          onAction={handleToolbarAction}
        />
      </div>

      {/* Search and Filters - Hide in NEW/EDIT modes */}
      {!isFormMode && (
        <div className="flex-shrink-0 bg-white shadow-sm border border-gray-200">
          <div className="px-6 py-4">
            <div className="flex items-center space-x-4">
              <div className="flex items-center space-x-2">
                <FileText className="w-6 h-6 text-blue-600" />
                <h1 className="text-lg font-bold text-gray-900">Document Management</h1>
              </div>

              <div className="relative flex-1 max-w-md">
                <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-4 h-4" />
                <input
                  id="doc-search"
                  type="text"
                  placeholder="Search documents..."
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  className="pl-10 pr-4 py-2 w-full border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
                />
              </div>

              <select
                id="type-filter"
                value={selectedType}
                onChange={(e) => setSelectedType(e.target.value)}
                className="px-3 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
              >
                <option value="all">All Types</option>
                {documentTypes.map(type => (
                  <option key={type.id} value={type.type_name}>{type.type_name}</option>
                ))}
              </select>

              <select
                value={selectedStatus}
                onChange={(e) => setSelectedStatus(e.target.value)}
                className="px-3 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
              >
                <option value="all">All Status</option>
                <option value="Draft">Draft</option>
                <option value="Uploaded">Uploaded</option>
                <option value="Verified">Verified</option>
                <option value="Rejected">Rejected</option>
                <option value="Expired">Expired</option>
                <option value="Archived">Archived</option>
              </select>

              <div className="text-sm text-gray-600 font-medium">
                {summaryStats.totalDocuments} documents
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Scrollable Content */}
      <div className="flex-1 overflow-auto bg-gray-50">
        <div className="p-6">
          <div className="space-y-6">
            {/* Summary Cards */}
            <h3 className="text-lg font-medium text-gray-900 mb-4">Document Overview</h3>

            <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
              <div className="bg-white border border-gray-200 rounded-lg p-4">
                <div className="flex items-center">
                  <div className="flex-shrink-0">
                    <FileText className="h-6 w-6 text-blue-600" />
                  </div>
                  <div className="ml-3">
                    <p className="text-sm font-medium text-gray-900">Total Documents</p>
                    <p className="text-2xl font-semibold text-gray-900">{summaryStats.totalDocuments}</p>
                  </div>
                </div>
              </div>

              <div className="bg-white border border-gray-200 rounded-lg p-4">
                <div className="flex items-center">
                  <div className="flex-shrink-0">
                    <CheckCircle className="h-6 w-6 text-green-600" />
                  </div>
                  <div className="ml-3">
                    <p className="text-sm font-medium text-gray-900">Verified</p>
                    <p className="text-2xl font-semibold text-gray-900">{summaryStats.verifiedDocuments}</p>
                  </div>
                </div>
              </div>

              <div className="bg-white border border-gray-200 rounded-lg p-4">
                <div className="flex items-center">
                  <div className="flex-shrink-0">
                    <Clock className="h-6 w-6 text-yellow-600" />
                  </div>
                  <div className="ml-3">
                    <p className="text-sm font-medium text-gray-900">Pending</p>
                    <p className="text-2xl font-semibold text-gray-900">{summaryStats.pendingDocuments}</p>
                  </div>
                </div>
              </div>

              <div className="bg-white border border-gray-200 rounded-lg p-4">
                <div className="flex items-center">
                  <div className="flex-shrink-0">
                    <AlertCircle className="h-6 w-6 text-red-600" />
                  </div>
                  <div className="ml-3">
                    <p className="text-sm font-medium text-gray-900">Expired</p>
                    <p className="text-2xl font-semibold text-gray-900">{summaryStats.expiredDocuments}</p>
                  </div>
                </div>
              </div>
            </div>

            {/* Documents Table */}
            <div className="space-y-4">
              <h3 className="text-lg font-medium text-gray-900 mb-4">Employee Documents</h3>
              <div className="bg-white border border-gray-200 rounded-lg shadow-sm overflow-hidden">
                <div className="overflow-x-auto">
                  <table className="min-w-full divide-y divide-gray-300">
                    <thead className="bg-gray-50">
                      <tr>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                          Document
                        </th>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                          Employee
                        </th>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                          Type
                        </th>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                          Status
                        </th>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                          Size
                        </th>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                          Upload Date
                        </th>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                          Expiry
                        </th>
                        <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                          Actions
                        </th>
                      </tr>
                    </thead>
                    <tbody className="bg-white divide-y divide-gray-200">
                      {filteredDocuments.map(doc => (
                        <tr key={doc.id}>
                          <td className="px-6 py-4 whitespace-nowrap">
                            <div className="flex items-center space-x-3">
                              <div className="w-10 h-10 bg-gray-100 rounded flex items-center justify-center">
                                <FileText className="w-5 h-5 text-gray-600" />
                              </div>
                              <div>
                                <div className="text-sm font-medium text-gray-900">{doc.document_name}</div>
                                <div className="text-xs text-gray-500">{doc.file_name}</div>
                              </div>
                            </div>
                          </td>
                          <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                            <div className="flex items-center space-x-2">
                              <User className="w-4 h-4 text-gray-400" />
                              <div>
                                <div className="font-medium">{doc.employee_name}</div>
                                <div className="text-xs text-gray-500">{doc.employee_number}</div>
                              </div>
                            </div>
                          </td>
                          <td className="px-6 py-4 whitespace-nowrap">
                            {getCategoryBadge(doc.document_type)}
                          </td>
                          <td className="px-6 py-4 whitespace-nowrap">
                            {getStatusBadge(doc.status)}
                          </td>
                          <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                            {formatFileSize(doc.file_size)}
                          </td>
                          <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                            {new Date(doc.upload_date).toLocaleDateString()}
                          </td>
                          <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                            {doc.expiry_date ? (
                              <span className={new Date(doc.expiry_date) < new Date() ? 'text-red-600' : 'text-gray-900'}>
                                {new Date(doc.expiry_date).toLocaleDateString()}
                              </span>
                            ) : (
                              'N/A'
                            )}
                          </td>
                          <td className="px-6 py-4 whitespace-nowrap text-sm font-medium">
                            <div className="flex items-center space-x-2">
                              <button
                                onClick={() => console.log('View document:', doc.id)}
                                className="text-blue-600 hover:text-blue-900"
                                title="View"
                              >
                                <Eye className="w-4 h-4" />
                              </button>
                              <button
                                onClick={() => console.log('Download document:', doc.id)}
                                className="text-green-600 hover:text-green-900"
                                title="Download"
                              >
                                <Download className="w-4 h-4" />
                              </button>
                              {doc.status === 'Uploaded' && (
                                <button
                                  onClick={() => console.log('Edit document:', doc.id)}
                                  className="text-gray-600 hover:text-gray-900"
                                  title="Edit"
                                >
                                  <Edit3 className="w-4 h-4" />
                                </button>
                              )}
                              <button
                                onClick={() => console.log('Delete document:', doc.id)}
                                className="text-red-600 hover:text-red-900"
                                title="Delete"
                              >
                                <Trash2 className="w-4 h-4" />
                              </button>
                              {doc.is_encrypted && (
                                <Lock className="w-4 h-4 text-gray-400" title="Encrypted" />
                              )}
                            </div>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DocumentManagement;
