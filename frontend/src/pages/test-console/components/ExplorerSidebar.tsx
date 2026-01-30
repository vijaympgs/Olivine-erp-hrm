
import React from "react";
import { Box, ChevronDown, ChevronRight, Folder } from "lucide-react";
import { ApplicationDef } from "../types";

interface ExplorerSidebarProps {
    consoleData: Record<string, ApplicationDef>;
    expandedNodes: Set<string>;
    setExpandedNodes: (nodes: Set<string>) => void;
    selectedApp: string | null;
    setSelectedApp: (appId: string) => void;
    selectedModuleId: string | null;
    setSelectedModuleId: (modId: string) => void;
}

export const ExplorerSidebar: React.FC<ExplorerSidebarProps> = ({
    consoleData,
    expandedNodes,
    setExpandedNodes,
    selectedApp,
    setSelectedApp,
    selectedModuleId,
    setSelectedModuleId
}) => {
    return (
        <div className="w-[240px] bg-slate-100 border-r border-slate-200 flex flex-col shrink-0 transition-all">
            {/* Header */}
            <div className="h-14 flex items-center justify-between px-4 border-b border-slate-200 bg-white/50 backdrop-blur-sm shrink-0">
                <div className="flex items-center gap-2 text-slate-600">
                    <Box size={16} />
                    <span className="font-bold text-xs uppercase tracking-widest text-slate-500">Explorer</span>
                </div>
            </div>

            {/* Tree Content */}
            <div className="flex-1 overflow-y-auto p-2 scrollbar-thin scrollbar-thumb-slate-300">
                {Object.values(consoleData).map(app => (
                    <div key={app.id} className="mb-1 select-none">
                        <div
                            className={`flex items-center gap-2 px-2 py-1.5 rounded cursor-pointer transition-colors
                                ${expandedNodes.has(app.id) ? 'bg-slate-200/50 text-slate-800' : 'text-slate-600 hover:bg-slate-200'}
                            `}
                            onClick={() => {
                                const next = new Set(expandedNodes);
                                if (next.has(app.id)) next.delete(app.id); else next.add(app.id);
                                setExpandedNodes(next);
                            }}
                        >
                            <button className="p-0.5 hover:bg-slate-300 rounded text-slate-400">
                                {expandedNodes.has(app.id) ? <ChevronDown size={14} /> : <ChevronRight size={14} />}
                            </button>
                            <span className="text-indigo-600">{app.icon}</span>
                            <span className="text-xs font-bold truncate tracking-tight">{app.label}</span>
                        </div>

                        {expandedNodes.has(app.id) && (
                            <div className="ml-[22px] border-l border-slate-300/50 pl-2 mt-0.5 space-y-0.5">
                                {app.modules.length === 0 && <div className="text-[10px] text-slate-400 italic px-2 py-1">No modules</div>}
                                {app.modules.map(mod => (
                                    <div
                                        key={mod.id}
                                        onClick={() => { setSelectedApp(app.id); setSelectedModuleId(mod.id); }}
                                        className={`flex items-center gap-2 px-2 py-1.5 rounded cursor-pointer text-xs transition-all border border-transparent
                                            ${selectedModuleId === mod.id
                                                ? 'bg-white border-slate-200 shadow-sm text-indigo-700 font-bold'
                                                : 'text-slate-600 hover:bg-slate-200 hover:text-slate-800'}
                                        `}
                                    >
                                        <Folder size={12} className={selectedModuleId === mod.id ? "text-indigo-500 fill-indigo-50" : "text-slate-400"} />
                                        <span className="truncate">{mod.label}</span>
                                    </div>
                                ))}
                            </div>
                        )}
                    </div>
                ))}
            </div>

            {/* Footer Info */}
            <div className="p-3 border-t border-slate-200 bg-slate-100 text-[10px] text-slate-400 text-center">
                Enterprise QA Console v2.4
            </div>
        </div>
    );
};

