import React from 'react';
import { CompanyListItem } from "@services/companyService";
import { Building, Globe } from "lucide-react";

interface CompanyListProps {
    companies: CompanyListItem[];
    selectedIds: string[];
    onSelectRow: (id: string, checked: boolean) => void;
    onSelectAll: (checked: boolean) => void;
    onRowClick: (id: string) => void;
    loading: boolean;
}

export const CompanyList: React.FC<CompanyListProps> = ({
    companies,
    selectedIds,
    onSelectRow,
    onSelectAll,
    onRowClick,
    loading
}) => {
    const getStatusBadge = (status: string) => {
        const isActive = status === "ACTIVE";
        return (
            <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${isActive
                ? 'bg-green-100 text-green-800'
                : 'bg-red-100 text-red-800'
                }`}>
                {isActive ? 'Active' : 'Inactive'}
            </span>
        );
    };

    return (
        <div className="flex-1 bg-white shadow-sm border border-gray-200 rounded-lg overflow-hidden">
            <div className="h-full overflow-auto">
                <table className="min-w-full divide-y divide-gray-200">
                    <thead className="bg-gray-50 sticky top-0 z-10">
                        <tr>
                            <th className="px-4 py-3 text-left w-12">
                                <input
                                    type="checkbox"
                                    checked={companies.length > 0 && selectedIds.length === companies.length}
                                    onChange={(e) => onSelectAll(e.target.checked)}
                                    className="rounded border-gray-300 text-blue-600 focus:ring-blue-500"
                                />
                            </th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Company</th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Code</th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Legal Entity</th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Currency</th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
                        </tr>
                    </thead>
                    <tbody className="bg-white divide-y divide-gray-200">
                        {loading ? (
                            <tr><td colSpan={6} className="text-center py-4 text-gray-500">Loading...</td></tr>
                        ) : companies.length === 0 ? (
                            <tr><td colSpan={6} className="text-center py-8 text-gray-500">No companies found.</td></tr>
                        ) : (
                            companies.map((company) => (
                                <tr
                                    key={company.id}
                                    onClick={() => onRowClick(company.id)}
                                    className={`hover:bg-blue-50 cursor-pointer transition-colors ${selectedIds.includes(company.id) ? 'bg-blue-50' : ''}`}
                                >
                                    <td className="px-4 py-4 whitespace-nowrap" onClick={(e) => e.stopPropagation()}>
                                        <input
                                            type="checkbox"
                                            checked={selectedIds.includes(company.id)}
                                            onChange={(e) => onSelectRow(company.id, e.target.checked)}
                                            className="rounded border-gray-300 text-blue-600 focus:ring-blue-500"
                                        />
                                    </td>
                                    <td className="px-6 py-4 whitespace-nowrap">
                                        <div className="flex items-center">
                                            <Building className="w-5 h-5 text-gray-400 mr-3" />
                                            <div className="text-sm font-medium text-gray-900">{company.company_name}</div>
                                        </div>
                                    </td>
                                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500 font-mono">{company.company_code}</td>
                                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{company.legal_entity_type}</td>
                                    <td className="px-6 py-4 whitespace-nowrap">
                                        <div className="flex items-center text-sm text-gray-900">
                                            <Globe className="w-4 h-4 mr-2 text-gray-400" />
                                            {company.default_currency}
                                        </div>
                                    </td>
                                    <td className="px-6 py-4 whitespace-nowrap">
                                        {getStatusBadge(company.status)}
                                    </td>
                                </tr>
                            ))
                        )}
                    </tbody>
                </table>
            </div>
        </div>
    );
};

