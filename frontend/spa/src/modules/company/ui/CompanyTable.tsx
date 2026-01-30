import React from 'react';
import { Company } from '../types/company';

interface CompanyTableProps {
  data: Company[];
  loading?: boolean;
  onEdit?: (row: Company) => void;
  onDeactivate?: (row: Company) => void;
}

export const CompanyTable: React.FC<CompanyTableProps> = ({ data, loading, onEdit, onDeactivate }) => (
  <div className="overflow-x-auto">
    <table className="min-w-full text-sm border">
      <thead className="bg-slate-100">
        <tr>
          <th className="px-4 py-2">Name</th>
          <th className="px-4 py-2">Code</th>
          <th className="px-4 py-2">Legal Entity Type</th>
          <th className="px-4 py-2">Currency</th>
          <th className="px-4 py-2">Status</th>
          <th className="px-4 py-2">Actions</th>
        </tr>
      </thead>
      <tbody>
        {loading ? (
          <tr><td colSpan={6} className="p-4 text-center">Loading…</td></tr>
        ) : data.length === 0 ? (
          <tr><td colSpan={6} className="p-4 text-center">No companies found</td></tr>
        ) : data.map(row => (
          <tr key={row.id} className="border-t">
            <td className="px-4 py-2 font-medium">{row.company_name}</td>
            <td className="px-4 py-2">{row.company_code}</td>
            <td className="px-4 py-2">{row.legal_entity_type}</td>
            <td className="px-4 py-2">{row.default_currency}</td>
            <td className="px-4 py-2">
              <span className={`inline-block px-2 py-1 rounded text-xs font-semibold ${row.status === 'Active' ? 'bg-green-100 text-green-800' : 'bg-slate-200 text-slate-700'}`}>{row.status}</span>
            </td>
            <td className="px-4 py-2 space-x-2">
              <button className="text-blue-700 underline" onClick={() => onEdit?.(row)}>Edit</button>
              {row.status === 'Active' && (
                <button className="text-red-700 underline" onClick={() => onDeactivate?.(row)}>
                  Deactivate
                </button>
              )}
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  </div>
);

export default CompanyTable;

