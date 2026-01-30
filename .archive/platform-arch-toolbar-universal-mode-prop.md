# 🏗️ PLATFORM ARCHITECTURE: TOOLBAR SYSTEM - UNIVERSAL GUIDE

**Single Source of Truth for Toolbar Implementation**  
**Version**: 1.0  
**Date**: 2026-01-20  
**Audience**: All Agents (Agent E, Astra, Future Agents)  
**Status**: ✅ CANONICAL AUTHORITY

---

## 📋 TABLE OF CONTENTS

1. [Unified Platform Architecture](#1-unified-platform-architecture)
2. [Toolbar Philosophy & Design](#2-toolbar-philosophy--design)
3. [Database Architecture](#3-database-architecture)
4. [Character Mapping System](#4-character-mapping-system)
5. [Backend Permission Pipeline](#5-backend-permission-pipeline)
6. [Frontend Integration](#6-frontend-integration)
7. [Mode-Based Behavior](#7-mode-based-behavior)
8. [Implementation Workflow](#8-implementation-workflow)
9. [Gold Standard Examples](#9-gold-standard-examples)
10. [Troubleshooting Guide](#10-troubleshooting-guide)

---

## 1. UNIFIED PLATFORM ARCHITECTURE

### 1.1 System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    USER BROWSER (localhost:3001)                │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│              UNIFIED FRONTEND (React - Port 3001)               │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  App Shell (Layout, Sidebar, Toolbar, Navigation)        │  │
│  │  ┌─────────────┬────────────────────────────────────────┐ │  │
│  │  │  Sidebar    │  Main Content Area                     │ │  │
│  │  │             │                                        │ │  │
│  │  │  📦 Retail  │  Module-Specific Pages:               │ │  │
│  │  │  👥 HRM     │  • /retail/* → Retail Components      │ │  │
│  │  │  🤝 CRM     │  • /hrm/*    → HRM Components         │ │  │
│  │  │  💰 FMS     │  • /crm/*    → CRM Components         │ │  │
│  │  │             │  • /fms/*    → FMS Components         │ │  │
│  │  └─────────────┴────────────────────────────────────────┘ │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              ↓ API Calls (Axios)
┌─────────────────────────────────────────────────────────────────┐
│              UNIFIED BACKEND (Django - Port 8000)               │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  URL Router (erp_core/urls.py)                           │  │
│  │  • /api/auth/           → Authentication                 │  │
│  │  • /api/toolbar-*       → Toolbar Config & Permissions   │  │
│  │  • /api/retail/*        → Retail APIs                    │  │
│  │  • /api/hrm/*           → HRM APIs                       │  │
│  │  • /api/crm/*           → CRM APIs                       │  │
│  │  • /api/fms/*           → FMS APIs                       │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                 │
│  Django Apps (INSTALLED_APPS):                                 │
│  • Core.auth_access.backend.user_management (Toolbar System)  │
│  • Retail.backend.* (Retail Module)                           │
│  • HRM.backend.hrm (HRM Module)                               │
│  • CRM.backend.crm (CRM Module)                               │
│  • FMS.backend.fms (FMS Module)                               │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    DATABASE (SQLite/PostgreSQL)                 │
│  • erp_menu_items (Menu Registry + Toolbar Configs)           │
│  • roles, user_roles (Role Management)                        │
│  • role_permissions (Permission Masks)                        │
│  • auth_user (User Authentication)                            │
└─────────────────────────────────────────────────────────────────┘
```

### 1.2 Repository Structure

```
olivine-platform/
├── backend/                    # Unified Django Gateway (Port 8000)
│   ├── erp_core/              # Django project settings
│   │   ├── settings/          # Configuration
│   │   └── urls.py            # All module routes aggregated here
│   ├── manage.py
│   └── db.sqlite3             # Shared database
│
├── frontend/                   # Unified React Shell (Port 3001)
│   ├── src/
│   │   ├── components/        # Shared components
│   │   ├── hooks/             # useToolbarConfig, etc.
│   │   ├── services/          # API clients
│   │   └── App.tsx            # Main routing
│   └── vite.config.ts
│
├── Core/                       # Shared canonical services
│   ├── auth_access/           # Authentication & Toolbar System
│   │   └── backend/
│   │       └── user_management/
│   │           ├── models.py           # ERPMenuItem, Role, etc.
│   │           ├── toolbar_views.py    # Toolbar APIs
│   │           └── services/
│   │               └── toolbar_permission_service.py
│   └── ui-canon/              # Shared UI components
│       └── frontend/ui/components/
│           └── MasterToolbarConfigDriven.tsx
│
├── Retail/                     # Retail Module (Ownership: Astra)
│   ├── backend/               # Retail Django apps
│   └── frontend/              # Retail React components
│
├── HRM/                        # HRM Module (Ownership: Agent E)
│   ├── backend/               # HRM Django apps
│   └── frontend/              # HRM React components
│
├── CRM/                        # CRM Module (Ownership: Agent E)
├── FMS/                        # FMS Module (Ownership: Astra)
│
├── Steering/                   # Governance (Single Source of Truth)
│   └── 20TOOLBAR_ROLLOUT/     # Toolbar documentation
│
└── Common/
    └── qa-launcher-console/    # DevOps Center (UI: 5174, API: 3100)
```

### 1.3 Key Architectural Principles

✅ **Single Backend**: One Django project aggregates all modules  
✅ **Single Frontend**: One React app routes to all modules  
✅ **Single Database**: All data in one database  
✅ **Module Boundaries**: Each module (Retail, HRM, CRM, FMS) owns its code  
✅ **Unified Toolbar**: Backend-driven, permission-aware, mode-based

---

## 2. TOOLBAR PHILOSOPHY & DESIGN

### 2.1 Why Backend-Driven?

**OLD WAY (Hardcoded - ❌ WRONG)**:
```typescript
// ❌ NEVER DO THIS
<MasterToolbar 
  allowedActions={['new', 'edit', 'save', 'delete']} 
/>
```

**NEW WAY (Backend-Driven - ✅ CORRECT)**:
```typescript
// ✅ ALWAYS DO THIS
<MasterToolbar 
  viewId="INVENTORY_UOM_SETUP"
  mode={mode}
  onAction={handleToolbarAction}
/>
```

### 2.2 Character-Based Configuration

Instead of hardcoding button arrays, we use **character strings**:

```
Config String: NESCKVDXRQF

N = New (F2)
E = Edit (F3)
S = Save (F8)
C = Cancel (ESC)
K = Clear (F5)
V = View (F7)
D = Delete (F4)
X = Exit (ESC)
R = Refresh (F9)
Q = Search (Ctrl+F)
F = Filter (Alt+F)
```

**Benefits**:
- ✅ Compact (11 characters vs 11-element array)
- ✅ Database-friendly (single string field)
- ✅ Easy to compare/audit
- ✅ Permission masking (binary 1s/0s)

### 2.3 Permission Resolution Formula

```
Final Toolbar = Screen Capability ∩ User Permission ∩ Mode Law
```

**Example**:
```
Screen String:  NESCKVDXRQF     (What the screen CAN do)
User Mask:      11111111111     (What the user CAN do - admin)
After Filter:   NESCKVDXRQF     (Intersection)
Mode Law (VIEW): Exclude S,C,K  (What the mode ALLOWS)
Final Actions:  NEVDXRQF        (What actually shows)
```

---

## 3. DATABASE ARCHITECTURE

### 3.1 Core Models

#### **ERPMenuItem** (Menu Registry)
```python
# Location: Core/auth_access/backend/user_management/models.py

class ERPMenuItem(models.Model):
    # Identification
    menu_id = CharField(max_length=100, unique=True)  # e.g., "INVENTORY_UOM_SETUP"
    menu_name = CharField(max_length=200)             # e.g., "UOM Setup"
    parent_menu = ForeignKey('self', null=True)
    
    # Module & Type
    module_name = CharField(choices=[...])            # RETAIL, HRM, CRM, FMS
    submodule = CharField(max_length=50)              # INVENTORY, SALES, etc.
    view_type = CharField(choices=[...])              # MASTER, TRANSACTION, REPORT
    
    # Toolbar Configuration
    applicable_toolbar_config = CharField(max_length=100)  # "NESCKVDXRQF"
    
    # Metadata
    route_path = CharField(max_length=200)            # "/inventory/uoms"
    component_name = CharField(max_length=100)
    is_active = BooleanField(default=True)
```

**Example Record**:
```python
{
    "menu_id": "INVENTORY_UOM_SETUP",
    "menu_name": "UOM Setup",
    "module_name": "RETAIL",
    "submodule": "INVENTORY",
    "view_type": "MASTER",
    "applicable_toolbar_config": "NESCKVDXRQF",
    "route_path": "/inventory/uoms"
}
```

#### **Role** (Role Definitions)
```python
class Role(models.Model):
    role_key = CharField(max_length=50, unique=True)   # "admin", "backofficemanager"
    role_name = CharField(max_length=100)              # "Administrator"
    is_system_role = BooleanField(default=False)
    is_active = BooleanField(default=True)
```

#### **RolePermission** (Permission Matrix)
```python
class RolePermission(models.Model):
    role = ForeignKey(Role)
    menu_item = ForeignKey(ERPMenuItem)
    
    # Permission Mask (Binary String)
    toolbar_string = CharField(max_length=100)         # "NESCKVDXRQF" (from menu)
    toolbar_permissions = CharField(max_length=100)    # "11111111111" (1=allow, 0=deny)
```

**Example**:
```python
{
    "role": "backofficeuser",
    "menu_item": "INVENTORY_UOM_SETUP",
    "toolbar_string": "NESCKVDXRQF",
    "toolbar_permissions": "11001111011"  # Deny S, C (Save, Cancel)
}
```

#### **UserRole** (User-Role Mapping)
```python
class UserRole(models.Model):
    user = ForeignKey(User)
    role = ForeignKey(Role)
    is_active = BooleanField(default=True)
```

### 3.2 Database Relationships

```
User (auth_user)
  ↓ (1:N)
UserRole
  ↓ (N:1)
Role
  ↓ (1:N)
RolePermission
  ↓ (N:1)
ERPMenuItem
```

---

## 4. CHARACTER MAPPING SYSTEM

### 4.1 Complete Character Map

```python
# Location: Core/auth_access/backend/user_management/services/toolbar_permission_service.py

TOOLBAR_CHAR_MAP = {
    # Group 1: CRUD Operations
    'N': 'new',        # F2
    'E': 'edit',       # F3
    'S': 'save',       # F8
    'C': 'cancel',     # ESC
    'K': 'clear',      # F5
    
    # Group 2: View & Navigation
    'V': 'view',       # F7
    '1': 'first',      # Home
    '2': 'previous',   # PgUp
    '3': 'next',       # PgDn
    '4': 'last',       # End
    
    # Group 3: Data Operations
    'D': 'delete',     # F4
    'R': 'refresh',    # F9
    'Q': 'search',     # Ctrl+F
    'F': 'filter',     # Alt+F
    
    # Group 4: Workflow (Transactions)
    'Z': 'authorize',  # F10
    'T': 'submit',     # Alt+S
    'J': 'reject',     # Alt+R
    'A': 'amend',      # Alt+A
    
    # Group 5: Output
    'P': 'print',      # Ctrl+P
    'M': 'email',      # Ctrl+E
    
    # Group 6: Import/Export
    'I': 'import',     # Ctrl+I
    'O': 'export',     # Ctrl+O
    'L': 'clone',      # Ctrl+Shift+C
    
    # Group 7: Tools
    'B': 'notes',      # Alt+N
    'G': 'attach',     # Alt+U
    'Y': 'settings',   # Alt+O
    '?': 'help',       # F1
    
    # Group 8: Status
    'H': 'hold',       # Alt+H
    'W': 'void',       # Alt+V
    
    # Group 9: Exit
    'X': 'exit',       # ESC
}
```

### 4.2 Standard Toolbar Configurations

```
MASTER (Simple):        NESCKVDXRQF          (11 chars)
MASTER (Advanced):      NESCKVDXRQFIO        (13 chars)
TRANSACTION (Standard): NESCKZTJAVPMRDX1234QF (21 chars)
REPORT:                 RPQFX                (5 chars)
DASHBOARD:              RQF                  (3 chars)
CONFIGURATION:          NESCKXR              (7 chars)
```

---

## 5. BACKEND PERMISSION PIPELINE

### 5.1 API Endpoint

```
GET /api/toolbar-permissions/?menu_id=<MENU_ID>&mode=<MODE>
```

**Parameters**:
- `menu_id`: Menu identifier (e.g., `INVENTORY_UOM_SETUP`)
- `mode`: UI mode (`VIEW`, `NEW`, `EDIT`, `VIEW_FORM`)

**Response**:
```json
{
  "menu_id": "INVENTORY_UOM_SETUP",
  "mode": "VIEW",
  "toolbar_string": "NESCKVDXRQF",
  "permission_mask": "11111111111",
  "allowed_characters": ["N", "E", "V", "D", "X", "R", "Q", "F"],
  "allowed_actions": ["new", "edit", "view", "delete", "exit", "refresh", "search", "filter"]
}
```

### 5.2 Five-Step Resolution Pipeline

```python
# Location: Core/auth_access/backend/user_management/services/toolbar_permission_service.py

def resolve_toolbar_permissions(user_id, menu_id, mode):
    """
    5-Step Resolution Pipeline (PLATFORM LAW)
    
    Toolbar = ScreenCapability ∩ UserPermission ∩ ModeLaw
    """
    
    # STEP 1: Get screen toolbar string
    menu_item = ERPMenuItem.objects.get(menu_id=menu_id)
    toolbar_string = menu_item.applicable_toolbar_config  # "NESCKVDXRQF"
    
    # STEP 2: Get user permission mask
    user = User.objects.get(id=user_id)
    if user.is_superuser or user.username == 'admin':
        permission_mask = '1' * len(toolbar_string)  # "11111111111"
    else:
        # Get from RolePermission
        user_role = UserRole.objects.filter(user=user, is_active=True).first()
        role_perm = RolePermission.objects.filter(
            role=user_role.role,
            menu_item=menu_item
        ).first()
        permission_mask = role_perm.toolbar_permissions if role_perm else '0' * len(toolbar_string)
    
    # STEP 3: Apply permission filter (bitwise AND)
    allowed_chars = []
    for i, char in enumerate(toolbar_string):
        if permission_mask[i] == '1':
            allowed_chars.append(char)
    
    # STEP 4: Apply mode law
    MODE_LAW = {
        'VIEW': {'exclude': ['S', 'C', 'K']},  # No Save, Cancel, Clear in list view
        'NEW': {'exclude': ['N', 'E', 'V', 'D', 'R', 'Q', 'F', 'I', 'O', '1', '2', '3', '4']},
        'EDIT': {'exclude': ['N', 'E', 'V', 'D', 'R', 'Q', 'F', 'I', 'O', '1', '2', '3', '4']},
    }
    
    if mode in MODE_LAW:
        exclude_list = MODE_LAW[mode]['exclude']
        allowed_chars = [c for c in allowed_chars if c not in exclude_list]
    
    # STEP 5: Convert to action names
    allowed_actions = [TOOLBAR_CHAR_MAP.get(c, c.lower()) for c in allowed_chars]
    
    return {
        'menu_id': menu_id,
        'mode': mode,
        'toolbar_string': toolbar_string,
        'permission_mask': permission_mask,
        'allowed_characters': allowed_chars,
        'allowed_actions': allowed_actions
    }
```

### 5.3 Mode Law (Exclusion Rules)

```python
MODE_LAW = {
    'VIEW': {
        'exclude': ['S', 'C', 'K'],  # Never show Save, Cancel, Clear in List/View mode
    },
    'NEW': {
        'exclude': ['N', 'E', 'V', 'D', 'R', 'Q', 'F', 'I', 'O', '1', '2', '3', '4'],
        # Only show: S, C, K, X (Save, Cancel, Clear, Exit)
    },
    'EDIT': {
        'exclude': ['N', 'E', 'V', 'D', 'R', 'Q', 'F', 'I', 'O', '1', '2', '3', '4'],
        # Only show: S, C, K, X (Save, Cancel, Clear, Exit)
    },
    'VIEW_FORM': {
        'exclude': ['N', 'V', 'D', 'S', 'C', 'K', 'R', 'Q', 'F', 'I', 'O', '1', '2', '3', '4'],
        # Only show: E, X (Edit, Exit) - Read-only record view
    }
}
```

---

## 6. FRONTEND INTEGRATION

### 6.1 Hook: `useToolbarConfig`

```typescript
// Location: HRM/frontend/src/hooks/useToolbarConfig.ts (or Core/ui-canon)

export const useToolbarConfig = (viewId: string, mode: string = 'VIEW') => {
  const [config, setConfig] = useState<ToolbarConfigResponse | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchToolbarConfig = async () => {
      try {
        setLoading(true);
        
        // API call to backend
        const response = await fetch(
          `http://localhost:8000/api/toolbar-permissions/?menu_id=${viewId}&mode=${mode}`,
          {
            headers: {
              'Authorization': `Token ${getAuthToken()}`,
            }
          }
        );

        const data = await response.json();
        
        // Convert to permissions object
        setConfig({
          permissions: convertActionsToPermissions(data.allowed_actions),
          config: data.toolbar_string,
        });
      } catch (error) {
        console.error('Failed to fetch toolbar config:', error);
        setConfig(null);
      } finally {
        setLoading(false);
      }
    };

    fetchToolbarConfig();
  }, [viewId, mode]);

  return { config, loading };
};
```

### 6.2 Component: `MasterToolbar`

```typescript
// Location: Core/ui-canon/frontend/ui/components/MasterToolbarConfigDriven.tsx

export type MasterMode = "VIEW" | "EDIT" | "CREATE";

interface MasterToolbarProps {
  viewId: string;           // Must match ERPMenuItem.menu_id
  mode: MasterMode;         // Current UI mode
  onAction: (action: string) => void;
  hasSelection?: boolean;
  showLabels?: boolean;
}

export const MasterToolbar: React.FC<MasterToolbarProps> = ({
  viewId,
  mode,
  onAction,
  hasSelection = false,
  showLabels = false
}) => {
  const { config, loading } = useToolbarConfig(viewId, mode);

  const isActionDisabled = useCallback((action: ActionButton): boolean => {
    if (!config) return action.id !== 'exit';
    
    // Check permission from config
    if (!config.permissions[action.permissionKey]) {
      return true;
    }

    // Mode-based logic (already filtered by backend, but double-check)
    switch (mode) {
      case 'VIEW':
        return !['new', 'edit', 'view', 'delete', 'refresh', 'search', 'filter', 'exit', ...].includes(action.id);
      case 'EDIT':
      case 'CREATE':
        return !['save', 'cancel', 'clear', 'exit'].includes(action.id);
      default:
        return false;
    }
  }, [mode, config]);

  // Render toolbar buttons
  return (
    <div className="toolbar">
      {ACTIONS.map((action) => {
        const disabled = isActionDisabled(action);
        return (
          <button
            key={action.id}
            onClick={() => onAction(action.id)}
            disabled={disabled}
            title={`${action.label} (${action.shortcutLabel})`}
          >
            <action.icon />
            {showLabels && <span>{action.label}</span>}
          </button>
        );
      })}
    </div>
  );
};
```

---

## 7. MODE-BASED BEHAVIOR

### 7.1 Mode State Machine

```
┌──────────┐
│   VIEW   │ ← Initial state (List view)
│ (List)   │
└──────────┘
     │
     ├─── New (F2) ────────────┐
     │                         ↓
     │                    ┌──────────┐
     │                    │  CREATE  │
     │                    │ (Form)   │
     │                    └──────────┘
     │                         │
     │                         │ Save (F8)
     │                         ↓
     │                    ┌──────────┐
     │                    │   VIEW   │
     │                    └──────────┘
     │
     ├─── Edit (F3) ───────────┐
     │                         ↓
     │                    ┌──────────┐
     │                    │   EDIT   │
     │                    │ (Form)   │
     │                    └──────────┘
     │                         │
     │                         │ Save (F8)
     │                         ↓
     │                    ┌──────────┐
     │                    │   VIEW   │
     │                    └──────────┘
     │
     └─── View (F7) ───────────┐
                               ↓
                          ┌──────────┐
                          │VIEW_FORM │
                          │(Read-Only)
                          └──────────┘
                               │
                               │ Edit (F3)
                               ↓
                          ┌──────────┐
                          │   EDIT   │
                          └──────────┘
```

### 7.2 Mode Definitions

| Mode | Description | Visible Buttons | Use Case |
|------|-------------|----------------|----------|
| **VIEW** | List view | N, E, V, D, R, Q, F, X | Browsing records |
| **CREATE** | Form create | S, C, K, X | Adding new record |
| **EDIT** | Form edit | S, C, K, X | Modifying existing record |
| **VIEW_FORM** | Read-only form | E, X | Viewing single record details |

### 7.3 Mode Transition Examples

**Example 1: Create New Record**
```typescript
const [mode, setMode] = useState<MasterMode>('VIEW');
const [showForm, setShowForm] = useState(false);

const handleToolbarAction = (action: string) => {
  switch (action) {
    case 'new':
      setMode('CREATE');
      setShowForm(true);
      setEditingId(null);
      break;
    case 'save':
      // Save logic
      formRef.current?.submit();
      break;
    case 'cancel':
      setMode('VIEW');
      setShowForm(false);
      break;
  }
};
```

**Example 2: Edit Existing Record**
```typescript
const handleToolbarAction = (action: string) => {
  switch (action) {
    case 'edit':
      if (selectedId) {
        setMode('EDIT');
        setShowForm(true);
        setEditingId(selectedId);
      }
      break;
    case 'save':
      // Save logic
      await updateRecord(editingId, formData);
      setMode('VIEW');
      setShowForm(false);
      break;
  }
};
```

---

## 8. IMPLEMENTATION WORKFLOW

### 8.1 Backend Setup (Django Admin)

**Step 1: Create ERPMenuItem Entry**

Navigate to: `http://localhost:8000/admin/user_management/erpmenuitem/`

**Click "Add ERP Menu Item"** and fill:

```
Menu ID:                    HRM_EMPLOYEE_RECORDS
Menu Name:                  Employee Records
Module Name:                HRM
Submodule:                  EMPLOYEE_MANAGEMENT
View Type:                  MASTER
Applicable Toolbar Config:  NESCKVDXRQF
Route Path:                 /hrm/employees
Component Name:             EmployeeRecords
Is Active:                  ✓
```

**Step 2: Verify Entry**

Search for `HRM_EMPLOYEE_RECORDS` in Django Admin and confirm all fields match.

### 8.2 Frontend Integration (React)

**Step 1: Import Components**

```typescript
// Location: HRM/frontend/src/pages/EmployeeRecords.tsx

import { MasterToolbar, MasterMode } from "@core/ui-canon/frontend/ui/components/MasterToolbarConfigDriven";
import { useToolbarConfig } from "@hooks/useToolbarConfig";
```

**Step 2: Setup State Management**

```typescript
export const EmployeeRecords: React.FC = () => {
  const [mode, setMode] = useState<MasterMode>('VIEW');
  const [showForm, setShowForm] = useState(false);
  const [editingId, setEditingId] = useState<string | null>(null);
  const [selectedId, setSelectedId] = useState<string | null>(null);
  
  const getToolbarMode = (): MasterMode => {
    if (!showForm) return 'VIEW';
    return editingId ? 'EDIT' : 'CREATE';
  };
  
  // ... rest of component
};
```

**Step 3: Add Toolbar Component**

```typescript
return (
  <div className="flex flex-col h-full">
    <MasterToolbar
      viewId="HRM_EMPLOYEE_RECORDS"  {/* Must match backend menu_id */}
      mode={getToolbarMode()}
      onAction={handleToolbarAction}
      hasSelection={!!selectedId}
      showLabels={false}
    />
    
    {/* Rest of UI */}
  </div>
);
```

**Step 4: Implement Toolbar Handlers**

```typescript
const handleToolbarAction = (action: string) => {
  switch (action) {
    case 'new':
      setEditingId(null);
      setMode('CREATE');
      setShowForm(true);
      break;
      
    case 'edit':
      if (selectedId) {
        setEditingId(selectedId);
        setMode('EDIT');
        setShowForm(true);
      }
      break;
      
    case 'save':
      if (showForm) {
        formRef.current?.submit();
      }
      break;
      
    case 'cancel':
      setShowForm(false);
      setMode('VIEW');
      setEditingId(null);
      break;
      
    case 'clear':
      formRef.current?.reset();
      break;
      
    case 'delete':
      if (selectedId) {
        handleDelete(selectedId);
      }
      break;
      
    case 'view':
      if (selectedId && !showForm) {
        setEditingId(selectedId);
        setMode('VIEW_FORM');
        setShowForm(true);
      }
      break;
      
    case 'refresh':
      loadRecords();
      break;
      
    case 'search':
      document.querySelector<HTMLInputElement>('input[type="text"]')?.focus();
      break;
      
    case 'filter':
      setShowFilterPanel(!showFilterPanel);
      break;
      
    case 'exit':
      navigate('/dashboard');
      break;
      
    default:
      console.warn(`Unhandled action: ${action}`);
  }
};
```

**Step 5: Wire Form Submit**

```typescript
const formRef = React.useRef<FormHandle>(null);

const handleFormSuccess = () => {
  setShowForm(false);
  setMode('VIEW');
  setEditingId(null);
  loadRecords();
};

// In JSX:
{showForm && (
  <EmployeeForm
    ref={formRef}
    employeeId={editingId}
    readOnly={mode === 'VIEW_FORM'}
    onSuccess={handleFormSuccess}
    onCancel={() => setShowForm(false)}
  />
)}
```

### 8.3 Implementation Checklist

- [ ] **Backend**: ERPMenuItem entry created in Django Admin
- [ ] **Backend**: `menu_id` set correctly (e.g., `HRM_EMPLOYEE_RECORDS`)
- [ ] **Backend**: `applicable_toolbar_config` set (e.g., `NESCKVDXRQF`)
- [ ] **Backend**: `view_type` set correctly (MASTER/TRANSACTION/REPORT)
- [ ] **Frontend**: `MasterToolbar` component imported
- [ ] **Frontend**: `viewId` prop matches backend `menu_id` exactly
- [ ] **Frontend**: Mode state management implemented
- [ ] **Frontend**: All toolbar actions have handlers
- [ ] **Frontend**: Form ref wired for save/clear actions
- [ ] **Frontend**: Navigation handlers implemented (exit, etc.)
- [ ] **Testing**: Tested in VIEW mode
- [ ] **Testing**: Tested in CREATE mode
- [ ] **Testing**: Tested in EDIT mode
- [ ] **Testing**: Keyboard shortcuts work (F2, F3, F8, etc.)

---

## 9. GOLD STANDARD EXAMPLES

### 9.1 UOM Setup (Simple Master)

**File**: `Retail/frontend/inventory/pages/UOMSetup.tsx`

**Backend Configuration**:
```json
{
  "menu_id": "INVENTORY_UOM_SETUP",
  "view_type": "MASTER",
  "applicable_toolbar_config": "NESCKVDXRQF"
}
```

**Frontend Implementation**:
```typescript
export const UOMSetup: React.FC = () => {
  const [mode, setMode] = useState<MasterMode>('VIEW');
  const [showForm, setShowForm] = useState(false);
  const [editingId, setEditingId] = useState<string | null>(null);
  const [selectedUOMId, setSelectedUOMId] = useState<string | null>(null);
  
  const getToolbarMode = (): MasterMode => {
    if (!showForm) return 'VIEW';
    return editingId ? 'EDIT' : 'CREATE';
  };

  return (
    <div className="flex flex-col h-full">
      <MasterToolbar
        viewId="INVENTORY_UOM_SETUP"
        mode={getToolbarMode()}
        onAction={handleToolbarAction}
        hasSelection={!!selectedUOMId}
      />
      
      {/* Fixed Header & Filters */}
      <div className="px-4 pt-4 pb-0">
        <h1>Units of Measure</h1>
        {!showForm && <FilterPanel />}
      </div>
      
      {/* Scrollable Content */}
      <div className="flex-1 overflow-y-auto">
        {showForm ? (
          <UOMForm
            uomId={editingId}
            onSuccess={handleFormSuccess}
            onCancel={() => setShowForm(false)}
          />
        ) : (
          <UOMTable
            uoms={uoms}
            selectedId={selectedUOMId}
            onSelect={setSelectedUOMId}
          />
        )}
      </div>
    </div>
  );
};
```

**Key Features**:
- ✅ In-place list ↔ form swap (no modals)
- ✅ Decoupled scrolling (header fixed, content scrolls)
- ✅ Selection-first architecture
- ✅ Clean mode transitions

### 9.2 Purchase Orders (Transaction)

**File**: `Retail/frontend/procurement/pages/PurchaseOrderListPage.tsx`

**Backend Configuration**:
```json
{
  "menu_id": "PURCHASE_ORDERS",
  "view_type": "TRANSACTION",
  "applicable_toolbar_config": "NESCKZTJAVPMRDX1234QF"
}
```

**Frontend Implementation**:
```typescript
export const PurchaseOrderListPage: React.FC = () => {
  const [mode, setMode] = useState<MasterMode>('VIEW');
  
  return (
    <div className="flex flex-col h-full">
      <MasterToolbar
        viewId="PURCHASE_ORDERS"
        mode={mode}
        onAction={handleToolbarAction}
        hasSelection={selectedIds.length > 0}
        showLabels={false}
      />
      
      {/* PO List/Form */}
    </div>
  );
};
```

**Key Features**:
- ✅ Workflow actions (Submit, Authorize, Reject)
- ✅ Document navigation (First, Prev, Next, Last)
- ✅ Status-based button enabling
- ✅ Print/Email functionality

---

## 10. TROUBLESHOOTING GUIDE

### 10.1 Common Issues

#### **Issue 1: Toolbar Not Loading**

**Symptom**: Toolbar shows "Loading toolbar..." indefinitely

**Diagnosis**:
```typescript
// Check browser console
// Expected: GET /api/toolbar-permissions/?menu_id=X&mode=VIEW → 200 OK
// Actual: 404 Not Found or 500 Error
```

**Solutions**:
1. ✅ Verify `menu_id` in backend matches `viewId` in frontend (case-sensitive!)
2. ✅ Check ERPMenuItem exists in Django Admin
3. ✅ Verify `is_active=True` in database
4. ✅ Check authentication token is valid

#### **Issue 2: Wrong Buttons Showing**

**Symptom**: Buttons don't match expected toolbar config

**Diagnosis**:
```python
# Django Admin: Search for menu_id
# Check: applicable_toolbar_config field
```

**Solutions**:
1. ✅ Verify `applicable_toolbar_config` in database
2. ✅ Check mode is correct (VIEW vs CREATE vs EDIT)
3. ✅ Verify permission mask for user role

#### **Issue 3: Mode Transitions Broken**

**Symptom**: Clicking "Edit" doesn't switch to edit mode

**Diagnosis**:
```typescript
// Check mode state management
console.log('Current mode:', mode);
console.log('Show form:', showForm);
```

**Solutions**:
1. ✅ Verify `setMode()` is called in handler
2. ✅ Check `getToolbarMode()` logic
3. ✅ Ensure `showForm` state is updated

#### **Issue 4: Save Button Not Working**

**Symptom**: Clicking "Save" does nothing

**Diagnosis**:
```typescript
// Check if formRef is wired
console.log('Form ref:', formRef.current);
```

**Solutions**:
1. ✅ Verify `formRef` is created: `const formRef = React.useRef<FormHandle>(null);`
2. ✅ Check form component has `ref` prop: `<Form ref={formRef} />`
3. ✅ Ensure form exposes `submit()` method via `useImperativeHandle`

### 10.2 Debugging Checklist

**Backend Verification**:
```bash
# 1. Check menu item exists
python manage.py shell
>>> from Core.auth_access.backend.user_management.models import ERPMenuItem
>>> ERPMenuItem.objects.filter(menu_id='HRM_EMPLOYEE_RECORDS').values()

# 2. Test API directly
curl -H "Authorization: Token YOUR_TOKEN" \
  "http://localhost:8000/api/toolbar-permissions/?menu_id=HRM_EMPLOYEE_RECORDS&mode=VIEW"
```

**Frontend Verification**:
```typescript
// 1. Check hook response
const { config, loading } = useToolbarConfig('HRM_EMPLOYEE_RECORDS', 'VIEW');
console.log('Config:', config);
console.log('Loading:', loading);

// 2. Check permissions
console.log('Permissions:', config?.permissions);

// 3. Verify mode
console.log('Current mode:', mode);
```

### 10.3 Quick Reference

| Problem | Check | Fix |
|---------|-------|-----|
| No toolbar | `menu_id` mismatch | Match frontend `viewId` to backend `menu_id` |
| Wrong buttons | `applicable_toolbar_config` | Update in Django Admin |
| Mode stuck | State management | Verify `setMode()` calls |
| Save not working | Form ref | Wire `formRef` and `submit()` |
| Permissions wrong | User role | Check `RolePermission` table |

### 10.4 Phase 2: Advanced Permission System (Future Roadmap)

**Current State (Phase 1)**:
- ✅ Admin user (`admin/admin123`) has full access (all 1s in permission mask)
- ✅ All toolbar actions available to admin
- ✅ Backend-driven permission resolution pipeline operational
- ✅ Mode law filtering working

**Phase 2 Enhancements (Planned)**:

#### **10.4.1 Role-Based Permission Masks**

**Concept**: Each role gets a custom permission mask for each menu item.

**Example Configuration**:
```python
# Django Admin: Role Permissions

# Role: Back Office Manager
# Menu: INVENTORY_UOM_SETUP
# Toolbar String: NESCKVDXRQF
# Permission Mask: 11111111111  (Full access)

# Role: Back Office User
# Menu: INVENTORY_UOM_SETUP
# Toolbar String: NESCKVDXRQF
# Permission Mask: 11001111011  (No Save, No Refresh)
#                  NE__KVD_RQF  (Can't save or refresh)

# Role: Warehouse Staff
# Menu: INVENTORY_UOM_SETUP
# Toolbar String: NESCKVDXRQF
# Permission Mask: 01000000010  (View and Search only)
#                  _E______Q_  (Read-only access)
```

**Implementation**:
```python
# In toolbar_permission_service.py

def get_user_permission_mask(user, menu_item, toolbar_string):
    """
    Get permission mask based on user's role(s)
    """
    # Admin bypass
    if user.is_superuser or user.username == 'admin':
        return '1' * len(toolbar_string)
    
    # Get active roles for user
    user_roles = UserRole.objects.filter(
        user=user,
        is_active=True
    ).select_related('role')
    
    if not user_roles.exists():
        return '0' * len(toolbar_string)  # No access
    
    # Aggregate permissions from all roles (OR operation)
    final_mask = ['0'] * len(toolbar_string)
    
    for user_role in user_roles:
        role_perm = RolePermission.objects.filter(
            role=user_role.role,
            menu_item=menu_item
        ).first()
        
        if role_perm and role_perm.toolbar_permissions:
            for i, char in enumerate(role_perm.toolbar_permissions):
                if char == '1':
                    final_mask[i] = '1'  # OR: If any role allows, allow
    
    return ''.join(final_mask)
```

#### **10.4.2 User-Specific Overrides**

**Concept**: Individual users can have custom permissions that override role permissions.

**Use Cases**:
- Temporary elevated access for specific users
- Restricted access for specific users within a role
- Training mode (limited actions)

**Example**:
```python
# User: john.doe (Role: Back Office User)
# Override: Grant Delete permission temporarily

UserPermission.objects.create(
    user=john_doe,
    menu_item=uom_setup,
    toolbar_override="NESCKVDXRQF",  # Full string
    override_enabled=True
)
```

**Resolution Priority**:
```
1. User-Specific Override (if override_enabled=True)
2. Role-Based Permission (aggregated from all roles)
3. Default (no access)
```

**Implementation**:
```python
def get_user_permission_mask(user, menu_item, toolbar_string):
    # Check for user-specific override first
    user_perm = UserPermission.objects.filter(
        user=user,
        menu_item=menu_item,
        override_enabled=True
    ).first()
    
    if user_perm and user_perm.toolbar_override:
        # Convert override string to permission mask
        return convert_string_to_mask(user_perm.toolbar_override, toolbar_string)
    
    # Fall back to role-based permissions
    return get_role_based_mask(user, menu_item, toolbar_string)
```

#### **10.4.3 Company-Scoped Permissions**

**Concept**: Permissions can vary by company in multi-tenant scenarios.

**Example**:
```python
# Company A: Full UOM management
# Company B: Read-only UOM access

class CompanyRolePermission(models.Model):
    company = ForeignKey(Company)
    role = ForeignKey(Role)
    menu_item = ForeignKey(ERPMenuItem)
    toolbar_permissions = CharField(max_length=100)
```

**Resolution Flow**:
```
1. Check CompanyRolePermission (company + role + menu)
2. Fall back to RolePermission (role + menu)
3. Fall back to default
```

#### **10.4.4 License-Controlled Features**

**Concept**: Toolbar actions can be disabled based on license tier.

**Example**:
```python
# License Tier: Basic
# Disabled: Import, Export, Email

class LicenseFeatureControl(models.Model):
    license_tier = CharField(choices=[
        ('BASIC', 'Basic'),
        ('PROFESSIONAL', 'Professional'),
        ('ENTERPRISE', 'Enterprise')
    ])
    disabled_actions = CharField(max_length=100)  # "IOMe" (Import, Export, Email)
```

**Implementation**:
```python
def apply_license_restrictions(allowed_chars, user_company):
    """
    Remove actions not allowed by license tier
    """
    license = user_company.license
    
    if license.tier == 'BASIC':
        # Remove Import, Export, Email
        restricted = ['I', 'O', 'M']
        allowed_chars = [c for c in allowed_chars if c not in restricted]
    
    elif license.tier == 'PROFESSIONAL':
        # Remove only advanced workflow
        restricted = ['Z', 'A']  # Authorize, Amend
        allowed_chars = [c for c in allowed_chars if c not in restricted]
    
    # ENTERPRISE: No restrictions
    
    return allowed_chars
```

#### **10.4.5 Dynamic Permission UI (Django Admin)**

**Concept**: Visual permission matrix in Django Admin.

**Mockup**:
```
┌──────────────────────────────────────────────────────────────┐
│ Role Permission Matrix: Back Office User                     │
├──────────────────────────────────────────────────────────────┤
│ Menu Item: UOM Setup                                         │
│ Toolbar Config: NESCKVDXRQF                                  │
│                                                              │
│ ┌────┬─────┬──────┬────────┬───────┬──────┬────────┬──────┐ │
│ │ N  │ E   │ S    │ C      │ K     │ V    │ D      │ X    │ │
│ │New │Edit │Save  │Cancel  │Clear  │View  │Delete  │Exit  │ │
│ ├────┼─────┼──────┼────────┼───────┼──────┼────────┼──────┤ │
│ │ ☑  │ ☑   │ ☐    │ ☐      │ ☑     │ ☑    │ ☐      │ ☑    │ │
│ └────┴─────┴──────┴────────┴───────┴──────┴────────┴──────┘ │
│                                                              │
│ Permission String: 11001101                                  │
│ Effective Actions: New, Edit, Clear, View, Exit             │
│                                                              │
│ [Save] [Cancel]                                              │
└──────────────────────────────────────────────────────────────┘
```

**Django Admin Customization**:
```python
# admin.py

class RolePermissionAdmin(admin.ModelAdmin):
    list_display = ['role', 'menu_item', 'permission_preview']
    
    def permission_preview(self, obj):
        if not obj.toolbar_permissions:
            return "Not Set"
        
        allowed = []
        for i, char in enumerate(obj.toolbar_string):
            if obj.toolbar_permissions[i] == '1':
                action = TOOLBAR_CHAR_MAP.get(char, char)
                allowed.append(action)
        
        return ", ".join(allowed)
    
    permission_preview.short_description = "Allowed Actions"
```

#### **10.4.6 Migration Strategy (Phase 1 → Phase 2)**

**Step 1: Create Default Roles**
```python
# management/commands/create_default_roles.py

def create_default_roles():
    roles = [
        {'key': 'admin', 'name': 'Administrator', 'is_system': True},
        {'key': 'backofficemanager', 'name': 'Back Office Manager'},
        {'key': 'backofficeuser', 'name': 'Back Office User'},
        {'key': 'warehousemanager', 'name': 'Warehouse Manager'},
        {'key': 'warehousestaff', 'name': 'Warehouse Staff'},
    ]
    
    for role_data in roles:
        Role.objects.get_or_create(
            role_key=role_data['key'],
            defaults={
                'role_name': role_data['name'],
                'is_system_role': role_data.get('is_system', False)
            }
        )
```

**Step 2: Populate Role Permissions**
```python
# management/commands/populate_role_permissions.py

def populate_role_permissions():
    # Get all menu items
    menu_items = ERPMenuItem.objects.filter(is_active=True)
    
    # Get all roles
    roles = Role.objects.filter(is_active=True)
    
    for menu_item in menu_items:
        toolbar_string = menu_item.applicable_toolbar_config
        
        for role in roles:
            # Default: Full access for admin, restricted for others
            if role.role_key == 'admin':
                permission_mask = '1' * len(toolbar_string)
            else:
                permission_mask = get_default_mask_for_role(
                    role.role_key,
                    menu_item.view_type,
                    toolbar_string
                )
            
            RolePermission.objects.get_or_create(
                role=role,
                menu_item=menu_item,
                defaults={
                    'toolbar_string': toolbar_string,
                    'toolbar_permissions': permission_mask
                }
            )
```

**Step 3: Assign Users to Roles**
```python
# Assign existing users to appropriate roles

admin_role = Role.objects.get(role_key='admin')
admin_users = User.objects.filter(is_superuser=True)

for user in admin_users:
    UserRole.objects.get_or_create(
        user=user,
        role=admin_role,
        defaults={'is_active': True}
    )
```

**Step 4: Test Permission Resolution**
```python
# Test that permissions work correctly

def test_permission_resolution():
    user = User.objects.get(username='testuser')
    menu_item = ERPMenuItem.objects.get(menu_id='INVENTORY_UOM_SETUP')
    
    result = resolve_toolbar_permissions(user.id, menu_item.menu_id, 'VIEW')
    
    print(f"Allowed Actions: {result['allowed_actions']}")
    # Expected: Based on user's role permissions
```

#### **10.4.7 Backward Compatibility**

**Principle**: Phase 2 must not break Phase 1 implementations.

**Strategy**:
- ✅ Keep admin bypass logic (admin always gets full access)
- ✅ Default to full permissions if no role permissions defined
- ✅ Graceful fallback if permission mask is missing
- ✅ Frontend remains unchanged (still calls same API)

**Fallback Logic**:
```python
def get_user_permission_mask(user, menu_item, toolbar_string):
    # Phase 1 compatibility: Admin bypass
    if user.is_superuser or user.username == 'admin':
        return '1' * len(toolbar_string)
    
    # Phase 2: Try to get role-based permissions
    try:
        return get_role_based_mask(user, menu_item, toolbar_string)
    except Exception as e:
        logger.warning(f"Permission resolution failed: {e}")
        # Fallback: Full access (safe default for Phase 1 compatibility)
        return '1' * len(toolbar_string)
```

#### **10.4.8 Testing Checklist for Phase 2**

- [ ] **Admin retains full access** (backward compatibility)
- [ ] **Role-based permissions work** (new feature)
- [ ] **User overrides work** (new feature)
- [ ] **Permission aggregation works** (user with multiple roles)
- [ ] **License restrictions work** (if applicable)
- [ ] **Django Admin UI shows permissions correctly**
- [ ] **Frontend remains unchanged** (API contract maintained)
- [ ] **Performance acceptable** (permission resolution < 100ms)

---

## 11. VISUAL DIAGRAMS & FLOW CHARTS

### 11.1 Complete System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     DJANGO BACKEND (Database)                    │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ ERPMenuItem Model                                        │   │
│  │                                                           │   │
│  │  menu_id: "HRM_EMPLOYEE_RECORDS"                        │   │
│  │  menu_name: "Employee Records"                          │   │
│  │  view_type: "MASTER"                                    │   │
│  │  applicable_toolbar_config: "NESCKVDXRQF"              │   │
│  │  module_name: "HRM"                                     │   │
│  │  is_active: True                                        │   │
│  └─────────────────────────────────────────────────────────┘   │
│                              │                                    │
│                              │ API Call                           │
│                              ▼                                    │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ toolbar_permission_service.py                           │   │
│  │                                                           │   │
│  │  resolve_toolbar_permissions(user_id, menu_id, mode)   │   │
│  │    ↓                                                     │   │
│  │  Returns: {                                             │   │
│  │    allowed_actions: ['new', 'edit', 'view', ...]       │   │
│  │  }                                                       │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ HTTP Response
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    REACT FRONTEND (Browser)                      │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ useToolbarConfig Hook                                    │   │
│  │                                                           │   │
│  │  Input: viewId="HRM_EMPLOYEE_RECORDS", mode="VIEW"     │   │
│  │  Fetches: /api/toolbar-permissions/                     │   │
│  │  Output: {                                               │   │
│  │    permissions: {                                        │   │
│  │      new: true, edit: true, view: true,                │   │
│  │      delete: true, refresh: true, ...                  │   │
│  │    }                                                     │   │
│  │  }                                                       │   │
│  └─────────────────────────────────────────────────────────┘   │
│                              │                                    │
│                              │ Props                              │
│                              ▼                                    │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ MasterToolbar Component                                  │   │
│  │                                                           │   │
│  │  Props:                                                  │   │
│  │    - viewId: "HRM_EMPLOYEE_RECORDS"                    │   │
│  │    - mode: "VIEW" | "CREATE" | "EDIT"                   │   │
│  │    - onAction: (actionId) => {...}                      │   │
│  │                                                           │   │
│  │  Renders: [New] [Edit] [View] [Delete] [Exit] ...      │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

### 11.2 Button Visibility Matrix

```
┌─────────────┬──────────┬──────────┬──────────┬──────────────┐
│   Button    │   VIEW   │  CREATE  │   EDIT   │  VIEW_FORM   │
│   (Code)    │   Mode   │   Mode   │   Mode   │     Mode     │
├─────────────┼──────────┼──────────┼──────────┼──────────────┤
│ New (N)     │    ✅    │    ❌    │    ❌    │      ❌      │
│ Edit (E)    │    ✅    │    ❌    │    ❌    │      ✅      │
│ Save (S)    │    ❌    │    ✅    │    ✅    │      ❌      │
│ Cancel (C)  │    ❌    │    ✅    │    ✅    │      ❌      │
│ Clear (K)   │    ❌    │    ✅    │    ✅    │      ❌      │
│ View (V)    │    ✅    │    ❌    │    ❌    │      ❌      │
│ Delete (D)  │    ✅    │    ❌    │    ❌    │      ❌      │
│ Exit (X)    │    ✅    │    ✅    │    ✅    │      ✅      │
│ Refresh (R) │    ✅    │    ❌    │    ❌    │      ❌      │
│ Search (Q)  │    ✅    │    ❌    │    ❌    │      ❌      │
│ Filter (F)  │    ✅    │    ❌    │    ❌    │      ❌      │
│ Import (I)  │    ✅    │    ❌    │    ❌    │      ❌      │
│ Export (O)  │    ✅    │    ❌    │    ❌    │      ❌      │
│ Print (P)   │    ✅    │    ❌    │    ❌    │      ❌      │
│ Submit (T)  │    ✅    │    ❌    │    ❌    │      ❌      │
│ Authorize(Z)│    ✅    │    ❌    │    ❌    │      ❌      │
│ Reject (J)  │    ✅    │    ❌    │    ❌    │      ❌      │
│ First (1)   │    ✅    │    ❌    │    ❌    │      ❌      │
│ Previous(2) │    ✅    │    ❌    │    ❌    │      ❌      │
│ Next (3)    │    ✅    │    ❌    │    ❌    │      ❌      │
│ Last (4)    │    ✅    │    ❌    │    ❌    │      ❌      │
└─────────────┴──────────┴──────────┴──────────┴──────────────┘

Legend:
✅ = Button is visible and enabled
❌ = Button is hidden (not rendered)
```

### 11.3 Config String Visual Breakdown

```
Transaction Config: N E S C K Z T J A V P M R D X 1 2 3 4 Q F
                    │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │
                    │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ └─ Filter (Alt+F)
                    │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ └─── Search (Ctrl+F)
                    │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ └───── Last (End)
                    │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ └─────── Next (PgDn)
                    │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ └───────── Previous (PgUp)
                    │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ └─────────── First (Home)
                    │ │ │ │ │ │ │ │ │ │ │ │ │ │ └───────────── Exit (ESC)
                    │ │ │ │ │ │ │ │ │ │ │ │ │ └─────────────── Delete (F4)
                    │ │ │ │ │ │ │ │ │ │ │ │ └───────────────── Refresh (F9)
                    │ │ │ │ │ │ │ │ │ │ │ └─────────────────── Email (Ctrl+M)
                    │ │ │ │ │ │ │ │ │ │ └───────────────────── Print (Ctrl+P)
                    │ │ │ │ │ │ │ │ │ └─────────────────────── View (F7)
                    │ │ │ │ │ │ │ │ └───────────────────────── Amend (Alt+A)
                    │ │ │ │ │ │ │ └─────────────────────────── Reject (Alt+R)
                    │ │ │ │ │ │ └───────────────────────────── Submit (Alt+S)
                    │ │ │ │ │ └─────────────────────────────── Authorize (F10)
                    │ │ │ │ └───────────────────────────────── Clear (F5)
                    │ │ │ └─────────────────────────────────── Cancel (ESC)
                    │ │ └───────────────────────────────────── Save (F8)
                    │ └─────────────────────────────────────── Edit (F3)
                    └───────────────────────────────────────── New (F2)

Total: 21 buttons
```

### 11.4 Screen Type Comparison

```
┌──────────────────────┬──────────────────┬──────────────────┬──────────────────┐
│   Simple Master      │ Advanced Master  │   Transaction    │      Report      │
│   (11 buttons)       │  (13 buttons)    │   (21 buttons)   │   (8 buttons)    │
├──────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│                      │                  │                  │                  │
│ [New]    [Edit]      │ [New]    [Edit]  │ [New]    [Edit]  │ [View]           │
│ [Save]   [Cancel]    │ [Save]   [Cancel]│ [Save]   [Cancel]│ [Refresh]        │
│ [Clear]  [View]      │ [Clear]  [View]  │ [Clear]  [Submit]│ [Print]          │
│ [Delete] [Exit]      │ [Delete] [Exit]  │ [Authorize]      │ [Export]         │
│ [Refresh][Search]    │ [Refresh][Search]│ [Reject] [Amend] │ [Search]         │
│ [Filter]             │ [Filter] [Import]│ [View]   [Print] │ [Filter]         │
│                      │ [Export]         │ [Email]  [Delete]│ [Settings]       │
│                      │                  │ [Refresh][Exit]  │ [Exit]           │
│                      │                  │ [First]  [Prev]  │                  │
│                      │                  │ [Next]   [Last]  │                  │
│                      │                  │ [Search] [Filter]│                  │
│                      │                  │                  │                  │
├──────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Config:              │ Config:          │ Config:          │ Config:          │
│ NESCKVDXRQF          │ NESCKVDXRQFIO    │ NESCKZTJAVPMRDX  │ VRXPYQFG         │
│                      │                  │ 1234QF           │                  │
├──────────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Examples:            │ Examples:        │ Examples:        │ Examples:        │
│ • UOM                │ • Item Master    │ • Purchase Order │ • Stock Report   │
│ • Brands             │ • Customers      │ • Sales Order    │ • Sales Analysis │
│ • Categories         │ • Suppliers      │ • Leave App      │ • Attendance     │
│ • Tax Classes        │ • Employees      │ • Expense Claim  │ • Payroll Report │
│ • Departments        │ • Locations      │ • Invoices       │ • Financial Stmt │
└──────────────────────┴──────────────────┴──────────────────┴──────────────────┘
```

### 11.5 User Interaction Flow

```
┌──────────────────────────────────────────────────────────────────┐
│                        LIST PAGE (VIEW Mode)                      │
│                                                                    │
│  Toolbar: [New] [Refresh] [Search] [Filter] [Exit]              │
│                                                                    │
│  ┌────────────────────────────────────────────────────────┐     │
│  │ Employee Records List                                   │     │
│  │ ┌────┬──────────┬────────────┬────────────┬──────────┐ │     │
│  │ │ ☑  │ Emp Code │ Name       │ Department │ Status   │ │     │
│  │ ├────┼──────────┼────────────┼────────────┼──────────┤ │     │
│  │ │ ☐  │ EMP001   │ John Doe   │ IT         │ Active   │ │     │
│  │ │ ☐  │ EMP002   │ Jane Smith │ HR         │ Active   │ │     │
│  │ └────┴──────────┴────────────┴────────────┴──────────┘ │     │
│  └────────────────────────────────────────────────────────┘     │
└──────────────────────────────────────────────────────────────────┘
                              │
                              │ User clicks [New] button
                              ▼
┌──────────────────────────────────────────────────────────────────┐
│                      FORM PAGE (CREATE Mode)                      │
│                                                                    │
│  Toolbar: [Save] [Cancel] [Clear] [Exit]                         │
│                                                                    │
│  ┌────────────────────────────────────────────────────────┐     │
│  │ New Employee Record                                     │     │
│  │                                                          │     │
│  │  Employee Code:  [Auto-generated_______]               │     │
│  │  First Name:     [_________________________]           │     │
│  │  Last Name:      [_________________________]           │     │
│  │  Department:     [Select Department ▼]                 │     │
│  │  Designation:    [Select Designation ▼]                │     │
│  │  Email:          [_________________________]           │     │
│  │                                                          │     │
│  └────────────────────────────────────────────────────────┘     │
└──────────────────────────────────────────────────────────────────┘
                              │
                              │ User clicks [Save] button
                              ▼
┌──────────────────────────────────────────────────────────────────┐
│                      DETAIL PAGE (VIEW Mode)                      │
│                                                                    │
│  Toolbar: [Edit] [Delete] [Print] [Exit]                        │
│                                                                    │
│  ┌────────────────────────────────────────────────────────┐     │
│  │ Employee Record #EMP003                                 │     │
│  │                                                          │     │
│  │  Employee Code:  EMP003                                 │     │
│  │  Name:           John Smith                             │     │
│  │  Department:     IT                                     │     │
│  │  Designation:    Software Engineer                      │     │
│  │  Email:          john.smith@company.com                 │     │
│  │  Status:         Active                                 │     │
│  │                                                          │     │
│  └────────────────────────────────────────────────────────┘     │
└──────────────────────────────────────────────────────────────────┘
                              │
                              │ User clicks [Edit] button
                              ▼
┌──────────────────────────────────────────────────────────────────┐
│                       FORM PAGE (EDIT Mode)                       │
│                                                                    │
│  Toolbar: [Save] [Cancel] [Clear] [Exit]                         │
│                                                                    │
│  ┌────────────────────────────────────────────────────────┐     │
│  │ Edit Employee Record #EMP003                            │     │
│  │                                                          │     │
│  │  Employee Code:  EMP003 (disabled)                      │     │
│  │  First Name:     [John_____________________]           │     │
│  │  Last Name:      [Smith____________________]           │     │
│  │  Department:     [IT ▼]                                │     │
│  │  Designation:    [Software Engineer ▼]                 │     │
│  │  Email:          [john.smith@company.com___]           │     │
│  │                                                          │     │
│  └────────────────────────────────────────────────────────┘     │
└──────────────────────────────────────────────────────────────────┘
                              │
                              │ User clicks [Cancel] button
                              ▼
                         Back to VIEW Mode
```

### 11.6 Data Flow Sequence

```
┌─────────────────────────────────────────────────────────────────┐
│                        USER INTERACTION                          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ User clicks [New] button
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    handleToolbarAction('new')                    │
│                                                                   │
│  switch (actionId) {                                             │
│    case 'new':                                                   │
│      setMode('CREATE');  ← Change mode state                    │
│      setShowForm(true);                                         │
│      setEditingId(null);                                        │
│      break;                                                      │
│  }                                                               │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ Mode state changes to 'CREATE'
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    MasterToolbar Re-renders                      │
│                                                                   │
│  useToolbarConfig("HRM_EMPLOYEE_RECORDS", "CREATE")            │
│    ↓                                                             │
│  Fetches: GET /api/toolbar-permissions/                        │
│           ?menu_id=HRM_EMPLOYEE_RECORDS&mode=CREATE            │
│    ↓                                                             │
│  Backend returns: {                                             │
│    allowed_actions: ['save', 'cancel', 'clear', 'exit']        │
│  }                                                               │
│    ↓                                                             │
│  Hook converts to permissions object                            │
│    ↓                                                             │
│  Component filters buttons based on permissions                 │
│    ↓                                                             │
│  Renders: [Save] [Cancel] [Clear] [Exit]                       │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ User sees updated toolbar
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                         UPDATED UI                               │
│                                                                   │
│  Toolbar: [Save] [Cancel] [Clear] [Exit]                        │
│  Form: Empty form ready for input                               │
│  List: Hidden (showForm = true)                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 11.7 Permission Resolution Visual

```
┌─────────────────────────────────────────────────────────────────┐
│              PERMISSION RESOLUTION PIPELINE                      │
└─────────────────────────────────────────────────────────────────┘

STEP 1: Get Screen Capability
┌─────────────────────────────────────────────────────────────────┐
│ ERPMenuItem.applicable_toolbar_config                           │
│ → "NESCKVDXRQF"                                                 │
└─────────────────────────────────────────────────────────────────┘
                              ↓
STEP 2: Get User Permission Mask
┌─────────────────────────────────────────────────────────────────┐
│ If user.is_superuser or user.username == 'admin':              │
│   permission_mask = "11111111111" (all 1s)                     │
│ Else:                                                            │
│   Get from RolePermission.toolbar_permissions                   │
│   Example: "11001111011" (deny Save, Cancel)                   │
└─────────────────────────────────────────────────────────────────┘
                              ↓
STEP 3: Apply Permission Filter (Bitwise AND)
┌─────────────────────────────────────────────────────────────────┐
│ Screen String:  N E S C K V D X R Q F                           │
│ Permission Mask: 1 1 0 0 1 1 1 1 0 1 1                          │
│ Result:          N E _ _ K V D X _ Q F                          │
│ Allowed Chars:  [N, E, K, V, D, X, Q, F]                       │
└─────────────────────────────────────────────────────────────────┘
                              ↓
STEP 4: Apply Mode Law
┌─────────────────────────────────────────────────────────────────┐
│ Mode: VIEW                                                       │
│ Exclude: [S, C, K] (Save, Cancel, Clear)                       │
│ Allowed Chars: [N, E, K, V, D, X, Q, F]                        │
│ After Filter:  [N, E, V, D, X, Q, F]                           │
└─────────────────────────────────────────────────────────────────┘
                              ↓
STEP 5: Convert to Action Names
┌─────────────────────────────────────────────────────────────────┐
│ Final Actions: ['new', 'edit', 'view', 'delete',               │
│                 'exit', 'search', 'filter']                     │
└─────────────────────────────────────────────────────────────────┘
```

---

## 12. ADVANCED IMPLEMENTATION PATTERNS

### 12.1 Unified Container Pattern (In-Place Swap)

**Gold Standard**: UOM Setup

```typescript
export const UOMSetup: React.FC = () => {
  // State management
  const [mode, setMode] = useState<MasterMode>('VIEW');
  const [showForm, setShowForm] = useState(false);
  const [editingId, setEditingId] = useState<string | null>(null);
  const [selectedUOMId, setSelectedUOMId] = useState<string | null>(null);
  
  // Determine toolbar mode
  const getToolbarMode = (): MasterMode => {
    if (!showForm) return 'VIEW';
    return editingId ? 'EDIT' : 'CREATE';
  };

  return (
    <div className="flex flex-col h-full">
      {/* Toolbar - Always visible */}
      <MasterToolbar
        viewId="INVENTORY_UOM_SETUP"
        mode={getToolbarMode()}
        onAction={handleToolbarAction}
        hasSelection={!!selectedUOMId}
      />
      
      {/* Fixed Header - Always visible */}
      <div className="px-4 pt-4 pb-0">
        <h1>Units of Measure</h1>
        {!showForm && <FilterPanel />}
      </div>
      
      {/* Scrollable Content - List OR Form (never both) */}
      <div className="flex-1 overflow-y-auto">
        {showForm ? (
          <UOMForm
            uomId={editingId}
            onSuccess={() => { setShowForm(false); loadUOMs(); }}
            onCancel={() => setShowForm(false)}
          />
        ) : (
          <UOMTable
            uoms={uoms}
            selectedId={selectedUOMId}
            onSelect={setSelectedUOMId}
          />
        )}
      </div>
    </div>
  );
};
```

**Key Principles**:
- ✅ Single component handles both list and form
- ✅ State-based swap (not routing)
- ✅ Persistent header and toolbar
- ✅ Only content area changes

### 12.2 Complete Action Handler Template

```typescript
const handleToolbarAction = (action: string) => {
  switch (action) {
    // CRUD Operations
    case 'new':
      setEditingId(null);
      setMode('CREATE');
      setShowForm(true);
      break;
      
    case 'edit':
      if (selectedId) {
        setEditingId(selectedId);
        setMode('EDIT');
        setShowForm(true);
      } else {
        showNotification('Please select a record to edit', 'warning');
      }
      break;
      
    case 'save':
      if (showForm) {
        formRef.current?.submit();
      }
      break;
      
    case 'cancel':
      if (showForm) {
        if (hasUnsavedChanges) {
          setIsCancelDialogOpen(true);
        } else {
          setShowForm(false);
          setMode('VIEW');
        }
      }
      break;
      
    case 'clear':
      if (showForm) {
        formRef.current?.reset();
      } else {
        clearFilters();
      }
      break;
      
    case 'view':
      if (selectedId && !showForm) {
        setEditingId(selectedId);
        setMode('VIEW_FORM');
        setShowForm(true);
      }
      break;
      
    case 'delete':
      if (selectedId) {
        setIsDeleteDialogOpen(true);
      }
      break;
      
    // Navigation
    case 'refresh':
      loadRecords();
      break;
      
    case 'search':
      document.querySelector<HTMLInputElement>('input[type="text"]')?.focus();
      break;
      
    case 'filter':
      setShowFilterPanel(!showFilterPanel);
      break;
      
    case 'first':
    case 'previous':
    case 'next':
    case 'last':
      handleRecordNavigation(action);
      break;
      
    // Import/Export
    case 'import':
      setShowImportDialog(true);
      break;
      
    case 'export':
      exportToExcel();
      break;
      
    // Workflow (Transactions)
    case 'submit':
      if (selectedId) {
        submitForApproval(selectedId);
      }
      break;
      
    case 'authorize':
      if (selectedId) {
        authorizeRecord(selectedId);
      }
      break;
      
    case 'reject':
      if (selectedId) {
        setIsRejectDialogOpen(true);
      }
      break;
      
    // Document Operations
    case 'print':
      if (selectedId) {
        printRecord(selectedId);
      } else {
        printList();
      }
      break;
      
    case 'email':
      if (selectedId) {
        setIsEmailDialogOpen(true);
      }
      break;
      
    // Utilities
    case 'notes':
      setShowNotesPanel(true);
      break;
      
    case 'attach':
      setShowAttachmentDialog(true);
      break;
      
    case 'help':
      setShowHelpDialog(true);
      break;
      
    // Exit
    case 'exit':
      if (showForm && hasUnsavedChanges) {
        setIsExitDialogOpen(true);
      } else {
        navigate('/dashboard');
      }
      break;
      
    default:
      console.warn(`Unhandled toolbar action: ${action}`);
  }
};
```

### 12.3 Form Ref Pattern

```typescript
// Define form handle interface
export interface FormHandle {
  submit: () => Promise<void>;
  reset: () => void;
  validate: () => boolean;
}

// In parent component
const formRef = React.useRef<FormHandle>(null);

// In form component
export const EmployeeForm = React.forwardRef<FormHandle, EmployeeFormProps>(
  ({ employeeId, readOnly, onSuccess, onCancel }, ref) => {
    const [formData, setFormData] = useState<EmployeeData>({});
    
    // Expose methods to parent via ref
    React.useImperativeHandle(ref, () => ({
      submit: async () => {
        if (!validate()) return;
        
        try {
          if (employeeId) {
            await employeeService.update(employeeId, formData);
          } else {
            await employeeService.create(formData);
          }
          onSuccess();
        } catch (error) {
          showError(error);
        }
      },
      
      reset: () => {
        setFormData({});
      },
      
      validate: () => {
        // Validation logic
        return true;
      }
    }));
    
    return (
      <form>
        {/* Form fields */}
      </form>
    );
  }
);
```

### 12.4 Validation Criteria Checklist

**Before declaring implementation complete, verify**:

- [ ] **Admin sees all actions in VIEW mode**
  - Test: Login as admin, open screen in VIEW mode
  - Expected: All configured buttons visible (except S, C, K)

- [ ] **Admin sees only S,C,K,X in NEW/EDIT mode**
  - Test: Click "New" or "Edit"
  - Expected: Only Save, Cancel, Clear, Exit visible

- [ ] **User without Delete permission never sees Delete**
  - Test: Login as restricted user
  - Expected: Delete button never appears

- [ ] **User with Submit permission does NOT see Submit in EDIT mode**
  - Test: Edit a record
  - Expected: Submit button hidden (mode law)

- [ ] **No screen shows Save in VIEW mode**
  - Test: Any screen in VIEW mode
  - Expected: Save button never visible

- [ ] **No screen shows Search in EDIT mode**
  - Test: Edit any record
  - Expected: Search button hidden

- [ ] **Customer Master (NESCKVDXRQF) behaves correctly**
  - Test: All mode transitions
  - Expected: Correct buttons in each mode

- [ ] **Purchase Order (NESCKZTJAVPMRDX1234QF) behaves correctly**
  - Test: Workflow actions (Submit, Authorize, Reject)
  - Expected: Status-based button enabling

---

## 📚 APPENDIX

### A. Complete Toolbar Configurations

```
# Masters (Simple)
NESCKVDXRQF                    # 11 chars - Basic CRUD + View

# Masters (Advanced)
NESCKVDXRQFIO                  # 13 chars - Add Import/Export

# Transactions (Standard)
NESCKZTJAVPMRDX1234QF          # 21 chars - Full workflow + navigation

# Reports
RPQFX                          # 5 chars - Refresh, Print, Search, Filter, Exit

# Dashboards
RQF                            # 3 chars - Refresh, Search, Filter

# Configuration
NESCKXR                        # 7 chars - Basic setup screens
```

### B. File Locations Reference

```
Backend:
  Core/auth_access/backend/user_management/
    ├── models.py                              # ERPMenuItem, Role, RolePermission
    ├── toolbar_views.py                       # API endpoints
    └── services/toolbar_permission_service.py # Permission resolution

Frontend:
  Core/ui-canon/frontend/ui/components/
    └── MasterToolbarConfigDriven.tsx          # Toolbar component
  
  HRM/frontend/src/hooks/
    └── useToolbarConfig.ts                    # Toolbar hook

Examples:
  Retail/frontend/inventory/pages/
    └── UOMSetup.tsx                           # Gold standard (Simple Master)
  
  Retail/frontend/procurement/pages/
    └── PurchaseOrderListPage.tsx              # Gold standard (Transaction)
```

### C. Related Documentation

- `UNIFIED_ARCHITECTURE.md` - Platform architecture overview
- `Steering/20TOOLBAR_ROLLOUT/01_ESSENTIAL/BENCHMARK_STABILIZATION_COMPLETE.md` - UOM & PO benchmarks
- `Steering/20TOOLBAR_ROLLOUT/01_ESSENTIAL/TOOLBAR_LEGEND_AND_MAPPING.md` - Character mappings
- `Common/qa-launcher-console/UNIFIED_APP_SHELL_GUIDE.md` - Unified shell guide

### D. Licensing vs Operating Companies - Architectural Report

#### D.1 Executive Summary

The Olivine Platform implements a **three-tier entity architecture**:

1. **Licensing Layer** (Commercial Control Plane) - Controls limits and entitlements
2. **Company Layer** (Business Entity) - Legal/operational entities
3. **Location Layer** (Retail-Specific) - Physical operational sites

**Key Principle**: **Licensing owns NO business data** - it only enforces limits.

#### D.2 Architectural Layers

##### **LAYER 1: LICENSING (Control Plane)**

**Location**: `Core/licensing/backend/licensing/models.py`

**Model**: `LicenseConfiguration`

**Purpose**: Commercial governance and platform limits

**Key Fields**:
```python
- license_key: str              # Unique license identifier
- licensee_name: str            # Organization name
- max_companies: int            # Maximum Companies allowed (default: 1)
- max_locations_per_company: int # Maximum Locations per Company (default: 5)
- max_total_locations: int      # Maximum total Locations (default: 10)
- is_active: bool               # Only one active license allowed
- valid_from: date
- valid_until: date             # Null = perpetual
```

**Current Seeded License**:
```
License Key: RETAIL-ERP-DEV-2025
Licensee: Refined Retail Inc
Max Companies: 5
Max Locations per Company: 10
Max Total Locations: 50
Valid From: 2025-01-01
Valid Until: Perpetual (None)
Status: Active
```

**What Licensing DOES**:
- ✅ Enforces Company creation limits
- ✅ Enforces Location creation limits (per-company + total)
- ✅ Controls app access/entitlements
- ✅ Provides license validity checks

**What Licensing DOES NOT DO**:
- ❌ Own business masters (Company, Item, Supplier, etc.)
- ❌ Manage operational data
- ❌ Provide UI for business users
- ❌ Store reference data

##### **LAYER 2: COMPANY (Business Entity)**

**Location**: `Core/licensing/backend/business_entities/models.py`

**Model**: `Company`

**Purpose**: **LICENSING METADATA ONLY** (per architectural lock)

**Key Fields**:
```python
- code: str                     # Company code (unique)
- name: str                     # Company name
- legal_entity_type: str        # SOLE_PROP, PARTNERSHIP, PRIVATE_LTD, etc.
- country: str                  # ISO 3166-1 alpha-2
- default_currency: str         # ISO 4217
- timezone: str
- status: str                   # ACTIVE, INACTIVE
- address_line1/2, city, state, postal_code, address_country
```

**Architectural Lock**:
```python
"""
⚠️ ARCHITECTURAL LOCK:
- This is the ONLY operational model allowed in business_entities
- ALL other operational models belong in domain.company
- DO NOT add operational models here
"""
```

**License Enforcement**:
```python
def clean(self):
    """🔒 LICENSE ENFORCEMENT"""
    if self.pk is None:  # Only for new Companies
        license_config = LicenseConfiguration.get_active_license()
        existing_count = Company.objects.count()
        
        if existing_count >= license_config.max_companies:
            raise ValidationError(
                f"Company limit exceeded. Your license allows only "
                f"{license_config.max_companies} companies. "
                f"Currently {existing_count} exist. "
                f"Please upgrade your license to create more companies."
            )
```

**Current Usage**: 2 Companies / 5 allowed

**Who Uses Company**:
- ✅ **ALL MODULES**: Retail, HRM, CRM, FMS
- ✅ **Platform Level**: Authentication, permissions, multi-tenancy
- ✅ **Licensing**: Limit enforcement only

##### **LAYER 3: LOCATION (Retail-Exclusive Operational Concept)**

**Location**: `Retail/backend/domain/models.py`

**Model**: `Location`

**Purpose**: **RETAIL-EXCLUSIVE** physical operational sites

**Key Fields**:
```python
- id: UUID
- company: ForeignKey(BusinessEntityCompany)  # Links to Company
- location_code: str
- name: str
- location_type: str            # STORE, WAREHOUSE, OFFICE, OTHER
- channel_type: str             # RETAIL, ONLINE, WHOLESALE, FRANCHISE
- parent_location: ForeignKey('self')  # Hierarchy support
- address_line1/2, city, state, country, postal_code
- phone, email
- timezone, opening_date, closing_date
- is_pos_enabled: bool          # POS capability
- is_dc: bool                   # Distribution Center flag
- is_active: bool
```

**Critical Ownership Rule**:
```python
"""
CRITICAL OWNERSHIP RULE:
- This model is OWNED by the Retail module
- HRM, CRM, FMS MUST NOT reference this model
- Non-Retail apps operate at COMPANY level only

USAGE:
- ✅ Retail Sales: Transaction location, customer location
- ✅ Retail Inventory: Stock location, warehouse
- ✅ Retail POS: Store location for POS sessions
- ✅ Retail Procurement: Receiving location

FORBIDDEN USAGE:
- ❌ HRM: Employee location (use Company instead)
- ❌ CRM: Customer location (use Company instead)
- ❌ FMS: GL location (use Company/Cost Center instead)
"""
```

**Current Usage**: 10 Locations / 50 total allowed

#### D.3 Entity Relationship Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    LICENSING (Control Plane)                     │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ LicenseConfiguration                                     │   │
│  │                                                           │   │
│  │  - license_key: "RETAIL-ERP-DEV-2025"                   │   │
│  │  - max_companies: 5                                      │   │
│  │  - max_locations_per_company: 10                        │   │
│  │  - max_total_locations: 50                              │   │
│  │  - is_active: True                                       │   │
│  └─────────────────────────────────────────────────────────┘   │
│                              │                                    │
│                              │ Enforces Limits                    │
│                              ▼                                    │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│              COMPANY (Business Entity - Platform Level)          │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Company (business_entities.Company)                     │   │
│  │                                                           │   │
│  │  - code: "COMP001"                                       │   │
│  │  - name: "Mumbai Retail Operations"                     │   │
│  │  - legal_entity_type: "PRIVATE_LTD"                     │   │
│  │  - country: "IN"                                         │   │
│  │  - default_currency: "INR"                              │   │
│  └─────────────────────────────────────────────────────────┘   │
│                              │                                    │
│                              │ 1:N (Retail Only)                  │
│                              ▼                                    │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│            LOCATION (Retail-Exclusive Operational)               │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Location (Retail.domain.Location)                       │   │
│  │                                                           │   │
│  │  - company: FK(Company)                                  │   │
│  │  - location_code: "LOC001"                              │   │
│  │  - name: "Phoenix Mall Store"                           │   │
│  │  - location_type: "STORE"                               │   │
│  │  - channel_type: "RETAIL"                               │   │
│  │  - is_pos_enabled: True                                 │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘

MODULE USAGE:
┌──────────┬──────────┬──────────┐
│ Retail   │ HRM      │ CRM/FMS  │
├──────────┼──────────┼──────────┤
│ Company  │ Company  │ Company  │
│ Location │ ❌       │ ❌       │
└──────────┴──────────┴──────────┘
```

#### D.4 Enforcement Points

**Where License Limits Are Enforced**:

1. ✅ **Django Admin** - Company/Location creation forms
2. ✅ **REST APIs** - Any endpoint creating Companies/Locations
3. ✅ **Model.save()** - Direct model saves
4. ✅ **Bulk creates** - QuerySet operations (if using save())

**Where Enforcement Does NOT Apply**:

- ❌ Platform Admin seeds (can bypass if needed)
- ❌ Migrations (historical data)
- ❌ Direct SQL inserts (not recommended)

#### D.5 Domain Ownership Matrix

| Entity | Owner | Used By | Purpose |
|--------|-------|---------|---------|
| **LicenseConfiguration** | Licensing | Platform | Commercial limits |
| **Company** | Platform (business_entities) | ALL modules | Legal entity, multi-tenancy |
| **Location** | Retail | Retail ONLY | Physical stores/warehouses |
| **Employee** | HRM | HRM | HR records |
| **Lead/Opportunity** | CRM | CRM | Sales pipeline |
| **GL/AP/AR** | FMS | FMS | Financial accounts |

#### D.6 Critical Rules

1. **Licensing owns NO business data** - Only enforces limits
2. **Company is Platform-level** - Used by ALL modules
3. **Location is Retail-exclusive** - HRM/CRM/FMS MUST NOT reference it
4. **HRM/CRM/FMS operate at Company level** - No Location references
5. **business_entities = LICENSING METADATA ONLY** - No operational models

#### D.7 File Locations

```
Core/
├── licensing/
│   └── backend/
│       ├── licensing/
│       │   └── models.py          # LicenseConfiguration
│       └── business_entities/
│           └── models.py          # Company (licensing metadata only)
│
Retail/
└── backend/
    └── domain/
        └── models.py              # Location (Retail-exclusive)
```

#### D.8 Validation Error Messages

**Company Limit Exceeded**:
```
Company limit exceeded. Your license allows only 5 companies. 
Currently 5 exist. Please upgrade your license to create more companies.
```

**Total Location Limit Exceeded**:
```
Total location limit exceeded. Your license allows only 50 locations 
across all companies. Currently 50 exist. Please upgrade your license 
to create more locations.
```

**Per-Company Location Limit Exceeded**:
```
Location limit exceeded for this company. Your license allows only 
10 locations per company. Company 'Mumbai Retail Operations' already 
has 10 locations. Please upgrade your license to create more locations.
```

**No Active License**:
```
No active license configuration found. Please contact your platform administrator.
```

#### D.9 Reference Documentation

- `Steering/01_ARCH_GOVERNANCE/ARCHITECTURAL_LOCK_REFERENCE.md` - Entity locks and terminology
- `Steering/00AGENT_ONBOARDING/Enterprise_Platform_Onboarding_v6.md` - Platform governance
- `Steering/06_REPORTS_AUDITS/LICENSE_ENFORCEMENT_REPORT.md` - License implementation details

---

**END OF DOCUMENT**

**Version**: 1.0  
**Last Updated**: 2026-01-20 19:05 IST  
**Maintained By**: Astra (Chief ERP Platform Owner)  
**Approved By**: Viji (Product Owner)

---

**This is the SINGLE SOURCE OF TRUTH for toolbar implementation across all modules (Retail, HRM, CRM, FMS).**
