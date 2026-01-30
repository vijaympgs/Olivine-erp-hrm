import React, { useState, useRef } from 'react';
import { Upload, FileText, X, AlertCircle, CheckCircle } from 'lucide-react';

interface DocumentUploadProps {
  employeeId: string;
  onUploadSuccess?: (document: any) => void;
  onUploadError?: (error: string) => void;
}

interface DocumentType {
  id: string;
  type_code: string;
  type_name: string;
  category: string;
  max_file_size_mb: number;
  allowed_file_types: string[];
}

export const DocumentUpload: React.FC<DocumentUploadProps> = ({
  employeeId,
  onUploadSuccess,
  onUploadError
}) => {
  const [file, setFile] = useState<File | null>(null);
  const [documentTypes, setDocumentTypes] = useState<DocumentType[]>([]);
  const [selectedType, setSelectedType] = useState<string>('');
  const [documentName, setDocumentName] = useState<string>('');
  const [documentDescription, setDocumentDescription] = useState<string>('');
  const [expiryDate, setExpiryDate] = useState<string>('');
  const [tags, setTags] = useState<string[]>([]);
  const [tagInput, setTagInput] = useState<string>('');
  const [isUploading, setIsUploading] = useState<boolean>(false);
  const [uploadProgress, setUploadProgress] = useState<number>(0);
  const [error, setError] = useState<string>('');
  const [success, setSuccess] = useState<string>('');
  const fileInputRef = useRef<HTMLInputElement>(null);

  // Fetch document types on component mount
  React.useEffect(() => {
    fetchDocumentTypes();
  }, []);

  const fetchDocumentTypes = async () => {
    try {
      const response = await fetch('/api/hrm/api/v1/document-types/active/');
      if (response.ok) {
        const data = await response.json();
        setDocumentTypes(data);
      }
    } catch (err) {
      console.error('Failed to fetch document types:', err);
    }
  };

  const handleFileSelect = (event: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFile = event.target.files?.[0];
    if (selectedFile) {
      setFile(selectedFile);
      // Auto-populate document name with file name (without extension)
      const nameWithoutExt = selectedFile.name.replace(/\.[^/.]+$/, '');
      setDocumentName(nameWithoutExt);
      setError('');
      setSuccess('');
    }
  };

  const handleDragOver = (event: React.DragEvent) => {
    event.preventDefault();
    event.stopPropagation();
  };

  const handleDrop = (event: React.DragEvent) => {
    event.preventDefault();
    event.stopPropagation();
    
    const droppedFile = event.dataTransfer.files[0];
    if (droppedFile) {
      setFile(droppedFile);
      const nameWithoutExt = droppedFile.name.replace(/\.[^/.]+$/, '');
      setDocumentName(nameWithoutExt);
      setError('');
      setSuccess('');
    }
  };

  const validateFile = (): boolean => {
    if (!file) {
      setError('Please select a file to upload');
      return false;
    }

    if (!selectedType) {
      setError('Please select a document type');
      return false;
    }

    if (!documentName.trim()) {
      setError('Please enter a document name');
      return false;
    }

    const selectedDocType = documentTypes.find(dt => dt.id === selectedType);
    if (selectedDocType) {
      // Check file size
      if (file.size > selectedDocType.max_file_size_mb * 1024 * 1024) {
        setError(`File size exceeds maximum limit of ${selectedDocType.max_file_size_mb}MB`);
        return false;
      }

      // Check file type
      const fileExtension = '.' + file.name.split('.').pop()?.toLowerCase();
      if (selectedDocType.allowed_file_types.length > 0 && 
          !selectedDocType.allowed_file_types.includes(fileExtension)) {
        setError(`File type ${fileExtension} not allowed. Allowed types: ${selectedDocType.allowed_file_types.join(', ')}`);
        return false;
      }
    }

    return true;
  };

  const handleUpload = async () => {
    if (!validateFile()) {
      return;
    }

    setIsUploading(true);
    setUploadProgress(0);
    setError('');
    setSuccess('');

    try {
      const formData = new FormData();
      formData.append('file', file);
      formData.append('document_type', selectedType);
      formData.append('document_name', documentName);
      formData.append('document_description', documentDescription);
      formData.append('employee_id', employeeId);
      
      if (expiryDate) {
        formData.append('expiry_date', expiryDate);
      }
      
      if (tags.length > 0) {
        formData.append('tags', JSON.stringify(tags));
      }

      const xhr = new XMLHttpRequest();
      
      // Track upload progress
      xhr.upload.addEventListener('progress', (event) => {
        if (event.lengthComputable) {
          const progress = Math.round((event.loaded / event.total) * 100);
          setUploadProgress(progress);
        }
      });

      // Handle completion
      xhr.addEventListener('load', () => {
        if (xhr.status === 201) {
          const response = JSON.parse(xhr.responseText);
          setSuccess('Document uploaded successfully!');
          setUploadProgress(100);
          
          // Reset form
          setFile(null);
          setDocumentName('');
          setDocumentDescription('');
          setExpiryDate('');
          setTags([]);
          setTagInput('');
          setSelectedType('');
          if (fileInputRef.current) {
            fileInputRef.current.value = '';
          }
          
          if (onUploadSuccess) {
            onUploadSuccess(response);
          }
        } else {
          const errorResponse = JSON.parse(xhr.responseText);
          setError(errorResponse.error || 'Upload failed');
          if (onUploadError) {
            onUploadError(errorResponse.error || 'Upload failed');
          }
        }
        setIsUploading(false);
      });

      // Handle error
      xhr.addEventListener('error', () => {
        setError('Upload failed. Please try again.');
        setIsUploading(false);
        if (onUploadError) {
          onUploadError('Upload failed. Please try again.');
        }
      });

      // Send request
      xhr.open('POST', '/api/hrm/api/v1/documents/upload/');
      xhr.send(formData);

    } catch (err) {
      setError('Upload failed. Please try again.');
      setIsUploading(false);
      if (onUploadError) {
        onUploadError('Upload failed. Please try again.');
      }
    }
  };

  const addTag = () => {
    const tag = tagInput.trim();
    if (tag && !tags.includes(tag)) {
      setTags([...tags, tag]);
      setTagInput('');
    }
  };

  const removeTag = (tagToRemove: string) => {
    setTags(tags.filter(tag => tag !== tagToRemove));
  };

  const handleTagInputKeyPress = (event: React.KeyboardEvent) => {
    if (event.key === 'Enter') {
      event.preventDefault();
      addTag();
    }
  };

  const formatFileSize = (bytes: number): string => {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  };

  return (
    <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
      <h3 className="text-lg font-medium text-gray-900 mb-4">Upload Document</h3>
      
      {/* Error and Success Messages */}
      {error && (
        <div className="mb-4 p-3 bg-red-50 border border-red-200 rounded-md flex items-center">
          <AlertCircle className="w-4 h-4 text-red-500 mr-2" />
          <span className="text-sm text-red-700">{error}</span>
        </div>
      )}
      
      {success && (
        <div className="mb-4 p-3 bg-green-50 border border-green-200 rounded-md flex items-center">
          <CheckCircle className="w-4 h-4 text-green-500 mr-2" />
          <span className="text-sm text-green-700">{success}</span>
        </div>
      )}

      {/* File Upload Area */}
      <div className="mb-6">
        <div
          className="border-2 border-dashed border-gray-300 rounded-lg p-6 text-center hover:border-gray-400 transition-colors cursor-pointer"
          onDragOver={handleDragOver}
          onDrop={handleDrop}
          onClick={() => fileInputRef.current?.click()}
        >
          <input
            ref={fileInputRef}
            type="file"
            className="hidden"
            onChange={handleFileSelect}
            accept=".pdf,.doc,.docx,.jpg,.jpeg,.png,.gif,.txt"
          />
          
          {file ? (
            <div className="flex items-center justify-center">
              <FileText className="w-8 h-8 text-blue-500 mr-3" />
              <div className="text-left">
                <p className="text-sm font-medium text-gray-900">{file.name}</p>
                <p className="text-xs text-gray-500">{formatFileSize(file.size)}</p>
              </div>
              <button
                onClick={(e) => {
                  e.stopPropagation();
                  setFile(null);
                }}
                className="ml-3 text-gray-400 hover:text-gray-600"
              >
                <X className="w-4 h-4" />
              </button>
            </div>
          ) : (
            <div>
              <Upload className="w-8 h-8 text-gray-400 mx-auto mb-2" />
              <p className="text-sm text-gray-600">
                Drag and drop a file here, or click to select
              </p>
              <p className="text-xs text-gray-500 mt-1">
                PDF, DOC, DOCX, JPG, PNG, GIF, TXT (Max: 10MB)
              </p>
            </div>
          )}
        </div>
      </div>

      {/* Document Type Selection */}
      <div className="mb-4">
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Document Type *
        </label>
        <select
          value={selectedType}
          onChange={(e) => setSelectedType(e.target.value)}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
        >
          <option value="">Select document type</option>
          {documentTypes.map((docType) => (
            <option key={docType.id} value={docType.id}>
              {docType.type_name} ({docType.category})
            </option>
          ))}
        </select>
      </div>

      {/* Document Name */}
      <div className="mb-4">
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Document Name *
        </label>
        <input
          type="text"
          value={documentName}
          onChange={(e) => setDocumentName(e.target.value)}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
          placeholder="Enter document name"
        />
      </div>

      {/* Document Description */}
      <div className="mb-4">
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Description
        </label>
        <textarea
          value={documentDescription}
          onChange={(e) => setDocumentDescription(e.target.value)}
          rows={3}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
          placeholder="Enter document description (optional)"
        />
      </div>

      {/* Expiry Date */}
      <div className="mb-4">
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Expiry Date
        </label>
        <input
          type="date"
          value={expiryDate}
          onChange={(e) => setExpiryDate(e.target.value)}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
        />
      </div>

      {/* Tags */}
      <div className="mb-6">
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Tags
        </label>
        <div className="flex flex-wrap gap-2 mb-2">
          {tags.map((tag) => (
            <span
              key={tag}
              className="inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-blue-100 text-blue-800"
            >
              {tag}
              <button
                onClick={() => removeTag(tag)}
                className="ml-1 text-blue-600 hover:text-blue-800"
              >
                <X className="w-3 h-3" />
              </button>
            </span>
          ))}
        </div>
        <div className="flex gap-2">
          <input
            type="text"
            value={tagInput}
            onChange={(e) => setTagInput(e.target.value)}
            onKeyPress={handleTagInputKeyPress}
            className="flex-1 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            placeholder="Add a tag and press Enter"
          />
          <button
            onClick={addTag}
            className="px-4 py-2 bg-gray-100 text-gray-700 rounded-md hover:bg-gray-200 transition-colors"
          >
            Add
          </button>
        </div>
      </div>

      {/* Upload Progress */}
      {isUploading && (
        <div className="mb-4">
          <div className="flex items-center justify-between mb-2">
            <span className="text-sm text-gray-600">Uploading...</span>
            <span className="text-sm text-gray-600">{uploadProgress}%</span>
          </div>
          <div className="w-full bg-gray-200 rounded-full h-2">
            <div
              className="bg-blue-600 h-2 rounded-full transition-all duration-300"
              style={{ width: `${uploadProgress}%` }}
            />
          </div>
        </div>
      )}

      {/* Upload Button */}
      <button
        onClick={handleUpload}
        disabled={isUploading || !file || !selectedType || !documentName.trim()}
        className="w-full px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors"
      >
        {isUploading ? 'Uploading...' : 'Upload Document'}
      </button>
    </div>
  );
};
