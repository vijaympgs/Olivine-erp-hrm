# 🔍 TABLE MODIFICATION ANALYSIS - USER MANAGEMENT TABLES

**Document Created**: 2026-01-09 08:01 IST  
**Author**: Astra  
**Purpose**: Detailed analysis of table modifications for toolbar-driven permission system  
**Status**: ⏳ PENDING APPROVAL

---

## 📋 EXECUTIVE SUMMARY

This document provides a comprehensive analysis of modifications required to existing `user_management` tables to support the new toolbar-driven permission system.

**Key Changes:**
- **Rename**: `MenuItemType` → `ERPMenuItem` (supports all modules: Retail, HRM, CRM, FMS)
- **Extend**: Add `toolbar_config` field to store 15-button configuration
- **Derive**: Auto-populate permission flags from toolbar configuration
- **Backward Compatible**: Existing data preserved, new fields nullable

---

## 📊 TABLE-BY-TABLE MODIFICATION REPORT

### **TABLE 1: MenuItemType → ERPMenuItem** ✏️ **RENAME + EXTEND**

**Current Name**: `menu_item_types` (MenuItemType)  
**New Name**: `erp_menu_items` (ERPMenuItem)  
**Rationale**: Support ALL modules (Retail, HRM, CRM, FMS), not just Retail

#### **EXISTING FIELDS** (Keep As-Is)

| Field Name | Type | Description | Action |
|------------|------|-------------|--------|
| `menu_id` | CharField(100) | Unique menu identifier | ✅ Keep |
| `menu_name` | CharField(200) | Display name | ✅ Keep |
| `parent_menu` | ForeignKey('self') | Parent menu for hierarchy | ✅ Keep |
| `module_name` | CharField(50) | Module name (currently defaults to 'retail') | ⚠️ Modify |
| `menu_order` | IntegerField | Display order | ✅ Keep |
| `is_active` | BooleanField | Active status | ✅ Keep |
| `created_at` | DateTimeField | Creation timestamp | ✅ Keep |

#### **FIELDS TO MODIFY**

**Field**: `module_name`

**Current Definition:**
```python
module_name = models.CharField(max_length=50, default='retail')
```

**New Definition:**
```python
module_name = models.CharField(
    max_length=50, 
    choices=[
        ('RETAIL', 'Retail Operations'),
        ('FMS', 'Financial Management'),
        ('HRM', 'Human Resources'),
        ('CRM', 'Customer Relationship Management')
    ]
)
```

**Reason**: Remove 'retail' default, support all ERP modules

#### **NEW FIELDS TO ADD**

| # | Field Name | Type | Default | Description | Nullable |
|---|------------|------|---------|-------------|----------|
| 1 | `submodule` | CharField(50) | NULL | Submodule categorization (e.g., INVENTORY, SALES) | Yes |
| 2 | `view_type` | CharField(20) | 'LIST' | UI type: MASTER/TRANSACTION/REPORT/DASHBOARD/LIST | No |
| 3 | `toolbar_config` | CharField(50) | '0,0,0,0,0,0,0,0,0,0,0,1,0,0,0' | 15-button toolbar configuration | No |
| 4 | `route_path` | CharField(200) | NULL | Frontend route path (e.g., /inventory/item-master) | Yes |
| 5 | `component_name` | CharField(100) | NULL | React component name (e.g., ItemMasterPage) | Yes |
| 6 | `description` | TextField | NULL | Detailed description | Yes |
| 7 | `is_system_menu` | BooleanField | False | System menus cannot be deleted | No |
| 8 | `updated_at` | DateTimeField | auto_now | Last update timestamp | No |
| 9 | `created_by` | ForeignKey(User) | NULL | User who created this menu | Yes |
| 10 | `updated_by` | ForeignKey(User) | NULL | User who last updated this menu | Yes |

#### **DETAILED FIELD SPECIFICATIONS**

**1. submodule**
```python
submodule = models.CharField(
    max_length=50, 
    null=True, 
    blank=True,
    help_text='Submodule categorization, e.g., INVENTORY, SALES, PROCUREMENT'
)
```
**Purpose**: Organize menus within modules  
**Example Values**: 'INVENTORY', 'SALES', 'PROCUREMENT', 'PAYROLL', 'RECRUITMENT'

---

**2. view_type**
```python
view_type = models.CharField(
    max_length=20,
    choices=[
        ('MASTER', 'Master Data'),
        ('TRANSACTION', 'Transaction'),
        ('REPORT', 'Report'),
        ('DASHBOARD', 'Dashboard'),
        ('LIST', 'List View')
    ],
    default='LIST'
)
```
**Purpose**: Classify UI screen type for appropriate toolbar configuration  
**Impact**: Determines default toolbar buttons available

---

