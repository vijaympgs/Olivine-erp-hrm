
import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { RefreshCw, Download, Folder, Box, X, ChevronRight, FileCode } from "lucide-react";
import { menuConfig, MenuItem } from "@app/menuConfig";
import { fetchReadiness, syncReadinessEntries, TestReadinessEntry } from "@services/qaService";
import { layoutManager } from "@config/layoutConfig";
import { ExplorerSidebar } from "./test-console/components/ExplorerSidebar";
import { ReadinessMatrix } from "./test-console/components/ReadinessMatrix";
import { RunQueue, ConsoleOutput } from "./test-console/components/ExecutionConsole";
import { ApplicationDef, ModuleDef, EnrichedSuite } from "./test-console/types";

// --- Types ---
// Helper to transform Menu Structure into Explorer structure
const mapMenuToConsoleData = (menu: MenuItem[]): Record<string, ApplicationDef> => {
    const data: Record<string, ApplicationDef> = {};
    menu.forEach(item => {
        if (item.children) {
            // Level 1: Application (e.g., Procurement, Inventory)
            data[item.id] = {
                id: item.id,
                label: item.label,
                icon: <Box size={14} />,
                description: "Application Module",
                modules: item.children.map(sub => ({
                    id: sub.id,
                    label: sub.label,
                    suites: [] // Will be populated with flat components list + API data
                }))
            };
        }
    });
    return data;
};

const flattenSuites = (items: MenuItem[], parentPath: string = ''): MenuItem[] => {
    let result: MenuItem[] = [];
    items.forEach(item => {
        const fullPath = parentPath ? `${parentPath} > ${item.label}` : item.label;
        if (item.path) { // It's a leaf/screen
            result.push({ ...item, label: item.label, path: fullPath } as MenuItem); // Store full path for breadcrumbs
        }
        if (item.children) {
            result = result.concat(flattenSuites(item.children, fullPath));
        }
    });
    return result;
};


