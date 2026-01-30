# 🦅 OLIVINE PLATFORM - MASTER GUIDE
**Date**: 2026-01-17
**Status**: Development Phase

---

## 🚀 **GETTING STARTED**

### **1. Launch the Platform**
Use the **App Launcher** (localhost:3000) to manage services. This is your command center.

```bash
cd c:\00mindra\olivine-platform\Common\qa-launcher-console
npm start
# Opens http://localhost:3000
```

### **2. Select Your Mode**
The App Launcher has two main buttons:

#### **A. "ERP Core - Retail,Hrm,Crm, Fms"** (Main)
- Starts the unified ERP platform
- **Backend**: Port 8000
- **Frontend**: Port 3001
- **Includes**: Retail (fully working), FMS/HRM/CRM (backend integration pending)

#### **B. "Meet"** (Collab)
- Starts the Meet collaboration tool
- **Backend**: Python/Poetry
- **Frontend**: Port 3005

---

## 🏗️ **SYSTEM ARCHITECTURE**

### **The Enterprise Shell**
The platform is organized as an Enterprise Shell containing modular components.

```
olivine-platform/
├── Retail/                   # Lead Module
├── HRM/                      # Module
├── CRM/                      # Module
├── FMS/                      # Module
└── Meet/                     # Separate App
```

### **Unified Access**
Although developed as modules, the **ERP Core** provides a unified entry point:
- **One Backend**: Port 8000 serves APIs for all ERP modules
- **One Frontend**: Port 3001 provides the shell with Sidebar navigation
- **Sidebar**: Navigate between Retail, HRM, CRM, FMS seamlessy

---

## 🎯 **YOUR DEVELOPMENT REPO**

You are currently focused on:
1. **Retail**: Core features (POS, Inventory) - ✅ Working
2. **FMS**: Financial Management - ⏳ Next Priority

Other agents work on HRM and CRM.

---

## 📋 **NEXT SESSION ACTION ITEMS**

1. **Start App Launcher**: `npm start` in `Common/qa-launcher-console`
2. **Click "ERP Core..."**: Launch the platform
3. **Login**: `admin` / `admin123`
4. **Develop Retail**: Continue adding features
5. **Setup FMS**: Begin FMS module setup if ready

---

**This is the single source of truth for the platform setup.**