**3. toolbar_config** ⭐ **CRITICAL FIELD**
```python
toolbar_config = models.CharField(
    max_length=50,
    default='0,0,0,0,0,0,0,0,0,0,0,1,0,0,0',
    help_text='15-button config: N,E,S,C,L,T,A,V,P,R,D,X,Y,Z,O (1=enabled, 0=disabled)'
)
```
**Purpose**: Define which toolbar buttons are available for this UI  
**Format**: 15 comma-separated values (0 or 1)  
**Positions**:
```
Position: 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14
Button:   N  E  S  C  L  T  A  V  P  R  D  X  Y  Z  O
Meaning:  New,Edit,Save,Cancel,Clear,auThorize,Amend,View,Print,Refresh,Delete,eXit,upload,download,clOne
```

**Example Configurations:**

| UI Type | Config | Enabled Buttons |
|---------|--------|-----------------|
| Master Data | `1,1,1,1,1,0,0,1,1,1,1,1,1,1,1` | All except Authorize, Amend |
| Transaction | `1,1,1,1,1,1,1,1,1,1,1,1,0,1,1` | All except Upload |
| Report | `0,0,0,0,0,0,0,0,1,1,0,1,0,1,0` | Print, Refresh, Exit, Download |
| Dashboard | `0,0,0,0,0,0,0,0,0,1,0,1,0,0,0` | Refresh, Exit only |

---

**4. route_path**
```python
route_path = models.CharField(
    max_length=200,
    null=True,
    blank=True,
    help_text='Frontend route path, e.g., /inventory/item-master'
)
```
**Purpose**: Link menu item to frontend route  
**Example Values**: '/inventory/item-master', '/sales/orders', '/reports/stock-valuation'

---

**5. component_name**
```python
component_name = models.CharField(
    max_length=100,
    null=True,
    blank=True,
    help_text='React component name, e.g., ItemMasterPage'
)
```
**Purpose**: Reference to React component for debugging/documentation  
**Example Values**: 'ItemMasterPage', 'SalesOrderPage', 'StockValuationReport'

---

**6. description**
```python
description = models.TextField(null=True, blank=True)
```
**Purpose**: Detailed description of menu item functionality  
**Example**: "Manage product catalog including SKU, pricing, and inventory settings"

---

**7. is_system_menu**
```python
is_system_menu = models.BooleanField(
    default=False,
    help_text='System menus cannot be deleted'
)
```
**Purpose**: Protect critical system menus from accidental deletion  
**Example**: Core menus like Dashboard, Settings should be system menus

---

**8. updated_at**
```python
updated_at = models.DateTimeField(auto_now=True)
```
**Purpose**: Track last modification time  
**Auto-populated**: Yes

---

**9. created_by**
```python
created_by = models.ForeignKey(
    'auth.User', 
    null=True, 
    on_delete=models.SET_NULL, 
    related_name='created_menus'
)
```
**Purpose**: Audit trail - who created this menu  
**Nullable**: Yes (for system-created menus)

---

**10. updated_by**
```python
updated_by = models.ForeignKey(
    'auth.User', 
    null=True, 
    on_delete=models.SET_NULL, 
    related_name='updated_menus'
)
```
**Purpose**: Audit trail - who last modified this menu  
**Nullable**: Yes

---

#### **MIGRATION IMPACT**

**Breaking Changes**: ⚠️ **YES**
- Table rename: `menu_item_types` → `erp_menu_items`
- Model rename: `MenuItemType` → `ERPMenuItem`
- All foreign key references need update

**Data Migration Required**: ✅ **YES**
- Existing menu items need `toolbar_config` populated based on `view_type`
- Existing `module_name='retail'` entries preserved

**Estimated Migration Time**: 30 minutes

---

### **TABLE 2: RolePermission** ✏️ **EXTEND**

**Table Name**: `role_permissions` (RolePermission)  
**Action**: Add toolbar override fields and derived permission flags

#### **EXISTING FIELDS** (Keep As-Is)

| Field Name | Type | Description | Action |
|------------|------|-------------|--------|
| `role` | ForeignKey(Role) | Role reference | ✅ Keep |
| `menu_item` | ForeignKey(MenuItemType) | Menu item reference | ⚠️ Update FK |
| `can_access` | BooleanField | Can access menu | ✅ Keep |
| `can_view` | BooleanField | Can view records | ✅ Keep |
| `can_create` | BooleanField | Can create records | ✅ Keep |
| `can_edit` | BooleanField | Can edit records | ✅ Keep |
| `can_delete` | BooleanField | Can delete records | ✅ Keep |
| `created_at` | DateTimeField | Creation timestamp | ✅ Keep |
| `updated_at` | DateTimeField | Update timestamp | ✅ Keep |

#### **FIELDS TO MODIFY**

**Field**: `menu_item`

**Current Definition:**
```python
menu_item = models.ForeignKey(MenuItemType, on_delete=models.CASCADE)
```

