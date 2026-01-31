# 📋 10-CPs - 10 Critical Concerns (Non-Negotiable)

**Purpose**: Quick reference for the 10 critical concerns that MUST be followed for every task  
**Last Updated**: January 31, 2026  
**Agent**: Hindra (HRM Domain Owner)  
**Status**: 🔒 LOCKED - NON-NEGOTIABLE

---

## 🚨 THE 10 CRITICAL CONCERNS

### 1. ✅ Unified Shell Approach
**Rule**: Single frontend shell serves all modules (HRM, CRM, FMS, Retail)
**Implementation**: 
- Frontend at `frontend/` serves all modules
- No separate frontend for each module
- All modules share the same React app

### 2. ✅ Different Folder Structure
**Rule**: HRM, CRM, FMS, Retail in different environments
**Current Machine**: HRM + Core + Common + Olivine-backend + Olivine-frontend
**Structure**:
```
HRM/          → HRM module (my ownership)
CRM/          → CRM module (Agent E)
FMS/          → FMS module (Finra)
Retail/       → Retail module (Astra)
Core/         → Shared core functionality
Common/       → Shared domain models
backend/      → Unified Django backend
frontend/     → Unified React frontend
```

### 3. ✅ Toolbar Approach Driven from Backend
**Rule**: Toolbar configuration driven from `erp_menu_item` table
**Reference**: `HRM/bootstrap-hrm-only/session_start/04_08_platform-arch-toolbar-universal-mode-prop.md`
**Implementation**:
- Backend: `erp_menu_items` table stores toolbar configs
- API: `/api/toolbar-permissions/?view_id=X&mode=Y`
- Frontend: Uses `MasterToolbar` component with backend-driven permissions
- NEVER create custom toolbars

### 4. ✅ Single manage.py
**Rule**: Only one `manage.py` at `D:\olivine-erp\backend`
**Location**: `backend/manage.py`
**NEVER**: Look for `d:\olivine-erp\manage.py`

### 5. ✅ Django Command Pattern
**Rule**: ALWAYS use `python backend/manage.py [command]`
**NEVER**: Use `cd backend && python manage.py [command]`
**Why it fails**: `cd backend` changes working directory, then `python manage.py` looks in wrong location
**Correct Pattern**:
```bash
python backend/manage.py check
python backend/manage.py makemigrations
python backend/manage.py migrate
python backend/manage.py runserver
python backend/manage.py shell
```

### 6. ✅ Layout Terminology Reference
**Rule**: Reference `HRM/bootstrap-hrm-only/session_start/06_Layout_Terminology.md`
**Purpose**: UI layout terminology reference
**When to use**: Before implementing any UI changes

### 7. ✅ Task Completion Compliance
**Rule**: Read concerns 1-6, wait for detailed prompt for #6
**Reference**: `HRM/bootstrap-hrm-only/session_start/toolbar-err.md`
**Implementation**: Do not proceed without understanding all requirements

### 8. ✅ File Location Registry
**Rule**: Use registry system to locate files
**Reference**: `HRM/bootstrap-hrm-only/session_start/00_hindra_registry_system.md`
**Key Locations**:
- ERPMenuItem: `backend/core/auth_access/backend/user_management/models.py`
- HRM Models: `HRM/backend/hrm/models/`
- Toolbar: `frontend/core/ui-canon/frontend/ui/components/MasterToolbarConfigDriven.tsx`

### 9. ✅ Registry System
**Rule**: Always reference registry for file locations, table routes, Django routes
**Reference**: `HRM/bootstrap-hrm-only/session_start/00_hindra_registry_system.md`
**Contents**:
- File locations (Django, frontend, HRM)
- Database table registry
- Import path registry
- API endpoint registry
- Django command patterns
- Common patterns
- Troubleshooting guide

### 10. ✅ Django Command Failure Prevention
**Rule**: NEVER use `cd backend && python manage.py [command]`
**Correct**: `python backend/manage.py [command]`
**Registry Reference**: `00_hindra_registry_system.md` - Section 1

---

## ✅ PRE-TASK CHECKLIST

Before starting ANY task, I MUST:

- [ ] Read `HRM/tasks/10-CPs.md` (this file)
- [ ] Read `HRM/bootstrap-hrm-only/session_start/00_hindra_registry_system.md` for file locations
- [ ] Confirm Django command pattern: `python backend/manage.py [command]`
- [ ] Confirm toolbar approach: backend-driven via `erp_menu_items` table
- [ ] Confirm unified shell approach
- [ ] Confirm folder structure boundaries
- [ ] Reference `04_08_platform-arch-toolbar-universal-mode-prop.md` if toolbar task
- [ ] Reference `06_Layout_Terminology.md` if UI task
- [ ] Verify all 10 concerns are addressed
- [ ] Proceed with task only after all checks pass

---

## 🎯 TASK COMPLETION CHECKLIST

Before completing ANY task, I MUST verify:

- [ ] 1. Unified shell approach followed
- [ ] 2. Different folder structure respected
- [ ] 3. Toolbar approach driven from backend
- [ ] 4. Single manage.py used correctly
- [ ] 5. Django command pattern correct
- [ ] 6. Layout terminology referenced (if UI task)
- [ ] 7. Task completion compliance verified
- [ ] 8. File location registry referenced
- [ ] 9. Registry system used for all lookups
- [ ] 10. Django command failure prevented

---

## 🔗 RELATED DOCUMENTATION

- **Full Binding Commitment**: `HRM/bootstrap-hrm-only/session_start/00_hindra_binding_commitment.md`
- **Registry System**: `HRM/bootstrap-hrm-only/session_start/00_hindra_registry_system.md`
- **Quick Start**: `HRM/bootstrap-hrm-only/session_start/00_hindra_start.md` (QUICK START section)
- **Toolbar Governance**: `HRM/bootstrap-hrm-only/session_start/04_08_platform-arch-toolbar-universal-mode-prop.md`
- **Layout Terminology**: `HRM/bootstrap-hrm-only/session_start/06_Layout_Terminology.md`
- **Session State Tracker**: `HRM/bootstrap-hrm-only/session_start/03_session_state_tracker.md`

---

**END OF 10-CPs**

**Version**: 1.0  
**Last Updated**: January 31, 2026  
**Agent**: Hindra (HRM Domain Owner)  
**Status**: 🔒 LOCKED - NON-NEGOTIABLE
