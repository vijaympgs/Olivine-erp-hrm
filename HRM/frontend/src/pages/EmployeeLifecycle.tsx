import React, { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import {
  Users,
  Calendar,
  TrendingUp,
  AlertCircle,
  CheckCircle,
  Clock,
  FileText,
  Settings,
  BarChart3,
  Activity,
  Search,
  Filter,
  Download,
  Eye,
  Edit3,
  Plus,
  UserCheck,
  UserX,
  RefreshCw
} from 'lucide-react';
import { MasterToolbar, MasterMode } from "../components/ui/MasterToolbar";

interface EmployeeLifecycle {
  id: string;
  employee_name: string;
  employee_number: string;
  hire_date: string;
  confirmation_date: string | null;
  employment_status: string;
  probation_end_date: string | null;
  contract_start_date: string | null;
  contract_end_date: string | null;
  notice_period_days: number;
  last_working_day: string | null;
  separation_reason: string | null;
  separation_type: string | null;
  is_rehireable: boolean;
  exit_interview_completed: boolean;
  final_payroll_processed: boolean;
  years_of_service: number;
  is_probation_complete: boolean;
  days_to_contract_end: number | null;
  created_at: string;
  updated_at: string;
}

interface LifecycleEvent {
  id: string;
  employee_name: string;
  employee_number: string;
  event_type: string;
  event_sub_type: string | null;
  previous_status: string | null;
  new_status: string | null;
  event_date: string;
  effective_date: string;
  reason_code: string | null;
  event_description: string | null;
  initiated_by_name: string | null;
  approved_by_name: string | null;
  approved_at: string | null;
  status: string;
  priority: string;
  workflow_instance_id: string | null;
  supporting_documents: any[];
  system_generated: boolean;
  batch_reference: string | null;
  created_at: string;
  updated_at: string;
}

interface LifecycleAnalytics {
  id: string;
  employee_name: string;
  employee_number: string;
  event_type: string;
  event_date: string;
  processing_time_days: number | null;
  workflow_completion_time_hours: number | null;
  satisfaction_rating: number | null;
  feedback_score: number | null;
  cost_impact: number | null;
  department_name: string | null;
  location_name: string | null;
  manager_name: string | null;
  hr_rep_name: string | null;
  metrics_data: any;
  benchmark_comparison: any;
  created_at: string;
}

const EmployeeLifecycle: React.FC = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  
  // Data states
  const [employeeLifecycles, setEmployeeLifecycles] = useState<EmployeeLifecycle[]>([]);
  const [lifecycleEvents, setLifecycleEvents] = useState<LifecycleEvent[]>([]);
  const [lifecycleAnalytics, setLifecycleAnalytics] = useState<LifecycleAnalytics[]>([]);
  
  // UI states
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedStatus, setSelectedStatus] = useState('all');
  const [selectedEventType, setSelectedEventType] = useState('all');
  const [activeTab, setActiveTab] = useState<'overview' | 'events' | 'analytics'>('overview');
  
  // Selection and mode states
  const [selectedItems, setSelectedItems] = useState<string[]>([]);
  const [isEditing, setIsEditing] = useState(false);

  // Determine toolbar mode
  const getMode = (): MasterMode => {
    const isForm = location.pathname.includes('/lifecycle/new');
    
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
      
      // Load employee lifecycles
      const mockEmployeeLifecycles: EmployeeLifecycle[] = [
        {
          id: '1',
          employee_name: 'John Doe',
          employee_number: 'EMP001',
          hire_date: '2022-01-15',
          confirmation_date: '2022-04-15',
          employment_status: 'Active',
          probation_end_date: '2022-04-15',
          contract_start_date: '2022-01-15',
          contract_end_date: null,
          notice_period_days: 30,
          last_working_day: null,
          separation_reason: null,
          separation_type: null,
          is_rehireable: true,
          exit_interview_completed: false,
          final_payroll_processed: false,
          years_of_service: 3,
          is_probation_complete: true,
          days_to_contract_end: null,
          created_at: '2022-01-15T10:30:00Z',
          updated_at: '2024-01-15T14:20:00Z'
        },
        {
          id: '2',
          employee_name: 'Jane Smith',
          employee_number: 'EMP002',
          hire_date: '2023-06-01',
          confirmation_date: null,
          employment_status: 'Probation',
          probation_end_date: '2023-09-01',
          contract_start_date: '2023-06-01',
          contract_end_date: '2024-06-01',
          notice_period_days: 30,
          last_working_day: null,
          separation_reason: null,
          separation_type: null,
          is_rehireable: true,
          exit_interview_completed: false,
          final_payroll_processed: false,
          years_of_service: 1,
          is_probation_complete: false,
          days_to_contract_end: 120,
          created_at: '2023-06-01T09:00:00Z',
          updated_at: '2024-01-15T14:20:00Z'
        },
        {
          id: '3',
          employee_name: 'Bob Johnson',
          employee_number: 'EMP003',
          hire_date: '2021-03-10',
          confirmation_date: '2021-06-10',
          employment_status: 'Notice Period',
          probation_end_date: '2021-06-10',
          contract_start_date: '2021-03-10',
          contract_end_date: null,
          notice_period_days: 30,
          last_working_day: '2024-02-15',
          separation_reason: 'Career change',
          separation_type: 'Resignation',
          is_rehireable: true,
          exit_interview_completed: true,
          final_payroll_processed: false,
          years_of_service: 3,
          is_probation_complete: true,
          days_to_contract_end: null,
          created_at: '2021-03-10T11:00:00Z',
          updated_at: '2024-01-20T10:00:00Z'
        }
      ];
      setEmployeeLifecycles(mockEmployeeLifecycles);

      // Load lifecycle events
      const mockLifecycleEvents: LifecycleEvent[] = [
        {
          id: '1',
          employee_name: 'John Doe',
          employee_number: 'EMP001',
          event_type: 'Hire',
          event_sub_type: 'Initial Employment',
          previous_status: null,
          new_status: 'Probation',
          event_date: '2022-01-15',
          effective_date: '2022-01-15',
          reason_code: 'NEW_HIRE',
          event_description: 'New employee onboarding',
          initiated_by_name: 'HR Manager',
          approved_by_name: null,
          approved_at: null,
          status: 'Completed',
          priority: 'Medium',
          workflow_instance_id: null,
          supporting_documents: [],
          system_generated: false,
          batch_reference: null,
          created_at: '2022-01-15T10:30:00Z',
          updated_at: '2022-01-15T10:30:00Z'
        },
        {
          id: '2',
          employee_name: 'John Doe',
          employee_number: 'EMP001',
          event_type: 'Confirmation',
          event_sub_type: 'Probation Completion',
          previous_status: 'Probation',
          new_status: 'Active',
          event_date: '2022-04-15',
          effective_date: '2022-04-15',
          reason_code: 'PROBATION_COMPLETE',
          event_description: 'Successful completion of probation period',
          initiated_by_name: 'HR Manager',
          approved_by_name: 'Department Head',
          approved_at: '2022-04-14T15:30:00Z',
          status: 'Completed',
          priority: 'High',
          workflow_instance_id: 'WF-001',
          supporting_documents: ['doc1.pdf', 'doc2.pdf'],
          system_generated: false,
          batch_reference: null,
          created_at: '2022-04-15T09:00:00Z',
          updated_at: '2022-04-15T16:00:00Z'
        },
        {
          id: '3',
          employee_name: 'Bob Johnson',
          employee_number: 'EMP003',
          event_type: 'Resignation',
          event_sub_type: 'Voluntary',
          previous_status: 'Active',
          new_status: 'Notice Period',
          event_date: '2024-01-20',
          effective_date: '2024-02-15',
          reason_code: 'CAREER_CHANGE',
          event_description: 'Employee resigned for better opportunity',
          initiated_by_name: 'Bob Johnson',
          approved_by_name: 'HR Manager',
          approved_at: '2024-01-21T11:00:00Z',
          status: 'Approved',
          priority: 'High',
          workflow_instance_id: 'WF-002',
          supporting_documents: ['resignation_letter.pdf'],
          system_generated: false,
          batch_reference: null,
          created_at: '2024-01-20T14:30:00Z',
          updated_at: '2024-01-21T11:00:00Z'
        }
      ];
      setLifecycleEvents(mockLifecycleEvents);

      // Load lifecycle analytics
      const mockLifecycleAnalytics: LifecycleAnalytics[] = [
        {
          id: '1',
          employee_name: 'John Doe',
          employee_number: 'EMP001',
          event_type: 'Hire',
          event_date: '2022-01-15',
          processing_time_days: 5,
          workflow_completion_time_hours: 24.5,
          satisfaction_rating: 4,
          feedback_score: 8,
          cost_impact: 5000.00,
          department_name: 'Engineering',
          location_name: 'Head Office',
          manager_name: 'Tech Lead',
          hr_rep_name: 'HR Manager',
          metrics_data: {
            'source': 'LinkedIn',
            'recruiter': 'Internal HR',
            'interview_rounds': 3
          },
          benchmark_comparison: {
            'industry_avg_hire_time': 7,
            'industry_avg_cost': 6000
          },
          created_at: '2022-01-20T10:00:00Z'
        },
        {
          id: '2',
          employee_name: 'Bob Johnson',
          employee_number: 'EMP003',
          event_type: 'Termination',
          event_date: '2024-01-20',
          processing_time_days: 15,
          workflow_completion_time_hours: 48.0,
          satisfaction_rating: 2,
          feedback_score: 5,
          cost_impact: 2000.00,
          department_name: 'Engineering',
          location_name: 'Head Office',
          manager_name: 'Tech Lead',
          hr_rep_name: 'HR Manager',
          metrics_data: {
            'reason': 'Voluntary',
            'exit_interview_completed': true,
            'offboarding_score': 6
          },
          benchmark_comparison: {
            'industry_avg_turnover_cost': 3000
          },
          created_at: '2024-01-25T10:00:00Z'
        }
      ];
      setLifecycleAnalytics(mockLifecycleAnalytics);

    } catch (err: any) {
      setError(err.message || 'Failed to load data');
    } finally {
      setLoading(false);
    }
  };

  // Calculate summary statistics
  const summaryStats = {
    totalEmployees: employeeLifecycles.length,
    activeEmployees: employeeLifecycles.filter(emp => emp.employment_status === 'Active').length,
    probationEmployees: employeeLifecycles.filter(emp => emp.employment_status === 'Probation').length,
    noticePeriodEmployees: employeeLifecycles.filter(emp => emp.employment_status === 'Notice Period').length,
    totalEvents: lifecycleEvents.length,
    pendingEvents: lifecycleEvents.filter(event => event.status === 'Pending Approval').length,
    avgProcessingTime: lifecycleAnalytics.length > 0 
      ? (lifecycleAnalytics.reduce((sum, item) => sum + (item.processing_time_days || 0), 0) / lifecycleAnalytics.length).toFixed(1)
      : 0,
    avgSatisfaction: lifecycleAnalytics.length > 0
      ? (lifecycleAnalytics.reduce((sum, item) => sum + (item.satisfaction_rating || 0), 0) / lifecycleAnalytics.length).toFixed(1)
      : 0
  };

  // Handle toolbar actions
  const handleToolbarAction = (action: string) => {
    switch (action) {
      case 'new':
        navigate('/hr/employees/lifecycle/new');
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
        document.getElementById('lifecycle-search')?.focus();
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
        // Handle save action
        break;
      case 'cancel':
        if (location.pathname.includes('/new')) {
          navigate('/hr/employees/lifecycle');
        }
        break;
      case 'clear':
        setSearchTerm('');
        setSelectedStatus('all');
        setSelectedEventType('all');
        break;
      default:
        console.log('Action:', action);
    }
  };

  const handleEdit = () => {
    if (selectedItems.length > 0) {
      setIsEditing(true);
      const itemId = selectedItems[0];
      navigate(`/hr/employees/lifecycle/${itemId}/edit`);
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
    const allData = employeeLifecycles.map(emp => ({
      'Employee Name': emp.employee_name,
      'Employee Number': emp.employee_number,
      'Employment Status': emp.employment_status,
      'Hire Date': emp.hire_date,
      'Confirmation Date': emp.confirmation_date || 'N/A',
      'Probation End Date': emp.probation_end_date || 'N/A',
      'Contract End Date': emp.contract_end_date || 'N/A',
      'Years of Service': emp.years_of_service,
      'Is Rehireable': emp.is_rehireable ? 'Yes' : 'No',
      'Exit Interview Completed': emp.exit_interview_completed ? 'Yes' : 'No',
      'Final Payroll Processed': emp.final_payroll_processed ? 'Yes' : 'No'
    }));
    
    if (allData.length > 0) {
      const csv = convertToCSV(allData);
      downloadCSV(csv, 'employee-lifecycle-export.csv');
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
      'Active': 'bg-green-100 text-green-800',
      'Probation': 'bg-yellow-100 text-yellow-800',
      'Notice Period': 'bg-orange-100 text-orange-800',
      'Terminated': 'bg-red-100 text-red-800',
      'Retired': 'bg-gray-100 text-gray-800',
      'Resigned': 'bg-purple-100 text-purple-800',
      'Contract Ended': 'bg-blue-100 text-blue-800'
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

  // Get event type badge styling
  const getEventTypeBadge = (eventType: string) => {
    const styles: Record<string, string> = {
      'Hire': 'bg-green-100 text-green-800',
      'Onboarding': 'bg-blue-100 text-blue-800',
      'Confirmation': 'bg-purple-100 text-purple-800',
      'Promotion': 'bg-indigo-100 text-indigo-800',
      'Transfer': 'bg-yellow-100 text-yellow-800',
      'Leave': 'bg-orange-100 text-orange-800',
      'Return from Leave': 'bg-teal-100 text-teal-800',
      'Suspension': 'bg-red-100 text-red-800',
      'Termination': 'bg-red-100 text-red-800',
      'Retirement': 'bg-gray-100 text-gray-800',
      'Resignation': 'bg-purple-100 text-purple-800',
      'Contract End': 'bg-blue-100 text-blue-800',
      'Death': 'bg-gray-100 text-gray-800'
    };
    return (
      <span className={`inline-flex items-center px-2.5 py-0.5 text-xs font-medium ${styles[eventType] || 'bg-gray-100 text-gray-800'}`}>
        {eventType}
      </span>
    );
  };

  // Filter data based on search and filters
  const filteredLifecycles = employeeLifecycles.filter(lifecycle => {
    const matchesSearch = lifecycle.employee_name.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         lifecycle.employee_number.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesStatus = selectedStatus === 'all' || lifecycle.employment_status === selectedStatus;
    return matchesSearch && matchesStatus;
  });

  const filteredEvents = lifecycleEvents.filter(event => {
    const matchesSearch = event.employee_name.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         event.employee_number.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         event.event_type.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesStatus = selectedEventType === 'all' || event.event_type === selectedEventType;
    return matchesSearch && matchesStatus;
  });

  // Check if we're in form mode
  const isFormMode = location.pathname.includes('/lifecycle/new');

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
          viewId="HRM_EMPLOYEE_LIFECYCLE"
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
                <Users className="w-6 h-6 text-blue-600" />
                <h1 className="text-lg font-bold text-gray-900">Employee Lifecycle</h1>
              </div>
              
              <div className="relative flex-1 max-w-md">
                <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-4 h-4" />
                <input
                  id="lifecycle-search"
                  type="text"
                  placeholder="Search employees..."
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
                <option value="Active">Active</option>
                <option value="Probation">Probation</option>
                <option value="Notice Period">Notice Period</option>
                <option value="Terminated">Terminated</option>
                <option value="Retired">Retired</option>
                <option value="Resigned">Resigned</option>
                <option value="Contract Ended">Contract Ended</option>
              </select>
              
              <div className="text-sm text-gray-600 font-medium">
                {summaryStats.totalEmployees} employees
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Scrollable Content */}
      <div className="flex-1 overflow-auto bg-gray-50">
        <div className="p-6">
          {activeTab === 'overview' && (
            <div className="space-y-6">
              {/* Summary Cards */}
              <h3 className="text-lg font-medium text-gray-900 mb-4">Lifecycle Overview</h3>
              
              <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                <div className="bg-white border border-gray-200 rounded-lg p-4">
                  <div className="flex items-center">
                    <div className="flex-shrink-0">
                      <Users className="h-6 w-6 text-blue-600" />
                    </div>
                    <div className="ml-3">
                      <p className="text-sm font-medium text-gray-900">Total Employees</p>
                      <p className="text-2xl font-semibold text-gray-900">{summaryStats.totalEmployees}</p>
                    </div>
                  </div>
                </div>
                
                <div className="bg-white border border-gray-200 rounded-lg p-4">
                  <div className="flex items-center">
                    <div className="flex-shrink-0">
                      <CheckCircle className="h-6 w-6 text-green-600" />
                    </div>
                    <div className="ml-3">
                      <p className="text-sm font-medium text-gray-900">Active Employees</p>
                      <p className="text-2xl font-semibold text-gray-900">{summaryStats.activeEmployees}</p>
                    </div>
                  </div>
                </div>
                
                <div className="bg-white border border-gray-200 rounded-lg p-4">
                  <div className="flex items-center">
                    <div className="flex-shrink-0">
                      <Clock className="h-6 w-6 text-yellow-600" />
                    </div>
                    <div className="ml-3">
                      <p className="text-sm font-medium text-gray-900">On Probation</p>
                      <p className="text-2xl font-semibold text-gray-900">{summaryStats.probationEmployees}</p>
                    </div>
                  </div>
                </div>
                
                <div className="bg-white border border-gray-200 rounded-lg p-4">
                  <div className="flex items-center">
                    <div className="flex-shrink-0">
                      <AlertCircle className="h-6 w-6 text-orange-600" />
                    </div>
                    <div className="ml-3">
                      <p className="text-sm font-medium text-gray-900">Notice Period</p>
                      <p className="text-2xl font-semibold text-gray-900">{summaryStats.noticePeriodEmployees}</p>
                    </div>
                  </div>
                </div>
              </div>

              {/* Employee Lifecycle Table */}
              <div className="space-y-4">
                <h3 className="text-lg font-medium text-gray-900 mb-4">Employee Lifecycle Management</h3>
                <div className="bg-white border border-gray-200 rounded-lg shadow-sm overflow-hidden">
                  <div className="overflow-x-auto">
                    <table className="min-w-full divide-y divide-gray-300">
                      <thead className="bg-gray-50">
                        <tr>
                          <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            Employee
                          </th>
                          <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            Status
                          </th>
                          <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            Hire Date
                          </th>
                          <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            Years of Service
                          </th>
                          <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            Contract End
                          </th>
                          <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            Actions
                          </th>
                        </tr>
                      </thead>
                      <tbody className="bg-white divide-y divide-gray-200">
                        {filteredLifecycles.map(lifecycle => (
                          <tr key={lifecycle.id}>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                              <div className="flex items-center space-x-2">
                                <div className="w-8 h-8 text-blue-600" />
                                <div>
                                  <div className="font-medium">{lifecycle.employee_name}</div>
                                  <div className="text-xs text-gray-500">{lifecycle.employee_number}</div>
                                </div>
                              </div>
                            </td>
                            <td className="px-6 py-4 whitespace-nowrap">
                              {getStatusBadge(lifecycle.employment_status)}
                            </td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                              {new Date(lifecycle.hire_date).toLocaleDateString()}
                            </td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                              {lifecycle.years_of_service} years
                            </td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                              {lifecycle.contract_end_date ? new Date(lifecycle.contract_end_date).toLocaleDateString() : 'N/A'}
                            </td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                              <div className="flex items-center space-x-2">
                                <button
                                  onClick={() => navigate(`/hr/employees/lifecycle/${lifecycle.id}`)}
                                  className="text-blue-600 hover:text-blue-900"
                                >
                                  <Eye className="w-4 h-4" />
                                </button>
                                <button
                                  onClick={() => {
                                    setSelectedItems([lifecycle.id]);
                                    handleEdit();
                                  }}
                                  className="text-gray-600 hover:text-gray-900"
                                >
                                  <Edit3 className="w-4 h-4" />
                                </button>
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
          )}
        </div>
      </div>
    </div>
  );
};

export default EmployeeLifecycle;