**New Definition:**
```python
menu_item = models.ForeignKey(
    'ERPMenuItem',  # Changed from MenuItemType
    on_delete=models.CASCADE,
    related_name='role_permissions'
)
```

**Reason**: Update reference to renamed model

---

#### **NEW FIELDS TO ADD**

| # | Field Name | Type | Default | Description | Nullable |
|---|------------|------|---------|-------------|----------|
| 1 | `toolbar_override` | CharField(50) | NULL | Role-specific toolbar override | Yes |
| 2 | `override_enabled` | BooleanField | False | Enable/disable toolbar override | No |
| 3 | `can_authorize` | BooleanField | False | Can authorize/approve (derived from toolbar pos 5) | No |
| 4 | `can_amend` | BooleanField | False | Can amend authorized docs (derived from toolbar pos 6) | No |
| 5 | `can_print` | BooleanField | False | Can print (derived from toolbar pos 8) | No |
| 6 | `can_upload` | BooleanField | False | Can upload/import (derived from toolbar pos 12) | No |
| 7 | `can_download` | BooleanField | False | Can download/export (derived from toolbar pos 13) | No |
| 8 | `can_clone` | BooleanField | False | Can clone records (derived from toolbar pos 14) | No |
| 9 | `created_by` | ForeignKey(User) | NULL | User who created this permission | Yes |
| 10 | `updated_by` | ForeignKey(User) | NULL | User who last updated this permission | Yes |

#### **DETAILED FIELD SPECIFICATIONS**

**1. toolbar_override** ⭐ **KEY FIELD**
```python
toolbar_override = models.CharField(
    max_length=50,
    null=True,
    blank=True,
    help_text='15-button override: N,E,S,C,L,T,A,V,P,R,D,X,Y,Z,O. If NULL, inherits from ERPMenuItem.toolbar_config'
)
```
**Purpose**: Override toolbar configuration for specific role  
**Behavior**:
- If `NULL`: Inherit from `ERPMenuItem.toolbar_config`
- If set AND `override_enabled=True`: Use this override
- If set AND `override_enabled=False`: Ignore override, use base config

**Example Use Case**:
```
Base Config (Item Master): "1,1,1,1,1,0,0,1,1,1,1,1,1,1,1" (Delete allowed)
POS User Override:         "1,1,1,1,1,0,0,1,1,1,0,1,1,1,1" (Delete denied)
                                                  ↑ Position 10 changed to 0
```

---

**2. override_enabled**
```python
override_enabled = models.BooleanField(
    default=False,
    help_text='If TRUE, toolbar_override is applied; if FALSE, uses ERPMenuItem.toolbar_config'
)
```
**Purpose**: Toggle to enable/disable override without deleting it  
**Use Case**: Temporarily disable override for testing

---

**3-8. Derived Permission Flags**

These fields are **auto-populated** from `toolbar_config` or `toolbar_override`:

```python
can_authorize = models.BooleanField(
    default=False, 
    help_text='Derived from toolbar position 5 (T)'
)
can_amend = models.BooleanField(
    default=False, 
    help_text='Derived from toolbar position 6 (A)'
)
can_print = models.BooleanField(
    default=False, 
    help_text='Derived from toolbar position 8 (P)'
)
can_upload = models.BooleanField(
    default=False, 
    help_text='Derived from toolbar position 12 (Y)'
)
can_download = models.BooleanField(
    default=False, 
    help_text='Derived from toolbar position 13 (Z)'
)
can_clone = models.BooleanField(
    default=False, 
    help_text='Derived from toolbar position 14 (O)'
)
```

**Auto-Population Logic**:
```python
def derive_permissions_from_toolbar(toolbar_config: str) -> dict:
    buttons = toolbar_config.split(',')
    return {
        'can_create': buttons[0] == '1',      # N
        'can_edit': buttons[1] == '1',        # E
        'can_authorize': buttons[5] == '1',   # T
        'can_amend': buttons[6] == '1',       # A
        'can_view': buttons[7] == '1',        # V
        'can_print': buttons[8] == '1',       # P
        'can_delete': buttons[10] == '1',     # D
        'can_upload': buttons[12] == '1',     # Y
        'can_download': buttons[13] == '1',   # Z
        'can_clone': buttons[14] == '1',      # O
    }
```

---

**9. created_by**
```python
created_by = models.ForeignKey(
    'auth.User', 
    null=True, 
    on_delete=models.SET_NULL, 
    related_name='created_role_perms'
)
```
**Purpose**: Audit trail - who created this role permission

---

**10. updated_by**
```python
updated_by = models.ForeignKey(
    'auth.User', 
    null=True, 
    on_delete=models.SET_NULL, 
    related_name='updated_role_perms'
)
```
**Purpose**: Audit trail - who last modified this role permission

