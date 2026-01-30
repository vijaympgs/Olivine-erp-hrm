import express from 'express';
import { WebSocketServer } from 'ws';
import { spawn } from 'child_process';
import cors from 'cors';
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
app.use(cors());
app.use(express.json());

const PORT = 3100;
const PROJECT_ROOT = path.resolve(__dirname, '../../../');

// --- Configuration ---
// UNIFIED ARCHITECTURE: All ERP modules under one backend/frontend
const APP_CONFIG = {
    ERP_Core: {
        // Unified backend with Retail, HRM, CRM, FMS
        backend: { cmd: 'python', args: ['manage.py', 'runserver', '0.0.0.0:8001'], cwd: 'backend' },
        // Unified frontend (Now on 3001)
        frontend: { cmd: 'npm', args: ['run', 'dev', '--', '--port', '3001'], cwd: 'frontend' }
    },
    Meet: {
        // Separate Meet application
        backend: { cmd: 'poetry', args: ['run', 'python', '-m', 'app.main', '--port', '8001'], cwd: 'Meet/backend' },
        frontend: { cmd: 'npm', args: ['run', 'dev', '--', '--port', '3002'], cwd: 'Meet/frontend' }
    }
};

// --- Job Store ---
// Map<jobId, { id, app, mode, status: 'pending'|'running'|'completed'|'failed', logs: { backend: [], frontend: [] }, logic: { backend: Process, frontend: Process } }>
const jobs = new Map();

// --- WebSocket Server ---
const wss = new WebSocketServer({ noServer: true });

function broadcast(jobId, type, data) {
    wss.clients.forEach(client => {
        if (client.jobId === jobId && client.readyState === 1) {
            client.send(JSON.stringify({ type, data }));
        }
    });
}

// --- Routes ---

const { exec } = await import('child_process');
const util = await import('util');
const execAsync = util.promisify(exec);

// Helper to kill process by port
const killPort = async (port) => {
    if (!port) return;
    try {
        const { stdout } = await execAsync(`netstat -ano | findstr :${port}`);
        if (!stdout) return;

        const lines = stdout.trim().split('\n');
        for (const line of lines) {
            const parts = line.trim().split(/\s+/);
            const pid = parts[parts.length - 1];
            if (pid && !isNaN(pid) && pid !== '0') {
                try {
                    await execAsync(`taskkill /PID ${pid} /F`);
                    console.log(`Killed process ${pid} on port ${port}`);
                } catch (e) { }
            }
        }
    } catch (e) { }
};

// Helper to extract port from args
const getPort = (config) => {
    // Frontend: look for --port X
    if (config.cmd === 'npm') {
        const idx = config.args.indexOf('--port');
        if (idx !== -1 && config.args[idx + 1]) return config.args[idx + 1];
    }
    // Backend: look for IP:PORT
    if (config.cmd === 'python' && config.args.includes('runserver')) {
        const arg = config.args.find(a => a.includes(':'));
        if (arg) return arg.split(':')[1];
    }
    return null;
};

app.post('/run', async (req, res) => {
    const { app, mode } = req.body;

    if (!APP_CONFIG[app]) {
        return res.status(400).json({ error: 'Invalid App' });
    }

    const jobId = Date.now().toString();
    const job = {
        id: jobId,
        app,
        mode,
        status: 'running',
        logs: { backend: [], frontend: [] },
        processes: {}
    };

    jobs.set(jobId, job);

    const log = (side, message) => {
        const entry = `[${new Date().toISOString()}] ${message}`;
        job.logs[side].push(entry);
        broadcast(jobId, 'log', { side, message: entry });
    };

    const runProcess = async (side) => {
        const config = APP_CONFIG[app][side];
        if (!config) {
            log(side, `No configuration for ${side} of ${app}`);
            return;
        }

        const cwd = path.join(PROJECT_ROOT, config.cwd);
        if (!fs.existsSync(cwd)) {
            log(side, `Directory not found: ${cwd}`);
            return;
        }

        const port = getPort(config);
        if (port) {
            log(side, `Checking/Freeing port ${port}...`);
            await killPort(port);
        }

        let finalCmd = config.cmd;
        if (process.platform === 'win32') {
            if (config.cmd === 'npm') finalCmd = 'npm.cmd';
        }

        log(side, `Starting ${finalCmd} ${config.args.join(' ')} in ${cwd}`);

        const proc = spawn(finalCmd, config.args, { cwd, shell: true });
        job.processes[side] = proc;

        const logFileName = `${app}-${side}.log`;
        const logFilePath = path.join(PROJECT_ROOT, logFileName);

        if (fs.existsSync(logFilePath)) fs.unlinkSync(logFilePath);

        const logStream = fs.createWriteStream(logFilePath, { flags: 'a' });
        job.processes[`${side}LogStream`] = logStream;

        proc.stdout.on('data', (data) => {
            log(side, data.toString());
            logStream.write(data);
        });

        proc.stderr.on('data', (data) => {
            log(side, data.toString());
            logStream.write(data);
        });

        proc.on('close', (code) => {
            log(side, `Process exited with code ${code}`);
            logStream.end();
            broadcast(jobId, 'status', { side, status: code === 0 ? 'PASS' : 'FAIL' });
        });
    };

    if (mode === 'backend' || mode === 'both') await runProcess('backend');
    if (mode === 'frontend' || mode === 'both') await runProcess('frontend');

    res.json({ jobId });
});

app.get('/status/:jobId', (req, res) => {
    const job = jobs.get(req.params.jobId);
    if (!job) return res.status(404).json({ error: 'Job not found' });
    res.json({
        id: job.id,
        status: job.status,
        logs: job.logs
    });
});

app.get('/export/:jobId', (req, res) => {
    const { side } = req.query;
    const job = jobs.get(req.params.jobId);
    if (!job) return res.status(404).json({ error: 'Job not found' });

    const logs = job.logs[side] || [];
    res.header('Content-Type', 'text/plain');
    res.attachment(`${job.app}-${side}-${job.id}.log`);
    res.send(logs.join('\n'));
});

app.post('/cancel/:jobId', (req, res) => {
    const job = jobs.get(req.params.jobId);
    if (!job) return res.status(404).json({ error: 'Job not found' });

    // Kill all running processes and close log streams
    let killed = false;
    if (job.processes.backend) {
        if (job.processes.backendLogStream) {
            job.processes.backendLogStream.end();
        }
        job.processes.backend.kill();
        killed = true;
    }
    if (job.processes.frontend) {
        if (job.processes.frontendLogStream) {
            job.processes.frontendLogStream.end();
        }
        job.processes.frontend.kill();
        killed = true;
    }

    job.status = 'cancelled';

    res.json({
        success: true,
        message: killed ? 'Job cancelled successfully' : 'No running processes to cancel'
    });
});


const server = app.listen(PORT, () => {
    console.log(`QA Launcher Backend running on port ${PORT}`);
});

server.on('upgrade', (request, socket, head) => {
    const url = new URL(request.url, `http://${request.headers.host}`);
    const jobId = url.searchParams.get('jobId');

    wss.handleUpgrade(request, socket, head, (ws) => {
        ws.jobId = jobId;
        wss.emit('connection', ws, request);
    });
});

wss.on('connection', (ws) => {
    // Can send history logs if needed
});
