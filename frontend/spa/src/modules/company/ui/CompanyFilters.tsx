import React from 'react';
import { CompanyLegalEntityType, CompanyStatus } from '../types/company';

interface CompanyFiltersProps {
  values: {
    status?: CompanyStatus | '';
    legal_entity_type?: CompanyLegalEntityType | '';
    search?: string;
  };
  onChange: (values: any) => void;
}

const legalEntityOptions: CompanyLegalEntityType[] = [
  'Sole Proprietor', 'Partnership', 'LLP', 'Pvt Ltd', 'Franchise',
];
const statusOptions: CompanyStatus[] = ['Active', 'Inactive'];

export const CompanyFilters: React.FC<CompanyFiltersProps> = ({ values, onChange }) => (
  <div className="flex gap-4 mb-4 flex-wrap">
    <input
      type="text"
      className="input"
      placeholder="Search by name/code"
      value={values.search || ''}
      onChange={e => onChange({ ...values, search: e.target.value })}
    />
    <select
      className="input"
      value={values.status || ''}
      onChange={e => onChange({ ...values, status: e.target.value as CompanyStatus })}
    >
      <option value="">All Status</option>
      {statusOptions.map(status => <option key={status} value={status}>{status}</option>)}
    </select>
    <select
      className="input"
      value={values.legal_entity_type || ''}
      onChange={e => onChange({ ...values, legal_entity_type: e.target.value as CompanyLegalEntityType })}
    >
      <option value="">All Entity Types</option>
      {legalEntityOptions.map(typ => <option key={typ} value={typ}>{typ}</option>)}
    </select>
  </div>
);

export default CompanyFilters;

