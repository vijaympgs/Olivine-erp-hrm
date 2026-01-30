# QA Launcher Console - Add STOP Buttons

## Summary
Added individual STOP buttons for Backend and Frontend services in the footer sections.

## Changes Required

### 1. Add STOP button to Backend Footer (Line 325-331)

Replace:
```tsx
<div className="flex items-center gap-2 mb-2">
    <div className={cn(
        "w-2 h-2 rounded-full",
        serverStatus.backend ? "bg-green-500 shadow-[0_0_8px_rgba(34,197,94,0.6)]" : "bg-red-500 shadow-[0_0_8px_rgba(239,68,68,0.6)]"
    )} />
    <span className="text-xs font-bold text-slate-400 uppercase tracking-widest">Backend Services</span>
</div>
```

With:
```tsx
<div className="flex items-center justify-between gap-2 mb-2">
    <div className="flex items-center gap-2">
        <div className={cn(
            "w-2 h-2 rounded-full",
            serverStatus.backend ? "bg-green-500 shadow-[0_0_8px_rgba(34,197,94,0.6)]" : "bg-red-500 shadow-[0_0_8px_rgba(239,68,68,0.6)]"
        )} />
        <span className="text-xs font-bold text-slate-400 uppercase tracking-widest">Backend Services</span>
    </div>
    {serverStatus.backend && (
        <button
            onClick={async () => {
                try {
                    const port = APP_PORTS[selectedApp || 'ERP_Core'].backend;
                    await fetch(`${API_URL}/stop-service`, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ port })
                    });
                    setServerStatus(prev => ({ ...prev, backend: false }));
                } catch (e) {
                    console.error('Failed to stop backend', e);
                }
            }}
            className="px-2 py-1 bg-red-600 hover:bg-red-500 text-white text-[10px] font-bold uppercase tracking-wide rounded transition-colors flex items-center gap-1"
        >
            <Square className="h-3 w-3" />
            STOP
        </button>
    )}
</div>
```

### 2. Add STOP button to Frontend Footer (Line 374-380)

Replace:
```tsx
<div className="flex items-center gap-2 mb-2">
    <div className={cn(
        "w-2 h-2 rounded-full",
        serverStatus.frontend ? "bg-green-500 shadow-[0_0_8px_rgba(34,197,94,0.6)]" : "bg-red-500 shadow-[0_0_8px_rgba(239,68,68,0.6)]"
    )} />
    <span className="text-xs font-bold text-slate-400 uppercase tracking-widest">Frontend Application</span>
</div>
```

With:
```tsx
<div className="flex items-center justify-between gap-2 mb-2">
    <div className="flex items-center gap-2">
        <div className={cn(
            "w-2 h-2 rounded-full",
            serverStatus.frontend ? "bg-green-500 shadow-[0_0_8px_rgba(34,197,94,0.6)]" : "bg-red-500 shadow-[0_0_8px_rgba(239,68,68,0.6)]"
        )} />
        <span className="text-xs font-bold text-slate-400 uppercase tracking-widest">Frontend Application</span>
    </div>
    {serverStatus.frontend && (
        <button
            onClick={async () => {
                try {
                    const port = APP_PORTS[selectedApp || 'ERP_Core'].frontend;
                    await fetch(`${API_URL}/stop-service`, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ port })
                    });
                    setServerStatus(prev => ({ ...prev, frontend: false }));
                } catch (e) {
                    console.error('Failed to stop frontend', e);
                }
            }}
            className="px-2 py-1 bg-red-600 hover:bg-red-500 text-white text-[10px] font-bold uppercase tracking-wide rounded transition-colors flex items-center gap-1"
        >
            <Square className="h-3 w-3" />
            STOP
        </button>
    )}
</div>
```

### 3. Add `/stop-service` endpoint to backend server.js

Add this endpoint after the `/cancel/:jobId` endpoint (around line 226):

```javascript
app.post('/stop-service', async (req, res) => {
    const { port } = req.body;
    if (!port) {
        return res.status(400).json({ error: 'Port is required' });
    }

    try {
        await killPort(port);
        res.json({ success: true, message: `Service on port ${port} stopped` });
    } catch (error) {
        res.status(500).json({ error: 'Failed to stop service', details: error.message });
    }
});
```

## Manual Steps
1. Open `Common/QA-Launcher-Console/frontend/src/App.tsx`
2. Apply changes to lines 325-331 (Backend footer)
3. Apply changes to lines 374-380 (Frontend footer)
4. Open `Common/QA-Launcher-Console/backend/server.js`
5. Add the `/stop-service` endpoint after line 225

This will add red STOP buttons that appear next to the service status indicators when services are running.
