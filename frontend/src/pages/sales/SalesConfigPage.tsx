import React, { useState } from "react";
import { Save, Info, Plus, Trash2 } from "lucide-react";

const SalesConfigPage: React.FC = () => {
    // Mock State for Settings
    const [settings, setSettings] = useState({
        quote_enabled: true,
        quote_required_for_order: false,
        returns_enabled: true,
        credit_check_enabled: true,
        max_discount_percent: 10,
        price_override_allowed: false,
    });

    // Mock State for Approval Matrix
    const [approvals, setApprovals] = useState([
        { id: 1, module: 'QUOTE', role: 'Sales Manager', min_amount: 0, max_amount: 5000 },
        { id: 2, module: 'QUOTE', role: 'Director', min_amount: 5000, max_amount: 100000 },
    ]);

    const handleSettingChange = (key: string, value: any) => {
        setSettings(prev => ({ ...prev, [key]: value }));
    };

    return (
        <div className="flex flex-col h-full bg-[#faf9f8] overflow-hidden">
            {/* Page Title */}
            <div className="px-6 py-4 border-b border-[#edebe9] bg-white shrink-0">
                <div className="flex justify-between items-center">
                    <div>
                        <h1 className="text-xl font-semibold text-[#201f1e]">Sales Configuration</h1>
                        <p className="text-xs text-[#605e5c] mt-1">Manage sales process rules and governance</p>
                    </div>
                    <button className="flex items-center gap-2 px-3 py-1.5 bg-[#0078d4] text-white font-medium hover:bg-[#106ebe] transition-colors rounded-sm">
                        <Save size={16} /> Save Changes
                    </button>
                </div>
            </div>

            <div className="flex-1 overflow-auto p-6">
                <div className="max-w-4xl mx-auto space-y-6">

                    {/* 1. Process Settings Card */}
                    <div className="bg-white p-6 border border-[#edebe9] shadow-sm rounded-sm">
                        <h2 className="text-lg font-semibold text-[#201f1e] mb-4 pb-2 border-b border-[#edebe9]">Process Controls</h2>

                        <div className="grid grid-cols-2 gap-8">
                            <div className="space-y-4">
                                {/* Quote Enabled */}
                                <div className="flex items-center justify-between">
                                    <div>
                                        <p className="font-medium text-[#323130]">Enable Quotes</p>
                                        <p className="text-xs text-[#605e5c]">Allow creating quotes/estimates</p>
                                    </div>
                                    <label className="relative inline-flex items-center cursor-pointer">
                                        <input type="checkbox" checked={settings.quote_enabled} onChange={(e) => handleSettingChange('quote_enabled', e.target.checked)} className="sr-only peer" />
                                        <div className="w-11 h-6 bg-gray-200 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-[#0078d4]"></div>
                                    </label>
                                </div>

                                {/* Order Requirements */}
                                <div className="flex items-center justify-between">
                                    <div>
                                        <p className="font-medium text-[#323130]">Quote Required for Order</p>
                                        <p className="text-xs text-[#605e5c]">Enforce Quote {'->'} Order workflow</p>
                                    </div>
                                    <label className="relative inline-flex items-center cursor-pointer">
                                        <input type="checkbox" checked={settings.quote_required_for_order} onChange={(e) => handleSettingChange('quote_required_for_order', e.target.checked)} className="sr-only peer" />
                                        <div className="w-11 h-6 bg-gray-200 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-[#0078d4]"></div>
                                    </label>
                                </div>

                                {/* Credit Check */}
                                <div className="flex items-center justify-between">
                                    <div>
                                        <p className="font-medium text-[#323130]">Credit Limit Check</p>
                                        <p className="text-xs text-[#605e5c]">Validate customer credit on order</p>
                                    </div>
                                    <label className="relative inline-flex items-center cursor-pointer">
                                        <input type="checkbox" checked={settings.credit_check_enabled} onChange={(e) => handleSettingChange('credit_check_enabled', e.target.checked)} className="sr-only peer" />
                                        <div className="w-11 h-6 bg-gray-200 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-[#0078d4]"></div>
                                    </label>
                                </div>
                            </div>

                            <div className="space-y-4">
                                {/* Price Override */}
                                <div className="flex items-center justify-between">
                                    <div>
                                        <p className="font-medium text-[#323130]">Allow Price Override</p>
                                        <p className="text-xs text-[#605e5c]">Reps can change unit prices</p>
                                    </div>
                                    <label className="relative inline-flex items-center cursor-pointer">
                                        <input type="checkbox" checked={settings.price_override_allowed} onChange={(e) => handleSettingChange('price_override_allowed', e.target.checked)} className="sr-only peer" />
                                        <div className="w-11 h-6 bg-gray-200 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-[#0078d4]"></div>
                                    </label>
                                </div>

                                {/* Max Discount */}
                                <div>
                                    <label className="block text-xs font-semibold text-[#605e5c] uppercase mb-1">Max Manual Discount (%)</label>
                                    <div className="flex items-center gap-2">
                                        <input
                                            type="number"
                                            value={settings.max_discount_percent}
                                            onChange={(e) => handleSettingChange('max_discount_percent', parseFloat(e.target.value))}
                                            className="border border-[#8a8886] p-1.5 w-24 text-sm focus:border-[#0078d4] outline-none"
                                        />
                                        <span className="text-sm text-[#605e5c]">%</span>
                                    </div>
                                    <p className="text-xs text-[#a19f9d] mt-1">Discounts above this require approval.</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    {/* 2. Approval Matrix Card */}
                    <div className="bg-white p-6 border border-[#edebe9] shadow-sm rounded-sm">
                        <div className="flex justify-between items-center mb-4 pb-2 border-b border-[#edebe9]">
                            <h2 className="text-lg font-semibold text-[#201f1e]">Approval Matrix</h2>
                            <button className="flex items-center gap-1 text-[#0078d4] hover:underline text-sm font-medium">
                                <Plus size={14} /> Add Pattern
                            </button>
                        </div>

                        <div className="overflow-x-auto">
                            <table className="w-full text-sm text-left">
                                <thead className="bg-[#f3f2f1] text-[#605e5c] font-semibold uppercase text-xs">
                                    <tr>
                                        <th className="p-2 border-b">Module</th>
                                        <th className="p-2 border-b">Role / Approver</th>
                                        <th className="p-2 border-b text-right">Min Amount</th>
                                        <th className="p-2 border-b text-right">Max Amount</th>
                                        <th className="p-2 border-b w-10"></th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {approvals.map((rule) => (
                                        <tr key={rule.id} className="border-b border-[#edebe9]">
                                            <td className="p-2 font-medium">{rule.module}</td>
                                            <td className="p-2">{rule.role}</td>
                                            <td className="p-2 text-right">${rule.min_amount.toLocaleString()}</td>
                                            <td className="p-2 text-right">${rule.max_amount.toLocaleString()}</td>
                                            <td className="p-2 text-center text-gray-400 hover:text-red-600 cursor-pointer">
                                                <Trash2 size={14} />
                                            </td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    );
};

export default SalesConfigPage;

