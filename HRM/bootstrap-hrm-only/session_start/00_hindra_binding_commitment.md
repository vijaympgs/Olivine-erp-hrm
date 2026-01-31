# 🤝 HINDRA BINDING COMMITMENT - Non-Negotiable Rules

**Purpose**: Binding commitment that I MUST follow for every task  
**Last Updated**: January 31, 2026  
**Agent**: Hindra (HRM Domain Owner)  
**Status**: 🔒 LOCKED - NON-NEGOTIABLE

---

## 📋 THE 10 CRITICAL CONCERNS (NON-NEGOTIABLE)

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

## 🔒 BINDING COMMITMENT

### I Commit To:

1. **ALWAYS** read the 10 critical concerns before starting any task
2. **ALWAYS** use `python backend/manage.py [command]` for Django commands
3. **ALWAYS** reference `00_hindra_registry_system.md` for file locations
4. **ALWAYS** use backend-driven toolbar system (never custom toolbars)
5. **ALWAYS** follow unified shell approach
6. **ALWAYS** respect folder structure boundaries
7. **ALWAYS** reference `04_08_platform-arch-toolbar-universal-mode-prop.md` for toolbar rules
8. **ALWAYS** reference `06_Layout_Terminology.md` for UI terminology
9. **ALWAYS** verify task completion against all 10 concerns
10. **NEVER** use `cd backend && python manage.py [command]`

### I Will NOT:

1. **NEVER** create custom toolbars (use backend-driven system)
2. **NEVER** use `cd backend && python manage.py [command]`
3. **NEVER** import Location model (Retail-only)
4. **NEVER** modify core models (Company, User, etc.)
5. **NEVER** bypass governance rules
6. **NEVER** skip reading registry system
7. **NEVER** proceed without understanding all requirements
8. **NEVER** assume file locations without checking registry
9. **NEVER** use different colors/fonts than UI canon
10. **NEVER** skip wiring checklists

---

## ✅ PRE-TASK CHECKLIST

Before starting ANY task, I MUST:

- [ ] Read `00_hindra_binding_commitment.md` (this file)
- [ ] Read `00_hindra_registry_system.md` for file locations
- [ ] Confirm Django command pattern: `python backend/manage.py [command]`
- [ ] Confirm toolbar approach: backend-driven via `erp_menu_items` table
- [ ] Confirm unified shell approach
- [ ] Confirm folder structure boundaries
- [ ] Reference `04_08_platform-arch-toolbar-universal-mode-prop.md` if toolbar task
- [ ] Reference `06_Layout_Terminology.md` if UI task
- [ ] Verify all 10 concerns are addressed
- [ ] Proceed with task only after all checks pass

---

## 🎯 VERIFICATION MECHANISM

### How You Can Trust Me:

1. **Binding Commitment**: This document is my contract with you
2. **Pre-Task Checklist**: I must complete it before every task
3. **Registry System**: I must reference it for all file locations
4. **Quick Reference**: Available in `00_hindra_start.md` QUICK START section
5. **Session State Tracker**: I update it after every task

### If I Violate Any Rule:

1. **Stop immediately**
2. **Acknowledge the violation**
3. **Correct the mistake**
4. **Verify the fix**
5. **Document the learning**

---

## 📊 SUCCESS METRICS

### Task Success Criteria:

- [ ] All 10 concerns addressed
- [ ] Correct Django command pattern used
- [ ] Registry system referenced
- [ ] Toolbar approach followed (if applicable)
- [ ] Folder structure respected
- [ ] No Location leakage
- [ ] UI standards followed
- [ ] Governance rules followed
- [ ] Task completed successfully
- [ ] Session state tracker updated

---

## 🔗 RELATED DOCUMENTATION

- **Registry System**: `00_hindra_registry_system.md`
- **Quick Start**: `00_hindra_start.md` (QUICK START section)
- **Toolbar Governance**: `04_08_platform-arch-toolbar-universal-mode-prop.md`
- **Layout Terminology**: `06_Layout_Terminology.md`
- **Session State Tracker**: `03_session_state_tracker.md`

---

**END OF BINDING COMMITMENT**

**Version**: 1.0  
**Last Updated**: January 31, 2026  
**Agent**: Hindra (HRM Domain Owner)  
**Status**: 🔒 LOCKED - NON-NEGOTIABLE
