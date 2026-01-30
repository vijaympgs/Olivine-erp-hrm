import React, { useEffect, useState, useRef } from "react";
import { useNavigate } from "react-router-dom";
import { Plus, Search, Edit3, Power, Database } from "lucide-react";
import { companyService, CompanyListItem } from "@services/companyService";
import { categoryService } from "@services/categoryService";
import { brandService } from "@services/brandService";
import { customerGroupService } from "@services/customerGroupService";
import { loyaltyProgramService } from "@services/loyaltyProgramService";
import { MasterToolbar, MasterMode } from "@core/ui-canon/frontend/ui/components/MasterToolbarConfigDriven";
import { SimpleMasterForm, SimpleMasterFormHandle, MasterType, SimpleMasterData } from "./SimpleMasterForm";

interface MasterItem {
    id: string;
    name: string;
    is_active: boolean;
}

export const SimpleMasterSetup: React.FC = () => {
    const navigate = useNavigate();
    const [masterType, setMasterType] = useState<MasterType>('category');
    const [companies, setCompanies] = useState<CompanyListItem[]>([]);
    const [selectedCompany, setSelectedCompany] = useState<string>('');
    const [items, setItems] = useState<MasterItem[]>([]);
    const [loading, setLoading] = useState(true);
    const [searchTerm, setSearchTerm] = useState('');

    // Pattern State
    const [showForm, setShowForm] = useState(false);
    const [editingId, setEditingId] = useState<string | null>(null);
    const [selectedIds, setSelectedIds] = useState<string[]>([]);
    const formRef = useRef<SimpleMasterFormHandle>(null);

    useEffect(() => {
        loadCompanies();
    }, []);

    useEffect(() => {
        if (selectedCompany && !showForm) {
            loadItems();
        }
    }, [masterType, selectedCompany, searchTerm, showForm]);

    useEffect(() => {
        // Reset selection when master type changes
        setSelectedIds([]);
        setShowForm(false);
        setEditingId(null);
    }, [masterType]);

    const getMasterLabel = () => {
        switch (masterType) {
            case "category": return "Category";
            case "brand": return "Brand";
            case "loyalty-program": return "Loyalty Program";
            default: return "Master";
        }
    };

    const getMasterPluralLabel = () => {
        switch (masterType) {
            case "category": return "Categories";
            case "brand": return "Brands";
            case "loyalty-program": return "Loyalty Programs";
            default: return "Masters";
        }
    };

    const loadCompanies = async () => {
        try {
            const activeCompanies = await companyService.getActiveCompanies();
            setCompanies(activeCompanies);
            if (activeCompanies.length > 0) {
                setSelectedCompany(activeCompanies[0].id);
            }
        } catch {
            console.error('Failed to load companies');
        }
    };

    const loadItems = async () => {
        try {
            setLoading(true);
            const filters = {
                company: selectedCompany,
                search: searchTerm || undefined,
            };

            let data: MasterItem[];
            if (masterType === 'category') {
                data = await categoryService.getCategories(filters);
            } else if (masterType === 'brand') {
                data = await brandService.getBrands(filters);
            } else if (masterType === 'loyalty-program') {
                const programs = await loyaltyProgramService.getLoyaltyPrograms(filters);
                data = programs.map(p => ({ id: p.id, name: p.program_name, is_active: p.is_active }));
            } else {
                data = [];
            }

            setItems(data);
        } catch (err) {
            console.error(`Failed to load ${getMasterPluralLabel().toLowerCase()}`);
        } finally {
            setLoading(false);
        }
    };

    const handleToggleActive = async (item: MasterItem) => {
        try {
            // ... existing logic ...
            if (masterType === 'category') {
                if (item.is_active) await categoryService.deactivateCategory(item.id);
                else await categoryService.activateCategory(item.id);
            } else if (masterType === 'brand') {
                if (item.is_active) await brandService.deactivateBrand(item.id);
                else await brandService.activateBrand(item.id);
            } else if (masterType === 'loyalty-program') {
                if (item.is_active) await loyaltyProgramService.deactivateLoyaltyProgram(item.id);
                else await loyaltyProgramService.activateLoyaltyProgram(item.id);
            }
            loadItems();
        } catch (err) {
            console.error(err);
        }
    };

    const handleRowClick = (item: MasterItem) => {
        setEditingId(item.id);
        setShowForm(true);
    };

    const handleToolbarAction = (action: string) => {
        switch (action) {
            case 'new':
                setEditingId(null);
                setShowForm(true);
                break;
            case 'save':
                if (showForm) formRef.current?.submit();
                break;
            case 'clear':
                if (showForm) {
                    formRef.current?.reset();
                } else {
                    setSearchTerm('');
                    setSelectedIds([]);
                }
                break;
            case 'view':
            case 'edit':
                if (selectedIds.length === 1) {
                    setEditingId(selectedIds[0]);
                    setShowForm(true);
                }
                break;
            case 'delete':
                if (!showForm && selectedIds.length > 0) {
                    if (confirm(`Toggle status for ${selectedIds.length} items?`)) {
                        const itemsToProcess = items.filter(i => selectedIds.includes(i.id));
                        Promise.all(itemsToProcess.map(i => handleToggleActive(i)))
                            .then(() => {
                                setSelectedIds([]);
                                loadItems();
                            });
                    }
                }
                break;
            case 'refresh':
                if (!showForm) loadItems();
                break;
            case 'exit':
                if (showForm) {
                    setShowForm(false);
                    setEditingId(null);
                } else {
                    navigate('/admin/layout-settings');
                }
                break;
            case 'search':
                document.getElementById('sm-search')?.focus();
                break;
        }
    };

    const getToolbarMode = (): MasterMode => {
        if (!showForm) return 'VIEW';
        return editingId ? 'EDIT' : 'CREATE';
    };

    const getDisabledActions = (): string[] => {
        if (showForm) return ['new', 'delete', 'refresh', 'export', 'import', 'search', 'filter', 'report', 'view', 'edit']; // Disable View/Edit in form

        // In List Mode
        const disabled = ['save']; // Clear is always enabled (reset form or reset filters)
        if (selectedIds.length !== 1) disabled.push('edit', 'view'); // Edit/View require single selection
        if (selectedIds.length === 0) disabled.push('delete'); // Delete requires selection

        return disabled;
    };

    const getInitialData = (): SimpleMasterData | null => {
        if (!editingId) return null;
        const item = items.find(i => i.id === editingId);
        return item ? { name: item.name, is_active: item.is_active } : null;
    };

    const handleSelectAll = (checked: boolean) => {
        if (checked) setSelectedIds(items.map(i => i.id));
        else setSelectedIds([]);
    };

    const handleSelectRow = (id: string, checked: boolean) => {
        if (checked) setSelectedIds(prev => [...prev, id]);
        else setSelectedIds(prev => prev.filter(x => x !== id));
    };

    return (
        <div className="flex flex-col h-full bg-slate-50">
            <MasterToolbar
                viewId="code-masters"
                mode={getToolbarMode()}
                onAction={handleToolbarAction}
                disabledActions={getDisabledActions()}
                hasSelection={selectedIds.length > 0}
                title="Code Masters"
                showLabels={false}
            />
            <div className="flex-1 overflow-hidden p-4">
                {showForm ? (
                    <SimpleMasterForm
                        ref={formRef}
                        masterType={masterType}
                        companyId={selectedCompany}
                        itemId={editingId}
                        initialData={getInitialData()}
                        onSuccess={() => {
                            setShowForm(false);
                            setEditingId(null);
                            loadItems();
                        }}
                        onCancel={() => {
                            setShowForm(false);
                            setEditingId(null);
                        }}
                    />
                ) : (
                    <div className="h-full flex flex-col space-y-4">
                        {/* Filters */}
                        <div className="bg-white p-4 shadow-sm border border-gray-200 rounded-lg flex-shrink-0">
                            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                                <div>
                                    <label className="block text-xs font-semibold text-gray-600 uppercase mb-1">Master Type</label>
                                    <select
                                        value={masterType}
                                        onChange={(e) => setMasterType(e.target.value as MasterType)}
                                        className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm focus:ring-blue-500 focus:border-blue-500"
                                    >
                                        <option value="category">Category</option>
                                        <option value="brand">Brand</option>
                                        <option value="loyalty-program">Loyalty Program</option>
                                    </select>
                                </div>
                                <div>
                                    <label className="block text-xs font-semibold text-gray-600 uppercase mb-1">Company</label>
                                    <select
                                        value={selectedCompany}
                                        onChange={(e) => setSelectedCompany(e.target.value)}
                                        className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm focus:ring-blue-500 focus:border-blue-500"
                                    >
                                        {companies.map(c => (
                                            <option key={c.id} value={c.id}>{c.company_name}</option>
                                        ))}
                                    </select>
                                </div>
                                <div className="relative">
                                    <label className="block text-xs font-semibold text-gray-600 uppercase mb-1">Search</label>
                                    <div className="relative">
                                        <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-4 h-4 mt-3" /> {/* MT fix for label offset? no, mt-3 is usually weird here. I'll rely on container center */}
                                        <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-4 h-4" style={{ top: '22px' }} />
                                        {/* Just simple input */}
                                        <input
                                            id="sm-search"
                                            type="text"
                                            placeholder={`Search ${getMasterLabel()}...`}
                                            value={searchTerm}
                                            onChange={(e) => setSearchTerm(e.target.value)}
                                            className="pl-10 pr-4 py-2 w-full border border-gray-300 rounded-md text-sm focus:ring-blue-500 focus:border-blue-500"
                                        />
                                    </div>
                                </div>
                            </div>
                        </div>

                        {/* Table */}
                        <div className="flex-1 bg-white shadow-sm border border-gray-200 rounded-lg overflow-hidden">
                            <div className="h-full overflow-auto">
                                <table className="min-w-full divide-y divide-gray-200">
                                    <thead className="bg-gray-50 sticky top-0 z-10">
                                        <tr>
                                            <th className="px-4 py-3 text-left w-12">
                                                <input
                                                    type="checkbox"
                                                    checked={items.length > 0 && selectedIds.length === items.length}
                                                    onChange={(e) => handleSelectAll(e.target.checked)}
                                                    className="rounded border-gray-300 text-blue-600 focus:ring-blue-500"
                                                />
                                            </th>
                                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
                                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
                                        </tr>
                                    </thead>
                                    <tbody className="bg-white divide-y divide-gray-200">
                                        {loading ? (
                                            <tr><td colSpan={3} className="text-center py-4">Loading...</td></tr>
                                        ) : items.length === 0 ? (
                                            <tr><td colSpan={3} className="text-center py-8 text-gray-500">No items found.</td></tr>
                                        ) : (
                                            items.map(item => (
                                                <tr
                                                    key={item.id}
                                                    onClick={() => handleRowClick(item)}
                                                    className="hover:bg-blue-50 cursor-pointer transition-colors"
                                                >
                                                    <td className="px-4 py-4 whitespace-nowrap" onClick={(e) => e.stopPropagation()}>
                                                        <input
                                                            type="checkbox"
                                                            checked={selectedIds.includes(item.id)}
                                                            onChange={(e) => handleSelectRow(item.id, e.target.checked)}
                                                            className="rounded border-gray-300 text-blue-600 focus:ring-blue-500"
                                                        />
                                                    </td>
                                                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{item.name}</td>
                                                    <td className="px-6 py-4 whitespace-nowrap">
                                                        <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${item.is_active ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-800'}`}>
                                                            {item.is_active ? 'Active' : 'Inactive'}
                                                        </span>
                                                    </td>
                                                </tr>
                                            ))
                                        )}
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