---

#### **MIGRATION IMPACT**

**Breaking Changes**: ✅ **NO**
- Only adding new columns (backward compatible)
- Existing data preserved

**Data Migration Required**: ⚠️ **OPTIONAL**
- Can populate `toolbar_override` for existing roles if needed
- Derived permission flags auto-populated on save

**Estimated Migration Time**: 15 minutes

---

### **TABLE 3: UserPermission** ✏️ **EXTEND**

**Table Name**: `user_permissions` (UserPermission)  
**Action**: Add toolbar override and derived permission flags

#### **EXISTING FIELDS** (Keep As-Is)

| Field Name | Type | Description | Action |
|------------|------|-------------|--------|
| `user` | ForeignKey(User) | User reference | ✅ Keep |
| `menu_item` | ForeignKey(MenuItemType) | Menu item reference | ⚠️ Update FK |
| `can_access` | BooleanField | Can access menu | ✅ Keep |
| `can_view` | BooleanField | Can view records | ✅ Keep |
| `can_create` | BooleanField | Can create records | ✅ Keep |
| `can_edit` | BooleanField | Can edit records | ✅ Keep |
| `can_delete` | BooleanField | Can delete records | ✅ Keep |
| `override` | BooleanField | Override role permissions | ✅ Keep |
| `created_at` | DateTimeField | Creation timestamp | ✅ Keep |
| `updated_at` | DateTimeField | Update timestamp | ✅ Keep |
| `created_by` | ForeignKey(User) | Creator | ✅ Keep |

#### **FIELDS TO MODIFY**

**Field**: `menu_item`

**Current Definition:**
```python
menu_item = models.ForeignKey(MenuItemType, on_delete=models.CASCADE)
```

**New Definition:**
```python
menu_item = models.ForeignKey(
    'ERPMenuItem',  # Changed from MenuItemType
    on_delete=models.CASCADE,
    related_name='user_permissions'
)
```

**Reason**: Update reference to renamed model

---

#### **NEW FIELDS TO ADD**

| # | Field Name | Type | Default | Description | Nullable |
|---|------------|------|---------|-------------|----------|
| 1 | `toolbar_override` | CharField(50) | NULL | User-specific toolbar override | Yes |
| 2 | `can_authorize` | BooleanField | False | Can authorize (derived from toolbar pos 5) | No |
| 3 | `can_amend` | BooleanField | False | Can amend (derived from toolbar pos 6) | No |
| 4 | `can_print` | BooleanField | False | Can print (derived from toolbar pos 8) | No |
| 5 | `can_upload` | BooleanField | False | Can upload (derived from toolbar pos 12) | No |
| 6 | `can_download` | BooleanField | False | Can download (derived from toolbar pos 13) | No |
| 7 | `can_clone` | BooleanField | False | Can clone (derived from toolbar pos 14) | No |
| 8 | `updated_by` | ForeignKey(User) | NULL | Last updater | Yes |

#### **DETAILED FIELD SPECIFICATIONS**

**1. toolbar_override**
```python
toolbar_override = models.CharField(
    max_length=50,
    null=True,
    blank=True,
    help_text='User-specific 15-button override. If NULL, inherits from Role or ERPMenuItem'
)
```
**Purpose**: User-specific toolbar override (highest priority)  
**Priority Order**:
1. `UserPermission.toolbar_override` (if set)
2. `RolePermission.toolbar_override` (if set and enabled)
3. `ERPMenuItem.toolbar_config` (base config)

---

**2-7. Derived Permission Flags**

Same as RolePermission, auto-populated from toolbar config.

---

**8. updated_by**
```python
updated_by = models.ForeignKey(
    'auth.User', 
    null=True, 
    on_delete=models.SET_NULL, 
    related_name='updated_user_perms'
)
```
**Purpose**: Audit trail - who last modified this user permission

---

#### **MIGRATION IMPACT**

**Breaking Changes**: ✅ **NO**
- Only adding new columns (backward compatible)

**Data Migration Required**: ✅ **NO**
- New fields nullable, no data migration needed

**Estimated Migration Time**: 10 minutes

---

### **TABLE 4: Role** ✅ **NO CHANGES**

**Table Name**: `roles` (Role)  
**Action**: Keep as-is

**Existing Fields**:
- `role_key` - Unique role identifier
- `role_name` - Display name
- `description` - Role description
- `is_system_role` - System role flag
- `is_active` - Active status
- `created_at` - Creation timestamp

**Recommendation**: ✅ **No changes needed** - Current structure is sufficient

---

### **TABLE 5: UserRole** ✅ **NO CHANGES**

**Table Name**: `user_roles` (UserRole)  
**Action**: Keep as-is

**Existing Fields**:
- `user` - User reference
- `role` - Role reference
- `assigned_by` - Who assigned this role
- `assigned_at` - Assignment timestamp
- `is_active` - Active status

