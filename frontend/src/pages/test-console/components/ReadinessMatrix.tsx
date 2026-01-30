
import React from "react";
import { Play, Filter } from "lucide-react";
import { EnrichedSuite } from "../types";

interface ReadinessMatrixProps {
    consoleData: any; // Using any to avoid circular dep issues deeply, or import proper type
    currentModule: any;
    filteredSuites: EnrichedSuite[];
    selectedIds: Set<string>;
    toggleSelection: (id: string, checked?: boolean) => void;
    setSelectedIds: (ids: Set<string>) => void;
    uiFilter: string;
    setUiFilter: (val: string) => void;
    scriptFilter: string;
    setScriptFilter: (val: string) => void;
    bbpFilter: string;
    setBbpFilter: (val: string) => void;
    ditFilter: string;
    setDitFilter: (val: string) => void;
    uatFilter: string;
    setUatFilter: (val: string) => void;
    handleBbpClick: (path: string, name: string) => void;
    handleUatChange: (id: string, val: any) => void;
    StatusBadge: React.FC<{ status: string, type: 'ui' | 'dit' | 'uat' }>;
}

export const ReadinessMatrix: React.FC<ReadinessMatrixProps> = ({
    filteredSuites,
    selectedIds,
    setSelectedIds,
    toggleSelection,
    uiFilter, setUiFilter,
    scriptFilter, setScriptFilter,
    bbpFilter, setBbpFilter,
    handleBbpClick,
    handleUatChange,
    StatusBadge
}) => {
    return (
        <div className="flex-1 flex flex-col min-h-0 overflow-hidden bg-white">
            {/* Toolbar: Scope & Filters */}
            <div className="border-b border-slate-200 p-2 bg-slate-50/50 flex flex-wrap gap-4 items-center shrink-0">
                {/* Scope Selection */}
                <div className="flex items-center gap-2 pl-2 border-r border-slate-200 pr-4">
                    <span className="text-[10px] font-bold text-slate-500 uppercase tracking-wide">Scope:</span>
                    <button onClick={() => setSelectedIds(new Set(filteredSuites.map(s => s.menu_id)))} className="text-[10px] text-indigo-600 hover:underline">All</button>
                    <span className="text-slate-300">|</span>
                    <button onClick={() => setSelectedIds(new Set())} className="text-[10px] text-slate-400 hover:text-slate-600">None</button>
                </div>

                {/* Filters */}
                <div className="flex items-center gap-2 ml-auto">
                    <Filter size={12} className="text-slate-400" />
                    <div className="flex gap-2 items-center">
                        <select value={scriptFilter} onChange={e => setScriptFilter(e.target.value)} className="text-[10px] border border-slate-200 rounded py-1 pl-1 pr-6 bg-white focus:ring-1 focus:ring-indigo-500 cursor-pointer">
                            <option value="All">Script: All</option>
                            <option value="Available">Script: Available</option>
                            <option value="None">Script: None</option>
                        </select>
                    </div>
                    <div className="flex gap-2 items-center">
                        <select value={bbpFilter} onChange={e => setBbpFilter(e.target.value)} className="text-[10px] border border-slate-200 rounded py-1 pl-1 pr-6 bg-white focus:ring-1 focus:ring-indigo-500 cursor-pointer">
                            <option value="All">BBP: All</option>
                            <option value="Available">BBP: Available</option>
                            <option value="None">BBP: None</option>
                        </select>
                    </div>
                    <div className="flex gap-2 items-center">
                        <select value={uiFilter} onChange={e => setUiFilter(e.target.value)} className="text-[10px] border border-slate-200 rounded py-1 pl-1 pr-6 bg-white focus:ring-1 focus:ring-indigo-500 cursor-pointer">
                            <option value="All">UI: All</option>
                            <option value="Done">UI: Done</option>
                            <option value="Pending">UI: Pending</option>
                        </select>
                    </div>
                    {(uiFilter !== "All" || bbpFilter !== "All" || scriptFilter !== "All") && (
                        <button onClick={() => { setUiFilter("All"); setBbpFilter("All"); setScriptFilter("All"); }} className="text-[10px] text-red-500 hover:underline ml-2">Reset</button>
                    )}
                </div>
            </div>

            {/* Timeline Component */}
            <div className="border-b border-slate-200 py-4 px-8 bg-gradient-to-b from-slate-50 to-white">
                <div className="max-w-3xl mx-auto">
                    <div className="relative flex items-center justify-between">
                        {/* Connecting Line */}
                        <div className="absolute top-[18px] left-0 right-0 h-0.5 bg-slate-200 z-0"></div>

                        {/* Timeline Steps */}
                        <div className="relative flex-1 flex items-center justify-between z-10">
                            {/* Step 1: BBP */}
                            <div className="flex flex-col items-center">
                                <div className="w-9 h-9 rounded-full bg-slate-900 border-2 border-slate-900 flex items-center justify-center font-bold text-white shadow-sm">
                                    1
                                </div>
                                <div className="mt-2 text-xs font-semibold text-slate-700">BBP</div>
                            </div>

                            {/* Step 2: UI */}
                            <div className="flex flex-col items-center">
                                <div className="w-9 h-9 rounded-full bg-slate-900 border-2 border-slate-900 flex items-center justify-center font-bold text-white shadow-sm">
                                    2
                                </div>
                                <div className="mt-2 text-xs font-semibold text-slate-700">UI</div>
                            </div>

                            {/* Step 3: TS */}
                            <div className="flex flex-col items-center">
                                <div className="w-9 h-9 rounded-full bg-slate-900 border-2 border-slate-900 flex items-center justify-center font-bold text-white shadow-sm">
                                    3
                                </div>
                                <div className="mt-2 text-xs font-semibold text-slate-700">TS</div>
                            </div>

                            {/* Step 4: DIT */}
                            <div className="flex flex-col items-center">
                                <div className="w-9 h-9 rounded-full bg-slate-900 border-2 border-slate-900 flex items-center justify-center font-bold text-white shadow-sm">
                                    4
                                </div>
                                <div className="mt-2 text-xs font-semibold text-slate-700">DIT</div>
                            </div>

                            {/* Step 5: UAT */}
                            <div className="flex flex-col items-center">
                                <div className="w-9 h-9 rounded-full bg-slate-900 border-2 border-slate-900 flex items-center justify-center font-bold text-white shadow-sm">
                                    5
                                </div>
                                <div className="mt-2 text-xs font-semibold text-slate-700">UAT</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            {/* Table Content */}
            <div className="flex-1 overflow-auto">
                <table className="w-full text-left border-collapse">
                    <thead className="bg-slate-50 sticky top-0 z-10 text-[10px] uppercase font-bold text-slate-500 tracking-wider border-b border-slate-200 shadow-sm">
                        <tr>
                            <th className="p-2 w-[40px] text-center">
                                <input
                                    type="checkbox"
                                    className="rounded border-slate-300 text-indigo-600 focus:ring-indigo-500"
                                    checked={filteredSuites.length > 0 && selectedIds.size === filteredSuites.length}
                                    onChange={() => {
                                        if (selectedIds.size === filteredSuites.length) setSelectedIds(new Set());
                                        else setSelectedIds(new Set(filteredSuites.map(s => s.menu_id)));
                                    }}
                                />
                            </th>
                            <th className="p-3 pl-2">Component</th>
                            <th className="text-center p-2 w-[50px]">BBP</th>
                            <th className="text-center p-2 w-[50px]">UI</th>
                            <th className="text-center p-2 w-[50px]">TS</th>
                            <th className="text-center p-2 w-[50px]">DIT</th>
                            <th className="text-center p-2 w-[50px]">UAT</th>
                        </tr>
                    </thead>
                    <tbody className="divide-y divide-slate-50">
                        {filteredSuites.map((suite) => (
                            <tr
                                key={suite.menu_id}
                                onClick={() => toggleSelection(suite.menu_id)}
                                className={`hover:bg-slate-50 border-b border-slate-50 transition-colors cursor-pointer ${selectedIds.has(suite.menu_id) ? 'bg-indigo-50/30' : ''}`}
                            >
                                <td className="py-0.5 px-1 text-center w-[30px]">
                                    <input
                                        type="checkbox"
                                        checked={selectedIds.has(suite.menu_id)}
                                        onChange={(e) => { e.stopPropagation(); toggleSelection(suite.menu_id, e.target.checked); }}
                                        className="rounded border-slate-300 text-indigo-600 focus:ring-indigo-500 scale-75"
                                    />
                                </td>
                                <td className="py-1 px-2">
                                    <div className="font-bold text-slate-700 text-[11px] truncate">{suite.name}</div>
                                </td>
                                <td className="py-1 text-center">
                                    {suite.bbp_path ? (
                                        <button
                                            className="text-blue-600 hover:text-blue-800 font-bold text-[10px]"
                                            onClick={() => handleBbpClick(suite.bbp_path!, suite.name)}
                                        >Yes</button>
                                    ) : <span className="text-slate-200 text-[10px]">No</span>}
                                </td>
                                <td className="py-1 text-center"><StatusBadge status={suite.ui_status} type="ui" /></td>
                                <td className="py-1 text-center">
                                    {suite.script_path ? (
                                        <span className="text-emerald-600 font-bold text-[10px]">Yes</span>
                                    ) : <span className="text-slate-200 text-[10px]">No</span>}
                                </td>
                                <td className="py-1 text-center"><StatusBadge status={suite.dit_status} type="dit" /></td>
                                <td className="py-1 text-center">
                                    <select
                                        value={suite.uat_status}
                                        onChange={(e) => handleUatChange(suite.menu_id, e.target.value as any)}
                                        className={`w-full text-[10px] border-none py-0 text-center bg-transparent appearance-none cursor-pointer font-bold focus:ring-0
                                            ${suite.uat_status === 'Complete' ? 'text-emerald-600' :
                                                suite.uat_status === 'InProgress' ? 'text-amber-500' : 'text-slate-200'}
                                        `}
                                    >
                                        <option value="Not Started" className="text-slate-500">No</option>
                                        <option value="InProgress" className="text-amber-500">WIP</option>
                                        <option value="Complete" className="text-emerald-600">Yes</option>
                                    </select>
                                </td>
                            </tr>
                        ))}
                        {filteredSuites.length === 0 && (
                            <tr><td colSpan={7} className="p-8 text-center text-slate-400 text-xs italic">No components match filters</td></tr>
                        )}
                    </tbody>
                </table>
            </div>
        </div>
    );
};

