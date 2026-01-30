import React, { useEffect, useState, useRef } from "react";
import { useNavigate } from "react-router-dom";
import { Search, MapPin } from "lucide-react";
import { companyService, CompanyListItem } from "@services/companyService";
import { locationService, LocationFilters, LocationListItem } from "@services/locationService";
import { MasterToolbar, MasterMode } from "@core/ui-canon/frontend/ui/components/MasterToolbarConfigDriven";
import { ConfirmationDialog } from "@core/ui-canon/frontend/ui/components/ConfirmationDialog";
import { LocationForm, LocationFormHandle } from "./LocationForm";
import { LocationList } from "./LocationList";

export const LocationSetup: React.FC = () => {
  const navigate = useNavigate();
  const [companies, setCompanies] = useState<CompanyListItem[]>([]);
  const [locations, setLocations] = useState<LocationListItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [filters, setFilters] = useState<LocationFilters>({});
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

  const formRef = useRef<LocationFormHandle>(null);

  useEffect(() => {
    (async () => {
      try {
        const activeCompanies = await companyService.getActiveCompanies();
        setCompanies(activeCompanies);
        if (activeCompanies.length > 0) {
          setFilters(prev => ({ ...prev, company_id: prev.company_id || activeCompanies[0].id }));
        }
      } catch (e) {
        console.error('Failed to load companies');
      }
    })();
  }, []);

  useEffect(() => {
    if (!showForm) loadLocations();
  }, [filters, showForm, searchTerm]);

  const loadLocations = async () => {
    try {
      setLoading(true);
      const response = await locationService.getLocations({
        ...filters,
        search: searchTerm || undefined,
      });
      setLocations(response?.results || []);
    } catch (err) {
      console.error('Error loading locations:', err);
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
          handleView(selectedIds[0]);
        }
        break;
      case 'refresh':
        if (!showForm) loadLocations();
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
          formRef.current?.reset();
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
        document.getElementById('loc-search')?.focus();
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

  const handleView = (id: string) => {
    setEditingId(id);
    setViewMode(true);
    setShowForm(true);
  };

  const handleFormSuccess = () => {
    setShowForm(false);
    setEditingId(null);
    setViewMode(false);
    loadLocations();
  };

  const handleFormCancel = () => {
    setShowForm(false);
    setEditingId(null);
    setViewMode(false);
  };

  const handleDeleteConfirm = async () => {
    try {
      await Promise.all(selectedIds.map(id => locationService.deleteLocation(id)));
      setSelectedIds([]);
      loadLocations();
    } catch (err) {
      console.error("Delete failed", err);
      alert("Failed to deactive locations");
    } finally {
      setIsDeleteDialogOpen(false);
    }
  };

  const handleSelectAll = (checked: boolean) => {
    if (checked) setSelectedIds(locations.map(x => x.id));
    else setSelectedIds([]);
  };

  const handleSelectRow = (id: string, checked: boolean) => {
    if (checked) setSelectedIds(prev => [...prev, id]);
    else setSelectedIds(prev => prev.filter(x => x !== id));
  };

  return (
    <div className="flex flex-col h-full bg-slate-50">
      <MasterToolbar
        viewId="LOCATIONS_SETUP"
        mode={getToolbarMode()}
        onAction={handleToolbarAction}
        hasSelection={selectedIds.length > 0}
      />

      {/* Persistent Header */}
      <div className="bg-white border-b border-gray-200 px-6 py-4 flex-shrink-0">
        <div className="flex items-center gap-3">
          <div className="p-2 bg-blue-50 rounded-none">
            <MapPin className="w-5 h-5 text-blue-600" />
          </div>
          <div>
            <h1 className="text-xl font-bold text-gray-900">Location Setup</h1>
            <p className="text-sm text-gray-500">Manage stores, warehouses, offices and distribution centers</p>
          </div>
        </div>
      </div>

      <div className="flex-1 overflow-hidden p-4">
        {showForm ? (
          <LocationForm
            ref={formRef}
            locationId={editingId}
            readOnly={viewMode}
            onSuccess={handleFormSuccess}
            onCancel={handleFormCancel}
          />
        ) : (
          <div className="h-full flex flex-col space-y-4">
            {/* Filters */}
            <div className="bg-white p-4 shadow-sm border border-gray-200 rounded-none flex-shrink-0">
              <div className="grid grid-cols-1 md:grid-cols-6 gap-4">
                <div className="md:col-span-2 relative">
                  <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-4 h-4" />
                  <input
                    id="loc-search"
                    type="text"
                    placeholder="Search locations..."
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                    onKeyDown={(e) => e.key === 'Enter' && loadLocations()}
                    className="pl-10 pr-4 py-2 w-full border border-gray-300 rounded-none focus:ring-blue-500 focus:border-blue-500 text-sm"
                  />
                </div>
                <div>
                  <select
                    value={filters.company_id || ''}
                    onChange={(e) => setFilters({ ...filters, company_id: e.target.value })}
                    className="w-full px-3 py-2 border border-gray-300 rounded-none focus:ring-blue-500 focus:border-blue-500 text-sm"
                  >
                    {companies.map(c => <option key={c.id} value={c.id}>{c.company_name}</option>)}
                  </select>
                </div>
                <div>
                  <select
                    value={filters.location_type || ''}
                    onChange={(e) => setFilters({ ...filters, location_type: e.target.value as any })}
                    className="w-full px-3 py-2 border border-gray-300 rounded-none focus:ring-blue-500 focus:border-blue-500 text-sm"
                  >
                    <option value="">All Types</option>
                    <option value="STORE">Store</option>
                    <option value="WAREHOUSE">Warehouse</option>
                    <option value="OFFICE">Office</option>
                    <option value="OTHER">Other</option>
                  </select>
                </div>
                <div>
                  <select
                    value={filters.include_inactive ? 'ALL' : filters.is_active === 'false' ? 'INACTIVE' : 'ACTIVE'}
                    onChange={(e) => {
                      const val = e.target.value;
                      if (val === 'ALL') setFilters({ ...filters, include_inactive: true, is_active: undefined });
                      else setFilters({ ...filters, include_inactive: undefined, is_active: val === 'ACTIVE' ? 'true' : 'false' });
                    }}
                    className="w-full px-3 py-2 border border-gray-300 rounded-none focus:ring-blue-500 focus:border-blue-500 text-sm"
                  >
                    <option value="ACTIVE">Active Only</option>
                    <option value="INACTIVE">Inactive Only</option>
                    <option value="ALL">All</option>
                  </select>
                </div>
              </div>
            </div>

            {/* Table */}
            <LocationList
              locations={locations}
              selectedIds={selectedIds}
              onSelectRow={handleSelectRow}
              onSelectAll={handleSelectAll}
              onEdit={handleView}
              loading={loading}
            />
          </div>
        )}
      </div>

      {/* Dialogs */}
      <ConfirmationDialog
        isOpen={isExitDialogOpen}
        title="Exit Location Setup?"
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
        title={`Deactivate ${selectedIds.length} Location(s)?`}
        message={`Are you sure you want to deactivate ${selectedIds.length} location(s)? This action cannot be undone easily.`}
        confirmLabel="Deactivate"
        cancelLabel="Cancel"
        onConfirm={handleDeleteConfirm}
        onCancel={() => setIsDeleteDialogOpen(false)}
        intent="danger"
      />
    </div>
  );
};