**Recommendation**: ✅ **No changes needed** - Current structure is sufficient

---

### **TABLE 6: GroupPermission** ✏️ **UPDATE FK ONLY**

**Table Name**: `group_permissions` (GroupPermission)  
**Action**: Update foreign key reference

#### **FIELDS TO MODIFY**

**Field**: `menu_item`

**Current Definition:**
```python
menu_item = models.ForeignKey(MenuItemType, on_delete=models.CASCADE)
```

**New Definition:**
```python
menu_item = models.ForeignKey(
    'ERPMenuItem',  # Changed from MenuItemType
    on_delete=models.CASCADE,
    related_name='group_permissions'
)
```

**Reason**: Update reference to renamed model

---

#### **MIGRATION IMPACT**

**Breaking Changes**: ✅ **NO**
- Only updating foreign key reference

**Data Migration Required**: ✅ **NO**
- Automatic FK update

**Estimated Migration Time**: 5 minutes

---

### **TABLE 7: Employee** ✅ **NO CHANGES** (Legacy/Deprecated)

**Table Name**: `user_management_employee` (Employee)  
**Action**: Keep as-is (read-only legacy model)

**Status**: Already marked as deprecated/read-only

**Recommendation**: ✅ **No changes needed**

---

## 🔗 **TOOLBAR CONFIG → PERMISSION MAPPING**

### **Button Position Mapping**

| Position | Code | Button | Action | F-Key | Permission Field | Description |
|----------|------|--------|--------|-------|------------------|-------------|
| 0 | **N** | New | `new` | F2 | `can_create` | Create new record |
| 1 | **E** | Edit | `edit` | F4 | `can_edit` | Edit existing record |
| 2 | **S** | Save | `save` | F8 | *(UI state)* | Save changes |
| 3 | **C** | Cancel | `cancel` | ESC | *(UI state)* | Cancel operation |
| 4 | **L** | Clear | `clear` | F5 | *(UI state)* | Clear form |
| 5 | **T** | auThorize | `authorize` | F10 | `can_authorize` | Approve/Authorize |
| 6 | **A** | Amend | `amend` | F11 | `can_amend` | Amend authorized doc |
| 7 | **V** | View | `view` | F7 | `can_view` | View details |
| 8 | **P** | Print | `print` | Ctrl+P | `can_print` | Print document |
| 9 | **R** | Refresh | `refresh` | F9 | *(always allowed)* | Reload data |
| 10 | **D** | Delete | `delete` | F3 | `can_delete` | Delete record |
| 11 | **X** | eXit | `exit` | ESC | *(always allowed)* | Close/Exit |
| 12 | **Y** | upload | `upload` | F6 | `can_upload` | Import/Upload |
| 13 | **Z** | download | `download` | Ctrl+D | `can_download` | Export/Download |
| 14 | **O** | clOne | `clone` | Ctrl+Shift+C | `can_clone` | Duplicate record |

### **Derivation Logic**

```python
def derive_permissions_from_toolbar(toolbar_config: str) -> dict:
    """
    Convert toolbar config string to permission dictionary
    
    Args:
        toolbar_config: "1,0,1,1,1,0,0,1,1,1,0,1,1,1,1"
    
    Returns:
        {
            'can_create': True,
            'can_edit': False,
            'can_authorize': False,
            'can_amend': False,
            'can_view': True,
            'can_print': True,
            'can_delete': False,
            'can_upload': True,
            'can_download': True,
            'can_clone': True
        }
    """
    buttons = toolbar_config.split(',')
    
    return {
        'can_create': buttons[0] == '1',      # N - New
        'can_edit': buttons[1] == '1',        # E - Edit
        'can_authorize': buttons[5] == '1',   # T - auThorize
        'can_amend': buttons[6] == '1',       # A - Amend
        'can_view': buttons[7] == '1',        # V - View
        'can_print': buttons[8] == '1',       # P - Print
        'can_delete': buttons[10] == '1',     # D - Delete
        'can_upload': buttons[12] == '1',     # Y - upload
        'can_download': buttons[13] == '1',   # Z - download
        'can_clone': buttons[14] == '1',      # O - clOne
    }
```

### **Example Configurations**

#### **Example 1: Item Master (MASTER UI)**
```
toolbar_config: "1,1,1,1,1,0,0,1,1,1,1,1,1,1,1"
                 N E S C L T A V P R D X Y Z O
                 ✓ ✓ ✓ ✓ ✓ ✗ ✗ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓

Derived Permissions:
- can_create = True (pos 0)
- can_edit = True (pos 1)
- can_authorize = False (pos 5)
- can_amend = False (pos 6)
- can_view = True (pos 7)
- can_print = True (pos 8)
- can_delete = True (pos 10)
- can_upload = True (pos 12)
- can_download = True (pos 13)
- can_clone = True (pos 14)
```

