# 🚀 HRM Task Template - Unified Execution Protocol

**Purpose**: Unified task execution template for all HRM development tasks  
**Last Updated**: January 31, 2026  
**Agent**: Hindra (HRM Domain Owner)  
**Status**: ✅ ACTIVE

---

## 📋 MANDATORY PRE-TASK READING

**Before starting ANY task, you MUST read:**

1. **`@tasks/10-CPs.md`** - The 10 Critical Concerns (Non-Negotiable)
2. **`@session_start/00_hindra_registry_system.md`** - File, Table, and Route Registry
3. **`@session_start/00_hindra_binding_commitment.md`** - Binding Commitment

**Quick Reference:**
```bash
# Read the 10 critical concerns
Read: HRM/tasks/10-CPs.md

# Read the registry system
Read: HRM/bootstrap-hrm-only/session_start/00_hindra_registry_system.md

# Read the binding commitment
Read: HRM/bootstrap-hrm-only/session_start/00_hindra_binding_commitment.md
```

---

## 🎯 TASK EXECUTION PROTOCOL

### Step 1: Pre-Task Checklist (MANDATORY)

Before starting ANY task, complete this checklist:

- [ ] Read `HRM/tasks/10-CPs.md` (The 10 Critical Concerns)
- [ ] Read `HRM/bootstrap-hrm-only/session_start/00_hindra_registry_system.md` (Registry System)
- [ ] Confirm Django command pattern: `python backend/manage.py [command]`
- [ ] Confirm toolbar approach: backend-driven via `erp_menu_items` table
- [ ] Confirm unified shell approach
- [ ] Confirm folder structure boundaries
- [ ] Reference `04_08_platform-arch-toolbar-universal-mode-prop.md` if toolbar task
- [ ] Reference `06_Layout_Terminology.md` if UI task
- [ ] Verify all 10 concerns are addressed
- [ ] Proceed with task only after all checks pass

### Step 2: Task Execution

Execute the task following the 10 critical concerns:

1. ✅ **Unified Shell Approach** - Single frontend serves all modules
2. ✅ **Different Folder Structure** - HRM, CRM, FMS, Retail in different environments
3. ✅ **Toolbar Approach** - Backend-driven via `erp_menu_item` table
4. ✅ **Single manage.py** - Only at `D:\olivine-erp\backend`
5. ✅ **Django Command Pattern** - ALWAYS use `python backend/manage.py [command]`
6. ✅ **Layout Terminology** - Reference `06_Layout_Terminology.md`
7. ✅ **Task Completion Compliance** - Read all concerns before proceeding
8. ✅ **File Location Registry** - Use registry system to locate files
9. ✅ **Registry System** - Always reference registry for file locations, table routes, Django routes
10. ✅ **Django Command Failure Prevention** - NEVER use `cd backend && python manage.py [command]`

### Step 3: Task Completion Checklist

Before completing ANY task, verify:

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

## 🔧 QUICK REFERENCE COMMANDS

### Django Commands (ALWAYS use this pattern)

```bash
# System checks
python backend/manage.py check

# Create migrations
python backend/manage.py makemigrations

# Apply migrations
python backend/manage.py migrate

# Start server
python backend/manage.py runserver

# Django shell
python backend/manage.py shell

# Create superuser
python backend/manage.py createsuperuser
```

### Database Queries

```bash
# Check ERPMenuItem table
python backend/manage.py shell -c "from core.auth_access.backend.user_management.models import ERPMenuItem; item = ERPMenuItem.objects.get(menu_id='EMPLOYEE_RECORDS'); print(item.applicable_toolbar_config)"

# List all HRM menu items
python backend/manage.py shell -c "from core.auth_access.backend.user_management.models import ERPMenuItem; items = ERPMenuItem.objects.filter(module_name='HRM'); [print(f'{item.menu_id}: {item.applicable_toolbar_config}') for item in items]"
```

---

## 📚 REFERENCE DOCUMENTATION

### Critical Documents

- **10-CPs**: `HRM/tasks/10-CPs.md` - The 10 Critical Concerns
- **Registry System**: `HRM/bootstrap-hrm-only/session_start/00_hindra_registry_system.md`
- **Binding Commitment**: `HRM/bootstrap-hrm-only/session_start/00_hindra_binding_commitment.md`
- **Quick Start**: `HRM/bootstrap-hrm-only/session_start/00_hindra_start.md` (QUICK START section)

### Toolbar Governance

