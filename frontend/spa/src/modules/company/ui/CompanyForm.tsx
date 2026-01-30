import React, { useCallback, useMemo, useState } from 'react';
import { Company, CompanyLegalEntityType, CompanyStatus } from '../types/company';

interface CompanyFormProps {
  initialData?: Partial<Company>;
  onSave: (data: Partial<Company>) => void;
  onCancel: () => void;
}

const legalEntityTypeOptions: CompanyLegalEntityType[] = [
  'Sole Proprietor',
  'Partnership',
  'LLP',
  'Pvt Ltd',
  'Franchise',
];

const statusOptions: CompanyStatus[] = ['Active', 'Inactive'];

export const CompanyForm: React.FC<CompanyFormProps> = ({ initialData = {}, onSave, onCancel }) => {
  const [formData, setFormData] = useState<Partial<Company>>({
    status: 'Active',
    default_currency: 'INR',
    timezone: 'Asia/Kolkata',
    ...initialData,
  });
  const [errors, setErrors] = useState<Record<string, string>>({});

  // Auto-generate code from name (slug)
  const autoGenCode = useMemo(() => {
    const str = (formData.company_name || '').replace(/[^a-zA-Z0-9]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 20);
    return str.toUpperCase();
  }, [formData.company_name]);

  const validate = useCallback(() => {
    const e: Record<string, string> = {};
    if (!formData.company_name) e.company_name = 'Company Name is required';
    if (!formData.company_code) e.company_code = 'Company Code is required';
    if (!formData.legal_entity_type) e.legal_entity_type = 'Legal Entity Type is required';
    if (!formData.default_currency) e.default_currency = 'Currency required';
    if (!formData.timezone) e.timezone = 'Timezone required';
    if (!formData.status) e.status = 'Status required';
    return e;
  }, [formData]);

  const handleInput = (field: keyof Company, value: any) => {
    setFormData(f => ({ ...f, [field]: value }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const validation = validate();
    setErrors(validation);
    if (Object.keys(validation).length === 0) {
      onSave(formData);
    }
  };

  return (
    <form className="space-y-4" onSubmit={handleSubmit}>
      {/* Basic Info */}
      <div>
        <label className="block font-medium">Company Name *</label>
        <input type="text" value={formData.company_name || ''} onChange={e => handleInput('company_name', e.target.value)} className="input" />
        {errors.company_name && <div className="text-red-600 text-sm">{errors.company_name}</div>}
      </div>
      <div>
        <label className="block font-medium">Company Code *</label>
        <input type="text" maxLength={20} value={formData.company_code || autoGenCode} onChange={e => handleInput('company_code', e.target.value.toUpperCase())} className="input" />
        {errors.company_code && <div className="text-red-600 text-sm">{errors.company_code}</div>}
        <div className="text-xs text-slate-500">Auto-generated from company name, editable</div>
      </div>
      <div>
        <label className="block font-medium">Legal Entity Type *</label>
        <select value={formData.legal_entity_type || ''} onChange={e => handleInput('legal_entity_type', e.target.value)} className="input">
          <option value="">Select...</option>
          {legalEntityTypeOptions.map(val => (
            <option key={val} value={val}>{val}</option>
          ))}
        </select>
        {errors.legal_entity_type && <div className="text-red-600 text-sm">{errors.legal_entity_type}</div>}
      </div>
      {/* Business Setup */}
      <div>
        <label className="block font-medium">Default Currency *</label>
        <input type="text" value={formData.default_currency || ''} onChange={e => handleInput('default_currency', e.target.value.toUpperCase())} maxLength={10} className="input" />
        {errors.default_currency && <div className="text-red-600 text-sm">{errors.default_currency}</div>}
      </div>
      <div>
        <label className="block font-medium">Timezone *</label>
        <input type="text" value={formData.timezone || ''} onChange={e => handleInput('timezone', e.target.value)} className="input" />
        {errors.timezone && <div className="text-red-600 text-sm">{errors.timezone}</div>}
      </div>
      {/* Address (JSON, optional) */}
      <div>
        <label className="block font-medium">Address (JSON)</label>
        <textarea value={formData.address ? JSON.stringify(formData.address, null, 2) : ''} onChange={e => {
          try {
            handleInput('address', JSON.parse(e.target.value));
            setErrors(er => ({ ...er, address: undefined }));
          } catch {
            handleInput('address', e.target.value);
            setErrors(er => ({ ...er, address: 'Invalid JSON' }));
          }
        }} className="input" rows={3} />
        {typeof formData.address === 'string' && (
          <div className="text-red-600 text-xs">Invalid JSON</div>
        )}
      </div>
      {/* Status */}
      <div>
        <label className="block font-medium">Status *</label>
        <select value={formData.status || ''} onChange={e => handleInput('status', e.target.value)} className="input">
          <option value="">Select...</option>
          {statusOptions.map(val => (
            <option key={val} value={val}>{val}</option>
          ))}
        </select>
        {errors.status && <div className="text-red-600 text-sm">{errors.status}</div>}
      </div>
      {/* Actions */}
      <div className="flex gap-3 justify-end mt-4">
        <button type="button" onClick={onCancel} className="px-4 py-2 bg-slate-200 rounded">Cancel</button>
        <button type="submit" className="px-4 py-2 bg-slate-900 text-white rounded">Save</button>
      </div>
    </form>
  );
};

export default CompanyForm;