#### **Example 2: Sales Order (TRANSACTION UI)**
```
toolbar_config: "1,1,1,1,1,1,1,1,1,1,1,1,0,1,1"
                 N E S C L T A V P R D X Y Z O
                 ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✗ ✓ ✓

Derived Permissions:
- can_create = True
- can_edit = True
- can_authorize = True (transactions need approval)
- can_amend = True (can amend authorized orders)
- can_view = True
- can_print = True
- can_delete = True
- can_upload = False (bulk upload not allowed)
- can_download = True
- can_clone = True
```

#### **Example 3: Stock Valuation Report (REPORT UI)**
```
toolbar_config: "0,0,0,0,0,0,0,0,1,1,0,1,0,1,0"
                 N E S C L T A V P R D X Y Z O
                 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✓ ✗ ✓ ✗ ✓ ✗

Derived Permissions:
- can_create = False (reports are read-only)
- can_edit = False
- can_authorize = False
- can_amend = False
- can_view = False (implicit via access)
- can_print = True
- can_delete = False
- can_upload = False
- can_download = True (export report)
- can_clone = False
```

#### **Example 4: Inventory Dashboard (DASHBOARD UI)**
```
toolbar_config: "0,0,0,0,0,0,0,0,0,1,0,1,0,0,0"
                 N E S C L T A V P R D X Y Z O
                 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✓ ✗ ✗ ✗

Derived Permissions:
- All permissions = False
- Only Refresh and Exit allowed (UI actions, not permissions)
```

---

## 📊 **SUMMARY TABLE**

| # | Table | Current Name | New Name | Action | Fields Added | Fields Modified | Breaking Change | Migration Time |
|---|-------|-------------|----------|--------|--------------|-----------------|-----------------|----------------|
| 1 | MenuItemType | MenuItemType | ERPMenuItem | Rename + Extend | 10 | 1 | ⚠️ YES | 30 min |
| 2 | RolePermission | RolePermission | RolePermission | Extend | 10 | 1 | ✅ NO | 15 min |
| 3 | UserPermission | UserPermission | UserPermission | Extend | 8 | 1 | ✅ NO | 10 min |
| 4 | Role | Role | Role | No Change | 0 | 0 | ✅ NO | 0 min |
| 5 | UserRole | UserRole | UserRole | No Change | 0 | 0 | ✅ NO | 0 min |
| 6 | GroupPermission | GroupPermission | GroupPermission | Update FK | 0 | 1 | ✅ NO | 5 min |
| 7 | Employee | Employee | Employee | No Change | 0 | 0 | ✅ NO | 0 min |
| **TOTAL** | | | | | **28** | **5** | **1** | **60 min** |

---

## ⚠️ **MIGRATION STRATEGY**

### **Phase 1: Rename MenuItemType → ERPMenuItem**

**Migration File**: `0001_rename_menuitemtype.py`

```python
from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('user_management', 'previous_migration'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MenuItemType',
            new_name='ERPMenuItem',
        ),
        migrations.AlterModelOptions(
            name='erpmenuitem',
            options={
                'verbose_name': 'ERP Menu Item',
                'verbose_name_plural': 'ERP Menu Items',
                'ordering': ['menu_order', 'menu_name']
            },
        ),
        migrations.AlterModelTable(
            name='erpmenuitem',
            table='erp_menu_items',
        ),
    ]
```

**Impact**: 
- ⚠️ All foreign key references will be automatically updated
- ⚠️ Admin interface will show new name
- ⚠️ API endpoints may need update

---

### **Phase 2: Add New Fields to ERPMenuItem**

**Migration File**: `0002_add_erpmenuitem_fields.py`

