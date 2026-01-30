import React, { useEffect, useState, forwardRef, useImperativeHandle } from "react";
import { MapPin, AlertCircle } from "lucide-react";
import { companyService, CompanyListItem } from "@services/companyService";
import { locationService, Location, LocationFormData, LocationType, ChannelType, LocationListItem } from "@services/locationService";

export interface LocationFormHandle {
    submit: () => void;
    reset: () => void;
}

interface LocationFormProps {
    locationId?: string | null;
    readOnly?: boolean;
    onSuccess: () => void;
    onCancel: () => void;
}

const initialFormData: LocationFormData = {
    company: '',
    location_code: '',
    name: '',
    display_name: '',
    location_type: 'STORE',
    channel_type: 'RETAIL',
    parent_location: null,
    address_line1: '',
    address_line2: '',
    city: '',
    state: '',
    country: 'India',
    postal_code: '',
    phone: '',
    email: '',
    timezone: '',
    opening_date: '',
    closing_date: '',
    is_pos_enabled: false,
    is_dc: false,
    is_active: true,
};

export const LocationForm = forwardRef<LocationFormHandle, LocationFormProps>(({ locationId, readOnly = false, onSuccess, onCancel }, ref) => {
    const [companies, setCompanies] = useState<CompanyListItem[]>([]);
    const [parentLocations, setParentLocations] = useState<LocationListItem[]>([]);
    const [formData, setFormData] = useState<LocationFormData>(initialFormData);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const [fieldErrors, setFieldErrors] = useState<Record<string, string>>({});

    const locationTypes: { value: LocationType; label: string }[] = [
        { value: 'STORE', label: 'Store' },
        { value: 'WAREHOUSE', label: 'Warehouse' },
        { value: 'OFFICE', label: 'Office' },
        { value: 'OTHER', label: 'Other' },
    ];

    const channelTypes: { value: ChannelType; label: string }[] = [
        { value: 'RETAIL', label: 'Retail' },
        { value: 'ONLINE', label: 'Online' },
        { value: 'WHOLESALE', label: 'Wholesale' },
        { value: 'FRANCHISE', label: 'Franchise' },
    ];

    useEffect(() => {
        (async () => {
            try {
                const activeCompanies = await companyService.getActiveCompanies();
                setCompanies(activeCompanies);
                if (!locationId && activeCompanies.length > 0) {
                    setFormData(prev => ({ ...prev, company: activeCompanies[0].id }));
                }
            } catch (e) {
                setError('Failed to load companies');
            }
        })();
    }, [locationId]);

    useEffect(() => {
        if (locationId) {
            loadLocation();
        } else {
            setFormData(initialFormData);
            if (companies.length > 0) {
                setFormData(prev => ({ ...prev, company: companies[0].id }));
            }
        }
    }, [locationId]);

    const loadLocation = async () => {
        if (!locationId) return;
        try {
            setLoading(true);
            const loc: Location = await locationService.getLocation(locationId);
            setFormData({
                company: loc.company,
                location_code: loc.location_code,
                name: loc.name,
                display_name: loc.display_name || '',
                location_type: loc.location_type as LocationType,
                channel_type: (loc.channel_type as ChannelType) || null,
                parent_location: loc.parent_location || null,
                address_line1: loc.address_line1,
                address_line2: loc.address_line2 || '',
                city: loc.city,
                state: loc.state,
                country: loc.country,
                postal_code: loc.postal_code || '',
                phone: loc.phone || '',
                email: loc.email || '',
                timezone: loc.timezone || '',
                opening_date: loc.opening_date || '',
                closing_date: loc.closing_date || '',
                is_pos_enabled: loc.is_pos_enabled,
                is_dc: !!loc.is_dc,
                is_active: loc.is_active,
            });
        } catch (err) {
            setError("Failed to load location details");
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        (async () => {
            try {
                if (!formData.company) {
                    setParentLocations([]);
                    return;
                }
                const response = await locationService.getLocations({
                    company_id: formData.company,
                    include_inactive: true,
                });
                const rows = response.results.filter(r => r.id !== locationId);
                setParentLocations(rows);
            } catch {
                setParentLocations([]);
            }
        })();
    }, [formData.company, locationId]);

    const handleInputChange = (field: keyof LocationFormData, value: any) => {
        if (readOnly) return;
        setFormData(prev => ({ ...prev, [field]: value }));
        if (fieldErrors[field as string]) {
            setFieldErrors(prev => ({ ...prev, [field as string]: '' }));
        }
    };

    const validateForm = (): boolean => {
        const errors: Record<string, string> = {};
        if (!formData.company) errors.company = "Company is required";
        if (!formData.location_code.trim()) errors.location_code = "Location code is required";
        if (!formData.name.trim()) errors.name = "Name is required";
        if (!formData.location_type) errors.location_type = "Location type is required";
        if (!formData.address_line1.trim()) errors.address_line1 = "Address line 1 is required";
        if (!formData.city.trim()) errors.city = "City is required";
        if (!formData.state.trim()) errors.state = "State is required";
        if (!formData.country.trim()) errors.country = "Country is required";

        if (formData.is_pos_enabled && formData.location_type !== 'STORE') {
            errors.is_pos_enabled = "POS can be enabled only when Location Type is STORE";
        }

        setFieldErrors(errors);
        return Object.keys(errors).length === 0;
    };

    const handleSubmit = async () => {
        if (readOnly) return;
        if (!validateForm()) return;
        try {
            setLoading(true);
            setError(null);
            const payload: LocationFormData = {
                ...formData,
                display_name: formData.display_name || null,
                channel_type: formData.channel_type || null,
                parent_location: formData.parent_location || null,
                address_line2: formData.address_line2 || null,
                postal_code: formData.postal_code || null,
                phone: formData.phone || null,
                email: formData.email || null,
                timezone: formData.timezone || null,
                opening_date: formData.opening_date || null,
                closing_date: formData.closing_date || null,
            };

            if (locationId) {
                await locationService.updateLocation(locationId, payload);
            } else {
                await locationService.createLocation(payload);
            }
            onSuccess();
        } catch (err: any) {
            if (err.response?.data && typeof err.response.data === 'object') {
                setFieldErrors(err.response.data);
            } else {
                setError('Failed to save location');
            }
        } finally {
            setLoading(false);
        }
    };

    useImperativeHandle(ref, () => ({
        submit: handleSubmit,
        reset: () => {
            if (readOnly) return;
            setFormData(initialFormData);
            if (companies.length > 0) {
                setFormData(prev => ({ ...prev, company: companies[0].id }));
            }
            setError(null);
            setFieldErrors({});
        }
    }));

    const isEditing = !!locationId;
    const posToggleDisabled = (formData.location_type !== "STORE") || readOnly;

    // Helper for input styles
    const inputClass = `block w-full px-3 py-2 text-sm border rounded-none shadow-sm focus:ring-blue-500 focus:border-blue-500 disabled:bg-gray-100 disabled:text-gray-500 ${readOnly ? 'bg-gray-50' : 'bg-white'}`;
    const getErrorClass = (field: string) => fieldErrors[field] ? 'border-red-300' : 'border-gray-300';
    const getInputClass = (field: string) => `${inputClass} ${getErrorClass(field)}`;

    return (
        <div className="h-full flex flex-col bg-white rounded-none shadow-sm border border-gray-200 overflow-hidden">
            <div className="flex-1 overflow-auto p-6">

                {error && (
                    <div className="bg-red-50 border border-red-200 rounded-none p-3 mb-4 flex items-start">
                        <AlertCircle className="w-5 h-5 text-red-500 mr-2 mt-0.5" />
                        <span className="text-sm text-red-700">{error}</span>
                    </div>
                )}

                <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
                    {/* Left Column */}
                    <div className="space-y-6">
                        <div className="bg-gray-50 p-4 rounded-none border border-gray-100">
                            <h4 className="text-sm font-medium text-gray-900 flex items-center mb-4">
                                <MapPin className="w-4 h-4 mr-2 text-blue-600" />
                                Basic Information
                            </h4>
                            <div className="space-y-4">
                                <div>
                                    <label className="block text-xs font-medium text-gray-700 mb-1">Company *</label>
                                    <select
                                        value={formData.company}
                                        onChange={(e) => {
                                            handleInputChange('company', e.target.value);
                                            handleInputChange('parent_location', null);
                                        }}
                                        disabled={readOnly}
                                        className={getInputClass('company')}
                                    >
                                        {companies.map(c => <option key={c.id} value={c.id}>{c.company_name}</option>)}
                                    </select>
                                </div>
                                <div>
                                    <label className="block text-xs font-medium text-gray-700 mb-1">Location Code *</label>
                                    <input
                                        type="text"
                                        value={formData.location_code}
                                        onChange={(e) => handleInputChange('location_code', e.target.value)}
                                        disabled={readOnly}
                                        className={getInputClass('location_code')}
                                    />
                                    {fieldErrors.location_code && <p className="mt-1 text-xs text-red-600">{fieldErrors.location_code}</p>}
                                </div>
                                <div>
                                    <label className="block text-xs font-medium text-gray-700 mb-1">Name *</label>
                                    <input
                                        type="text"
                                        value={formData.name}
                                        onChange={(e) => handleInputChange('name', e.target.value)}
                                        disabled={readOnly}
                                        className={getInputClass('name')}
                                    />
                                    {fieldErrors.name && <p className="mt-1 text-xs text-red-600">{fieldErrors.name}</p>}
                                </div>
                                <div>
                                    <label className="block text-xs font-medium text-gray-700 mb-1">Display Name</label>
                                    <input
                                        type="text"
                                        value={formData.display_name || ''}
                                        onChange={(e) => handleInputChange('display_name', e.target.value)}
                                        disabled={readOnly}
                                        className={inputClass}
                                    />
                                </div>
                                <div className="grid grid-cols-2 gap-4">
                                    <div>
                                        <label className="block text-xs font-medium text-gray-700 mb-1">Location Type *</label>
                                        <select
                                            value={formData.location_type}
                                            onChange={(e) => {
                                                const nextType = e.target.value as LocationType;
                                                handleInputChange('location_type', nextType);
                                                if (nextType !== 'STORE') handleInputChange('is_pos_enabled', false);
                                            }}
                                            disabled={readOnly}
                                            className={inputClass}
                                        >
                                            {locationTypes.map(t => <option key={t.value} value={t.value}>{t.label}</option>)}
                                        </select>
                                    </div>
                                    <div>
                                        <label className="block text-xs font-medium text-gray-700 mb-1">Channel Type</label>
                                        <select
                                            value={formData.channel_type || ''}
                                            onChange={(e) => handleInputChange('channel_type', e.target.value || null)}
                                            disabled={readOnly}
                                            className={inputClass}
                                        >
                                            <option value="">(None)</option>
                                            {channelTypes.map(t => <option key={t.value} value={t.value}>{t.label}</option>)}
                                        </select>
                                    </div>
                                </div>
                                <div>
                                    <label className="block text-xs font-medium text-gray-700 mb-1">Parent Location</label>
                                    <select
                                        value={formData.parent_location || ''}
                                        onChange={(e) => handleInputChange('parent_location', e.target.value || null)}
                                        disabled={readOnly}
                                        className={inputClass}
                                    >
                                        <option value="">(None)</option>
                                        {parentLocations.map(pl => <option key={pl.id} value={pl.id}>{pl.location_code} - {pl.name}</option>)}
                                    </select>
                                </div>
                                <div className="grid grid-cols-2 gap-4">
                                    <div>
                                        <label className="block text-xs font-medium text-gray-700 mb-1">POS Enabled</label>
                                        <div className="flex items-center space-x-2">
                                            <input type="checkbox" checked={formData.is_pos_enabled} disabled={posToggleDisabled} onChange={e => handleInputChange('is_pos_enabled', e.target.checked)} className="rounded-none h-4 w-4 text-blue-600 focus:ring-blue-500" />
                                            <span className="text-xs text-gray-600">Enable POS</span>
                                        </div>
                                        {fieldErrors.is_pos_enabled && <p className="mt-1 text-xs text-red-600">{fieldErrors.is_pos_enabled}</p>}
                                    </div>
                                    <div>
                                        <label className="block text-xs font-medium text-gray-700 mb-1">Distribution Center</label>
                                        <div className="flex items-center space-x-2">
                                            <input type="checkbox" checked={!!formData.is_dc} disabled={readOnly} onChange={e => handleInputChange('is_dc', e.target.checked)} className="rounded-none h-4 w-4 text-blue-600 focus:ring-blue-500" />
                                            <span className="text-xs text-gray-600">Mark as DC</span>
                                        </div>
                                    </div>
                                </div>
                                <div>
                                    <label className="block text-xs font-medium text-gray-700 mb-1">Status</label>
                                    <select
                                        value={formData.is_active ? 'ACTIVE' : 'INACTIVE'}
                                        onChange={(e) => handleInputChange('is_active', e.target.value === 'ACTIVE')}
                                        disabled={readOnly}
                                        className={inputClass}
                                    >
                                        <option value="ACTIVE">Active</option>
                                        <option value="INACTIVE">Inactive</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                    </div>

                    {/* Right Column */}
                    <div className="space-y-6">
                        <div className="bg-green-50 p-4 rounded-none border border-green-100 h-full">
                            <h4 className="text-sm font-medium text-gray-900 flex items-center mb-4">
                                <MapPin className="w-4 h-4 mr-2 text-green-600" />
                                Address & Contact
                            </h4>
                            <div className="space-y-4">
                                <div>
                                    <label className="block text-xs font-medium text-gray-700 mb-1">Address Line 1 *</label>
                                    <input
                                        type="text"
                                        value={formData.address_line1}
                                        onChange={(e) => handleInputChange('address_line1', e.target.value)}
                                        disabled={readOnly}
                                        className={getInputClass('address_line1')}
                                    />
                                    {fieldErrors.address_line1 && <p className="mt-1 text-xs text-red-600">{fieldErrors.address_line1}</p>}
                                </div>
                                <div>
                                    <label className="block text-xs font-medium text-gray-700 mb-1">Address Line 2</label>
                                    <input
                                        type="text"
                                        value={formData.address_line2 || ''}
                                        onChange={(e) => handleInputChange('address_line2', e.target.value)}
                                        disabled={readOnly}
                                        className={inputClass}
                                    />
                                </div>
                                <div className="grid grid-cols-2 gap-4">
                                    <div>
                                        <label className="block text-xs font-medium text-gray-700 mb-1">City *</label>
                                        <input
                                            type="text"
                                            value={formData.city}
                                            onChange={(e) => handleInputChange('city', e.target.value)}
                                            disabled={readOnly}
                                            className={getInputClass('city')}
                                        />
                                    </div>
                                    <div>
                                        <label className="block text-xs font-medium text-gray-700 mb-1">State *</label>
                                        <input
                                            type="text"
                                            value={formData.state}
                                            onChange={(e) => handleInputChange('state', e.target.value)}
                                            disabled={readOnly}
                                            className={getInputClass('state')}
                                        />
                                    </div>
                                </div>
                                <div className="grid grid-cols-2 gap-4">
                                    <div>
                                        <label className="block text-xs font-medium text-gray-700 mb-1">Country *</label>
                                        <input
                                            type="text"
                                            value={formData.country}
                                            onChange={(e) => handleInputChange('country', e.target.value)}
                                            disabled={readOnly}
                                            className={getInputClass('country')}
                                        />
                                    </div>
                                    <div>
                                        <label className="block text-xs font-medium text-gray-700 mb-1">Postal Code</label>
                                        <input
                                            type="text"
                                            value={formData.postal_code || ''}
                                            onChange={(e) => handleInputChange('postal_code', e.target.value)}
                                            disabled={readOnly}
                                            className={inputClass}
                                        />
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div className="bg-blue-50 p-4 rounded-none border border-blue-100">
                            <h4 className="text-sm font-medium text-gray-900 flex items-center mb-4">Contact Info</h4>
                            <div className="space-y-4">
                                <div className="grid grid-cols-2 gap-4">
                                    <div>
                                        <label className="block text-xs font-medium text-gray-700 mb-1">Phone</label>
                                        <input type="text" value={formData.phone || ''} onChange={e => handleInputChange('phone', e.target.value)} disabled={readOnly} className={inputClass} />
                                    </div>
                                    <div>
                                        <label className="block text-xs font-medium text-gray-700 mb-1">Email</label>
                                        <input type="email" value={formData.email || ''} onChange={e => handleInputChange('email', e.target.value)} disabled={readOnly} className={inputClass} />
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

LocationForm.displayName = 'LocationForm';

