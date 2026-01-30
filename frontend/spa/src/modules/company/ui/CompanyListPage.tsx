import React, { useCallback, useState } from 'react';
import { useCompanies } from '../hooks/useCompanies';
import CompanyTable from './CompanyTable';
import CompanyForm from './CompanyForm';
import CompanyFilters from './CompanyFilters';
import { Company, CompanyStatus, CompanyLegalEntityType } from '../types/company';

interface FilterState {
  status?: CompanyStatus | '';
  legal_entity_type?: CompanyLegalEntityType | '';
  search?: string;
}

const initialFilters: FilterState = {
  status: '',
  legal_entity_type: '',
  search: '',
};

export const CompanyListPage: React.FC = () => {
  const [filters, setFilters] = useState<FilterState>(initialFilters);
  const { data, loading, refresh } = useCompanies(filters);

  const [showForm, setShowForm] = useState(false);
  const [editData, setEditData] = useState<Company | undefined>(undefined);

  const handleEdit = (row: Company) => {
    setEditData(row);
    setShowForm(true);
  };
  const handleDeactivate = (row: Company) => {
    // Call API for status change; confirm at least one active remains
    // TODO: Implement backend logic for unique active rule
    // e.g., show toast or modal if needed
    setShowForm(false);
    refresh();
  };
  const handleNew = () => {
    setEditData(undefined);
    setShowForm(true);
  };
  const handleSave = async (formData: any) => {
    // Create or update depending on editData
    setShowForm(false);
    setEditData(undefined);
    refresh();
  };

  return (
    <div className="max-w-4xl mx-auto py-8">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-2xl font-bold">Companies</h2>
        <button className="bg-slate-900 text-white px-4 py-2 rounded" onClick={handleNew}>Add Company</button>
      </div>
      <CompanyFilters values={filters} onChange={setFilters} />
      <CompanyTable data={data} loading={loading} onEdit={handleEdit} onDeactivate={handleDeactivate} />
      {showForm && (
        <div className="fixed inset-0 bg-black bg-opacity-30 flex items-center justify-center z-40">
          <div className="bg-white rounded-lg p-6 w-full max-w-lg shadow-lg">
            <h3 className="font-semibold text-xl mb-2">{editData ? 'Edit Company' : 'Add Company'}</h3>
            <CompanyForm initialData={editData} onSave={handleSave} onCancel={() => setShowForm(false)} />
          </div>
        </div>
      )}
    </div>
  );
};

export default CompanyListPage;

