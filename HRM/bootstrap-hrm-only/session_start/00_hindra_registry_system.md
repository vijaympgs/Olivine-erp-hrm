# 🗂️ HINDRA REGISTRY SYSTEM - File, Table, and Route Reference

**Purpose**: Comprehensive registry for locating files, database tables, Django routes, and command patterns  
**Last Updated**: January 31, 2026  
**Agent**: Hindra (HRM Domain Owner)  
**Status**: ✅ ACTIVE

---

## 📋 TABLE OF CONTENTS

1. [Critical Command Patterns](#1-critical-command-patterns)
2. [Django File Locations](#2-django-file-locations)
3. [Database Table Registry](#3-database-table-registry)
4. [Import Path Registry](#4-import-path-registry)
5. [Frontend File Locations](#5-frontend-file-locations)
6. [HRM Module Structure](#6-hrm-module-structure)
7. [API Endpoint Registry](#7-api-endpoint-registry)
8. [Common Patterns](#8-common-patterns)
9. [Troubleshooting](#9-troubleshooting)

---

## 1. CRITICAL COMMAND PATTERNS

### ✅ CORRECT Django Commands

**ALWAYS use this pattern:**
```bash
python backend/manage.py [command]
```

**Examples:**
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

# Shell command with inline code
python backend/manage.py shell -c "from core.auth_access.backend.user_management.models import ERPMenuItem; print(ERPMenuItem.objects.count())"
```

### ❌ WRONG Django Commands

**NEVER use these patterns:**
```bash
# WRONG - cd changes working directory
cd backend && python manage.py check

# WRONG - Wrong path
python manage.py check

# WRONG - Wrong path
cd backend && python backend/manage.py check
```

**Why it fails:**
- `cd backend` changes working directory to `d:\olivine-erp\backend`
- Then `python manage.py check` looks for `d:\olivine-erp\manage.py` (wrong!)
- Correct path is `d:\olivine-erp\backend\manage.py`

---

## 2. DJANGO FILE LOCATIONS

### Core Django Files

| File | Location | Purpose |
|------|----------|---------|
| **manage.py** | `backend/manage.py` | Django management entry point |
| **settings** | `backend/erp_core/settings/` | Django settings (base.py, local.py, etc.) |
| **urls.py** | `backend/erp_core/urls.py` | Main URL router |
| **wsgi.py** | `backend/erp_core/wsgi.py` | WSGI entry point |

### Backend Module Locations

| Module | Location | Purpose |
|--------|----------|---------|
| **Core Auth** | `backend/core/auth_access/backend/user_management/` | Authentication, toolbar system |
| **Core Models** | `backend/core/auth_access/backend/user_management/models.py` | ERPMenuItem, Role, RolePermission, UserRole |
| **Core Admin** | `backend/core/auth_access/backend/user_management/admin.py` | Django admin for core models |
| **Core Services** | `backend/core/auth_access/backend/user_management/services/` | Business logic (toolbar_permission_service.py) |
| **Core Views** | `backend/core/auth_access/backend/user_management/toolbar_views.py` | API endpoints |

### HRM Backend Locations

| Module | Location | Purpose |
|--------|----------|---------|
| **HRM Models** | `HRM/backend/hrm/models/` | HRM domain models (employee.py, department.py, etc.) |
| **HRM Admin** | `HRM/backend/hrm/admin.py` | Django admin for HRM models |
| **HRM Mixins** | `HRM/backend/hrm/admin_mixins.py` | Admin mixins (TableNameDisplayMixin) |
| **HRM Services** | `HRM/backend/hrm/services/` | HRM business logic |

### Common Module Locations

| Module | Location | Purpose |
|--------|----------|---------|
| **Common Domain** | `common/domain/models.py` | Shared models (Company) |
| **Common Auth** | `common/auth/` | Authentication utilities |
| **Common Permissions** | `common/permissions/` | Permission utilities |

---

## 3. DATABASE TABLE REGISTRY

### Core Tables (Toolbar System)

| Table | Model | Location | Purpose |
|-------|-------|----------|---------|
| **erp_menu_items** | ERPMenuItem | `backend/core/auth_access/backend/user_management/models.py` | Menu registry + toolbar configs |
| **roles** | Role | `backend/core/auth_access/backend/user_management/models.py` | Role definitions |
| **role_permissions** | RolePermission | `backend/core/auth_access/backend/user_management/models.py` | Permission matrix |
| **user_roles** | UserRole | `backend/core/auth_access/backend/user_management/models.py` | User-role mapping |
| **auth_user** | User | Django built-in | User authentication |

### HRM Tables

| Table | Model | Location | Purpose |
|-------|-------|----------|---------|
| **hrm_employee_records** | EmployeeRecord | `HRM/backend/hrm/models/employee.py` | Employee master data |
| **hrm_departments** | Department | `HRM/backend/hrm/models/department.py` | Department master data |
| **hrm_positions** | Position | `HRM/backend/hrm/models/organizational_unit.py` | Position master data |

### System Tools Tables

| Table | Model | Location | Purpose |
|-------|-------|----------|---------|
| **erp_menu_items** | ERPMenuItem | `backend/core/auth_access/backend/user_management/models.py` | System Tools menu registry |

### System Tools Menu Items

| Menu ID | Menu Name | Toolbar Config | Route Path | Module |
|---------|-----------|----------------|-------------|--------|
| **FILE_SEARCH_EXPLORER** | File Search Explorer | `NESCKVDXRQF` | `/system-tools/file-search-explorer` | SYSTEM_TOOLS |
| **VISUAL_EXTRACTOR** | Visual Extractor | `NESCKVDXRQF` | `/system-tools/visual-extractor` | SYSTEM_TOOLS |
| **DATAOPS_STUDIO** | DataOps Studio | `NESCKVDXRQF` | `/system-tools/dataops-studio` | SYSTEM_TOOLS |

### Shared Tables

| Table | Model | Location | Purpose |
|-------|-------|----------|---------|
| **companies** | Company | `common/domain/models.py` | Company entities (lazy string reference) |

### How to Access Tables

**Django Shell:**
```bash
python backend/manage.py shell
```

**Import Pattern:**
```python
from core.auth_access.backend.user_management.models import ERPMenuItem, Role, RolePermission, UserRole
from HRM.backend.hrm.models.employee import EmployeeRecord
from common.domain.models import Company
```

**Query Examples:**
```python
# Get ERPMenuItem
item = ERPMenuItem.objects.get(menu_id='EMPLOYEE_RECORDS')

# Get all HRM menu items
hrm_items = ERPMenuItem.objects.filter(module_name='HRM')

# Get employee records
employees = EmployeeRecord.objects.all()

# Get company
company = Company.objects.first()
```

---

## 4. IMPORT PATH REGISTRY

### Core Models

```python
# Correct import paths
from core.auth_access.backend.user_management.models import ERPMenuItem
from core.auth_access.backend.user_management.models import Role
from core.auth_access.backend.user_management.models import RolePermission
from core.auth_access.backend.user_management.models import UserRole
from core.auth_access.backend.user_management.services.toolbar_permission_service import resolve_toolbar_permissions
```

### HRM Models

```python
# Correct import paths
from HRM.backend.hrm.models.employee import EmployeeRecord
from HRM.backend.hrm.models.department import Department
from HRM.backend.hrm.models.organizational_unit import Position
```

### Common Models

```python
# Correct import paths
from common.domain.models import Company
```

### Django Admin

```python
# Correct import paths
from django.contrib import admin
from core.auth_access.backend.user_management.admin import ERPMenuItemAdmin
```

---

## 5. FRONTEND FILE LOCATIONS

### Core Frontend Files

| File | Location | Purpose |
|------|----------|---------|
| **App.tsx** | `frontend/src/App.tsx` | Main React app |
| **index.html** | `frontend/index.html` | HTML entry point |
| **package.json** | `frontend/package.json` | Frontend dependencies |

### Shared UI Components

| Component | Location | Purpose |
|-----------|----------|---------|
| **MasterToolbar** | `frontend/core/ui-canon/frontend/ui/components/MasterToolbarConfigDriven.tsx` | Backend-driven toolbar |
| **useToolbarConfig** | `frontend/src/hooks/useToolbarConfig.ts` | Toolbar configuration hook |
| **Sidebar** | `frontend/src/components/ui/Sidebar.tsx` | Navigation sidebar |
| **AppHeader** | `frontend/src/components/ui/AppHeader.tsx` | Application header |

### HRM Frontend Files

| File | Location | Purpose |
|------|----------|---------|
| **EmployeeRecords** | `HRM/frontend/src/pages/EmployeeRecords.tsx` | Employee records page |
| **EmployeeForm** | `HRM/frontend/src/pages/EmployeeForm.tsx` | Employee form component |
| **employeeService** | `HRM/frontend/src/services/employeeService.ts` | Employee API service |

### System Tools Frontend Files

| File | Location | Purpose |
|------|----------|---------|
| **VisualExtractorPage** | `frontend/src/pages/system_tools/visual_extractor/VisualExtractorPage.tsx` | OCR image to text extraction |
| **FileSearchExplorerPage** | `frontend/src/pages/admin/FileSearchExplorerPage.tsx` | File search explorer |
| **DataOpsStudioPage** | `frontend/src/pages/system_tools/dataops_studio/DataOpsStudioPage.tsx` | Data operations studio |
| **WebConsolePage** | `frontend/src/pages/system_tools/web_console/WebConsolePage.tsx` | Embedded web browser |

---

## 6. HRM MODULE STRUCTURE

### Backend Structure

```
HRM/backend/hrm/
├── models/
│   ├── employee.py          # EmployeeRecord model
│   ├── department.py        # Department model
│   └── organizational_unit.py  # Position model
├── admin.py                 # Django admin for HRM models
├── admin_mixins.py          # Admin mixins (TableNameDisplayMixin)
└── services/                # HRM business logic
```

### Frontend Structure

```
HRM/frontend/src/
├── pages/
│   ├── EmployeeRecords.tsx  # Employee records page
│   ├── EmployeeForm.tsx     # Employee form component
│   └── ProfileView.tsx      # Profile view page
└── services/
    └── employeeService.ts   # Employee API service
```

---

## 7. API ENDPOINT REGISTRY

### Toolbar API

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/toolbar-permissions/` | GET | Get toolbar permissions for a screen |

**Request:**
```http
GET /api/toolbar-permissions/?view_id=EMPLOYEE_RECORDS&mode=VIEW
Authorization: Bearer <token>
```

**Response:**
```json
{
  "menu_id": "EMPLOYEE_RECORDS",
  "mode": "VIEW",
  "toolbar_string": "NRQFVEDIOX",
  "permission_mask": "1111111111",
  "allowed_characters": ["N", "R", "Q", "F", "V", "E", "D", "I", "O", "X"],
  "allowed_actions": ["new", "refresh", "search", "filter", "view", "edit", "delete", "import", "export", "exit"]
}
```

### Employee API

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/hrm/employees/` | GET | List employees |
| `/api/hrm/employees/` | POST | Create employee |
| `/api/hrm/employees/{id}/` | GET | Get employee details |
| `/api/hrm/employees/{id}/` | PUT | Update employee |
| `/api/hrm/employees/{id}/` | DELETE | Delete employee |

---

## 8. COMMON PATTERNS

### Pattern 1: Update Toolbar Configuration

```bash
# Step 1: Check current config
python backend/manage.py shell -c "from core.auth_access.backend.user_management.models import ERPMenuItem; item = ERPMenuItem.objects.get(menu_id='EMPLOYEE_RECORDS'); print(item.applicable_toolbar_config)"

# Step 2: Update config
python backend/manage.py shell -c "from core.auth_access.backend.user_management.models import ERPMenuItem; item = ERPMenuItem.objects.get(menu_id='EMPLOYEE_RECORDS'); item.applicable_toolbar_config = 'NRQFVEDIOX'; item.save(); print('Updated')"

# Step 3: Verify update
python backend/manage.py shell -c "from core.auth_access.backend.user_management.models import ERPMenuItem; item = ERPMenuItem.objects.get(menu_id='EMPLOYEE_RECORDS'); print(item.applicable_toolbar_config)"
```

### Pattern 2: Check Menu Item

```bash
python backend/manage.py shell -c "from core.auth_access.backend.user_management.models import ERPMenuItem; item = ERPMenuItem.objects.get(menu_id='EMPLOYEE_RECORDS'); print('Menu ID:', item.menu_id); print('Menu Name:', item.menu_name); print('View Type:', item.view_type); print('Toolbar Config:', item.applicable_toolbar_config)"
```

### Pattern 3: List All HRM Menu Items

```bash
python backend/manage.py shell -c "from core.auth_access.backend.user_management.models import ERPMenuItem; items = ERPMenuItem.objects.filter(module_name='HRM'); [print(f'{item.menu_id}: {item.applicable_toolbar_config}') for item in items]"
```

### Pattern 4: Verify Toolbar Compliance

```bash
python backend/manage.py shell -c "from core.auth_access.backend.user_management.models import ERPMenuItem; item = ERPMenuItem.objects.get(menu_id='EMPLOYEE_RECORDS'); required = ['N', 'R', 'Q', 'F', 'V', 'E', 'D', 'I', 'O', 'X']; missing = [c for c in required if c not in item.applicable_toolbar_config]; print('Missing:', missing if missing else 'None'); print('Status:', 'COMPLIANT' if not missing else 'NON-COMPLIANT')"
```

---

## 9. TROUBLESHOOTING

### Issue: "python: can't open file 'd:\\olivine-erp\\manage.py'"

**Cause**: Using `cd backend && python manage.py [command]`

**Solution**: Use `python backend/manage.py [command]`

**Example:**
```bash
# WRONG
cd backend && python manage.py check

# CORRECT
python backend/manage.py check
```

### Issue: "ModuleNotFoundError: No module named 'core.auth_access.backend.user_management.models'"

**Cause**: Wrong import path or Django not set up correctly

**Solution**: 
1. Use correct import path: `from core.auth_access.backend.user_management.models import ERPMenuItem`
2. Run from Django shell: `python backend/manage.py shell`
3. Or use Django settings: `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.base')`

### Issue: Can't find ERPMenuItem table

**Cause**: Looking in wrong location

**Solution**: 
- Table: `erp_menu_items`
- Model: `ERPMenuItem`
- Location: `backend/core/auth_access/backend/user_management/models.py`
- Import: `from core.auth_access.backend.user_management.models import ERPMenuItem`

### Issue: Toolbar buttons not showing

**Cause**: Toolbar config in database is incorrect

**Solution**:
1. Check config: `python backend/manage.py shell -c "from core.auth_access.backend.user_management.models import ERPMenuItem; item = ERPMenuItem.objects.get(menu_id='EMPLOYEE_RECORDS'); print(item.applicable_toolbar_config)"`
2. Update config: `python backend/manage.py shell -c "from core.auth_access.backend.user_management.models import ERPMenuItem; item = ERPMenuItem.objects.get(menu_id='EMPLOYEE_RECORDS'); item.applicable_toolbar_config = 'NRQFVEDIOX'; item.save()"`
3. Refresh browser

---

## 10. QUICK REFERENCE CHEAT SHEET

### Django Commands

```bash
# Always use this pattern
python backend/manage.py [command]

# Common commands
python backend/manage.py check
python backend/manage.py makemigrations
python backend/manage.py migrate
python backend/manage.py runserver
python backend/manage.py shell
python backend/manage.py createsuperuser
```

### Import Paths

```python
# Core models
from core.auth_access.backend.user_management.models import ERPMenuItem, Role, RolePermission, UserRole

# HRM models
from HRM.backend.hrm.models.employee import EmployeeRecord
from HRM.backend.hrm.models.department import Department
from HRM.backend.hrm.models.organizational_unit import Position

# Common models
from common.domain.models import Company
```

### File Locations

```
Django: backend/manage.py
Core Models: backend/core/auth_access/backend/user_management/models.py
HRM Models: HRM/backend/hrm/models/
HRM Admin: HRM/backend/hrm/admin.py
Toolbar: frontend/core/ui-canon/frontend/ui/components/MasterToolbarConfigDriven.tsx
```

### Database Tables

```
erp_menu_items → ERPMenuItem model
roles → Role model
role_permissions → RolePermission model
user_roles → UserRole model
hrm_employee_records → EmployeeRecord model
```

---

**END OF REGISTRY SYSTEM**

**Version**: 1.0  
**Last Updated**: January 31, 2026  
**Agent**: Hindra (HRM Domain Owner)
