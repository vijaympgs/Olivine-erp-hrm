# 🚀 Olivine Platform Startup Scripts

**Last Updated**: 2026-01-17  
**Version**: 2.0 (Unified Shell Architecture)

---

## 📋 Overview

This directory contains batch scripts for starting the Olivine ERP Platform in various configurations. The platform uses a **Unified Shell Architecture** where all modules (Retail, HRM, CRM, FMS) run through a single backend and frontend.

---

## 🎯 Recommended Startup Methods

### **Option 1: Unified Platform (RECOMMENDED)** ⭐
**Script**: `START_UNIFIED.bat`

Starts the complete ERP platform with all modules integrated:
- **Unified Backend** (Port 8000) - Django REST API serving all modules
- **Unified Frontend** (Port 3001) - React shell with all module UIs

**When to use**:
- ✅ Normal development work
- ✅ Testing cross-module features
- ✅ Full platform QA
- ✅ Demo/presentation mode

**Features**:
- ✅ Automatic port cleanup (8000, 3001)
- ✅ Auto-opens browser to http://localhost:3001
- ✅ Displays login credentials
- ✅ Separate console windows for backend/frontend logs

**Usage**:
```bash
cd C:\00mindra\olivine-platform
scripts\START_UNIFIED.bat
```

---

### **Option 2: QA Launcher Console** 🎛️
**Script**: `START_LAUNCHER.bat`

Starts the orchestration console for managing multiple applications:
- **Launcher Backend** (Port 3000) - Process controller
- **Launcher Frontend** (Port 5174) - Console UI

**When to use**:
- ✅ Need to start/stop modules independently
- ✅ Real-time log monitoring across modules
- ✅ Testing module isolation
- ✅ Advanced QA scenarios

**Features**:
- ✅ Visual process management
- ✅ Side-by-side console views
- ✅ Automatic port cleanup (3000, 5174)
- ✅ Health checks and port monitoring
- ✅ Auto-installs dependencies if missing

**Usage**:
```bash
cd C:\00mindra\olivine-platform
scripts\START_LAUNCHER.bat
```

**Next Step**: From the launcher UI, click "ERP Core - Retail, HRM, CRM, FMS" to start the unified platform.

---

### **Option 3: Quick Start** ⚡
**Script**: `QUICK_START.bat`

Simplified startup for rapid development iterations:
- No port checking
- No browser launch
- Minimal output

**When to use**:
- ✅ Quick restarts during development
- ✅ You already have browser tabs open
- ✅ Testing backend-only changes

**Usage**:
```bash
cd C:\00mindra\olivine-platform
scripts\QUICK_START.bat
```

---

## 📦 Legacy Scripts (Still Available)

### `setup.bat`
Initial environment setup - creates venv, installs dependencies, runs migrations.

**Use once** when first setting up the project.

### `dev.bat`
Legacy development startup (uses relative paths, port 5173).

⚠️ **Note**: This script uses the old port configuration. Use `QUICK_START.bat` instead.

### `START_BACKEND.bat`
Starts only the backend server.

⚠️ **Warning**: Uses incorrect path (`olivine-erp-platform` instead of `olivine-platform`). Use `QUICK_START.bat` or `START_UNIFIED.bat` instead.

### `START_FRONTEND.bat`
Starts only the frontend server.

⚠️ **Warning**: Uses port 5173 instead of 3001. Use `QUICK_START.bat` or `START_UNIFIED.bat` instead.

### `START_BOTH.bat`
Starts both servers with aggressive cleanup.

⚠️ **Warning**: 
- Kills ALL Python/Node processes (may affect other work)
- Uses incorrect paths
- Use `START_UNIFIED.bat` instead

---

## 🌐 Port Reference

| Service | Port | URL |
|---------|------|-----|
| **Unified Backend** | 8000 | http://localhost:8000 |
| **Django Admin** | 8000 | http://localhost:8000/admin |
| **Unified Frontend** | 3001 | http://localhost:3001 |
| **Launcher Backend** | 3000 | http://localhost:3000 |
| **Launcher Frontend** | 5174 | http://localhost:5174 |

---

## 🔐 Default Credentials

| Role | Username | Password |
|------|----------|----------|
| **Admin** | admin | admin123 |
| **Back Office Manager** | boadmin | boadmin123 |
| **Back Office User** | bouser | bouser123 |
| **POS Manager** | posadmin | posadmin123 |
| **POS User** | posuser | posuser123 |

---

## 🏗️ Architecture Notes

### **Unified Shell Design**
The platform uses a single integrated backend and frontend:

```
olivine-platform/
├── backend/              # Unified Django backend (Port 8000)
│   ├── manage.py
│   └── erp_core/        # Settings and URL routing
├── frontend/            # Unified React frontend (Port 3001)
│   ├── src/
│   └── package.json
├── Retail/              # Retail module (integrated)
├── HRM/                 # HRM module (integrated)
├── CRM/                 # CRM module (integrated)
├── FMS/                 # FMS module (integrated)
└── Common/
    └── qa-launcher-console/  # Orchestration tool
```

### **Module Integration**
All modules are **consumers** of the unified shell:
- Backend: Django apps registered in `backend/erp_core/settings/base.py`
- Frontend: React routes registered in `frontend/src/App.tsx`
- No standalone module servers (except for isolated debugging)

---

## 🛠️ Troubleshooting

### **Port Already in Use**
The `START_UNIFIED.bat` script automatically clears ports 8000 and 3001. If you need manual cleanup:

```bash
# Find process on port 8000
netstat -ano | findstr :8000

# Kill by PID
taskkill /F /PID <PID>
```

### **Backend Won't Start**
1. Check if virtual environment is activated
2. Verify Python dependencies: `pip install -r backend/requirements.txt`
3. Run migrations: `python backend/manage.py migrate`

### **Frontend Won't Start**
1. Check Node.js version (should be 18+)
2. Install dependencies: `cd frontend && npm install`
3. Clear cache: `npm cache clean --force`

### **Module Not Loading**
1. Check `backend/erp_core/settings/base.py` - module app in `INSTALLED_APPS`?
2. Check `backend/erp_core/urls.py` - module URLs included?
3. Check frontend routing in `frontend/src/App.tsx`

---

## 📚 Related Documentation

- **Unified Shell Guide**: `Common/qa-launcher-console/UNIFIED_APP_SHELL_GUIDE.md`
- **HRM Implementation**: `HRM/bootstrap-hrm-only/HRM_CORE_IMPLEMENTATION_GUIDE.md`
- **Astra Bootstrap**: `astra-bootstrap.md`
- **Architecture**: `ARCHITECTURE.md`

---

## 🎯 Quick Reference

**First time setup**:
```bash
scripts\setup.bat
```

**Daily development** (recommended):
```bash
scripts\START_UNIFIED.bat
```

**Advanced QA/monitoring**:
```bash
scripts\START_LAUNCHER.bat
```

**Quick restart**:
```bash
scripts\QUICK_START.bat
```

---

**Maintained by**: Astra (AI Agent)  
**Approved by**: Viji (Product Owner)  
**Status**: ⚡ ACTIVE