```python
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    dependencies = [
        ('user_management', '0001_rename_menuitemtype'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        # Add submodule
        migrations.AddField(
            model_name='erpmenuitem',
            name='submodule',
            field=models.CharField(
                max_length=50, 
                null=True, 
                blank=True,
                help_text='Submodule categorization'
            ),
        ),
        
        # Add view_type
        migrations.AddField(
            model_name='erpmenuitem',
            name='view_type',
            field=models.CharField(
                max_length=20,
                choices=[
                    ('MASTER', 'Master Data'),
                    ('TRANSACTION', 'Transaction'),
                    ('REPORT', 'Report'),
                    ('DASHBOARD', 'Dashboard'),
                    ('LIST', 'List View')
                ],
                default='LIST'
            ),
        ),
        
        # Add toolbar_config
        migrations.AddField(
            model_name='erpmenuitem',
            name='toolbar_config',
            field=models.CharField(
                max_length=50,
                default='0,0,0,0,0,0,0,0,0,0,0,1,0,0,0',
                help_text='15-button config: N,E,S,C,L,T,A,V,P,R,D,X,Y,Z,O'
            ),
        ),
        
        # Add route_path
        migrations.AddField(
            model_name='erpmenuitem',
            name='route_path',
            field=models.CharField(
                max_length=200, 
                null=True, 
                blank=True
            ),
        ),
        
        # Add component_name
        migrations.AddField(
            model_name='erpmenuitem',
            name='component_name',
            field=models.CharField(
                max_length=100, 
                null=True, 
                blank=True
            ),
        ),
        
        # Add description
        migrations.AddField(
            model_name='erpmenuitem',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        
        # Add is_system_menu
        migrations.AddField(
            model_name='erpmenuitem',
            name='is_system_menu',
            field=models.BooleanField(default=False),
        ),
        
        # Add updated_at
        migrations.AddField(
            model_name='erpmenuitem',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        
        # Add created_by
        migrations.AddField(
            model_name='erpmenuitem',
            name='created_by',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='created_menus',
                to='auth.user'
            ),
        ),
        
        # Add updated_by
        migrations.AddField(
            model_name='erpmenuitem',
            name='updated_by',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='updated_menus',
                to='auth.user'
            ),
        ),
        
        # Modify module_name choices
        migrations.AlterField(
            model_name='erpmenuitem',
            name='module_name',
            field=models.CharField(
                max_length=50,
                choices=[
                    ('RETAIL', 'Retail Operations'),
                    ('FMS', 'Financial Management'),
                    ('HRM', 'Human Resources'),
                    ('CRM', 'Customer Relationship Management')
                ]
            ),
        ),
    ]
```

**Impact**:
- ✅ Backward compatible (all new fields nullable or have defaults)
- ⚠️ Existing menu items will have default `toolbar_config`

---

### **Phase 3: Extend RolePermission**

**Migration File**: `0003_extend_rolepermission.py`

```python
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    dependencies = [
        ('user_management', '0002_add_erpmenuitem_fields'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        # Update FK reference
        migrations.AlterField(
            model_name='rolepermission',
            name='menu_item',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='role_permissions',
                to='user_management.erpmenuitem'
            ),
        ),
        
        # Add toolbar_override
        migrations.AddField(
            model_name='rolepermission',
            name='toolbar_override',
            field=models.CharField(
                max_length=50,
                null=True,
                blank=True,
                help_text='15-button override'
            ),
        ),
        
        # Add override_enabled
        migrations.AddField(
            model_name='rolepermission',
            name='override_enabled',
            field=models.BooleanField(default=False),
        ),
        
        # Add derived permission flags
        migrations.AddField(
            model_name='rolepermission',
            name='can_authorize',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rolepermission',
            name='can_amend',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rolepermission',
            name='can_print',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rolepermission',
            name='can_upload',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rolepermission',
            name='can_download',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rolepermission',
            name='can_clone',
            field=models.BooleanField(default=False),
        ),
        
        # Add audit fields
        migrations.AddField(
            model_name='rolepermission',
            name='created_by',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='created_role_perms',
                to='auth.user'
            ),
        ),
        migrations.AddField(
            model_name='rolepermission',
            name='updated_by',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='updated_role_perms',
                to='auth.user'
            ),
        ),
    ]
```

**Impact**:
- ✅ Backward compatible
- ✅ Existing data preserved

---

### **Phase 4: Extend UserPermission**

**Migration File**: `0004_extend_userpermission.py`

```python
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    dependencies = [
        ('user_management', '0003_extend_rolepermission'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        # Update FK reference
        migrations.AlterField(
            model_name='userpermission',
            name='menu_item',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='user_permissions',
                to='user_management.erpmenuitem'
            ),
        ),
        
        # Add toolbar_override
        migrations.AddField(
            model_name='userpermission',
            name='toolbar_override',
            field=models.CharField(
                max_length=50,
                null=True,
                blank=True,
                help_text='User-specific 15-button override'
            ),
        ),
        
        # Add derived permission flags
        migrations.AddField(
            model_name='userpermission',
            name='can_authorize',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userpermission',
            name='can_amend',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userpermission',
            name='can_print',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userpermission',
            name='can_upload',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userpermission',
            name='can_download',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userpermission',
            name='can_clone',
            field=models.BooleanField(default=False),
        ),
        
        # Add audit field
        migrations.AddField(
            model_name='userpermission',
            name='updated_by',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='updated_user_perms',
                to='auth.user'
            ),
        ),
    ]
```

**Impact**:
- ✅ Backward compatible
- ✅ Existing data preserved

---

### **Phase 5: Update GroupPermission FK**

**Migration File**: `0005_update_grouppermission_fk.py`

```python
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    dependencies = [
        ('user_management', '0004_extend_userpermission'),
    ]

    operations = [
        # Update FK reference
        migrations.AlterField(
            model_name='grouppermission',
            name='menu_item',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='group_permissions',
                to='user_management.erpmenuitem'
            ),
        ),
    ]
```

