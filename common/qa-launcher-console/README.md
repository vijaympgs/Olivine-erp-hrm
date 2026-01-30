# QA Launcher Console

A standalone verification and launcher console for the Olivine Platform.
Allows Quality Assurance Engineers and Developers to verify backend services and frontend applications in an isolated, monitored environment.

## Supported Applications
- Retail
- HRM
- CRM
- FMS
- Meet

## Architecture

- **Backend**: Node.js (Express + WS) - Handles process spawning and log streaming.
- **Frontend**: React + Vite + Tailwind - Provides the console UI.

## Setup Instructions

### Prerequisites
- Node.js (v18+)
- Python (v3.10+) with `requirements.txt` installed for the platform.

### Installation

1. Navigate to `Common/qa-launcher-console/backend` and install dependencies:
   ```bash
   cd backend
   npm install
   ```

2. Navigate to `Common/qa-launcher-console/frontend` and install dependencies:
   ```bash
   cd ../frontend
   npm install
   ```

## Running the Console

You can run the backend and frontend separately, or use a helper script if provided.

**1. Start Backend Controller:**
```bash
cd backend
npm start
```
(Runs on port 3001)

**2. Start Frontend Console:**
```bash
cd frontend
npm run dev
```
(Runs on port 5174)

Open [http://localhost:5174](http://localhost:5174) to use the console.

## Usage

1. Select **Target Application** (e.g., Retail).
2. Select **Execution Mode** (Backend, Frontend, or Both).
3. Click **EXECUTE RUN**.
4. Monitor logs in the dual console view.
5. Check Pass/Fail status.
6. Export logs if needed.
