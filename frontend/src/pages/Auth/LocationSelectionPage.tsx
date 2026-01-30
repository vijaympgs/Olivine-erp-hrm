import React, { useState, useEffect } from "react";
import {
    MapPin,
    Calendar,
    ArrowRight
} from "lucide-react";
import { useNavigate } from "react-router-dom";
import { useAuthContext } from "../../auth/auth.context";
import { useGlobalLocation } from "../../core/contexts/GlobalLocationContext";
import { locationService } from "@services/locationService";

export const LocationSelectionPage: React.FC = () => {
    const navigate = useNavigate();
    const { user } = useAuthContext();
    const { setLocation, currentLocationId } = useGlobalLocation();

    const [locations, setLocations] = useState<any[]>([]);
    const [selectedLocationId, setSelectedLocationId] = useState<string>('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const currentCompanyId = user?.currentCompanyId || (user?.authorizedCompanies?.length === 1 ? user.authorizedCompanies[0].id : null);

    // 1. Check Roles & POS Bypass specific logic
    const isPosUser = (user?.role as any) === 'pos'; // Simplified check, adapt to actual role strings

    useEffect(() => {
        // If POS User, they should have been redirected or auto-assigned already. 
        // But if they land here, we try to auto-assign current or assigned location.
        if (isPosUser) {
            // Logic to auto-select assigned location would go here, 
            // but for now we'll just redirect to dashboard or pos dashboard if already set
            if (currentLocationId) {
                navigate('/');
            }
        }
    }, [isPosUser, currentLocationId, navigate]);

    // 2. Fetch Locations
    useEffect(() => {
        if (!user?.id || !currentCompanyId) return;

        setLoading(true);
        locationService.getUserAccessibleLocations(user.id, currentCompanyId)
            .then(res => {
                setLocations(res);
                if (res.length === 1) {
                    setSelectedLocationId(res[0].id);
                }
            })
            .catch(err => {
                console.error(err);
                setError('Failed to load locations.');
            })
            .finally(() => setLoading(false));
    }, [user, currentCompanyId]);


    const handleContinue = () => {
        if (!selectedLocationId) return;

        const loc = locations.find(l => l.id === selectedLocationId);
        if (loc) {
            setLocation(loc.id, loc.name, loc.location_code);
            navigate('/');
        }
    };

    const handleSkip = () => {
        navigate('/');
    };

    if (loading) {
        return (
            <div className="min-h-screen flex items-center justify-center bg-gray-50">
                <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary"></div>
            </div>
        );
    }

    return (
        <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-indigo-600 to-purple-700 p-4">
            <div className="bg-white rounded-lg shadow-xl w-full max-w-md p-8 animate-in fade-in zoom-in-95 duration-200">
                <div className="text-center mb-8">
                    <div className="bg-indigo-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                        <MapPin className="w-8 h-8 text-indigo-600" />
                    </div>
                    <h1 className="text-2xl font-bold text-gray-900">Select Location</h1>
                    <p className="text-gray-500 mt-2">Choose a location to work with for this session</p>
                </div>

                <div className="bg-blue-50 border border-blue-100 rounded-md p-4 mb-6">
                    <div className="flex gap-3">
                        <div className="flex-shrink-0">
                            <svg className="h-5 w-5 text-blue-400" viewBox="0 0 20 20" fill="currentColor">
                                <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clipRule="evenodd" />
                            </svg>
                        </div>
                        <p className="text-sm text-blue-700">
                            <strong>Note:</strong> This location selection is for this session only and does not modify your user profile.
                        </p>
                    </div>
                </div>

                {error && (
                    <div className="bg-red-50 border border-red-100 text-red-700 px-4 py-3 rounded mb-4 text-sm">
                        {error}
                    </div>
                )}

                <div className="space-y-4">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">
                            Select Location *
                        </label>
                        <select
                            value={selectedLocationId}
                            onChange={(e) => setSelectedLocationId(e.target.value)}
                            className="w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 py-2.5"
                            disabled={locations.length === 0}
                        >
                            <option value="">-- Select a location --</option>
                            {locations.map(loc => (
                                <option key={loc.id} value={loc.id}>
                                    {loc.name} ({loc.location_code})
                                </option>
                            ))}
                        </select>
                    </div>

                    <div className="flex items-center justify-between pt-4">
                        <button
                            onClick={handleSkip}
                            className="text-indigo-600 hover:text-indigo-800 text-sm font-medium"
                        >
                            Skip for Now
                        </button>

                        <button
                            onClick={handleContinue}
                            disabled={!selectedLocationId}
                            className={`flex items-center px-4 py-2 rounded-md text-white font-medium transition-colors ${selectedLocationId
                                ? 'bg-indigo-600 hover:bg-indigo-700 shadow-md'
                                : 'bg-gray-300 cursor-not-allowed'
                                }`}
                        >
                            Continue
                            <ArrowRight className="w-4 h-4 ml-2" />
                        </button>
                    </div>
                </div>

                <div className="mt-6 pt-6 border-t border-gray-100 text-center">
                    <p className="text-xs text-gray-400">
                        You can change the location anytime from your profile or settings.
                    </p>
                </div>
            </div>
        </div>
    );
};


