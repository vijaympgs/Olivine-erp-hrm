import React, { useEffect, useState } from "react";
import { Plus, Search, Edit3, Users } from "lucide-react";
import { companyService, CompanyListItem } from "@services/companyService";
import { customerService, CustomerFilters, CustomerListItem } from "@services/customerService";
import { CustomerModal } from "@core/ui-canon/frontend/components/CustomerModal";
import { MasterToolbar, MasterMode } from "@core/ui-canon/frontend/ui/components/MasterToolbarConfigDriven";

export const CustomerSetup: React.FC = () => {
  const [companies, setCompanies] = useState<CompanyListItem[]>([]);
  const [customers, setCustomers] = useState<CustomerListItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const [filters, setFilters] = useState<CustomerFilters>({});
  const [searchTerm, setSearchTerm] = useState('');

  const [showModal, setShowModal] = useState(false);
  const [editingId, setEditingId] = useState<string | null>(null);
  const [selectedCustomerId, setSelectedCustomerId] = useState<string | null>(null);
  const [toolbarMode, setToolbarMode] = useState<MasterMode>('VIEW');

  useEffect(() => {
    (async () => {
      try {
        const activeCompanies = await companyService.getActiveCompanies();
        setCompanies(activeCompanies);
        if (activeCompanies.length > 0) {
          setFilters(prev => ({ ...prev, company_id: prev.company_id || activeCompanies[0].id }));
        }
      } catch {
        setError('Failed to load companies');
      }
    })();
  }, []);

  useEffect(() => {
    loadCustomers();
  }, [filters]);

  const loadCustomers = async () => {
    try {
      setLoading(true);
      const resp = await customerService.getCustomers({
        ...filters,
        search: searchTerm || undefined,
      });
      setCustomers(resp?.results || []);
      setError(null);
    } catch (err) {
      setError('Failed to load customers');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = () => {
    setFilters({ ...filters, search: searchTerm || undefined });
  };

  const handleFilterChange = (key: keyof CustomerFilters, value: any) => {
    setFilters({ ...filters, [key]: value || undefined });
  };

  const handleCreate = () => {
    setEditingId(null);
    setShowModal(true);
  };

  const handleEdit = (id: string) => {
    setEditingId(id);
    setShowModal(true);
  };

  const handleModalClose = (shouldRefresh?: boolean) => {
    setShowModal(false);
    setEditingId(null);
    if (shouldRefresh) loadCustomers();
  };

  const getStatusBadge = (status: string) => {
    const colors: Record<string, string> = {
      ACTIVE: 'bg-green-100 text-green-800',
      INACTIVE: 'bg-gray-100 text-gray-800',
      BLACKLISTED: 'bg-red-100 text-red-800',
    };
    return (
      <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${colors[status] || 'bg-gray-100 text-gray-800'}`}>
        {status}
      </span>
    );
  };

  const getTypeBadge = (type: string) => {
    const colors: Record<string, string> = {
      INDIVIDUAL: 'bg-blue-100 text-blue-800',
      BUSINESS: 'bg-purple-100 text-purple-800',
    };
    return (
      <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${colors[type] || 'bg-gray-100 text-gray-800'}`}>
        {type}
      </span>
    );
  };

  const handleToolbarAction = (action: string) => {
    switch (action) {
      case 'new':
        handleCreate();
        break;
      case 'save':
        // Save is handled within the modal
        break;
      case 'delete':
        if (selectedCustomerId) {
          if (confirm('Delete selected customer?')) {
            console.log('Delete customer:', selectedCustomerId);
          }
        }
        break;
      case 'refresh':
        loadCustomers();
        break;
      case 'clear':
        setSearchTerm('');
        setFilters({});
        setSelectedCustomerId(null);
        break;
      case 'export':
        console.log('Export Customers');
        break;
      case 'import':
        console.log('Import Customers');
        break;
      case 'search':
        document.querySelector<HTMLInputElement>('input[type="text"]')?.focus();
        break;
      case 'filter':
        break;
      case 'report':
        console.log('Generate Customer Report');
        break;
    }
  };

  if (loading && customers.length === 0) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-purple-600"></div>
      </div>
    );
  }

  return (
    <>
      <MasterToolbar
        viewId="CUSTOMER_MASTER"
        mode={toolbarMode}
        onAction={handleToolbarAction}
        hasSelection={!!selectedCustomerId}
        showLabels={false}
      />
      <div className="page-container space-y-6">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <Users className="w-8 h-8 text-purple-600" />
            <div>
              <h1 className="erp-page-title">Customers</h1>
              <p className="erp-page-subtitle">Manage customer master data</p>
            </div>
          </div>
        </div>

        <div className="bg-white p-4 shadow-sm border border-gray-200">
          <div className="grid grid-cols-1 md:grid-cols-5 gap-4">
            <div className="md:col-span-2">
              <div className="relative">
                <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-4 h-4" />
                <input
                  type="text"
                  placeholder="Search by code, name, phone, email..."
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  onKeyDown={(e) => e.key === 'Enter' && handleSearch()}
                  className="pl-10 pr-4 py-2 w-full border border-gray-300 focus:ring-purple-500 focus:border-purple-500"
                />
              </div>
            </div>

            <div>
              <select
                value={filters.company_id || ''}
                onChange={(e) => handleFilterChange('company_id', e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 focus:ring-purple-500 focus:border-purple-500"
              >
                {companies.map(c => (
                  <option key={c.id} value={c.id}>{c.company_name}</option>
                ))}
              </select>
            </div>

            <div>
              <select
                value={filters.customer_type || ''}
                onChange={(e) => handleFilterChange('customer_type', e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 focus:ring-purple-500 focus:border-purple-500"
              >
                <option value="">All Types</option>
                <option value="INDIVIDUAL">Individual</option>
                <option value="BUSINESS">Business</option>
              </select>
            </div>

            <div>
              <select
                value={filters.status || ''}
                onChange={(e) => handleFilterChange('status', e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 focus:ring-purple-500 focus:border-purple-500"
              >
                <option value="">Active Only</option>
                <option value="ACTIVE">Active</option>
                <option value="INACTIVE">Inactive</option>
                <option value="BLACKLISTED">Blacklisted</option>
              </select>
            </div>
          </div>
        </div>

        {error && (
          <div className="bg-red-50 border border-red-200 rounded-md p-4">
            <div className="text-sm text-red-600">{error}</div>
          </div>
        )}

        <div className="bg-white shadow-lg border border-gray-200 overflow-hidden">
          <div className="overflow-x-auto">
            <table className="min-w-full divide-y divide-gray-200">
              <thead className="bg-gradient-to-r from-gray-50 to-gray-100">
                <tr>
                  <th className="px-6 py-4 text-left erp-table-header text-gray-600">Company</th>
                  <th className="px-6 py-4 text-left erp-table-header text-gray-600">Code</th>
                  <th className="px-6 py-4 text-left erp-table-header text-gray-600">Name</th>
                  <th className="px-6 py-4 text-left erp-table-header text-gray-600">Type</th>
                  <th className="px-6 py-4 text-left erp-table-header text-gray-600">Phone</th>
                  <th className="px-6 py-4 text-left erp-table-header text-gray-600">Email</th>
                  <th className="px-6 py-4 text-left erp-table-header text-gray-600">Status</th>
                  <th className="px-6 py-4 text-right erp-table-header text-gray-600">Actions</th>
                </tr>
              </thead>
              <tbody className="bg-white divide-y divide-gray-200">
                {customers.map(customer => (
                  <tr
                    key={customer.id}
                    className={`transition-colors duration-200 cursor-pointer ${selectedCustomerId === customer.id
                      ? 'bg-purple-100'
                      : 'hover:bg-purple-50'
                      }`}
                    onClick={() => setSelectedCustomerId(customer.id)}
                  >
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{customer.company_name || customer.company}</td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm font-mono text-gray-900">{customer.customer_code}</td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{customer.customer_name}</td>
                    <td className="px-6 py-4 whitespace-nowrap">{getTypeBadge(customer.customer_type)}</td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{customer.phone || '-'}</td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{customer.email || '-'}</td>
                    <td className="px-6 py-4 whitespace-nowrap">{getStatusBadge(customer.status)}</td>
                    <td className="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                      <div className="flex items-center justify-end space-x-2">
                        <button
                          onClick={() => handleEdit(customer.id)}
                          className="text-purple-600 hover:text-purple-900 p-1 rounded"
                          title="Edit"
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

        {showModal && (
          <CustomerModal customerId={editingId} onClose={handleModalClose} />
        )}
      </div>
    </>
  );
};





