import { useState, useEffect, useRef } from 'react';
import { Play, Square, Terminal, CheckCircle2, XCircle, Download, Activity, Clock } from 'lucide-react';
import { clsx } from 'clsx';
import { twMerge } from 'tailwind-merge';

// --- Types ---
type AppName = 'ERP_Core' | 'Meet';
type ExecutionMode = 'backend' | 'frontend' | 'both';
type JobStatus = 'running' | 'completed' | 'failed';

interface Job {
    id: string;
    app: AppName;
    mode: ExecutionMode;
    status: JobStatus;
    startTime: string;
}



// --- Utils ---
function cn(...inputs: (string | undefined | null | false)[]) {
    return twMerge(clsx(inputs));
}

const API_URL = 'http://localhost:3100';
const WS_URL = 'ws://localhost:3100';

const APP_PORTS: Record<AppName, { backend: number, frontend: number }> = {
    ERP_Core: { backend: 8000, frontend: 3001 },  // Unified ERP (Retail, HRM, CRM, FMS)
    Meet: { backend: 8001, frontend: 3002 }       // Separate Meet app
};

export default function App() {
    const [selectedApp, setSelectedApp] = useState<AppName>('ERP_Core'); // Default to unified ERP
    const [modes, setModes] = useState({ backend: true, frontend: true });
    const [queue, setQueue] = useState<Job[]>([]);
    const [activeJobId, setActiveJobId] = useState<string | null>(null);
    const [logs, setLogs] = useState<{ backend: string[], frontend: string[] }>({ backend: [], frontend: [] });
    const [status, setStatus] = useState<{ backend: 'PASS' | 'FAIL' | null, frontend: 'PASS' | 'FAIL' | null }>({ backend: null, frontend: null });
    const [isRunning, setIsRunning] = useState(false);
    const [serverStatus, setServerStatus] = useState({ backend: false, frontend: false });

    const wsRef = useRef<WebSocket | null>(null);
    const backendConsoleRef = useRef<HTMLDivElement>(null);
    const frontendConsoleRef = useRef<HTMLDivElement>(null);

    // --- Server Status Check ---
    useEffect(() => {
        const checkServers = async () => {
            if (!selectedApp) return;

            const ports = APP_PORTS[selectedApp];

            // Check backend
            try {
                await fetch(`http://localhost:${ports.backend}`, { method: 'HEAD', mode: 'no-cors' });
                setServerStatus(prev => ({ ...prev, backend: true }));
            } catch {
                setServerStatus(prev => ({ ...prev, backend: false }));
            }

            // Check frontend
            try {
                await fetch(`http://localhost:${ports.frontend}`, { method: 'HEAD', mode: 'no-cors' });
                setServerStatus(prev => ({ ...prev, frontend: true }));
            } catch {
                setServerStatus(prev => ({ ...prev, frontend: false }));
            }
        };

        checkServers();
        const interval = setInterval(checkServers, 5000);
        return () => clearInterval(interval);
    }, [selectedApp]); // Re-run when app changes

    // ... existing ...

    // In Render:
    // ...


    // --- Actions ---

    const toggleMode = (key: 'backend' | 'frontend') => {
        setModes(prev => ({ ...prev, [key]: !prev[key] }));
    };

    const runJob = async () => {
        if (!selectedApp) return;
        if (!modes.backend && !modes.frontend) return;

        const mode = (modes.backend && modes.frontend) ? 'both' : (modes.backend ? 'backend' : 'frontend');

        try {
            const res = await fetch(`${API_URL}/run`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ app: selectedApp, mode })
            });
            const data = await res.json();

            if (data.jobId) {
                const newJob: Job = {
                    id: data.jobId,
                    app: selectedApp,
                    mode: mode as ExecutionMode,
                    status: 'running',
                    startTime: new Date().toLocaleTimeString()
                };
                setQueue(prev => [newJob, ...prev]);
                setActiveJobId(data.jobId);
                setLogs({ backend: [], frontend: [] }); // Clear logs for new run
                setStatus({ backend: null, frontend: null });
                setIsRunning(true);
                connectWs(data.jobId);
            }
        } catch (err) {
            console.error("Failed to start job", err);
        }
    };

    const connectWs = (jobId: string) => {
        if (wsRef.current) wsRef.current.close();

        // Pass jobId as query parameter to handle initial connection context
        wsRef.current = new WebSocket(`${WS_URL}?jobId=${jobId}`);

        wsRef.current.onmessage = (event) => {
            const payload = JSON.parse(event.data);
            if (payload.type === 'log') {
                const { side, message } = payload.data as { side: 'backend' | 'frontend', message: string };
                setLogs(prev => ({
                    ...prev,
                    [side]: [...prev[side], message]
                }));
                // Auto scroll
                if (side === 'backend' && backendConsoleRef.current) {
                    backendConsoleRef.current.scrollTop = backendConsoleRef.current.scrollHeight;
                }
                if (side === 'frontend' && frontendConsoleRef.current) {
                    frontendConsoleRef.current.scrollTop = frontendConsoleRef.current.scrollHeight;
                }
            } else if (payload.type === 'status') {
                const { side, status: result } = payload.data;
                setStatus(prev => ({ ...prev, [side]: result }));
                // Check if both sides are done
                setTimeout(() => setIsRunning(false), 1000);
            }
        };
    };

    const exportLog = (side: 'backend' | 'frontend') => {
        if (!activeJobId) return;
        window.open(`${API_URL}/export/${activeJobId}?side=${side}`, '_blank');
    };

    const stopJob = async () => {
        if (!activeJobId) return;
        try {
            await fetch(`${API_URL}/cancel/${activeJobId}`, { method: 'POST' });
            setIsRunning(false);
            setQueue(prev => prev.map(job =>
                job.id === activeJobId ? { ...job, status: 'failed' } : job
            ));
        } catch (err) {
            console.error('Failed to stop job', err);
        }
    };

    return (
        <div className="h-screen bg-slate-950 text-slate-100 p-4 flex flex-col gap-4 font-sans overflow-hidden">

            {/* HEADER */}
            <header className="flex items-center justify-between border-b border-slate-800 pb-2 flex-shrink-0">
                <div className="flex items-center gap-3">
                    <Activity className="h-5 w-5 text-green-500" />
                    <h1 className="text-lg font-bold tracking-tight text-slate-100">App Launcher</h1>
                </div>
                <div className="text-[10px] text-slate-400">v1.0.0 &bull; Olivine Platform</div>
            </header>

            {/* COMPACT CONTROL BAR */}
            <div className="bg-slate-900 border border-slate-800 rounded-lg p-2 flex items-center justify-between gap-6 shadow-sm">

                {/* Target App Section */}
                <div className="flex-1 flex flex-col gap-1">
                    <span className="text-[10px] font-bold text-slate-500 uppercase tracking-widest px-2">Target Application</span>
                    <div className="flex items-center border border-slate-700 rounded overflow-hidden bg-slate-950/50">
                        {(['ERP_Core', 'Meet'] as AppName[]).map((app) => (
                            <button
                                key={app}
                                onClick={() => setSelectedApp(app)}
                                className={cn(
                                    "flex-1 py-2 text-sm font-medium transition-colors border-r border-slate-700 last:border-r-0 hover:bg-slate-800",
                                    selectedApp === app
                                        ? "text-green-500 bg-green-500/10"
                                        : "text-slate-400"
                                )}
                            >
                                {app === 'ERP_Core' ? 'ERP Core (Retail, HRM, CRM, FMS)' : 'Meet'}
                            </button>
                        ))}
                    </div>
                </div>

                {/* Execution Mode Section */}
                <div className="flex flex-col gap-1">
                    <span className="text-[10px] font-bold text-slate-500 uppercase tracking-widest px-1">Execution Mode</span>
                    <div className="flex items-center gap-4 h-[38px] px-2">
                        <label className="flex items-center gap-2 cursor-pointer hover:text-slate-200 transition-colors text-sm">
                            <input
                                type="checkbox"
                                checked={modes.backend}
                                onChange={() => toggleMode('backend')}
                                className="h-4 w-4 rounded border-slate-600 bg-slate-800 text-green-500 focus:ring-offset-0 focus:ring-green-500/50"
                            />
                            <span className={modes.backend ? "text-slate-200" : "text-slate-500"}>Backend Services</span>
                        </label>
                        <label className="flex items-center gap-2 cursor-pointer hover:text-slate-200 transition-colors text-sm">
                            <input
                                type="checkbox"
                                checked={modes.frontend}
                                onChange={() => toggleMode('frontend')}
                                className="h-4 w-4 rounded border-slate-600 bg-slate-800 text-green-500 focus:ring-offset-0 focus:ring-green-500/50"
                            />
                            <span className={modes.frontend ? "text-slate-200" : "text-slate-500"}>Frontend Application</span>
                        </label>
                    </div>
                </div>

                {/* Action Buttons */}
                <div className="h-full flex items-end pb-[1px] gap-2">
                    {!isRunning ? (
                        <button
                            onClick={runJob}
                            disabled={!selectedApp || (!modes.backend && !modes.frontend)}
                            className="h-[38px] px-4 bg-green-600 hover:bg-green-500 text-white font-bold text-xs uppercase tracking-wide rounded flex items-center justify-center gap-2 transition-all disabled:opacity-50 disabled:grayscale hover:shadow-[0_0_15px_rgba(34,197,94,0.3)]">
                            <Play className="h-4 w-4 fill-current flex-shrink-0" />
                            <span className="text-center leading-none max-w-[80px] whitespace-normal">Start the Services</span>
                        </button>
                    ) : (
                        <button
                            onClick={stopJob}
                            className="h-[38px] px-4 bg-red-600 hover:bg-red-500 text-white font-bold text-xs uppercase tracking-wide rounded flex items-center justify-center gap-2 transition-all hover:shadow-[0_0_15px_rgba(220,38,38,0.3)]">
                            <Square className="h-4 w-4 fill-current flex-shrink-0" />
                            <span className="text-center leading-none">Stop Job</span>
                        </button>
                    )}
                </div>
            </div>

            {/* MAIN CONTENT GRID - Full Height minus header/controls */}
            <div className="grid grid-cols-12 gap-4 flex-1 min-h-0 pb-4">

                {/* SECTION 3: QUEUE - Left Sidebar */}
                <div className="col-span-3 bg-slate-900 rounded-lg border border-slate-800 flex flex-col h-full overflow-hidden shadow-sm">
                    <div className="p-3 border-b border-slate-800 bg-slate-950/30">
                        <h2 className="text-xs font-bold text-slate-500 uppercase tracking-widest flex items-center gap-2">
                            <Clock className="h-3 w-3" /> Execution Queue
                        </h2>
                    </div>
                    <div className="flex-1 overflow-y-auto p-2 space-y-2 console-scroll">
                        {queue.length === 0 && (
                            <div className="text-center text-slate-600 mt-10 p-4 text-sm">
                                No jobs in queue.
                            </div>
                        )}
                        {queue.map(job => (
                            <div
                                key={job.id}
                                onClick={() => { setActiveJobId(job.id); connectWs(job.id); }}
                                className={cn(
                                    "p-3 rounded border-l-2 cursor-pointer transition-all hover:bg-slate-800/50",
                                    activeJobId === job.id
                                        ? "bg-slate-800/80 border-l-green-500 border-y border-r border-y-slate-700 border-r-slate-700 shadow-md"
                                        : "bg-slate-900 border-transparent border-l-transparent text-slate-500"
                                )}
                            >
                                <div className="flex justify-between items-start mb-1">
                                    <span className={cn("font-bold text-sm", activeJobId === job.id ? "text-slate-100" : "text-slate-400")}>{job.app}</span>
                                    <span className="text-[10px] bg-slate-950 px-1.5 py-0.5 rounded text-slate-500 font-mono">{job.startTime}</span>
                                </div>
                                <div className="flex justify-between items-center text-[10px] font-bold tracking-wide">
                                    <span className="text-slate-500 uppercase">{job.mode}</span>
                                    {job.status === 'running' && <span className="text-yellow-500 animate-pulse">Running...</span>}
                                    {job.status === 'completed' && <span className="text-green-500">Completed</span>}
                                    {job.status === 'failed' && <span className="text-red-500">Failed</span>}
                                </div>
                            </div>
                        ))}
                    </div>
                </div>

                {/* RIGHT SIDE: CONSOLES + FOOTERS */}
                <div className="col-span-9 grid grid-cols-2 gap-4 h-full">

                    {/* COL 1: BACKEND STACK */}
                    <div className="flex flex-col gap-4 h-full min-h-0">
                        {/* BACKEND CONSOLE */}
                        <div className="flex flex-col bg-slate-900 rounded-lg border border-slate-800 overflow-hidden shadow-sm min-h-0 max-h-[200px]">
                            <div className="flex items-center justify-between p-2 border-b border-slate-800 bg-slate-950/30 px-3 h-[42px] flex-shrink-0">
                                <div className="flex items-center gap-2">
                                    <Terminal className="h-4 w-4 text-slate-500" />
                                    <span className="font-semibold text-sm text-slate-300">Backend</span>
                                    {modes.backend && selectedApp && <span className="text-xs text-slate-600 font-mono italic">({selectedApp} Service)</span>}
                                </div>
                                <div className="flex items-center gap-3">
                                    {status.backend === 'PASS' && <span className="flex items-center gap-1 text-green-500 font-bold text-xs tracking-wider"><CheckCircle2 className="h-3 w-3" /> PASS</span>}
                                    {status.backend === 'FAIL' && <span className="flex items-center gap-1 text-red-500 font-bold text-xs tracking-wider"><XCircle className="h-3 w-3" /> FAIL</span>}
                                    <button onClick={() => exportLog('backend')} className="p-1 hover:bg-slate-800 rounded text-slate-500 hover:text-white transition-colors" title="Export Log">
                                        <Download className="h-4 w-4" />
                                    </button>
                                </div>
                            </div>
                            <div className="flex-1 bg-black p-3 font-mono text-[11px] leading-relaxed overflow-auto console-scroll text-slate-300" ref={backendConsoleRef}>
                                {logs.backend.length === 0 ? <span className="text-slate-700 italic">Waiting for logs...</span> : logs.backend.map((l, i) => (
                                    <div key={i} className="whitespace-pre-wrap break-all">{l}</div>
                                ))}
                            </div>
                        </div>

                        {/* BACKEND FOOTER BOX */}
                        <div className="bg-slate-900 border border-slate-800 rounded-lg p-3 flex-shrink-0 shadow-sm h-[80px] flex flex-col justify-center">
                            <div className="flex items-center gap-2 mb-2">
                                <div className={cn(
                                    "w-2 h-2 rounded-full",
                                    serverStatus.backend ? "bg-green-500 shadow-[0_0_8px_rgba(34,197,94,0.6)]" : "bg-red-500 shadow-[0_0_8px_rgba(239,68,68,0.6)]"
                                )} />
                                <span className="text-xs font-bold text-slate-400 uppercase tracking-widest">Backend Services</span>
                            </div>
                            <div className="flex items-center gap-3 pl-4">
                                <a href={`http://localhost:${APP_PORTS[selectedApp || 'Retail'].backend}/admin`} target="_blank" rel="noopener noreferrer"
                                    className="flex items-center gap-2 px-3 py-1.5 bg-slate-800 hover:bg-slate-700 rounded transition-colors group border border-slate-700">
                                    <span className="text-[10px] font-bold text-slate-500 group-hover:text-slate-300">ADMIN</span>
                                    <span className="text-xs font-mono text-blue-400 group-hover:text-blue-300">/admin</span>
                                </a>
                                <a href={`http://localhost:${APP_PORTS[selectedApp || 'Retail'].backend}/api/docs/`} target="_blank" rel="noopener noreferrer"
                                    className="flex items-center gap-2 px-3 py-1.5 bg-slate-800 hover:bg-slate-700 rounded transition-colors group border border-slate-700">
                                    <span className="text-[10px] font-bold text-slate-500 group-hover:text-slate-300">API DOCS</span>
                                    <span className="text-xs font-mono text-blue-400 group-hover:text-blue-300">/api/docs/</span>
                                </a>
                            </div>
                        </div>
                    </div>

                    {/* COL 2: FRONTEND STACK */}
                    <div className="flex flex-col gap-4 h-full min-h-0">
                        {/* FRONTEND CONSOLE */}
                        <div className="flex flex-col bg-slate-900 rounded-lg border border-slate-800 overflow-hidden shadow-sm min-h-0 max-h-[200px]">
                            <div className="flex items-center justify-between p-2 border-b border-slate-800 bg-slate-950/30 px-3 h-[42px] flex-shrink-0">
                                <div className="flex items-center gap-2">
                                    <Terminal className="h-4 w-4 text-slate-500" />
                                    <span className="font-semibold text-sm text-slate-300">Frontend</span>
                                    {modes.frontend && selectedApp && <span className="text-xs text-slate-600 font-mono italic">({selectedApp} UI)</span>}
                                </div>
                                <div className="flex items-center gap-3">
                                    {status.frontend === 'PASS' && <span className="flex items-center gap-1 text-green-500 font-bold text-xs tracking-wider"><CheckCircle2 className="h-3 w-3" /> PASS</span>}
                                    {status.frontend === 'FAIL' && <span className="flex items-center gap-1 text-red-500 font-bold text-xs tracking-wider"><XCircle className="h-3 w-3" /> FAIL</span>}
                                    <button onClick={() => exportLog('frontend')} className="p-1 hover:bg-slate-800 rounded text-slate-500 hover:text-white transition-colors" title="Export Log">
                                        <Download className="h-4 w-4" />
                                    </button>
                                </div>
                            </div>
                            <div className="flex-1 bg-black p-3 font-mono text-[11px] leading-relaxed overflow-auto console-scroll text-slate-300" ref={frontendConsoleRef}>
                                {logs.frontend.length === 0 ? <span className="text-slate-700 italic">Waiting for logs...</span> : logs.frontend.map((l, i) => (
                                    <div key={i} className="whitespace-pre-wrap break-all">{l}</div>
                                ))}
                            </div>
                        </div>

                        {/* FRONTEND FOOTER BOX */}
                        <div className="bg-slate-900 border border-slate-800 rounded-lg p-3 flex-shrink-0 shadow-sm h-[80px] flex flex-col justify-center">
                            <div className="flex items-center gap-2 mb-2">
                                <div className={cn(
                                    "w-2 h-2 rounded-full",
                                    serverStatus.frontend ? "bg-green-500 shadow-[0_0_8px_rgba(34,197,94,0.6)]" : "bg-red-500 shadow-[0_0_8px_rgba(239,68,68,0.6)]"
                                )} />
                                <span className="text-xs font-bold text-slate-400 uppercase tracking-widest">Frontend Application</span>
                            </div>
                            <div className="flex items-center gap-3 pl-4">
                                <a href={`http://localhost:${APP_PORTS[selectedApp || 'Retail'].frontend}`} target="_blank" rel="noopener noreferrer"
                                    className="flex items-center gap-2 px-3 py-1.5 bg-slate-800 hover:bg-slate-700 rounded transition-colors group border border-slate-700">
                                    <span className="text-[10px] font-bold text-slate-500 group-hover:text-slate-300">APP</span>
                                    <span className="text-xs font-mono text-blue-400 group-hover:text-blue-300">localhost:{APP_PORTS[selectedApp || 'Retail'].frontend}</span>
                                </a>
                            </div>
                        </div>
                    </div>

                </div>
            </div>


        </div>
    )
}