**Impact**:
- ✅ Automatic FK update
- ✅ No data loss

---

## ✅ **BENEFITS OF THIS APPROACH**

### **1. Single Source of Truth**
- ✅ `ERPMenuItem.toolbar_config` defines base button availability
- ✅ No hardcoded button logic in frontend

### **2. Flexible Permission Model**
- ✅ UI-level config (ERPMenuItem)
- ✅ Role-level override (RolePermission)
- ✅ User-level override (UserPermission)
- ✅ 3-tier permission hierarchy

### **3. Auto-Derived Permissions**
- ✅ `can_create`, `can_edit`, `can_delete` derived from toolbar
- ✅ `can_authorize`, `can_amend`, `can_print` derived from toolbar
- ✅ No manual permission flag management

### **4. Backward Compatible**
- ✅ Existing `can_access`, `can_view`, `can_create`, `can_edit`, `can_delete` preserved
- ✅ New fields nullable or have defaults
- ✅ Gradual migration possible

### **5. Audit Trail**
- ✅ `created_by`, `updated_by` on all tables
- ✅ Track who changed toolbar configs
- ✅ Track who modified permissions

### **6. Scalable**
- ✅ Works for 10 UIs or 1000 UIs
- ✅ Easy to add new buttons (extend toolbar_config)
- ✅ Easy to add new modules (RETAIL, FMS, HRM, CRM)

---

## 📋 **IMPLEMENTATION CHECKLIST**

### **Backend (Django)**
- [ ] Create migration 0001: Rename MenuItemType → ERPMenuItem
- [ ] Create migration 0002: Add fields to ERPMenuItem
- [ ] Create migration 0003: Extend RolePermission
- [ ] Create migration 0004: Extend UserPermission
- [ ] Create migration 0005: Update GroupPermission FK
- [ ] Run migrations: `python manage.py migrate user_management`
- [ ] Update admin.py to show new fields
- [ ] Create API endpoint: `/api/ui-config/<view_id>/`
- [ ] Implement `derive_permissions_from_toolbar()` utility function
- [ ] Add model save hooks to auto-populate derived permissions

### **Frontend**
- [ ] Create `useToolbarConfig(viewId)` hook
- [ ] Enhance `MasterToolbar` component to use config
- [ ] Update all UI pages to use `useToolbarConfig`
- [ ] Test toolbar button visibility
- [ ] Test role-based overrides
- [ ] Test user-specific overrides

### **Data Seeding**
- [ ] Seed ERPMenuItem records for all 93 Retail UIs
- [ ] Set appropriate `toolbar_config` for each UI type
- [ ] Populate `route_path` and `component_name`
- [ ] Mark system menus with `is_system_menu=True`

### **Testing**
- [ ] Test permission derivation logic
- [ ] Test 3-tier override hierarchy (UI → Role → User)
- [ ] Test toolbar button enabling/disabling
- [ ] Test admin interface for new fields
- [ ] Test API endpoint responses

### **Documentation**
- [ ] Document toolbar config format
- [ ] Document permission derivation logic
- [ ] Document migration steps
- [ ] Update API documentation

---

## 🚀 **ESTIMATED TIMELINE**

| Phase | Task | Estimated Time |
|-------|------|----------------|
| 1 | Create migrations (5 files) | 2 hours |
| 2 | Run migrations + verify | 1 hour |
| 3 | Update admin.py | 1 hour |
| 4 | Create API endpoint | 2 hours |
| 5 | Implement utility functions | 1 hour |
| 6 | Create frontend hook | 1 hour |
| 7 | Enhance MasterToolbar | 2 hours |
| 8 | Seed data (93 UIs) | 2 hours |
| 9 | Testing | 3 hours |
| 10 | Documentation | 1 hour |
| **TOTAL** | | **16 hours** |

---

## ⏳ **NEXT STEPS - AWAITING YOUR APPROVAL**

**Please review this document and provide feedback on:**

1. ✅ **Table structure** - Approve or request changes
2. ✅ **Field names** - Approve or suggest alternatives
3. ✅ **Migration strategy** - Approve phased approach
4. ✅ **Timeline** - Confirm 16-hour estimate acceptable

**Once approved, I will:**
1. Create all 5 migration files
2. Implement utility functions
3. Create API endpoints
4. Update frontend components
5. Seed initial data

---

## 📝 **APPROVAL SIGNATURE**

**Reviewed By**: ________________  
**Date**: ________________  
**Status**: [ ] Approved  [ ] Needs Revision  [ ] Rejected  

**Comments**:
_____________________________________________
_____________________________________________
_____________________________________________

---

**Document Status**: ⏳ PENDING APPROVAL  
**Last Updated**: 2026-01-09 08:01 IST  
**Version**: 1.0
