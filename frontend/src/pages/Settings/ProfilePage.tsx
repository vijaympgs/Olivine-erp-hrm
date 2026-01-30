import React, { useState, useEffect } from "react";
import { useAuth } from "../../auth/useAuth";
import { Button } from "@ui/Button";
import { Input } from "@ui/Input";
import {
    User, Mail, Phone, Lock,
    Shield, MapPin, Bell, Eye, EyeOff, Save
} from "lucide-react";
import { useGlobalLocation } from "../../core/contexts/GlobalLocationContext";

export const ProfilePage: React.FC = () => {
    const { user, isLoading, updateProfile, logout } = useAuth();
    const { currentLocationName, currentLocationCode } = useGlobalLocation();

    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [email, setEmail] = useState('');
    const [phone, setPhone] = useState('');
    const [role, setRole] = useState('');

    // UI State
    const [isEditing, setIsEditing] = useState(false);
    const [isSaving, setIsSaving] = useState(false); // Add Loading state
    const [activeTab, setActiveTab] = useState<'profile' | 'security' | 'preferences' | 'context' | 'sessions' | 'notifications' | 'audit' | 'accessibility'>('profile');

    useEffect(() => {
        if (user) {
            // Split name if needed or use directly if available
            const names = user.name?.split(' ') || ['', ''];
            setFirstName(names[0] || '');
            setLastName(names.slice(1).join(' ') || '');
            setEmail(user.email || '');
            setRole(user.role || 'User');
            // Assuming phone isn't in default user token yet, keep empty or fetch if extended
        }
    }, [user]);

    const handleSave = async (e: React.FormEvent) => {
        e.preventDefault();
        setIsSaving(true);
        try {
            await updateProfile({
                first_name: firstName,
                last_name: lastName,
                // phone: phone // Backend needs to support this field on User model or OneToOne profile
            } as any);
            setIsEditing(false);
        } catch (error) {
            console.error(error);
            alert("Failed to update profile");
        } finally {
            setIsSaving(false);
        }
    };

    const handleLogout = () => {
        if (window.confirm("Are you sure you want to log out?")) {
            logout();
        }
    };

    if (isLoading) return <div className="p-8">Loading profile...</div>;

    return (
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            <div className="mb-8">
                <h1 className="text-2xl font-bold text-gray-900">User Profile</h1>
                <p className="text-sm text-gray-500 mt-1">Manage your account settings and preferences.</p>
            </div>

            <div className="flex flex-col lg:flex-row gap-8">
                {/* Left Sidebar: Mindra Human Card Style */}
                <div className="w-full lg:w-80 flex-shrink-0">
                    <div className="bg-white shadow-sm rounded-none border-r border-gray-100 flex flex-col h-full min-h-[600px]">
                        {/* Profile Header */}
                        <div className="p-8 pb-4 text-center border-b border-gray-50">
                            <div className="h-20 w-20 mx-auto bg-gray-100 rounded-none flex items-center justify-center text-2xl font-semibold text-gray-500 mb-4">
                                {firstName?.[0]}{lastName?.[0]}
                            </div>
                            <h2 className="text-lg font-medium text-gray-900">{user?.name}</h2>
                            <p className="text-sm text-gray-400 mt-1">{role} • {email}</p>
                        </div>

                        {/* Navigation Menu (Text-Only, Generous Spacing) */}
                        <nav className="flex-1 overflow-y-auto py-6 space-y-1">
                            {[
                                { id: 'profile', label: 'Personal Details' },
                                { id: 'context', label: 'Work Context' },
                                { id: 'preferences', label: 'Preferences' },
                                { id: 'security', label: 'Security' },
                                { id: 'sessions', label: 'Active Sessions' },
                                { id: 'notifications', label: 'Notifications' },
                                { id: 'accessibility', label: 'Accessibility', disabled: true },
                                { id: 'audit', label: 'Audit & Activity', disabled: true },
                            ].map((item) => (
                                <button
                                    key={item.id}
                                    onClick={() => !item.disabled && setActiveTab(item.id as any)}
                                    disabled={item.disabled}
                                    className={`w-full text-left px-8 py-3 text-sm transition-colors duration-200 ${activeTab === item.id
                                        ? 'text-gray-900 font-medium bg-gray-50 border-l-2 border-gray-900'
                                        : 'text-gray-500 hover:bg-gray-50 hover:text-gray-700 border-l-2 border-transparent'
                                        } ${item.disabled ? 'opacity-40 cursor-not-allowed' : ''}`}
                                >
                                    {item.label}
                                </button>
                            ))}
                        </nav>

                        {/* Bottom Action: Logout */}
                        <div className="p-6 border-t border-gray-50 mt-auto">
                            <button
                                onClick={handleLogout}
                                className="w-full text-left px-2 py-3 text-sm font-medium text-red-600 hover:bg-red-50 transition-colors rounded-none"
                            >
                                Log Out
                            </button>
                        </div>
                    </div>
                </div>

                {/* Right Content Area */}
                <div className="w-full lg:w-2/3">
                    <div className="bg-white rounded-none shadow-sm border border-gray-100 min-h-[600px] h-full">

                        {/* Tab: Personal Information */}
                        {activeTab === 'profile' && (
                            <div className="p-8">
                                <div className="flex items-center justify-between mb-8 pb-4 border-b border-gray-50">
                                    <h3 className="text-xl font-light text-gray-900">Personal Details</h3>
                                    {!isEditing && (
                                        <Button
                                            variant="outline"
                                            onClick={() => setIsEditing(true)}
                                            className="rounded-none border-gray-300"
                                        >
                                            Edit Details
                                        </Button>
                                    )}
                                </div>
                                <form onSubmit={handleSave} className="max-w-3xl space-y-8">
                                    <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                                        <div className="space-y-2">
                                            <label className="text-xs font-semibold text-gray-400 uppercase tracking-wider">First Name</label>
                                            <Input
                                                value={firstName}
                                                onChange={e => setFirstName(e.target.value)}
                                                disabled={!isEditing}
                                                className="w-full rounded-none border-gray-200 focus:border-gray-900 focus:ring-0 transition-all py-2.5 bg-gray-50/50"
                                            />
                                        </div>
                                        <div className="space-y-2">
                                            <label className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Last Name</label>
                                            <Input
                                                value={lastName}
                                                onChange={e => setLastName(e.target.value)}
                                                disabled={!isEditing}
                                                className="w-full rounded-none border-gray-200 focus:border-gray-900 focus:ring-0 transition-all py-2.5 bg-gray-50/50"
                                            />
                                        </div>
                                    </div>

                                    <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                                        <div className="space-y-2">
                                            <label className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Email Address</label>
                                            <div className="relative">
                                                <Input
                                                    value={email}
                                                    readOnly
                                                    disabled
                                                    className="w-full rounded-none border-transparent bg-transparent pl-0 text-gray-500"
                                                />
                                                <p className="text-[10px] text-gray-300 mt-1">Managed by Admin</p>
                                            </div>
                                        </div>
                                        <div className="space-y-2">
                                            <label className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Phone</label>
                                            <Input
                                                value={phone}
                                                onChange={e => setPhone(e.target.value)}
                                                disabled={!isEditing}
                                                placeholder="+91..."
                                                className="w-full rounded-none border-gray-200 focus:border-gray-900 focus:ring-0 transition-all py-2.5 bg-gray-50/50"
                                            />
                                        </div>
                                    </div>

                                    {isEditing && (
                                        <div className="flex items-center gap-4 pt-8 mt-4">
                                            <Button
                                                type="submit"
                                                disabled={isSaving}
                                                className="rounded-none bg-gray-900 text-white hover:bg-black px-8 py-2.5"
                                            >
                                                {isSaving ? 'Saving...' : 'Save Changes'}
                                            </Button>
                                            <Button
                                                variant="ghost"
                                                onClick={() => setIsEditing(false)}
                                                disabled={isSaving}
                                                className="rounded-none text-gray-500 hover:text-gray-900"
                                            >
                                                Cancel
                                            </Button>
                                        </div>
                                    )}
                                </form>
                            </div>
                        )}

                        {/* Tab: Work Context */}
                        {activeTab === 'context' && (
                            <div className="p-6">
                                <h3 className="text-lg font-medium text-gray-900 mb-6">Work Context</h3>
                                <div className="bg-blue-50 border border-blue-100 rounded-md p-6 flex items-start space-x-4">
                                    <div className="p-2 bg-blue-100 rounded-full">
                                        <MapPin className="w-6 h-6 text-blue-600" />
                                    </div>
                                    <div>
                                        <p className="text-sm font-medium text-blue-900">
                                            Current Location: {currentLocationName || 'Unknown'}
                                            {currentLocationCode && <span className="opacity-75"> ({currentLocationCode})</span>}
                                        </p>
                                        <p className="text-sm text-blue-700 mt-2">
                                            This location is set for your current session only. All transactions and records created will be associated with this location.
                                        </p>
                                    </div>
                                </div>
                            </div>
                        )}

                        {/* Tab: Security */}
                        {activeTab === 'security' && (
                            <div className="p-6">
                                <h3 className="text-lg font-medium text-gray-900 mb-6">Security Settings</h3>
                                <div className="space-y-6">
                                    <div className="bg-yellow-50 border border-yellow-100 rounded-md p-4">
                                        <div className="flex">
                                            <Lock className="h-5 w-5 text-yellow-400" />
                                            <div className="ml-3">
                                                <h3 className="text-sm font-medium text-yellow-800">Password Management</h3>
                                                <div className="mt-2 text-sm text-yellow-700">
                                                    <p>Password changes are currently managed by your organization's administrator.</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        )}

                        {/* Tab: Active Sessions */}
                        {activeTab === 'sessions' && (
                            <div className="p-6">
                                <h3 className="text-lg font-medium text-gray-900 mb-6">Active Sessions</h3>
                                <div className="border rounded-md p-4">
                                    <p className="text-sm font-medium text-gray-900">Current Session</p>
                                    <p className="text-sm text-gray-500">You are currently logged in from this device.</p>
                                </div>
                            </div>
                        )}

                        {/* Tab: Preferences */}
                        {(activeTab === 'preferences' || activeTab === 'notifications') && (
                            <div className="p-6">
                                <h3 className="text-lg font-medium text-gray-900 mb-6">{activeTab === 'notifications' ? 'Notifications' : 'Preferences'}</h3>
                                <div className="text-center py-12 text-gray-400">
                                    <Bell className="w-12 h-12 mx-auto mb-3 opacity-20" />
                                    <p>Settings coming soon.</p>
                                </div>
                            </div>
                        )}

                    </div>
                </div>
            </div>
        </div>
    );
};

