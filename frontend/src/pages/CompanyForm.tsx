import React, { useState, useEffect, forwardRef, useImperativeHandle } from "react";
import { Building, Globe, MapPin, AlertCircle } from "lucide-react";
import { companyService, CompanyFormData } from "@services/companyService";

export interface CompanyFormHandle {
    submit: () => void;
    reset: () => void;
}

interface CompanyFormProps {
    companyId?: string | null;
    readOnly?: boolean;
    onSuccess: () => void;
    onCancel: () => void;
}

const initialFormData: CompanyFormData = {
    company_name: '',
    legal_entity_type: 'PVT_LTD',
    default_currency: 'INR',
    timezone: 'Asia/Kolkata',
    status: 'ACTIVE',
    address: {
        line1: '',
        line2: '',
        city: '',
        state: '',
        country: 'India',
        postal_code: '',
    }
};

export const CompanyForm = forwardRef<CompanyFormHandle, CompanyFormProps>(({ companyId, readOnly = false, onSuccess, onCancel }, ref) => {
    const [formData, setFormData] = useState<CompanyFormData>(initialFormData);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const [fieldErrors, setFieldErrors] = useState<Record<string, string>>({});
    const [originalCurrency, setOriginalCurrency] = useState<string | null>(null);

    const legalEntityTypes = [
        { value: 'SOLE_PROPRIETOR', label: 'Sole Proprietor' },
        { value: 'PARTNERSHIP', label: 'Partnership' },
        { value: 'LLP', label: 'LLP' },
        { value: 'PVT_LTD', label: 'Pvt Ltd' },
        { value: 'FRANCHISE', label: 'Franchise' },
    ];

    const currencies = [
        { value: 'INR', label: 'INR - Indian Rupee' },
        { value: 'USD', label: 'USD - US Dollar' },
        { value: 'EUR', label: 'EUR - Euro' },
        { value: 'GBP', label: 'GBP - British Pound' },
        { value: 'AUD', label: 'AUD - Australian Dollar' },
    ];

    const timezones = [
        { value: 'Asia/Kolkata', label: 'Asia/Kolkata (IST)' },
        { value: 'America/New_York', label: 'America/New_York (EST)' },
        { value: 'Europe/London', label: 'Europe/London (GMT)' },
        { value: 'Asia/Singapore', label: 'Asia/Singapore (SGT)' },
        { value: 'Australia/Sydney', label: 'Australia/Sydney (AEST)' },
    ];

    useEffect(() => {
        if (companyId) {
            loadCompany();
        } else {
            setFormData(initialFormData);
            setOriginalCurrency(null);
        }
    }, [companyId]);

    const loadCompany = async () => {
        if (!companyId) return;

        try {
            setLoading(true);
            const company = await companyService.getCompany(companyId);
            setOriginalCurrency(company.default_currency);
            setFormData({
                company_code: company.company_code,
                company_name: company.company_name,
                legal_entity_type: company.legal_entity_type,
                default_currency: company.default_currency,
                timezone: company.timezone,
                status: company.status,
                address: company.address || {
                    line1: '',
                    line2: '',
                    city: '',
                    state: '',
                    country: 'India',
                    postal_code: '',
                }
            });
        } catch (err) {
            setError('Failed to load company details');
            console.error('Error loading company:', err);
        } finally {
            setLoading(false);
        }
    };

    const handleInputChange = (field: string, value: string) => {
        if (readOnly) return;
        setFormData(prev => ({ ...prev, [field]: value }));
        if (fieldErrors[field]) {
            setFieldErrors(prev => ({ ...prev, [field]: '' }));
        }
    };

    const handleAddressChange = (field: string, value: string) => {
        if (readOnly) return;
        setFormData(prev => ({
            ...prev,
            address: {
                ...prev.address,
                [field]: value
            }
        }));
    };

    const validateForm = (): boolean => {
        const errors: Record<string, string> = {};
        if (!formData.company_name.trim()) errors.company_name = "Company name is required";
        if (!formData.legal_entity_type) errors.legal_entity_type = "Legal entity type is required";
        if (!formData.default_currency) errors.default_currency = "Default currency is required";
        if (!formData.timezone) errors.timezone = "Timezone is required";

        setFieldErrors(errors);
        return Object.keys(errors).length === 0;
    };

    const handleSubmit = async () => {
        if (readOnly) return;
        if (!validateForm()) return;

        if (companyId && originalCurrency && formData.default_currency !== originalCurrency) {
            const confirmed = window.confirm(
                `⚠️ Currency Change Warning\n\nChanging the default currency from ${originalCurrency} to ${formData.default_currency} will affect system-wide pricing.\n\nAre you sure?`
            );
            if (!confirmed) return;
        }

        try {
            setLoading(true);
            setError(null);
            if (companyId) {
                await companyService.updateCompany(companyId, formData);
            } else {
                await companyService.createCompany(formData);
            }
            onSuccess();
        } catch (err: any) {
            console.error('Error saving company:', err);
            setError(err.response?.data?.message || 'Failed to save company');
        } finally {
            setLoading(false);
        }
    };

    useImperativeHandle(ref, () => ({
        submit: handleSubmit,
        reset: () => {
            if (readOnly) return;
            setFormData(initialFormData);
            setError(null);
            setFieldErrors({});
        }
    }));

    const isEditing = !!companyId;
    const inputClass = `block w-full px-3 py-2 text-sm border rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 disabled:bg-gray-100 disabled:text-gray-500 ${readOnly ? 'bg-gray-50' : 'bg-white'}`;
    const getErrorClass = (field: string) => fieldErrors[field] ? 'border-red-300' : 'border-gray-300';
    const getInputClass = (field: string) => `${inputClass} ${getErrorClass(field)}`;

    return (
        <div className="h-full flex flex-col bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden">
            <div className="flex-1 overflow-auto p-6">
                <h3 className="text-lg font-semibold text-gray-900 mb-6">
                    {isEditing ? 'Edit Company' : 'New Company'}
                </h3>

                {error && (
                    <div className="mb-4 bg-red-50 border border-red-200 rounded p-3 flex items-start">
                        <AlertCircle className="w-5 h-5 text-red-500 mr-2 mt-0.5" />
                        <span className="text-sm text-red-700">{error}</span>
                    </div>
                )}

                <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
                    {/* Left Column: Basic & Business */}
                    <div className="space-y-6">
                        <div className="bg-gray-50 p-4 rounded-lg border border-gray-100">
                            <h4 className="text-sm font-medium text-gray-900 flex items-center mb-4">
                                <Building className="w-4 h-4 mr-2 text-blue-600" />
                                Basic Information
                            </h4>
                            <div className="space-y-4">
                                <div>
                                    <label className="block text-xs font-medium text-gray-700 mb-1">Company Name *</label>
                                    <input
                                        type="text"
                                        value={formData.company_name}
                                        onChange={(e) => handleInputChange('company_name', e.target.value)}
                                        className={getInputClass('company_name')}
                                        disabled={readOnly}
                                    />
                                    {fieldErrors.company_name && <p className="mt-1 text-xs text-red-600">{fieldErrors.company_name}</p>}
                                </div>
                                <div>
                                    <label className="block text-xs font-medium text-gray-700 mb-1">Company Code</label>
                                    <input
                                        type="text"
                                        value={formData.company_code || ''}
                                        disabled
                                        className="block w-full px-3 py-2 text-sm border border-gray-200 bg-gray-100 rounded-md text-gray-500"
                                        placeholder="Auto-generated"
                                    />
                                </div>
                                <div>
                                    <label className="block text-xs font-medium text-gray-700 mb-1">Legal Entity Type *</label>
                                    <select
                                        value={formData.legal_entity_type}
                                        onChange={(e) => handleInputChange('legal_entity_type', e.target.value)}
                                        className={inputClass}
                                        disabled={readOnly}
                                    >
                                        {legalEntityTypes.map(t => <option key={t.value} value={t.value}>{t.label}</option>)}
                                    </select>
                                </div>
                                <div>
                                    <label className="block text-xs font-medium text-gray-700 mb-1">Status</label>
                                    <select
                                        value={formData.status}
                                        onChange={(e) => handleInputChange('status', e.target.value)}
                                        className={inputClass}
                                        disabled={readOnly}
                                    >
                                        <option value="ACTIVE">Active</option>
                                        <option value="INACTIVE">Inactive</option>
                                    </select>
                                </div>
                            </div>
                        </div>

                        <div className="bg-blue-50 p-4 rounded-lg border border-blue-100">
                            <h4 className="text-sm font-medium text-gray-900 flex items-center mb-4">
                                <Globe className="w-4 h-4 mr-2 text-blue-600" />
                                Business Setup
                            </h4>
                            <div className="space-y-4">
                                <div>
                                    <label className="block text-xs font-medium text-gray-700 mb-1">Default Currency *</label>
                                    <select
                                        value={formData.default_currency}
                                        onChange={(e) => handleInputChange('default_currency', e.target.value)}
                                        className={inputClass}
                                        disabled={readOnly}
                                    >
                                        {currencies.map(c => <option key={c.value} value={c.value}>{c.label}</option>)}
                                    </select>
                                </div>
                                <div>
                                    <label className="block text-xs font-medium text-gray-700 mb-1">Timezone *</label>
                                    <select
                                        value={formData.timezone}
                                        onChange={(e) => handleInputChange('timezone', e.target.value)}
                                        className={inputClass}
                                        disabled={readOnly}
                                    >
                                        {timezones.map(t => <option key={t.value} value={t.value}>{t.label}</option>)}
                                    </select>
                                </div>
                            </div>
                        </div>
                    </div>

                    {/* Right Column: Address */}
                    <div className="space-y-6">
                        <div className="bg-green-50 p-4 rounded-lg border border-green-100 h-full">
                            <h4 className="text-sm font-medium text-gray-900 flex items-center mb-4">
                                <MapPin className="w-4 h-4 mr-2 text-green-600" />
                                Registered Address
                            </h4>
                            <div className="space-y-4">
                                <div>
                                    <label className="block text-xs font-medium text-gray-700 mb-1">Line 1</label>
                                    <input
                                        type="text"
                                        value={formData.address?.line1 || ''}
                                        onChange={(e) => handleAddressChange('line1', e.target.value)}
                                        className={inputClass}
                                        disabled={readOnly}
                                    />
                                </div>
                                <div>
                                    <label className="block text-xs font-medium text-gray-700 mb-1">Line 2</label>
                                    <input
                                        type="text"
                                        value={formData.address?.line2 || ''}
                                        onChange={(e) => handleAddressChange('line2', e.target.value)}
                                        className={inputClass}
                                        disabled={readOnly}
                                    />
                                </div>
                                <div className="grid grid-cols-2 gap-4">
                                    <div>
                                        <label className="block text-xs font-medium text-gray-700 mb-1">City</label>
                                        <input
                                            type="text"
                                            value={formData.address?.city || ''}
                                            onChange={(e) => handleAddressChange('city', e.target.value)}
                                            className={inputClass}
                                            disabled={readOnly}
                                        />
                                    </div>
                                    <div>
                                        <label className="block text-xs font-medium text-gray-700 mb-1">State</label>
                                        <input
                                            type="text"
                                            value={formData.address?.state || ''}
                                            onChange={(e) => handleAddressChange('state', e.target.value)}
                                            className={inputClass}
                                            disabled={readOnly}
                                        />
                                    </div>
                                </div>
                                <div className="grid grid-cols-2 gap-4">
                                    <div>
                                        <label className="block text-xs font-medium text-gray-700 mb-1">Country</label>
                                        <input
                                            type="text"
                                            value={formData.address?.country || ''}
                                            onChange={(e) => handleAddressChange('country', e.target.value)}
                                            className={inputClass}
                                            disabled={readOnly}
                                        />
                                    </div>
                                    <div>
                                        <label className="block text-xs font-medium text-gray-700 mb-1">Postal Code</label>
                                        <input
                                            type="text"
                                            value={formData.address?.postal_code || ''}
                                            onChange={(e) => handleAddressChange('postal_code', e.target.value)}
                                            className={inputClass}
                                            disabled={readOnly}
                                        />
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
});

CompanyForm.displayName = 'CompanyForm';

