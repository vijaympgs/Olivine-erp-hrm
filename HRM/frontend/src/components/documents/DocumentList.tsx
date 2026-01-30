import React, { useState, useEffect } from 'react';
import { FileText, Download, Eye, Calendar, Tag, AlertCircle, CheckCircle, Clock, X } from 'lucide-react';

interface Document {
  id: string;
  document_name: string;
  document_description: string;
  file_name: string;
  file_size_display: string;
  file_type: string;
  status: string;
  upload_date: string;
  expiry_date: string;
  document_type_name: string;
  document_type_category: string;
  tags: string[];
  file_url?: string;
}

interface DocumentListProps {
  employeeId: string;
  onDocumentSelect?: (document: Document) => void;
  refreshTrigger?: number;
}

export const DocumentList: React.FC<DocumentListProps> = ({
  employeeId,
  onDocumentSelect,
  refreshTrigger
}) => {
  const [documents, setDocuments] = useState<Document[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string>('');
  const [selectedDocument, setSelectedDocument] = useState<Document | null>(null);

  useEffect(() => {
    fetchDocuments();
  }, [employeeId, refreshTrigger]);

  const fetchDocuments = async () => {
    if (!employeeId) return;

    setLoading(true);
    setError('');

    try {
      const response = await fetch(`/api/hrm/api/v1/employees/${employeeId}/documents/`);
      if (response.ok) {
        const data = await response.json();
        setDocuments(data);
      } else {
        setError('Failed to fetch documents');
      }
    } catch (err) {
      setError('Failed to fetch documents');
      console.error('Error fetching documents:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleDownload = async (document: Document) => {
    try {
      const response = await fetch(`/api/hrm/api/v1/documents/${document.id}/download/`);
      if (response.ok) {
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = document.file_name;
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);
      } else {
        setError('Failed to download document');
      }
    } catch (err) {
      setError('Failed to download document');
      console.error('Error downloading document:', err);
    }
  };

  const handlePreview = async (document: Document) => {
    try {
      const response = await fetch(`/api/hrm/api/v1/documents/${document.id}/preview/`);
      if (response.ok) {
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        window.open(url, '_blank');
      } else {
        setError('Preview not available for this document type');
      }
    } catch (err) {
      setError('Failed to preview document');
      console.error('Error previewing document:', err);
    }
  };

  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'Uploaded':
        return <Clock className="w-4 h-4 text-yellow-500" />;
      case 'Verified':
        return <CheckCircle className="w-4 h-4 text-green-500" />;
      case 'Rejected':
        return <X className="w-4 h-4 text-red-500" />;
      case 'Expired':
        return <AlertCircle className="w-4 h-4 text-red-500" />;
      default:
        return <FileText className="w-4 h-4 text-gray-500" />;
    }
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'Uploaded':
        return 'bg-yellow-100 text-yellow-800';
      case 'Verified':
        return 'bg-green-100 text-green-800';
      case 'Rejected':
        return 'bg-red-100 text-red-800';
      case 'Expired':
        return 'bg-red-100 text-red-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  };

  const getFileIcon = (fileType: string) => {
    const iconClass = "w-5 h-5";
    switch (fileType.toLowerCase()) {
      case '.pdf':
        return <FileText className={`${iconClass} text-red-500`} />;
      case '.doc':
      case '.docx':
        return <FileText className={`${iconClass} text-blue-500`} />;
      case '.jpg':
      case '.jpeg':
      case '.png':
      case '.gif':
        return <FileText className={`${iconClass} text-green-500`} />;
      default:
        return <FileText className={`${iconClass} text-gray-500`} />;
    }
  };

  const isExpired = (expiryDate: string) => {
    if (!expiryDate) return false;
    return new Date(expiryDate) < new Date();
  };

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString();
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center py-8">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
        <span className="ml-2 text-gray-600">Loading documents...</span>
      </div>
    );
  }

  if (error) {
    return (
      <div className="bg-red-50 border border-red-200 rounded-md p-4">
        <div className="flex items-center">
          <AlertCircle className="w-4 h-4 text-red-500 mr-2" />
          <span className="text-sm text-red-700">{error}</span>
        </div>
      </div>
    );
  }

  if (documents.length === 0) {
    return (
      <div className="text-center py-8">
        <FileText className="w-12 h-12 text-gray-400 mx-auto mb-4" />
        <h3 className="text-lg font-medium text-gray-900 mb-1">No documents found</h3>
        <p className="text-gray-500">Upload documents to get started</p>
      </div>
    );
  }

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h3 className="text-lg font-medium text-gray-900">
          Documents ({documents.length})
        </h3>
      </div>

      <div className="grid gap-4">
        {documents.map((document) => (
          <div
            key={document.id}
            className="bg-white border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow cursor-pointer"
            onClick={() => {
              setSelectedDocument(document);
              if (onDocumentSelect) {
                onDocumentSelect(document);
              }
            }}
          >
            <div className="flex items-start justify-between">
              <div className="flex items-start space-x-3 flex-1">
                {getFileIcon(document.file_type)}
                
                <div className="flex-1 min-w-0">
                  <div className="flex items-center space-x-2 mb-1">
                    <h4 className="text-sm font-medium text-gray-900 truncate">
                      {document.document_name}
                    </h4>
                    <span className={`inline-flex items-center px-2 py-0.5 rounded text-xs font-medium ${getStatusColor(document.status)}`}>
                      {getStatusIcon(document.status)}
                      <span className="ml-1">{document.status}</span>
                    </span>
                  </div>
                  
                  <p className="text-sm text-gray-600 mb-2">
                    {document.document_type_name} • {document.document_type_category}
                  </p>
                  
                  {document.document_description && (
                    <p className="text-sm text-gray-500 mb-2 line-clamp-2">
                      {document.document_description}
                    </p>
                  )}
                  
                  <div className="flex items-center space-x-4 text-xs text-gray-500">
                    <div className="flex items-center">
                      <FileText className="w-3 h-3 mr-1" />
                      {document.file_name}
                    </div>
                    <div className="flex items-center">
                      <span>{document.file_size_display}</span>
                    </div>
                    <div className="flex items-center">
                      <Calendar className="w-3 h-3 mr-1" />
                      Uploaded: {formatDate(document.upload_date)}
                    </div>
                    {document.expiry_date && (
                      <div className={`flex items-center ${isExpired(document.expiry_date) ? 'text-red-500' : ''}`}>
                        <AlertCircle className="w-3 h-3 mr-1" />
                        Expires: {formatDate(document.expiry_date)}
                      </div>
                    )}
                  </div>
                  
                  {document.tags && document.tags.length > 0 && (
                    <div className="flex items-center space-x-1 mt-2">
                      <Tag className="w-3 h-3 text-gray-400" />
                      <div className="flex flex-wrap gap-1">
                        {document.tags.map((tag, index) => (
                          <span
                            key={index}
                            className="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-gray-100 text-gray-800"
                          >
                            {tag}
                          </span>
                        ))}
                      </div>
                    </div>
                  )}
                </div>
              </div>
              
              <div className="flex items-center space-x-2 ml-4">
                <button
                  onClick={(e) => {
                    e.stopPropagation();
                    handlePreview(document);
                  }}
                  className="p-2 text-gray-400 hover:text-blue-600 transition-colors"
                  title="Preview"
                >
                  <Eye className="w-4 h-4" />
                </button>
                <button
                  onClick={(e) => {
                    e.stopPropagation();
                    handleDownload(document);
                  }}
                  className="p-2 text-gray-400 hover:text-green-600 transition-colors"
                  title="Download"
                >
                  <Download className="w-4 h-4" />
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
