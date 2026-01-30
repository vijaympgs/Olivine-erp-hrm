import React, { useState, useEffect, useRef } from "react";
import { useNavigate } from "react-router-dom";
import {
  Building,
  Search,
} from "lucide-react";
import { companyService, CompanyListItem, CompanyFilters } from "@services/companyService";
import { MasterToolbar, MasterMode } from "@core/ui-canon/frontend/ui/components/MasterToolbarConfigDriven";
import { ConfirmationDialog } from "@core/ui-canon/frontend/ui/components/ConfirmationDialog";
import { CompanyForm, CompanyFormHandle } from "./CompanyForm";
import { CompanyList } from "./CompanyList";

export const CompanySettings: React.FC = () => {
  const navigate = useNavigate();
  const [companies, setCompanies] = useState<CompanyListItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [filters, setFilters] = useState<CompanyFilters>({});
  const [searchTerm, setSearchTerm] = useState('');

  // Pattern States
  const [showForm, setShowForm] = useState(false);
  const [editingId, setEditingId] = useState<string | null>(null);
  const [viewMode, setViewMode] = useState(false);
  const [selectedIds, setSelectedIds] = useState<string[]>([]);

  // Dialog States
  const [isExitDialogOpen, setIsExitDialogOpen] = useState(false);
  const [isDiscardDialogOpen, setIsDiscardDialogOpen] = useState(false);
  const [isDeleteDialogOpen, setIsDeleteDialogOpen] = useState(false);

  const formRef = useRef<CompanyFormHandle>(null);

  useEffect(() => {
    loadCompanies();
  }, [filters]);

  const loadCompanies = async () => {
    try {
      setLoading(true);
      const response = await companyService.getCompanies({
        ...filters,
        search: searchTerm || undefined
      });
      setCompanies(response?.results || []);
    } catch (err) {
      console.error('Error loading companies:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleToolbarAction = (action: string) => {
    switch (action) {
      case 'new':
        setEditingId(null);
        setViewMode(false);
        setShowForm(true);
        break;
      case 'edit':
        if (selectedIds.length === 1) {
          handleEdit(selectedIds[0]);
        }
        break;
      case 'view':
        if (selectedIds.length === 1) {
          handleRowClick(selectedIds[0]);
        }
        break;
      case 'refresh':
        if (!showForm) loadCompanies();
        break;
      case 'save':
        if (showForm && !viewMode) formRef.current?.submit();
        break;
      case 'cancel':
        if (showForm && !viewMode) {
          setIsDiscardDialogOpen(true);
        }
        break;
      case 'clear':
        if (showForm && !viewMode) {
          if (editingId) {
            formRef.current?.reset();
          } else {
            formRef.current?.reset();
          }
        }
        break;
      case 'exit':
        if (showForm && !viewMode) {
          setIsExitDialogOpen(true);
        } else if (showForm && viewMode) {
          handleFormCancel();
        } else {
          navigate('/dashboard');
        }
        break;
      case 'delete':
        if (!showForm && selectedIds.length > 0) {
          setIsDeleteDialogOpen(true);
        }
        break;
      case 'search':
        document.getElementById('company-search')?.focus();
        break;
    }
  };

  const getToolbarMode = (): MasterMode => {
    if (!showForm) return 'VIEW';
    if (viewMode) return 'VIEW_FORM';
    return editingId ? 'EDIT' : 'CREATE';
  };

  const handleEdit = (id: string) => {
    setEditingId(id);
    setViewMode(false);
    setShowForm(true);
  };

  const handleRowClick = (id: string) => {
    setEditingId(id);
    setViewMode(true);
    setShowForm(true);
  };

  const handleFormSuccess = () => {
    setShowForm(false);
    setEditingId(null);
    setViewMode(false);
    loadCompanies();
  };

  const handleFormCancel = () => {
    setShowForm(false);
    setEditingId(null);
    setViewMode(false);
  };

  const handleDeleteConfirm = async () => {
    try {
      await Promise.all(selectedIds.map(id => companyService.deactivateCompany(id)));
      setSelectedIds([]);
      loadCompanies();
    } catch (err) {
      console.error("Delete failed", err);
      alert("Failed to deactive companies");
    } finally {
      setIsDeleteDialogOpen(false);
    }
  };

  const handleSelectAll = (checked: boolean) => {
    if (checked) setSelectedIds(companies.map(c => c.id));
    else setSelectedIds([]);
  };

  const handleSelectRow = (id: string, checked: boolean) => {
    if (checked) setSelectedIds(prev => [...prev, id]);
    else setSelectedIds(prev => prev.filter(x => x !== id));
  };

  const statusOptions = [
    { value: 'ACTIVE', label: 'Active' },
    { value: 'INACTIVE', label: 'Inactive' },
  ];

  return (
    <div className="flex flex-col h-full bg-slate-50">
      <MasterToolbar
        viewId="COMPANY"
        mode={getToolbarMode()}
        onAction={handleToolbarAction}
        hasSelection={selectedIds.length > 0}
      />

      {/* Persistent Header */}
      <div className="bg-white border-b border-gray-200 px-6 py-4 flex-shrink-0">
        <div className="flex items-center gap-3">
          <div className="p-2 bg-blue-50 rounded-lg">
            <Building className="w-5 h-5 text-blue-600" />
          </div>
          <div>
            <h1 className="text-xl font-bold text-gray-900">Company Settings</h1>
            <p className="text-sm text-gray-500">Manage company details, legal entities, and preferences</p>
          </div>
        </div>
      </div>

      <div className="flex-1 overflow-hidden p-4">
        {showForm ? (
          <CompanyForm
            ref={formRef}
            companyId={editingId}
            readOnly={viewMode}
            onSuccess={handleFormSuccess}
            onCancel={handleFormCancel}
          />
        ) : (
          <div className="h-full flex flex-col space-y-4">
            {/* Filters Bar */}
            <div className="bg-white p-4 shadow-sm border border-gray-200 rounded-lg flex-shrink-0">
              <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                <div className="md:col-span-2 relative">
                  <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-4 h-4" />
                  <input
                    id="company-search"
                    type="text"
                    placeholder="Search companies..."
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                    onKeyPress={(e) => e.key === 'Enter' && loadCompanies()}
                    className="pl-10 pr-4 py-2 w-full border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500 text-sm"
                  />
                </div>
                <div>
                  <select
                    value={filters.status || ''}
                    onChange={(e) => setFilters({ ...filters, status: e.target.value || undefined })}
                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500 text-sm"
                  >
                    <option value="">All Status</option>
                    {statusOptions.map(o => <option key={o.value} value={o.value}>{o.label}</option>)}
                  </select>
                </div>
              </div>
            </div>

            {/* Table */}
            <CompanyList
              companies={companies}
              selectedIds={selectedIds}
              onSelectRow={handleSelectRow}
              onSelectAll={handleSelectAll}
              onRowClick={handleRowClick}
              loading={loading}
            />
          </div>
        )}
      </div>

      {/* Dialogs */}
      <ConfirmationDialog
        isOpen={isExitDialogOpen}
        title="Exit Company Settings?"
        message="You have unsaved changes. Are you sure you want to exit? All changes will be lost."
        confirmLabel="Exit & Discard"
        cancelLabel="Stay"
        onConfirm={() => { setIsExitDialogOpen(false); handleFormCancel(); }}
        onCancel={() => setIsExitDialogOpen(false)}
        intent="danger"
      />

      <ConfirmationDialog
        isOpen={isDiscardDialogOpen}
        title="Discard Changes?"
        message="Are you sure you want to discard your changes?"
        confirmLabel="Discard"
        cancelLabel="Keep Editing"
        onConfirm={() => { setIsDiscardDialogOpen(false); handleFormCancel(); }}
        onCancel={() => setIsDiscardDialogOpen(false)}
        intent="danger"
      />

      <ConfirmationDialog
        isOpen={isDeleteDialogOpen}
        title={`Deactivate ${selectedIds.length} Company(s)?`}
        message={`Are you sure you want to deactivate ${selectedIds.length} company(s)? This action cannot be undone easily.`}
        confirmLabel="Deactivate"
        cancelLabel="Cancel"
        onConfirm={handleDeleteConfirm}
        onCancel={() => setIsDeleteDialogOpen(false)}
        intent="danger"
      />
    </div>
  );
};


export default CompanySettings;


