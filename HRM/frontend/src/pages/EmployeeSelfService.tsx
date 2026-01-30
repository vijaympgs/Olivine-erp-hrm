import React, { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { 
  User, 
  FileText, 
  Phone, 
  Calendar, 
  Clock, 
  CheckCircle, 
  AlertCircle, 
  Plus,
  Search,
  Filter,
  Download,
  Eye,
  Edit3,
  Trash2,
  CreditCard,
  ChevronDownIcon
} from 'lucide-react';
import { MasterToolbar, MasterMode } from "../components/ui/MasterToolbar";

interface ServiceCatalog {
  id: string;
  service_code: string;
  service_name: string;
  service_category: string;
  service_description: string;
  service_type: string;
  icon_name?: string;
  is_active: boolean;
}

interface ChangeRequest {
  id: string;
  request_type: string;
  field_name: string;
  old_value: string;
  new_value: string;
  change_reason: string;
  status: string;
  priority: string;
  submitted_at: string;
  employee_name: string;
  employee_number: string;
}

interface ServiceRequest {
  id: string;
  request_number: string;
  service_name: string;
  status: string;
  priority: string;
  submitted_at: string;
  employee_name: string;
  employee_number: string;
}

interface DashboardData {
  total_change_requests: number;
  pending_change_requests: number;
  total_service_requests: number;
  pending_service_requests: number;
  recent_activities: any[];
  quick_actions: Array<{id: string; name: string; icon: string}>;
}

// Unified request types
type RequestType = 'Service' | 'Change';
type ChangeFor = 'Update Personal Information' | 'Update Contact Information' | 'Update Bank Details';
type ServiceFor = 'Apply for Leave' | 'Approval Request';

interface UnifiedFormState {
  requestType: RequestType | '';
  requestFor: ChangeFor | ServiceFor | '';
  notes: string;
  // Personal Info fields
  first_name?: string;
  last_name?: string;
  date_of_birth?: string;
  email?: string;
  phone?: string;
  // Contact Info fields
  address?: string;
  city?: string;
  state?: string;
  postal_code?: string;
  country?: string;
  // Bank Details fields
  bank_name?: string;
  account_number?: string;
  // Leave fields
  leave_type?: string;
  start_date?: string;
  end_date?: string;
  // Approval Request fields
  approval_reason?: string;
}

interface MergedRequest {
  id: string;
  requestType: 'Service' | 'Change';
  requestFor: string;
  status: string;
  priority: string;
  submitted_at: string;
  employee_name: string;
  employee_number: string;
  request_number?: string;
  field_name?: string;
  old_value?: string;
  new_value?: string;
  change_reason?: string;
}

const EmployeeSelfService: React.FC = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  
  // Data states
  const [dashboardData, setDashboardData] = useState<DashboardData | null>(null);
  const [services, setServices] = useState<ServiceCatalog[]>([]);
  const [changeRequests, setChangeRequests] = useState<ChangeRequest[]>([]);
  const [serviceRequests, setServiceRequests] = useState<ServiceRequest[]>([]);
  
  // UI states
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('all');
  const [selectedStatus, setSelectedStatus] = useState('all');
  
  // Selection and mode states
  const [selectedItems, setSelectedItems] = useState<string[]>([]);
  const [isEditing, setIsEditing] = useState(false);

  // Unified form state
  const [formState, setFormState] = useState<UnifiedFormState>({
    requestType: '',
    requestFor: '',
    notes: '',
  });

  // Form submission state
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitMessage, setSubmitMessage] = useState('');

  // Determine toolbar mode
  const getMode = (): MasterMode => {
    const isForm = location.pathname.includes('/request/new');
    
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
      
      // Load dashboard data
      const mockDashboardData: DashboardData = {
        total_change_requests: 5,
        pending_change_requests: 2,
        total_service_requests: 8,
        pending_service_requests: 3,
        recent_activities: [],
        quick_actions: []
      };
      setDashboardData(mockDashboardData);

      // Load services (kept for potential future use)
      const mockServices: ServiceCatalog[] = [];
      setServices(mockServices);

      // Load change requests
      const mockChangeRequests: ChangeRequest[] = [
        {
          id: '1',
          request_type: 'Personal Info',
          field_name: 'Phone Number',
          old_value: '+1-555-0123',
          new_value: '+1-555-0456',
          change_reason: 'Updated phone number to new mobile device',
          status: 'Pending Approval',
          priority: 'Medium',
          submitted_at: '2024-01-15T10:30:00Z',
          employee_name: 'John Doe',
          employee_number: 'EMP001'
        },
        {
          id: '2',
          request_type: 'Contact Info',
          field_name: 'Email Address',
          old_value: 'john.doe@oldemail.com',
          new_value: 'john.doe@newemail.com',
          change_reason: 'Changed to personal email address',
          status: 'Approved',
          priority: 'Low',
          submitted_at: '2024-01-10T14:20:00Z',
          employee_name: 'John Doe',
          employee_number: 'EMP001'
        }
      ];
      setChangeRequests(mockChangeRequests);

      // Load service requests
      const mockServiceRequests: ServiceRequest[] = [
        {
          id: '3',
          request_number: 'SR-20240115-001',
          service_name: 'Apply for Leave',
          status: 'In Progress',
          priority: 'High',
          submitted_at: '2024-01-15T09:00:00Z',
          employee_name: 'John Doe',
          employee_number: 'EMP001'
        },
        {
          id: '4',
          request_number: 'SR-20240114-002',
          service_name: 'Approval Request',
          status: 'Completed',
          priority: 'Medium',
          submitted_at: '2024-01-14T16:30:00Z',
          employee_name: 'John Doe',
          employee_number: 'EMP001'
        }
      ];
      setServiceRequests(mockServiceRequests);

    } catch (err: any) {
      setError(err.message || 'Failed to load data');
    } finally {
      setLoading(false);
    }
  };

  // Merge requests for unified table
  const mergedRequests: MergedRequest[] = [
    ...changeRequests.map(req => ({
      ...req,
      requestType: 'Change' as const,
      requestFor: req.request_type,
    })),
    ...serviceRequests.map(req => ({
      ...req,
      requestType: 'Service' as const,
      requestFor: req.service_name,
    }))
  ];

  // Calculate summary statistics
  const summaryStats = {
    totalRequests: mergedRequests.length,
    serviceRequests: mergedRequests.filter(req => req.requestType === 'Service').length,
    changeRequests: mergedRequests.filter(req => req.requestType === 'Change').length,
    pendingRequests: mergedRequests.filter(req => req.status === 'Pending Approval' || req.status === 'Submitted').length,
    // Request For breakdown
    personalInfoRequests: mergedRequests.filter(req => req.requestFor === 'Personal Info').length,
    contactInfoRequests: mergedRequests.filter(req => req.requestFor === 'Contact Info').length,
    leaveRequests: mergedRequests.filter(req => req.requestFor === 'Apply for Leave').length,
    approvalRequests: mergedRequests.filter(req => req.requestFor === 'Approval Request').length,
  };

  // Handle toolbar actions
  const handleToolbarAction = (action: string) => {
    switch (action) {
      case 'new':
        navigate('/hr/employees/self-service/request/new');
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
        document.getElementById('ess-search')?.focus();
        break;
      case 'filter':
        document.getElementById('status-filter')?.focus();
        break;
      case 'export':
        handleExport();
        break;
      case 'print':
        window.print();
        break;
      case 'save':
        if (isFormMode) {
          handleSubmit(new Event('submit') as any);
        }
        break;
      case 'cancel':
      case 'exit':
        if (isFormMode) {
          navigate('/hr/employees/self-service');
        }
        break;
      case 'clear':
      case 'reset':
        if (isFormMode) {
          resetForm();
        } else {
          setSearchTerm('');
          setSelectedCategory('all');
          setSelectedStatus('all');
        }
        break;
      default:
        console.log('Action:', action);
    }
  };

  const handleEdit = () => {
    if (selectedItems.length > 0) {
      setIsEditing(true);
      const itemId = selectedItems[0];
      console.log('Editing item:', itemId);
    }
  };

  const handleDelete = () => {
    if (selectedItems.length > 0) {
      const confirmDelete = window.confirm(
        `Are you sure you want to delete ${selectedItems.length} item(s)?`
      );
      if (confirmDelete) {
        console.log('Deleting items:', selectedItems);
        setSelectedItems([]);
      }
    }
  };

  const handleRefresh = () => {
    loadAllData();
  };

  const handleExport = () => {
    const allData = mergedRequests.map(req => ({
      'Request Type': req.requestType,
      'Request For': req.requestFor,
      'Request #': req.request_number || '',
      'Field': req.field_name || '',
      'Old Value': req.old_value || '',
      'New Value': req.new_value || '',
      'Reason': req.change_reason || '',
      'Status': req.status,
      'Priority': req.priority,
      'Submitted': new Date(req.submitted_at).toLocaleDateString(),
      'Employee': req.employee_name
    }));
    
    if (allData.length > 0) {
      const csv = convertToCSV(allData);
      downloadCSV(csv, 'ess-all-requests-export.csv');
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
      'Submitted': 'bg-blue-100 text-blue-800',
      'Pending Approval': 'bg-yellow-100 text-yellow-800',
      'Approved': 'bg-green-100 text-green-800',
      'Rejected': 'bg-red-100 text-red-800',
      'Completed': 'bg-green-100 text-green-800',
      'In Progress': 'bg-blue-100 text-blue-800',
      'Cancelled': 'bg-gray-100 text-gray-800'
    };
    return (
      <span className={`inline-flex items-center px-2.5 py-0.5 text-xs font-medium ${styles[status] || 'bg-gray-100 text-gray-800'}`}>
        {status}
      </span>
    );
  };

  // Get priority badge styling
  const getPriorityBadge = (priority: string) => {
    const styles: Record<string, string> = {
      'Low': 'bg-gray-100 text-gray-800',
      'Medium': 'bg-blue-100 text-blue-800',
      'High': 'bg-orange-100 text-orange-800',
      'Urgent': 'bg-red-100 text-red-800'
    };
    return (
      <span className={`inline-flex items-center px-2.5 py-0.5 text-xs font-medium ${styles[priority] || 'bg-gray-100 text-gray-800'}`}>
        {priority}
      </span>
    );
  };

  // Filter data based on search and filters
  const filteredRequests = mergedRequests.filter(request => {
    const matchesSearch = request.requestFor.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         request.requestType.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         (request.request_number && request.request_number.toLowerCase().includes(searchTerm.toLowerCase()));
    const matchesStatus = selectedStatus === 'all' || request.status === selectedStatus;
    return matchesSearch && matchesStatus;
  });

  // Check if we're in form mode
  const isFormMode = location.pathname.includes('/request/new');

  // Form handlers
  const handleFormChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormState(prev => ({ ...prev, [name]: value }));
  };

  const handleRequestTypeChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const type = e.target.value as RequestType;
    setFormState({
      requestType: type,
      requestFor: '',
      notes: '',
    });
  };

  const handleRequestForChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setFormState(prev => ({
      ...prev,
      requestFor: e.target.value as ChangeFor | ServiceFor,
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsSubmitting(true);
    setSubmitMessage('');

    try {
      // Validation
      if (!formState.requestType || !formState.requestFor) {
        setSubmitMessage('Please select Request Type and Request For.');
        setIsSubmitting(false);
        return;
      }

      // Prepare submission data
      const submissionData = {
        type: formState.requestType,
        request_for: formState.requestFor,
        data: formState,
      };

      // Submit to backend API
      const response = await fetch('/api/ess/requests/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem('authToken') || ''}`
        },
        body: JSON.stringify(submissionData)
      });

      if (!response.ok) {
        throw new Error('Failed to submit request');
      }

      const result = await response.json();
      setSubmitMessage('Your request has been submitted successfully and is pending approval.');
      
      setTimeout(() => {
        navigate('/hr/employees/self-service');
      }, 2000);

    } catch (error) {
      console.error('Submit error:', error);
      setSubmitMessage('Failed to submit request. Please try again or contact HR.');
    } finally {
      setIsSubmitting(false);
    }
  };

  const resetForm = () => {
    setFormState({
      requestType: '',
      requestFor: '',
      notes: '',
    });
    setSubmitMessage('');
  };

  // Accordion component
  const Accordion = ({ title, children, isOpen, onToggle }: { 
    title: string; 
    children: React.ReactNode; 
    isOpen: boolean;
    onToggle: () => void;
  }) => (
    <div className="border border-gray-200 rounded-lg">
      <button
        type="button"
        onClick={onToggle}
        className="flex w-full justify-between rounded-lg bg-gray-100 px-4 py-2 text-left text-sm font-medium text-gray-900 hover:bg-gray-200"
      >
        <span>{title}</span>
        <ChevronDownIcon className={`h-5 w-5 ${isOpen ? 'rotate-180 transform' : ''}`} />
      </button>
      {isOpen && (
        <div className="px-4 pt-4 pb-2 text-sm text-gray-500">
          {children}
        </div>
      )}
    </div>
  );

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
          viewId="HRM_EMPLOYEE_SELF_SERVICE"
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
                <User className="w-6 h-6 text-blue-600" />
                <h1 className="text-lg font-bold text-gray-900">Employee Self Service</h1>
              </div>
              
              <div className="relative flex-1 max-w-md">
                <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-4 h-4" />
                <input
                  id="ess-search"
                  type="text"
                  placeholder="Search requests..."
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  className="pl-10 pr-4 py-2 w-full border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
                />
              </div>
              
              <select
                id="status-filter"
                value={selectedStatus}
                onChange={(e) => setSelectedStatus(e.target.value)}
                className="px-3 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
              >
                <option value="all">All Status</option>
                <option value="Draft">Draft</option>
                <option value="Submitted">Submitted</option>
                <option value="Pending Approval">Pending Approval</option>
                <option value="Approved">Approved</option>
                <option value="Rejected">Rejected</option>
                <option value="Completed">Completed</option>
                <option value="In Progress">In Progress</option>
                <option value="Cancelled">Cancelled</option>
              </select>
              
              <div className="text-sm text-gray-600 font-medium">
                {summaryStats.totalRequests} requests
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Scrollable Content */}
      <div className="flex-1 overflow-auto bg-gray-50">
        <div className="p-6">
          {isFormMode ? (
            <div className="max-w-4xl mx-auto">
              <div className="bg-white border border-gray-200 rounded-lg shadow-sm">
                <div className="px-6 py-4 border-b border-gray-200">
                  <div className="flex items-center justify-between">
                    <h2 className="text-xl font-semibold text-gray-900">
                      Create New Request
                    </h2>
                    <button
                      onClick={() => navigate('/hr/employees/self-service')}
                      className="text-blue-600 hover:text-blue-800 text-sm"
                    >
                      ← Back to Requests
                    </button>
                  </div>
                </div>
                
                <form onSubmit={handleSubmit} className="p-6 space-y-6">
                  {/* Request Type */}
                  <div>
                    <label className="block text-sm font-medium text-gray-700">Request Type</label>
                    <select
                      name="requestType"
                      value={formState.requestType}
                      onChange={handleRequestTypeChange}
                      className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500"
                      required
                    >
                      <option value="">Select …</option>
                      <option value="Service">Service Request</option>
                      <option value="Change">Change Request</option>
                    </select>
                  </div>

                  {/* Request For */}
                  {formState.requestType && (
                    <div>
                      <label className="block text-sm font-medium text-gray-700">Request For</label>
                      <select
                        name="requestFor"
                        value={formState.requestFor}
                        onChange={handleRequestForChange}
                        className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500"
                        required
                      >
                        <option value="">Select …</option>
                        {formState.requestType === 'Change' && (
                          <>
                            <option value="Update Personal Information">Update Personal Information</option>
                            <option value="Update Contact Information">Update Contact Information</option>
                            <option value="Update Bank Details">Update Bank Details</option>
                          </>
                        )}
                        {formState.requestType === 'Service' && (
                          <>
                            <option value="Apply for Leave">Apply for Leave</option>
                            <option value="Approval Request">Approval Request</option>
                          </>
                        )}
                      </select>
                    </div>
                  )}

                  {/* Accordions */}
                  {formState.requestFor && (
                    <div className="space-y-4">
                      {/* Personal Information */}
                      {formState.requestFor === 'Update Personal Information' && (
                        <Accordion 
                          title="Update Personal Information" 
                          isOpen={true}
                          onToggle={() => {}}
                        >
                          <div className="grid md:grid-cols-2 gap-4">
                            <input
                              name="first_name"
                              placeholder="First name"
                              value={formState.first_name || ''}
                              onChange={handleFormChange}
                              className="border rounded-md p-2 focus:ring-blue-500 focus:border-blue-500"
                              required
                            />
                            <input
                              name="last_name"
                              placeholder="Last name"
                              value={formState.last_name || ''}
                              onChange={handleFormChange}
                              className="border rounded-md p-2 focus:ring-blue-500 focus:border-blue-500"
                              required
                            />
                            <input
                              type="date"
                              name="date_of_birth"
                              value={formState.date_of_birth || ''}
                              onChange={handleFormChange}
                              className="border rounded-md p-2 focus:ring-blue-500 focus:border-blue-500"
                            />
                            <input
                              type="email"
                              name="email"
                              placeholder="Email"
                              value={formState.email || ''}
                              onChange={handleFormChange}
                              className="border rounded-md p-2 focus:ring-blue-500 focus:border-blue-500"
                              required
                            />
                            <input
                              name="phone"
                              placeholder="Phone"
                              value={formState.phone || ''}
                              onChange={handleFormChange}
                              className="border rounded-md p-2 focus:ring-blue-500 focus:border-blue-500"
                            />
                          </div>
                        </Accordion>
                      )}

                      {/* Contact Information */}
                      {formState.requestFor === 'Update Contact Information' && (
                        <Accordion 
                          title="Update Contact Information" 
                          isOpen={true}
                          onToggle={() => {}}
                        >
                          <div className="grid md:grid-cols-2 gap-4">
                            <input
                              name="address"
                              placeholder="Address"
                              value={formState.address || ''}
                              onChange={handleFormChange}
                              className="border rounded-md p-2 focus:ring-blue-500 focus:border-blue-500"
                            />
                            <input
                              name="city"
                              placeholder="City"
                              value={formState.city || ''}
                              onChange={handleFormChange}
                              className="border rounded-md p-2 focus:ring-blue-500 focus:border-blue-500"
                            />
                            <input
                              name="state"
                              placeholder="State"
                              value={formState.state || ''}
                              onChange={handleFormChange}
                              className="border rounded-md p-2 focus:ring-blue-500 focus:border-blue-500"
                            />
                            <input
                              name="postal_code"
                              placeholder="Postal Code"
                              value={formState.postal_code || ''}
                              onChange={handleFormChange}
                              className="border rounded-md p-2 focus:ring-blue-500 focus:border-blue-500"
                            />
                            <input
                              name="country"
                              placeholder="Country"
                              value={formState.country || ''}
                              onChange={handleFormChange}
                              className="border rounded-md p-2 focus:ring-blue-500 focus:border-blue-500"
                            />
                          </div>
                        </Accordion>
                      )}

                      {/* Bank Details */}
                      {formState.requestFor === 'Update Bank Details' && (
                        <Accordion 
                          title="Update Bank Details" 
                          isOpen={true}
                          onToggle={() => {}}
                        >
                          <div className="grid md:grid-cols-2 gap-4">
                            <input
                              name="bank_name"
                              placeholder="Bank name"
                              value={formState.bank_name || ''}
                              onChange={handleFormChange}
                              className="border rounded-md p-2 focus:ring-blue-500 focus:border-blue-500"
                            />
                            <input
                              name="account_number"
                              placeholder="Account number"
                              value={formState.account_number || ''}
                              onChange={handleFormChange}
                              className="border rounded-md p-2 focus:ring-blue-500 focus:border-blue-500"
                            />
                          </div>
                        </Accordion>
                      )}

                      {/* Apply for Leave */}
                      {formState.requestFor === 'Apply for Leave' && (
                        <Accordion 
                          title="Apply for Leave" 
                          isOpen={true}
                          onToggle={() => {}}
                        >
                          <div className="grid md:grid-cols-2 gap-4">
                            <select
                              name="leave_type"
                              value={formState.leave_type || ''}
                              onChange={handleFormChange}
                              className="border rounded-md p-2 focus:ring-blue-500 focus:border-blue-500"
                              required
                            >
                              <option value="">Leave type …</option>
                              <option value="Annual">Annual</option>
                              <option value="Sick">Sick</option>
                              <option value="Maternity">Maternity</option>
                            </select>
                            <input
                              type="date"
                              name="start_date"
                              value={formState.start_date || ''}
                              onChange={handleFormChange}
                              className="border rounded-md p-2 focus:ring-blue-500 focus:border-blue-500"
                              required
                            />
                            <input
                              type="date"
                              name="end_date"
                              value={formState.end_date || ''}
                              onChange={handleFormChange}
                              className="border rounded-md p-2 focus:ring-blue-500 focus:border-blue-500"
                              required
                            />
                          </div>
                        </Accordion>
                      )}

                      {/* Approval Request */}
                      {formState.requestFor === 'Approval Request' && (
                        <Accordion 
                          title="Approval Request" 
                          isOpen={true}
                          onToggle={() => {}}
                        >
                          <textarea
                            name="approval_reason"
                            placeholder="Reason for approval"
                            value={formState.approval_reason || ''}
                            onChange={handleFormChange}
                            className="w-full border rounded-md p-2 focus:ring-blue-500 focus:border-blue-500"
                            rows={4}
                            required
                          />
                        </Accordion>
                      )}
                    </div>
                  )}

                  {/* Notes */}
                  {formState.requestFor && (
                    <div>
                      <label className="block text-sm font-medium text-gray-700">Notes</label>
                      <textarea
                        name="notes"
                        value={formState.notes}
                        onChange={handleFormChange}
                        className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500"
                        rows={3}
                      />
                    </div>
                  )}

                  {/* Submit message */}
                  {submitMessage && (
                    <div className={`mb-4 p-3 rounded-md text-sm ${
                      submitMessage.includes('successfully') 
                        ? 'bg-green-50 text-green-800 border border-green-200' 
                        : 'bg-red-50 text-red-800 border border-red-200'
                    }`}>
                      {submitMessage}
                    </div>
                  )}

                </form>
              </div>
            </div>
          ) : (
            <div className="space-y-6">
              {/* Summary Cards */}
              <div className="space-y-6">
                <h3 className="text-lg font-medium text-gray-900">Request Summary</h3>
                
                {/* Request Type Summary */}
                <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                  <div className="bg-white border border-gray-200 rounded-lg p-4">
                    <div className="flex items-center">
                      <div className="flex-shrink-0">
                        <FileText className="h-6 w-6 text-blue-600" />
                      </div>
                      <div className="ml-3">
                        <p className="text-sm font-medium text-gray-900">Total Requests</p>
                        <p className="text-2xl font-semibold text-gray-900">{summaryStats.totalRequests}</p>
                      </div>
                    </div>
                  </div>
                  
                  <div className="bg-white border border-gray-200 rounded-lg p-4">
                    <div className="flex items-center">
                      <div className="flex-shrink-0">
                        <User className="h-6 w-6 text-green-600" />
                      </div>
                      <div className="ml-3">
                        <p className="text-sm font-medium text-gray-900">Service Requests</p>
                        <p className="text-2xl font-semibold text-gray-900">{summaryStats.serviceRequests}</p>
                      </div>
                    </div>
                  </div>
                  
                  <div className="bg-white border border-gray-200 rounded-lg p-4">
                    <div className="flex items-center">
                      <div className="flex-shrink-0">
                        <Edit3 className="h-6 w-6 text-orange-600" />
                      </div>
                      <div className="ml-3">
                        <p className="text-sm font-medium text-gray-900">Change Requests</p>
                        <p className="text-2xl font-semibold text-gray-900">{summaryStats.changeRequests}</p>
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
                        <p className="text-2xl font-semibold text-gray-900">{summaryStats.pendingRequests}</p>
                      </div>
                    </div>
                  </div>
                </div>

                {/* Request For Summary */}
                <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                  <div className="bg-white border border-gray-200 rounded-lg p-4">
                    <div className="flex items-center">
                      <div className="flex-shrink-0">
                        <User className="h-6 w-6 text-purple-600" />
                      </div>
                      <div className="ml-3">
                        <p className="text-sm font-medium text-gray-900">Personal Info</p>
                        <p className="text-2xl font-semibold text-gray-900">{summaryStats.personalInfoRequests}</p>
                      </div>
                    </div>
                  </div>
                  
                  <div className="bg-white border border-gray-200 rounded-lg p-4">
                    <div className="flex items-center">
                      <div className="flex-shrink-0">
                        <Phone className="h-6 w-6 text-indigo-600" />
                      </div>
                      <div className="ml-3">
                        <p className="text-sm font-medium text-gray-900">Contact Info</p>
                        <p className="text-2xl font-semibold text-gray-900">{summaryStats.contactInfoRequests}</p>
                      </div>
                    </div>
                  </div>
                  
                  <div className="bg-white border border-gray-200 rounded-lg p-4">
                    <div className="flex items-center">
                      <div className="flex-shrink-0">
                        <Calendar className="h-6 w-6 text-teal-600" />
                      </div>
                      <div className="ml-3">
                        <p className="text-sm font-medium text-gray-900">Leave Requests</p>
                        <p className="text-2xl font-semibold text-gray-900">{summaryStats.leaveRequests}</p>
                      </div>
                    </div>
                  </div>
                  
                  <div className="bg-white border border-gray-200 rounded-lg p-4">
                    <div className="flex items-center">
                      <div className="flex-shrink-0">
                        <CheckCircle className="h-6 w-6 text-cyan-600" />
                      </div>
                      <div className="ml-3">
                        <p className="text-sm font-medium text-gray-900">Approval Requests</p>
                        <p className="text-2xl font-semibold text-gray-900">{summaryStats.approvalRequests}</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              {/* Unified Requests Table */}
              <div className="space-y-4">
                <h3 className="text-lg font-medium text-gray-900 mb-4">My Requests</h3>
                <div className="bg-white border border-gray-200 rounded-lg shadow-sm overflow-hidden">
                  <div className="overflow-x-auto">
                    <table className="min-w-full divide-y divide-gray-300">
                      <thead className="bg-gray-50">
                        <tr>
                          <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            Request Type
                          </th>
                          <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            Request For
                          </th>
                          <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            Status
                          </th>
                          <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            Priority
                          </th>
                          <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            Submitted
                          </th>
                          <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            Actions
                          </th>
                        </tr>
                      </thead>
                      <tbody className="bg-white divide-y divide-gray-200">
                        {filteredRequests.map(req => (
                          <tr key={req.id}>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                              {req.requestType}
                            </td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                              {req.requestFor}
                            </td>
                            <td className="px-6 py-4 whitespace-nowrap">
                              {getStatusBadge(req.status)}
                            </td>
                            <td className="px-6 py-4 whitespace-nowrap">
                              {getPriorityBadge(req.priority)}
                            </td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                              {new Date(req.submitted_at).toLocaleDateString()}
                            </td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm font-medium">
                              <button
                                onClick={() => console.log('View request:', req.id)}
                                className="text-blue-600 hover:text-blue-900 mr-3"
                              >
                                <Eye className="w-4 h-4" />
                              </button>
                              {req.status === 'Draft' && (
                                <button
                                  onClick={() => console.log('Edit request:', req.id)}
                                  className="text-green-600 hover:text-green-900"
                                >
                                  <Edit3 className="w-4 h-4" />
                                </button>
                              )}
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default EmployeeSelfService;