- **Toolbar Universal Mode Prop**: `HRM/bootstrap-hrm-only/session_start/04_08_platform-arch-toolbar-universal-mode-prop.md`
- **Toolbar Mode Filtering**: `HRM/bootstrap-hrm-only/session_start/04_02_toolbar_mode_based_filtering_v2.md`
- **Toolbar Final Governance**: `HRM/bootstrap-hrm-only/session_start/04_07_toolbar_final_governance_v2_3001.md`

### UI Standards

- **Layout Terminology**: `HRM/bootstrap-hrm-only/session_start/06_Layout_Terminology.md`
- **Quick Reference Patterns**: `HRM/bootstrap-hrm-only/session_start/01_quick_reference_patterns.md`

### Development

- **HRM Development Guide**: `HRM/bootstrap-hrm-only/session_start/05_01_hindra_hrm_development_guide.md`
- **Task Prompt Reference**: `HRM/bootstrap-hrm-only/session_start/05_01_hindra_hrm_task_prompt_ref.md`
- **BBP Creation Template**: `HRM/bootstrap-hrm-only/session_start/06_01_only_for_bbp_creation.md`

---

## 🎯 TASK EXECUTION EXAMPLE

### Example: Fix Employee Records Toolbar

**User Request:**
```
Refer @tasks @10-CPs, and complete the task with all checklists required

Task: Fix Employee Records toolbar - E and D buttons are missing
```

**Execution:**

1. **Pre-Task Checklist:**
   - [x] Read `HRM/tasks/10-CPs.md`
   - [x] Read `HRM/bootstrap-hrm-only/session_start/00_hindra_registry_system.md`
   - [x] Confirm Django command pattern: `python backend/manage.py [command]`
   - [x] Confirm toolbar approach: backend-driven via `erp_menu_item` table
   - [x] Confirm unified shell approach
   - [x] Confirm folder structure boundaries
   - [x] Reference `04_08_platform-arch-toolbar-universal-mode-prop.md`
   - [x] Reference `06_Layout_Terminology.md` (if UI task)
   - [x] Verify all 10 concerns are addressed
   - [x] Proceed with task

2. **Task Execution:**
   - Check database: `python backend/manage.py shell -c "from core.auth_access.backend.user_management.models import ERPMenuItem; item = ERPMenuItem.objects.get(menu_id='EMPLOYEE_RECORDS'); print(item.applicable_toolbar_config)"`
   - Result: `NRQFVEDIOX` (correct)
   - Check frontend: `HRM/frontend/src/hooks/useToolbarConfig.ts`
   - Found hardcoded config: `toolbar_list: 'NRQFVIOX'` (missing E and D)
   - Fix: Update to `toolbar_list: 'NRQFVEDIOX'`

3. **Task Completion Checklist:**
   - [x] 1. Unified shell approach followed
   - [x] 2. Different folder structure respected
   - [x] 3. Toolbar approach driven from backend
   - [x] 4. Single manage.py used correctly
   - [x] 5. Django command pattern correct
   - [x] 6. Layout terminology referenced (if UI task)
   - [x] 7. Task completion compliance verified
   - [x] 8. File location registry referenced
   - [x] 9. Registry system used for all lookups
   - [x] 10. Django command failure prevented

4. **Result:**
   - ✅ Database updated: `NRQFVEDIOX`
   - ✅ Frontend updated: `NRQFVEDIOX`
   - ✅ Both in sync
   - ✅ SCCB compliant

---

## 📋 TASK COMPLETION TEMPLATE

Use this template when completing a task:

```
**Task Complete**

**Summary**: [Brief description of what was done]

**Changes Made**:
- [File 1]: [Description of change]
- [File 2]: [Description of change]

**Verification**:
- [x] 1. Unified shell approach followed
- [x] 2. Different folder structure respected
- [x] 3. Toolbar approach driven from backend
- [x] 4. Single manage.py used correctly
- [x] 5. Django command pattern correct
- [x] 6. Layout terminology referenced (if UI task)
- [x] 7. Task completion compliance verified
- [x] 8. File location registry referenced
- [x] 9. Registry system used for all lookups
- [x] 10. Django command failure prevented

**Status**: ✅ COMPLIANT with all 10 critical concerns
```

---

**END OF TASK TEMPLATE**

**Version**: 1.0  
**Last Updated**: January 31, 2026  
**Agent**: Hindra (HRM Domain Owner)  
**Status**: ✅ ACTIVE