// --- Component ---
export const TestConsolePage: React.FC = () => {
    const navigate = useNavigate();

    // 1. Explorer State
    const [consoleData, setConsoleData] = useState<Record<string, ApplicationDef>>({});
    const [selectedApp, setSelectedApp] = useState<string | null>(null);
    const [selectedModuleId, setSelectedModuleId] = useState<string | null>(null);
    const [expandedNodes, setExpandedNodes] = useState<Set<string>>(new Set());

    // 2. Data State
    const [entries, setEntries] = useState<TestReadinessEntry[]>([]);
    const [loading, setLoading] = useState(false);
    const [refreshing, setRefreshing] = useState(false);

    // 3. UI State
    // 3. UI State
    const [selectedSuites, setSelectedSuites] = useState<Set<string>>(new Set());
    const [executionLogs, setExecutionLogs] = useState<string[]>([]);
    const [isRunning, setIsRunning] = useState(false);

    // 4. Modals
    const [isPromptModalOpen, setIsPromptModalOpen] = useState(false);
    const [generatedPrompt, setGeneratedPrompt] = useState('');
    const [isBbpModalOpen, setIsBbpModalOpen] = useState(false);
    const [bbpContent, setBbpContent] = useState('');
    const [bbpTitle, setBbpTitle] = useState('');



    // 5. Filters
    const [uiFilter, setUiFilter] = useState("All");
    const [scriptFilter, setScriptFilter] = useState("All");
    const [bbpFilter, setBbpFilter] = useState("All");
    const [ditFilter, setDitFilter] = useState("All");
    const [uatFilter, setUatFilter] = useState("All");

    // Initialize Menu Data
    useEffect(() => {
        const config = layoutManager.getConfig();
        const options = config.sidebar.testConsoleOptions;

        // Filter menuConfig based on layout settings
        const filteredMenu = menuConfig.filter(item => {
            if (item.id === 'retail') return options.showRetail;
            if (item.id === 'finance') return options.showFinance;
            if (item.id === 'crm') return options.showCRM;
            if (item.id === 'hr') return options.showHRM;
            if (item.id === 'productivity' || item.id === 'meet') return options.showMeet;
            // Keep other items (e.g., Administration) if they don't have a specific toggle
            // or if you want to be strict, default to false.
            // For now, let's allow items that aren't explicitly toggled.
            return true;
        }).filter(item => !item.divider); // Also filter out dividers if they end up at top level

        const initialData = mapMenuToConsoleData(filteredMenu);

        // Expand first app by default
        const firstAppKey = Object.keys(initialData)[0];
        if (firstAppKey) {
            setExpandedNodes(new Set([firstAppKey]));
        }

        setConsoleData(initialData);
        loadReadinessData(initialData);
    }, []);

    const loadReadinessData = async (structure: Record<string, ApplicationDef>) => {
        setLoading(true);
        try {
            const data = await fetchReadiness();
            setEntries(data);
            mergeDataIntoStructure(structure, data);
        } catch (err) {
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    const mergeDataIntoStructure = (structure: Record<string, ApplicationDef>, items: TestReadinessEntry[]) => {
        const nextStructure = { ...structure };

        // We need to map flat API entries to the hierarchical menu structure
        // Iterating menu config again to match IDs is safest
        menuConfig.forEach(app => {
            if (app.children && nextStructure[app.id]) {
                app.children.forEach(mod => {
                    const moduleDef = nextStructure[app.id].modules.find(m => m.id === mod.id);
                    if (moduleDef) {
                        // Get all leaf components for this module
                        const leafComponents = flattenSuites(mod.children || [], `${app.label} > ${mod.label}`);

                        // Map them to API data
                        moduleDef.suites = leafComponents.map(comp => {
                            const entry = items.find(e => e.menu_id === comp.id) || {
                                menu_id: comp.id,
                                module: mod.id,
                                ui_status: 'Pending',
                                dit_status: 'Pending',
                                uat_status: 'Not Started',
                                last_updated: new Date().toISOString(),
                                bbp_path: null,
                                script_path: null
                            };
                            return {
                                ...entry,
                                name: comp.label,
                                path: comp.path || comp.label // flattened path
                            } as EnrichedSuite;
                        });
                    }
                });
            }
        });
        setConsoleData(nextStructure);
    };

    // Derived State
    const currentApp = selectedApp ? consoleData[selectedApp] : null;
    const currentModule = (currentApp && selectedModuleId) ? currentApp.modules.find(m => m.id === selectedModuleId) || null : null;


    // Filter Logic
    const getFilteredSuites = (): EnrichedSuite[] => {
        if (!currentModule) return [];
        return currentModule.suites.filter(suite => {
            if (uiFilter !== "All" && suite.ui_status !== uiFilter) return false;
            // Script Filter
            if (scriptFilter === "Available" && !suite.script_path) return false;
            if (scriptFilter === "None" && suite.script_path) return false;
            // BBP Filter
            if (bbpFilter === "Available" && !suite.bbp_path) return false;
            if (bbpFilter === "None" && suite.bbp_path) return false;

            return true;
        });
    };

    const filteredSuites = getFilteredSuites();

    // Handlers
    const toggleSuite = (id: string, checked?: boolean) => {
        const next = new Set(selectedSuites);
        // If checked is provided, specific set/unset. If undefined, toggle.
        if (checked === false) {
            next.delete(id);
        } else if (checked === true) {
            next.add(id);
        } else {
            // Toggle
            if (next.has(id)) next.delete(id); else next.add(id);
        }
        setSelectedSuites(next);
    };

    const handleRefreshScripts = async () => {
        setRefreshing(true);
        try {
            // 1. First sync standard readiness entries
            const flatMenu = flattenSuites(menuConfig); // Need all leaf IDs
            const missingEntries: Partial<TestReadinessEntry>[] = [];

            // Re-scan menu to find newly added items not in DB
            // (Simplified sync logic)
            // Ideally backend handles this, but here we just trigger refresh endpoint

            // 2. Call backend to scan file system
            const response = await fetch('/api/qa/readiness/refresh_scripts/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
            });

            if (response.ok) {
                const data = await response.json();
                setExecutionLogs(prev => [...prev, `> Synced ${data.updated_count} scripts.`]);
                // Reload data
                loadReadinessData(consoleData);
            } else {
                setExecutionLogs(prev => [...prev, `[Error] Failed to sync scripts: ${response.statusText}`]);
            }
        } catch (error) {
            console.error(error);
            setExecutionLogs(prev => [...prev, `[Error] Sync exception.`]);
        } finally {
            setRefreshing(false);
        }
    };

    const handleUatChange = async (menuId: string, newStatus: TestReadinessEntry['uat_status']) => {
        // Optimistic update
        const updatedEntries = entries.map(e => e.menu_id === menuId ? { ...e, uat_status: newStatus } : e);
        setEntries(updatedEntries);
        mergeDataIntoStructure(consoleData, updatedEntries);

        try {
            await syncReadinessEntries([{ menu_id: menuId, uat_status: newStatus }]);
            // Success
        } catch (error) {
            console.error("Failed to save UAT status", error);
            // Revert on failure (could implement)
        }
    };

    const handleGenerateTsPrompt = () => {
        if (selectedSuites.size === 0) return;
        const suites = Array.from(selectedSuites).map(id => currentModule?.suites.find(s => s.menu_id === id)).filter(Boolean);

        let prompt = `Create a Playwright test specification for the following components in ${currentModule?.label}:\n\n`;
        suites.forEach((s: any) => {
            prompt += `Component: ${s.name}\nPath: ${s.path}\nBBP: ${s.bbp_path || 'None'}\nCurrent Script: ${s.script_path || 'None'}\n\n`;
        });
        prompt += `Requirement: Implement robust E2E tests covering happy paths and edge cases defined in BBP.`;

        setGeneratedPrompt(prompt);
        setIsPromptModalOpen(true);
    };

    const runTests = async () => {
        setIsRunning(true);
        setExecutionLogs([`> Initializing test runner for ${selectedSuites.size} suites...`, '> Environment: Local Dev']);

        // Mock Execution
        const suites = Array.from(selectedSuites);

        for (const suiteId of suites) {
            const suite = currentModule?.suites.find(s => s.menu_id === suiteId);
            setExecutionLogs(prev => [...prev, `> [RUNNING] ${suite?.name} (${suite?.script_path || 'No script'})...`]);

            await new Promise(r => setTimeout(r, 1500)); // Fake delay

            if (suite?.script_path) {
                setExecutionLogs(prev => [...prev, `> [PASS] ${suite?.name} tests passed (2/2).`]);
            } else {
                setExecutionLogs(prev => [...prev, `> [WARN] ${suite?.name} skipped (no script mapped).`]);
            }
        }

        setExecutionLogs(prev => [...prev, `> Execution complete.`]);
        setIsRunning(false);
    };

    const handleGenerateReport = () => {
        // Generate CSV from filteredSuites (or all entries if needed, but usually visible view)
        const headers = ["Menu ID", "Component", "Module", "UI Status", "DIT Status", "UAT Status", "Has Script", "Script Path"];
        const rows = filteredSuites.map(s => [
            s.menu_id,
            s.name.replace(/,/g, ''), // Escape commas
            (s as any).module,
            s.ui_status,
            s.dit_status,
            s.uat_status,
            s.script_path ? "Yes" : "No",
            s.script_path || ""
        ]);

        const csvContent = [
            headers.join(","),
            ...rows.map(r => r.join(","))
        ].join("\n");

        const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
        const link = document.createElement("a");
        const url = URL.createObjectURL(blob);
        link.setAttribute("href", url);
        link.setAttribute("download", `test_readiness_report_${new Date().toISOString().split('T')[0]}.csv`);
        link.style.visibility = "hidden";
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    };

    const handleBbpClick = (path: string, name: string) => {
        // In a real app, fetch the MD content. Here mock or show path.
        setBbpTitle(`BBP: ${name}`);
        setBbpContent(`Loading Business Blueprint from: ${path}\n\n(Content fetching to be implemented via backend API reading file system)`);
        setIsBbpModalOpen(true);
    };

    // Render Helpers
    const StatusBadge = ({ status, type }: { status: string, type: 'ui' | 'dit' | 'uat' }) => {
        let label = status;
        let color = "text-slate-300"; // Default/No

        if (status === 'Done' || status === 'Pass' || status === 'Complete') {
            color = "text-emerald-600 font-bold";
            label = "Yes";
        }
        if (status === 'Pending' || status === 'Not Started' || status === 'Fail') {
            color = "text-slate-300"; // Muted for No
            label = "No";
        }
        if (status === 'InProgress') {
            color = "text-amber-500 font-bold";
            label = "WIP";
        }

        return (
            <span className={`text-[10px] ${color}`}>
                {label}
            </span>
        );
    };

    return (
        <div className="fixed left-0 right-0 bottom-0 top-16 z-40 flex w-full overflow-hidden bg-slate-50 text-slate-800 font-sans selection:bg-indigo-100">
            {/* 1. SIDEBAR EXPLORER */}
            <ExplorerSidebar
                consoleData={consoleData}
                expandedNodes={expandedNodes}
                setExpandedNodes={setExpandedNodes}
                selectedApp={selectedApp}
                setSelectedApp={setSelectedApp}
                selectedModuleId={selectedModuleId}
                setSelectedModuleId={setSelectedModuleId}
            />

            {/* MAIN CONTENT AREA */}
            <div className="flex-1 flex flex-col min-w-0 bg-white">

                {/* 2. GLOBAL HEADER */}
                <div className="h-14 border-b border-slate-200 flex justify-between items-center px-6 shrink-0 bg-white z-20 shadow-sm">
                    <div className="flex items-center gap-3 overflow-hidden">
                        {currentApp && currentModule ? (
                            <div className="flex items-center gap-2 text-sm text-slate-500">
                                <span className="font-bold text-slate-800 flex items-center gap-2">
                                    {currentApp.icon} {currentApp.label}
                                </span>
                                <ChevronRight size={14} className="text-slate-300" />
                                <span className="font-bold text-indigo-600 flex items-center gap-2">
                                    <Folder size={14} /> {currentModule.label}
                                </span>
                            </div>
                        ) : (
                            <span className="text-slate-400 text-sm font-medium italic">Select a module from the Explorer...</span>
                        )}
                    </div>

                    <div className="flex items-center gap-2">
                        <button
                            onClick={() => navigate('/')}
                            className="btn flex items-center gap-2 px-3 py-1.5 text-xs font-bold uppercase border border-slate-200 bg-slate-100 text-slate-500 rounded hover:bg-rose-50 hover:text-rose-600 hover:border-rose-200 transition-colors mr-2"
                            title="Exit to Home"
                        >
                            <X size={14} /> Close
                        </button>
                        <button
                            onClick={handleRefreshScripts}
                            disabled={refreshing}
                            className={`btn flex items-center gap-2 px-3 py-1.5 text-xs font-bold uppercase border rounded transition-colors
                                 ${refreshing ? 'bg-slate-50 text-slate-400 border-slate-200 cursor-not-allowed' : 'bg-white text-slate-600 border-slate-300 hover:bg-slate-50 hover:text-slate-900'}
                             `}
                        >
                            <RefreshCw size={14} className={refreshing ? 'animate-spin' : ''} />
                            {refreshing ? 'Syncing...' : 'Sync Scripts'}
                        </button>
                        <button
                            onClick={handleGenerateReport}
                            className="btn flex items-center gap-2 px-3 py-1.5 text-xs font-bold uppercase border border-slate-300 bg-white text-slate-600 rounded hover:bg-slate-50 transition-colors"
                        >
                            <Download size={14} /> CSV
                        </button>
                    </div>
                </div>

                {/* 3. WORKBENCH 3-COLUMN LAYOUT */}
                {currentApp && currentModule ? (
                    <div className="flex-1 flex min-h-0 overflow-hidden">

                        {/* COLUMN 2: READINESS GRID (Middle) */}
                        <div className="w-[550px] shrink-0 flex flex-col min-w-0 border-r border-slate-200">
                            <ReadinessMatrix
                                consoleData={consoleData}
                                currentModule={currentModule}
                                filteredSuites={filteredSuites}
                                selectedIds={selectedSuites}
                                setSelectedIds={setSelectedSuites}
                                toggleSelection={toggleSuite}
                                uiFilter={uiFilter} setUiFilter={setUiFilter}
                                scriptFilter={scriptFilter} setScriptFilter={setScriptFilter}
                                bbpFilter={bbpFilter} setBbpFilter={setBbpFilter}
                                ditFilter={ditFilter} setDitFilter={setDitFilter}
                                uatFilter={uatFilter} setUatFilter={setUatFilter}
                                handleBbpClick={handleBbpClick}
                                handleUatChange={handleUatChange}
                                StatusBadge={StatusBadge}
                            />
                        </div>

                        {/* COLUMN 3: EXECUTION PANEL (Right) */}
                        <div className="flex-1 flex flex-col bg-slate-50 border-l border-slate-200 shadow-xl z-10 transition-all min-w-[400px]">

                            {/* Run Queue (Top - Fixed/Smaller Height) */}
                            <div className="h-[50%] shrink-0 flex flex-col min-h-0 border-b border-slate-300">
                                <RunQueue
                                    selectedSuites={selectedSuites}
                                    setSelectedSuites={setSelectedSuites}
                                    currentModule={currentModule}
                                    toggleSuite={toggleSuite}
                                    runTests={runTests}
                                    isRunning={isRunning}
                                />
                            </div>

                            {/* Console Output (Bottom - Fills remaining space) */}
                            <div className="flex-1 flex flex-col min-h-0 bg-slate-950 overflow-hidden">
                                <ConsoleOutput
                                    executionLogs={executionLogs}
                                    setExecutionLogs={setExecutionLogs}
                                    isRunning={isRunning}
                                />
                            </div>
                        </div>

                    </div>
                ) : (
                    <div className="flex-1 flex flex-col items-center justify-center text-slate-300 select-none">
                        <Folder size={64} className="mb-4 text-slate-200 stroke-1" />
                        <p className="text-sm font-medium text-slate-400">Select a module from the Explorer to view components.</p>
                        <p className="text-xs text-slate-300 mt-2">Use the generic &gt; buttons to expand sections.</p>
                    </div>
                )}
            </div>

            {/* MODALS */}
            {isPromptModalOpen && (
                <div className="fixed inset-0 bg-black/50 z-50 flex items-center justify-center backdrop-blur-sm">
                    <div className="bg-white rounded-lg shadow-2xl w-[800px] max-w-[90vw] flex flex-col max-h-[90vh]">
                        <div className="p-4 border-b border-slate-100 flex justify-between items-center bg-slate-50 rounded-t-lg">
                            <h3 className="font-bold text-slate-700 flex items-center gap-2">
                                <FileCode size={18} className="text-indigo-600" />
                                Generate Test Script Prompt
                            </h3>
                            <button onClick={() => setIsPromptModalOpen(false)} className="text-slate-400 hover:text-slate-600">
                                <span className="text-xl font-bold">×</span>
                            </button>
                        </div>
                        <div className="p-0 flex-1 overflow-hidden relative">
                            <textarea
                                className="w-full h-[400px] p-4 font-mono text-xs bg-slate-900 text-slate-200 resize-none focus:outline-none"
                                value={generatedPrompt}
                                readOnly
                            />
                        </div>
                        <div className="p-4 border-t border-slate-100 flex justify-end gap-3 bg-slate-50 rounded-b-lg">
                            <button
                                onClick={() => setIsPromptModalOpen(false)}
                                className="px-4 py-2 text-xs font-bold uppercase tracking-wider text-slate-500 hover:bg-slate-200 rounded transition-colors"
                            >
                                Close
                            </button>
                            <button
                                onClick={() => {
                                    navigator.clipboard.writeText(generatedPrompt);
                                    setExecutionLogs(prev => [...prev, `> Prompt copied to clipboard!`]);
                                    setIsPromptModalOpen(false);
                                }}
                                className="px-4 py-2 text-xs font-bold uppercase tracking-wider bg-indigo-600 text-white hover:bg-indigo-700 rounded shadow-md transition-colors flex items-center gap-2"
                            >
                                <span className="text-lg">📋</span> Copy to Clipboard
                            </button>
                        </div>
                    </div>
                </div>
            )}
            {isBbpModalOpen && (
                <div className="fixed inset-0 bg-black/50 z-50 flex items-center justify-center backdrop-blur-sm">
                    <div className="bg-white rounded-lg shadow-2xl w-[900px] max-w-[95vw] flex flex-col max-h-[90vh]">
                        <div className="p-4 border-b border-slate-100 flex justify-between items-center bg-slate-50 rounded-t-lg">
                            <h3 className="font-bold text-slate-700 flex items-center gap-2">
                                <Box size={18} className="text-blue-600" />
                                {bbpTitle}
                            </h3>
                            <button onClick={() => setIsBbpModalOpen(false)} className="text-slate-400 hover:text-slate-600">
                                <span className="text-xl font-bold">×</span>
                            </button>
                        </div>
                        <div className="flex-1 overflow-auto p-6 bg-slate-50/30">
                            <pre className="whitespace-pre-wrap text-sm text-slate-700 font-mono leading-relaxed p-4 bg-white border border-slate-200 rounded shadow-sm">
                                {bbpContent}
                            </pre>
                        </div>
                        <div className="p-4 border-t border-slate-100 flex justify-end gap-3 bg-slate-50 rounded-b-lg">
                            <button
                                onClick={() => setIsBbpModalOpen(false)}
                                className="px-4 py-2 text-xs font-bold uppercase tracking-wider bg-slate-800 text-white hover:bg-slate-900 rounded shadow-sm transition-colors"
                            >
                                Close
                            </button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
};

export default TestConsolePage;


