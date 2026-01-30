import React, { useState, useEffect, forwardRef, useImperativeHandle } from "react";
import { Database, AlertCircle } from "lucide-react";
import { categoryService } from "@services/categoryService";
import { brandService } from "@services/brandService";
import { customerGroupService } from "@services/customerGroupService";
import { loyaltyProgramService } from "@services/loyaltyProgramService";

export type MasterType = "category" | "brand" | "customer-group" | "loyalty-program";

export interface SimpleMasterFormHandle {
    submit: () => void;
    reset: () => void;
}

export interface SimpleMasterData {
    name: string;
    is_active: boolean;
}

interface SimpleMasterFormProps {
    masterType: MasterType;
    companyId: string; // <-- Added
    itemId?: string | null;
    initialData?: SimpleMasterData | null;
    onSuccess: () => void;
    onCancel: () => void;
}

export const SimpleMasterForm = forwardRef<SimpleMasterFormHandle, SimpleMasterFormProps>(({ masterType, companyId, itemId, initialData, onSuccess, onCancel }, ref) => {
    const [formData, setFormData] = useState<SimpleMasterData>({ name: '', is_active: true });
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        if (itemId && initialData) {
            setFormData(initialData);
        } else {
            setFormData({ name: '', is_active: true });
        }
    }, [itemId, initialData]);

    const handleSubmit = async () => {
        if (!formData.name.trim()) {
            setError('Name is required');
            return;
        }

        try {
            setLoading(true);
            setError(null);

            const baseData = { name: formData.name, is_active: formData.is_active, company: companyId };

            if (masterType === 'category') {
                if (itemId) await categoryService.updateCategory(itemId, baseData);
                else await categoryService.createCategory(baseData);
            } else if (masterType === 'brand') {
                if (itemId) await brandService.updateBrand(itemId, baseData);
                else await brandService.createBrand(baseData);
            } else if (masterType === 'customer-group') {
                const groupData = { group_name: formData.name, is_active: formData.is_active, company: companyId };
                if (itemId) await customerGroupService.updateCustomerGroup(itemId, groupData);
                else await customerGroupService.createCustomerGroup(groupData);
            } else if (masterType === 'loyalty-program') {
                const programData = { program_name: formData.name, is_active: formData.is_active, company: companyId }; // <-- Added company
                if (itemId) await loyaltyProgramService.updateLoyaltyProgram(itemId, programData);
                else await loyaltyProgramService.createLoyaltyProgram(programData);
            }

            onSuccess();
        } catch (err: any) {
            console.error(err);
            setError(`Failed to save ${masterType}`);
        } finally {
            setLoading(false);
        }
    };

    useImperativeHandle(ref, () => ({
        submit: handleSubmit,
        reset: () => {
            if (itemId && initialData) {
                setFormData(initialData);
            } else {
                setFormData({ name: '', is_active: true });
            }
            setError(null);
        }
    }));

    const getMasterLabel = () => {
        switch (masterType) {
            case "category": return "Category";
            case "brand": return "Brand";
            case "customer-group": return "Customer Group";
            case "loyalty-program": return "Loyalty Program";
            default: return "Master";
        }
    };

    const isEditing = !!itemId;

    return (
        <div className="h-full flex flex-col bg-white rounded-lg shadow-sm border border-gray-200">
            <div className="p-6 border-b border-gray-200">
                <h3 className="text-lg font-semibold text-gray-900">
                    {isEditing ? `Edit ${getMasterLabel()}` : `Add ${getMasterLabel()}`}
                </h3>
            </div>

            <div className="flex-1 p-6">
                {error && (
                    <div className="mb-4 bg-red-50 border border-red-200 rounded p-3 flex items-start">
                        <AlertCircle className="w-5 h-5 text-red-500 mr-2 mt-0.5" />
                        <span className="text-sm text-red-700">{error}</span>
                    </div>
                )}

                <div className="max-w-md space-y-6">
                    <div className="bg-gray-50 p-4 rounded-lg border border-gray-100">
                        <h4 className="text-sm font-medium text-gray-900 flex items-center mb-4">
                            <Database className="w-4 h-4 mr-2 text-blue-600" />
                            Details
                        </h4>
                        <div className="space-y-4">
                            <div>
                                <label className="block text-xs font-medium text-gray-700 mb-1">Name *</label>
                                <input
                                    type="text"
                                    value={formData.name}
                                    onChange={(e) => setFormData(prev => ({ ...prev, name: e.target.value }))}
                                    className="block w-full px-3 py-2 text-sm border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
                                    placeholder={`Enter ${getMasterLabel()} name`}
                                    disabled={loading}
                                />
                            </div>
                            <div>
                                <label className="block text-xs font-medium text-gray-700 mb-1">Status</label>
                                <div className="flex items-center mt-2">
                                    <input
                                        type="checkbox"
                                        checked={formData.is_active}
                                        onChange={(e) => setFormData(prev => ({ ...prev, is_active: e.target.checked }))}
                                        className="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
                                        disabled={loading}
                                    />
                                    <label className="ml-2 block text-sm text-gray-900">Active</label>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
});

SimpleMasterForm.displayName = 'SimpleMasterForm';

