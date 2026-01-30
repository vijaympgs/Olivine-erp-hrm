
import React from "react";
import { Play, Terminal, X, RefreshCw, FileCode, AlertCircle, Trash2 } from "lucide-react";
import { ModuleDef } from "../types";

interface RunQueueProps {
    selectedSuites: Set<string>;
    setSelectedSuites: (ids: Set<string>) => void;
    currentModule: ModuleDef | null;
    toggleSuite: (id: string, checked: boolean) => void;
    runTests: () => void;
    isRunning: boolean;
}

export const RunQueue: React.FC<RunQueueProps> = ({
    selectedSuites,
    setSelectedSuites,
    currentModule,
    toggleSuite,
    runTests,
    isRunning
}) => {
    return (
        <div className="flex flex-col h-full bg-slate-50 border-b border-slate-200">
            {/* Header with Actions */}
            <div className="h-10 flex justify-between items-center px-4 border-b border-slate-200 bg-white shrink-0">
                <div className="flex items-center gap-2">
                    <Play size={14} className="text-indigo-600 fill-current" />
                    <span className="text-xs font-bold text-slate-700 uppercase tracking-widest">Run Queue</span>
                    <span className="bg-indigo-100 text-indigo-700 text-[10px] font-bold px-2 py-0.5 rounded-full border border-indigo-200">{selectedSuites.size}</span>
                </div>

                {/* Actions */}
                <div className="flex items-center gap-2">
                    {selectedSuites.size > 0 && (
                        <button
                            onClick={() => setSelectedSuites(new Set())}
                            className="flex items-center gap-1.5 px-3 py-1 text-[10px] font-bold uppercase rounded border border-slate-200 bg-slate-50 text-slate-500 hover:bg-slate-100 hover:text-red-500 transition-colors"
                        >
                            <Trash2 size={12} /> Clear
                        </button>
                    )}
                    <button
                        onClick={runTests}
                        disabled={isRunning || selectedSuites.size === 0}
                        className={`flex items-center gap-2 px-4 py-1.5 text-[10px] font-bold uppercase rounded shadow-sm text-white transition-all
                              ${isRunning || selectedSuites.size === 0 ? 'bg-slate-300 cursor-not-allowed text-slate-500' : 'bg-indigo-600 hover:bg-indigo-700'}
                           `}
                    >
                        {isRunning ? <RefreshCw size={12} className="animate-spin" /> : <Play size={12} className="fill-current" />}
                        {isRunning ? 'Running...' : 'Run Selected'}
                    </button>
                </div>
            </div>

            {/* Content */}
            <div className="flex-1 overflow-y-auto p-4 scrollbar-thin scrollbar-thumb-slate-200">
                {selectedSuites.size === 0 ? (
                    <div className="h-full flex flex-col items-center justify-center text-center opacity-60">
                        <div className="w-16 h-16 rounded-full bg-slate-200/50 flex items-center justify-center mb-4">
                            <Play size={24} className="text-slate-400 ml-1" />
                        </div>
                        <p className="text-sm font-bold text-slate-500 uppercase tracking-wide">No components selected</p>
                        <p className="text-xs text-slate-400 mt-2 font-medium">Select from table on the left<br />to add to execution queue</p>
                    </div>
                ) : (
                    <div className="space-y-2">
                        {Array.from(selectedSuites).map(id => {
                            const suite = currentModule?.suites.find(s => s.menu_id === id);
                            return (
                                <div key={id} className="group flex items-center justify-between p-3 bg-white border border-slate-200 rounded-md shadow-sm hover:border-indigo-300 hover:shadow-md transition-all">
                                    <div className="flex flex-col min-w-0">
                                        <div className="flex items-center gap-2">
                                            <span className="font-bold text-xs text-slate-700">{suite?.name || id}</span>
                                            {suite?.script_path ? (
                                                <span className="w-1.5 h-1.5 rounded-full bg-emerald-500" title="Script Available" />
                                            ) : (
                                                <span className="w-1.5 h-1.5 rounded-full bg-amber-400" title="No Script" />
                                            )}
                                        </div>
                                        <span className="truncate text-[10px] text-slate-400 font-mono mt-0.5">{suite?.script_path ? suite.script_path.split('/').pop() : 'No script mapped'}</span>
                                    </div>
                                    <button onClick={() => toggleSuite(id, false)} className="p-1.5 rounded hover:bg-rose-50 text-slate-300 hover:text-rose-500 shrink-0 opacity-0 group-hover:opacity-100 transition-all">
                                        <X size={14} />
                                    </button>
                                </div>
                            );
                        })}
                    </div>
                )}
            </div>
        </div>
    );
};

interface ConsoleOutputProps {
    executionLogs: string[];
    setExecutionLogs: (logs: string[]) => void;
    isRunning: boolean;
}

export const ConsoleOutput: React.FC<ConsoleOutputProps> = ({
    executionLogs,
    setExecutionLogs,
    isRunning
}) => {
    return (
        <div className="flex flex-col h-full bg-slate-950">
            {/* Header */}
            <div className="h-9 bg-slate-900 border-b border-slate-800 flex items-center justify-between px-4 shrink-0">
                <div className="flex items-center gap-2">
                    <Terminal size={12} className="text-emerald-500" />
                    <span className="text-[10px] font-mono text-slate-400 uppercase tracking-widest">Execution Console</span>
                </div>
                <div className="flex items-center gap-4">
                    <div className="flex items-center gap-2 text-[10px] text-slate-600 font-mono">
                        <span className={`w-1.5 h-1.5 rounded-full ${isRunning ? 'bg-amber-500 animate-pulse' : 'bg-emerald-500'}`}></span>
                        {isRunning ? 'Executing' : 'Idle'}
                    </div>
                    <button onClick={() => setExecutionLogs([])} className="text-[10px] font-bold text-slate-600 hover:text-slate-300 uppercase tracking-wider transition-colors">Clear</button>
                </div>
            </div>

            {/* Logs */}
            <div className="flex-1 overflow-y-auto p-4 font-mono text-xs text-slate-300 whitespace-pre-wrap leading-relaxed scrollbar-thin scrollbar-thumb-slate-700 scrollbar-track-transparent">
                {executionLogs.length === 0 && (
                    <div className="h-full flex flex-col items-center justify-center text-slate-800 opacity-20 select-none">
                        <Terminal size={48} />
                    </div>
                )}
                {executionLogs.map((log, i) => (
                    <div key={i} className="mb-0.5 break-all border-l-2 border-transparent hover:border-slate-800 pl-2 -ml-2 transition-colors">
                        {log.includes("[RUNNING]") ? (
                            <span className="text-indigo-400 font-bold">{log}</span>
                        ) : log.includes("[WARN]") ? (
                            <span className="text-amber-400">{log}</span>
                        ) : log.includes("Error") ? (
                            <span className="text-rose-400 font-bold">{log}</span>
                        ) : log.startsWith(">") ? (
                            <span className="text-emerald-400 font-bold">{log}</span>
                        ) : log.includes("File:") ? (
                            <span className="text-slate-500 italic">{log}</span>
                        ) : (
                            <span className="text-slate-300">{log}</span>
                        )}
                    </div>
                ))}
            </div>
        </div>
    );
};

