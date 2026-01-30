import React from 'react';
import { LocationListItem } from "@services/locationService";
import { Edit3 } from "lucide-react";

interface LocationListProps {
    locations: LocationListItem[];
    selectedIds: string[];
    onSelectRow: (id: string, checked: boolean) => void;
    onSelectAll: (checked: boolean) => void;
    onEdit: (id: string) => void;
    loading: boolean;
}

export const LocationList: React.FC<LocationListProps> = ({
    locations,
    selectedIds,
    onSelectRow,
    onSelectAll,
    onEdit,
    loading
}) => {
    const getActiveBadge = (isActive: boolean) => (
        <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${isActive ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}`}>
            {isActive ? 'Active' : 'Inactive'}
        </span>
    );

    return (
        <div className="flex-1 bg-white shadow-sm border border-gray-200 rounded-lg overflow-hidden">
            <div className="h-full overflow-auto">
                <table className="min-w-full divide-y divide-gray-200">
                    <thead className="bg-gray-50 sticky top-0 z-10">
                        <tr>
                            <th className="px-4 py-3 text-left w-12">
                                <input
                                    type="checkbox"
                                    checked={locations.length > 0 && selectedIds.length === locations.length}
                                    onChange={(e) => onSelectAll(e.target.checked)}
                                    className="rounded border-gray-300 text-blue-600 focus:ring-blue-500"
                                />
                            </th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Company</th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Code</th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Type</th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">POS</th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">City</th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
                            <th className="px-4 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">Action</th>
                        </tr>
                    </thead>
                    <tbody className="bg-white divide-y divide-gray-200">
                        {loading ? (
                            <tr><td colSpan={9} className="text-center py-4 text-gray-500">Loading...</td></tr>
                        ) : locations.length === 0 ? (
                            <tr><td colSpan={9} className="text-center py-8 text-gray-500">No locations found.</td></tr>
                        ) : (
                            locations.map(loc => (
                                <tr
                                    key={loc.id}
                                    onClick={() => onEdit(loc.id)}
                                    className={`hover:bg-blue-50 cursor-pointer transition-colors ${selectedIds.includes(loc.id) ? 'bg-blue-50' : ''}`}
                                >
                                    <td className="px-4 py-4 whitespace-nowrap" onClick={(e) => e.stopPropagation()}>
                                        <input
                                            type="checkbox"
                                            checked={selectedIds.includes(loc.id)}
                                            onChange={(e) => onSelectRow(loc.id, e.target.checked)}
                                            className="rounded border-gray-300 text-blue-600 focus:ring-blue-500"
                                        />
                                    </td>
                                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{loc.company_name || loc.company}</td>
                                    <td className="px-6 py-4 whitespace-nowrap text-sm font-mono text-gray-900">{loc.location_code}</td>
                                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                                        <div className="flex items-center gap-2">
                                            <span className="font-medium">{loc.name}</span>
                                            {loc.is_dc && <span className="px-2 py-0.5 rounded-full text-[10px] bg-amber-100 text-amber-800 border border-amber-200">DC</span>}
                                        </div>
                                    </td>
                                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{loc.location_type}</td>
                                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{loc.is_pos_enabled ? 'Yes' : 'No'}</td>
                                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{loc.city}</td>
                                    <td className="px-6 py-4 whitespace-nowrap">{getActiveBadge(loc.is_active)}</td>
                                    <td className="px-4 py-4 whitespace-nowrap text-right text-sm font-medium">
                                        <button className="text-blue-600 hover:text-blue-900 p-1" title="Edit">
                                            <Edit3 className="w-4 h-4" />
                                        </button>
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

