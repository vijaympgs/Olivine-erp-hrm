# 🎯 TABLE-DRIVEN TOOLBAR CONFIGURATION SYSTEM - DESIGN DOCUMENT

**Created**: 2026-01-09 07:52 IST  
**Author**: Astra  
**Status**: ⏳ AWAITING APPROVAL

---

## 📊 EXECUTIVE SUMMARY

**Objective**: Implement a comprehensive, table-driven toolbar configuration system that:
1. Defines UI-level toolbar button availability (View Master)
2. Enforces role-based button permissions (Role Permissions)
3. Supports dynamic state-based button enabling/disabling
4. Provides complete audit trail

---

## 🏗️ DATABASE DESIGN

### **TABLE 1: VIEW_MASTER_ERP** (UI Configuration)

**Purpose**: Define toolbar configuration for each UI screen

```sql
CREATE TABLE view_master_erp (
    id BIGSERIAL PRIMARY KEY,
    
    -- Identification
    company_id BIGINT NOT NULL REFERENCES business_entities_company(id),
    module VARCHAR(50) NOT NULL,  -- 'RETAIL', 'FMS', 'HRM', 'CRM'
    submodule VARCHAR(50),         -- 'INVENTORY', 'SALES', 'PROCUREMENT', etc.
    view_id VARCHAR(100) NOT NULL UNIQUE,  -- 'ITEM_MASTER', 'SALES_ORDER', 'STOCK_VALUATION_REPORT'
    view_name VARCHAR(200) NOT NULL,       -- 'Item Master', 'Sales Order', 'Stock Valuation Report'
    view_type VARCHAR(20) NOT NULL,        -- 'MASTER', 'TRANSACTION', 'REPORT', 'DASHBOARD'
    
    -- Toolbar Configuration (15 buttons)
    -- Format: "N,E,S,C,L,T,A,V,P,R,D,X,Y,Z,O"
    -- Positions: 0=New, 1=Edit, 2=Save, 3=Cancel, 4=Clear, 5=auThorize, 6=Amend, 
    --            7=View, 8=Print, 9=Refresh, 10=Delete, 11=eXit, 
    --            12=upload(Y), 13=download(Z), 14=clOne
    toolbar_config VARCHAR(50) NOT NULL DEFAULT '0,0,0,0,0,0,0,0,0,0,0,1,0,0,0',
    
    -- Metadata
    route_path VARCHAR(200),       -- '/inventory/item-master'
    component_name VARCHAR(100),   -- 'ItemMasterPage'
    description TEXT,
    display_order INT DEFAULT 0,
    
    -- Status
    is_active BOOLEAN DEFAULT TRUE,
    is_system_view BOOLEAN DEFAULT FALSE,  -- System views cannot be deleted
    
    -- Audit
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by BIGINT REFERENCES auth_user(id),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_by BIGINT REFERENCES auth_user(id),
    
    -- Constraints
    UNIQUE(company_id, view_id),
    CHECK (toolbar_config ~ '^[01](,[01]){14}$')  -- Validate format
);

CREATE INDEX idx_view_master_company ON view_master_erp(company_id);
CREATE INDEX idx_view_master_module ON view_master_erp(module, submodule);
CREATE INDEX idx_view_master_type ON view_master_erp(view_type);
CREATE INDEX idx_view_master_active ON view_master_erp(is_active);
```

---

### **TABLE 2: ROLE_TOOLBAR_PERMISSIONS** (Role-Based Overrides)

**Purpose**: Override toolbar permissions per role (inherits from view_master_erp)

**Approach**: Extend existing `RolePermission` model

```sql
-- MODIFY EXISTING TABLE: role_permissions
ALTER TABLE role_permissions ADD COLUMN toolbar_override VARCHAR(50) NULL;
ALTER TABLE role_permissions ADD COLUMN override_enabled BOOLEAN DEFAULT FALSE;
ALTER TABLE role_permissions ADD CONSTRAINT chk_toolbar_override 
    CHECK (toolbar_override IS NULL OR toolbar_override ~ '^[01](,[01]){14}$');

-- Add comment
COMMENT ON COLUMN role_permissions.toolbar_override IS 
    'Toolbar button override config (15 buttons): N,E,S,C,L,T,A,V,P,R,D,X,Y,Z,O. 
     If NULL, inherits from view_master_erp. If set, overrides view_master config.';
```

**Alternative**: Create new table (cleaner separation)

```sql
CREATE TABLE role_toolbar_permissions (
    id BIGSERIAL PRIMARY KEY,
    
    -- References
    role_id BIGINT NOT NULL REFERENCES roles(id) ON DELETE CASCADE,
    view_id VARCHAR(100) NOT NULL,  -- Links to view_master_erp.view_id
    
    -- Toolbar Override (15 buttons)
    -- Format: "N,E,S,C,L,T,A,V,P,R,D,X,Y,Z,O"
    -- 1 = Allowed, 0 = Denied (overrides view_master_erp)
    toolbar_override VARCHAR(50) NOT NULL,
    
    -- Control
    override_enabled BOOLEAN DEFAULT TRUE,
    
    -- Audit
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by BIGINT REFERENCES auth_user(id),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_by BIGINT REFERENCES auth_user(id),
    
    -- Constraints
    UNIQUE(role_id, view_id),
    CHECK (toolbar_override ~ '^[01](,[01]){14}$')
);

CREATE INDEX idx_role_toolbar_role ON role_toolbar_permissions(role_id);
CREATE INDEX idx_role_toolbar_view ON role_toolbar_permissions(view_id);
```

---

## 🎨 BUTTON CONFIGURATION MAPPING

### **15-Button Toolbar Configuration**

| Position | Code | Button | Action | F-Key | Use Case |
|----------|------|--------|--------|-------|----------|
| 0 | **N** | New | `new` | F2 | Create new record |
| 1 | **E** | Edit | `edit` | F4 | Edit existing record |
| 2 | **S** | Save | `save` | F8 | Save changes |
| 3 | **C** | Cancel | `cancel` | ESC | Cancel operation |
| 4 | **L** | Clear | `clear` | F5 | Clear form |
| 5 | **T** | auThorize | `authorize` | F10 | Approve/Authorize |
| 6 | **A** | Amend | `amend` | F11 | Amend authorized doc |
| 7 | **V** | View | `view` | F7 | View details |
| 8 | **P** | Print | `print` | Ctrl+P | Print document |
| 9 | **R** | Refresh | `refresh` | F9 | Reload data |
| 10 | **D** | Delete | `delete` | F3 | Delete record |
| 11 | **X** | eXit | `exit` | ESC | Close/Exit |
| 12 | **Y** | upload (Y) | `upload` | F6 | Import/Upload |
| 13 | **Z** | download (Z) | `download` | Ctrl+D | Export/Download |
| 14 | **O** | clOne | `clone` | Ctrl+Shift+C | Duplicate record |

---

## 📋 CONFIGURATION EXAMPLES

### **Example 1: Item Master (MASTER UI)**
```
View ID: ITEM_MASTER
View Type: MASTER
Toolbar Config: "1,1,1,1,1,0,0,1,1,1,1,1,1,1,1"
                 N E S C L T A V P R D X Y Z O
                 ✓ ✓ ✓ ✓ ✓ ✗ ✗ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓

Enabled: New, Edit, Save, Cancel, Clear, View, Print, Refresh, Delete, Exit, Upload, Download, Clone
Disabled: Authorize, Amend (not applicable for master data)
```

### **Example 2: Sales Order (TRANSACTION UI)**
```
View ID: SALES_ORDER
View Type: TRANSACTION
Toolbar Config: "1,1,1,1,1,1,1,1,1,1,1,1,0,1,1"
                 N E S C L T A V P R D X Y Z O
                 ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✗ ✓ ✓

Enabled: All except Upload (Y)
Disabled: Upload (bulk upload not allowed for transactions)
```

### **Example 3: Stock Valuation Report (REPORT UI)**
```
View ID: STOCK_VALUATION_REPORT
View Type: REPORT
Toolbar Config: "0,0,0,0,0,0,0,0,1,1,0,1,0,1,0"
                 N E S C L T A V P R D X Y Z O
                 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✓ ✗ ✓ ✗ ✓ ✗

Enabled: Print, Refresh, Exit, Download
Disabled: All CRUD operations (read-only report)
```

### **Example 4: Inventory Dashboard (DASHBOARD UI)**
```
View ID: INVENTORY_DASHBOARD
View Type: DASHBOARD
Toolbar Config: "0,0,0,0,0,0,0,0,0,1,0,1,0,0,0"
                 N E S C L T A V P R D X Y Z O
                 ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✗ ✓ ✗ ✓ ✗ ✗ ✗

Enabled: Refresh, Exit only
Disabled: All other operations (view-only dashboard)
```

---

## 🔐 ROLE-BASED PERMISSION LOGIC

### **Permission Resolution Flow**

```
1. Load View Config from view_master_erp
   ↓
2. Check if Role has toolbar_override in role_toolbar_permissions
   ↓
3. If override exists AND override_enabled = TRUE:
      Use toolbar_override
   Else:
      Use view_master_erp.toolbar_config
   ↓
4. Apply Mode-Based State Rules (VIEW/EDIT/CREATE)
   ↓
5. Render Toolbar with final button states
```

### **Example: Role Override**

**Scenario**: POS User should NOT be able to Delete items in Item Master

**View Config** (ITEM_MASTER):
```
toolbar_config: "1,1,1,1,1,0,0,1,1,1,1,1,1,1,1"
                                      ↑ Delete=1 (allowed)
```

**Role Override** (POS User):
```sql
INSERT INTO role_toolbar_permissions (role_id, view_id, toolbar_override)
VALUES (
    (SELECT id FROM roles WHERE role_key = 'posuser'),
    'ITEM_MASTER',
    '1,1,1,1,1,0,0,1,1,1,0,1,1,1,1'  -- Delete=0 (denied)
);
```

**Result**: POS User sees Delete button disabled in Item Master

---

## 🎯 STATE-BASED BUTTON LOGIC

### **Mode Transition Rules**

```typescript
// State machine for button enabling/disabling
const MODE_RULES = {
    VIEW: {
        // After page load or Save/Cancel
        enabled: ['new', 'edit', 'view', 'print', 'refresh', 'delete', 'exit', 'download', 'clone']
    },
    EDIT: {
        // After Edit button clicked
        enabled: ['save', 'cancel', 'clear', 'refresh']
    },
    CREATE: {
        // After New button clicked
        enabled: ['save', 'cancel', 'clear', 'refresh']
    },
    AUTHORIZE: {
        // After Authorize button clicked
        enabled: ['exit', 'print', 'view']
    }
};
```

---

## 🔧 IMPLEMENTATION COMPONENTS

### **1. Django Models**

```python
# File: core/auth_access/backend/user_management/models.py

class ViewMasterERP(models.Model):
    """UI View Configuration with Toolbar Settings"""
    
    # Identification
    company = models.ForeignKey('business_entities.Company', on_delete=models.CASCADE)
    module = models.CharField(max_length=50)  # RETAIL, FMS, HRM, CRM
    submodule = models.CharField(max_length=50, null=True, blank=True)
    view_id = models.CharField(max_length=100, unique=True, db_index=True)
    view_name = models.CharField(max_length=200)
    view_type = models.CharField(max_length=20, choices=[
        ('MASTER', 'Master Data'),
        ('TRANSACTION', 'Transaction'),
        ('REPORT', 'Report'),
        ('DASHBOARD', 'Dashboard')
    ])
    
    # Toolbar Configuration (15 buttons: N,E,S,C,L,T,A,V,P,R,D,X,Y,Z,O)
    toolbar_config = models.CharField(
        max_length=50,
        default='0,0,0,0,0,0,0,0,0,0,0,1,0,0,0',
        help_text='15-button config: N,E,S,C,L,T,A,V,P,R,D,X,Y,Z,O'
    )
    
    # Metadata
    route_path = models.CharField(max_length=200, null=True, blank=True)
    component_name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    display_order = models.IntegerField(default=0)
    
    # Status
    is_active = models.BooleanField(default=True)
    is_system_view = models.BooleanField(default=False)
    
    # Audit
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='created_views')
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='updated_views')
    
    class Meta:
        db_table = 'view_master_erp'
        unique_together = [['company', 'view_id']]
        verbose_name = 'View Master'
        verbose_name_plural = 'View Masters'
        ordering = ['module', 'submodule', 'display_order']
    
    def __str__(self):
        return f"{self.view_name} ({self.view_id})"


class RoleToolbarPermission(models.Model):
    """Role-specific toolbar button overrides"""
    
    role = models.ForeignKey('Role', on_delete=models.CASCADE, related_name='toolbar_permissions')
    view_id = models.CharField(max_length=100, db_index=True)
    
    # Toolbar Override (15 buttons)
    toolbar_override = models.CharField(
        max_length=50,
        help_text='15-button override: N,E,S,C,L,T,A,V,P,R,D,X,Y,Z,O'
    )
    
    override_enabled = models.BooleanField(default=True)
    
    # Audit
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='updated_toolbar_perms')
    
    class Meta:
        db_table = 'role_toolbar_permissions'
        unique_together = [['role', 'view_id']]
        verbose_name = 'Role Toolbar Permission'
        verbose_name_plural = 'Role Toolbar Permissions'
    
    def __str__(self):
        return f"{self.role.role_name} - {self.view_id}"
```

---

### **2. API Endpoints**

```python
# File: core/auth_access/backend/user_management/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_view_config(request, view_id):
    """
    Get toolbar configuration for a specific view
    Applies role-based overrides if applicable
    """
    user = request.user
    company_id = request.GET.get('company_id')
    
    # Get base view config
    view_config = ViewMasterERP.objects.get(
        view_id=view_id,
        company_id=company_id,
        is_active=True
    )
    
    # Get user's roles
    user_roles = UserRole.objects.filter(user=user, is_active=True).values_list('role_id', flat=True)
    
    # Check for role-based toolbar override
    toolbar_override = RoleToolbarPermission.objects.filter(
        role_id__in=user_roles,
        view_id=view_id,
        override_enabled=True
    ).first()
    
    # Use override if exists, otherwise use base config
    toolbar_config = toolbar_override.toolbar_override if toolbar_override else view_config.toolbar_config
    
    return Response({
        'view_id': view_config.view_id,
        'view_name': view_config.view_name,
        'view_type': view_config.view_type,
        'toolbar_config': toolbar_config,
        'has_override': toolbar_override is not None
    })
```

---

### **3. Frontend Hook**

```typescript
// File: frontend/src/hooks/useToolbarConfig.ts

import { useState, useEffect } from 'react';
import { useAuth } from '@auth/useAuth';

export interface ToolbarConfig {
    viewId: string;
    viewName: string;
    viewType: string;
    toolbarConfig: string;
    hasOverride: boolean;
}

export function useToolbarConfig(viewId: string) {
    const { user } = useAuth();
    const [config, setConfig] = useState<ToolbarConfig | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        async function fetchConfig() {
            try {
                const response = await fetch(
                    `/api/ui-config/${viewId}/?company_id=${user?.currentCompanyId}`
                );
                const data = await response.json();
                setConfig(data);
            } catch (error) {
                console.error('Failed to load toolbar config:', error);
            } finally {
                setLoading(false);
            }
        }

        if (viewId && user?.currentCompanyId) {
            fetchConfig();
        }
    }, [viewId, user?.currentCompanyId]);

    return { config, loading };
}
```

---

## 📊 SEED DATA EXAMPLES

```sql
-- Master Data UIs
INSERT INTO view_master_erp (company_id, module, submodule, view_id, view_name, view_type, toolbar_config, route_path, is_system_view) VALUES
(1, 'RETAIL', 'INVENTORY', 'ITEM_MASTER', 'Item Master', 'MASTER', '1,1,1,1,1,0,0,1,1,1,1,1,1,1,1', '/inventory/item-master', TRUE),
(1, 'RETAIL', 'PARTNERS', 'CUSTOMER_MASTER', 'Customer Master', 'MASTER', '1,1,1,1,1,0,0,1,1,1,1,1,1,1,1', '/partners/customers', TRUE),
(1, 'RETAIL', 'PARTNERS', 'SUPPLIER_MASTER', 'Supplier Master', 'MASTER', '1,1,1,1,1,0,0,1,1,1,1,1,1,1,1', '/partners/suppliers', TRUE);

-- Transaction UIs
INSERT INTO view_master_erp (company_id, module, submodule, view_id, view_name, view_type, toolbar_config, route_path, is_system_view) VALUES
(1, 'RETAIL', 'SALES', 'SALES_ORDER', 'Sales Order', 'TRANSACTION', '1,1,1,1,1,1,1,1,1,1,1,1,0,1,1', '/sales/orders', TRUE),
(1, 'RETAIL', 'PROCUREMENT', 'PURCHASE_ORDER', 'Purchase Order', 'TRANSACTION', '1,1,1,1,1,1,1,1,1,1,1,1,0,1,1', '/procurement/purchase-orders', TRUE);

-- Report UIs
INSERT INTO view_master_erp (company_id, module, submodule, view_id, view_name, view_type, toolbar_config, route_path, is_system_view) VALUES
(1, 'RETAIL', 'INVENTORY', 'STOCK_VALUATION_REPORT', 'Stock Valuation Report', 'REPORT', '0,0,0,0,0,0,0,0,1,1,0,1,0,1,0', '/inventory/reports/valuation', TRUE),
(1, 'RETAIL', 'INVENTORY', 'MOVEMENT_REPORT', 'Movement Report', 'REPORT', '0,0,0,0,0,0,0,0,1,1,0,1,0,1,0', '/inventory/reports/movements', TRUE);

-- Dashboard UIs
INSERT INTO view_master_erp (company_id, module, submodule, view_id, view_name, view_type, toolbar_config, route_path, is_system_view) VALUES
(1, 'RETAIL', 'INVENTORY', 'INVENTORY_DASHBOARD', 'Inventory Dashboard', 'DASHBOARD', '0,0,0,0,0,0,0,0,0,1,0,1,0,0,0', '/inventory/dashboard', TRUE),
(1, 'RETAIL', 'SALES', 'SALES_DASHBOARD', 'Sales Dashboard', 'DASHBOARD', '0,0,0,0,0,0,0,0,0,1,0,1,0,0,0', '/sales/dashboard', TRUE);
```

---

## ✅ BENEFITS OF THIS APPROACH

1. **✅ Centralized Configuration**: Single source of truth for all UI toolbar settings
2. **✅ Role-Based Security**: Fine-grained control per role
3. **✅ Flexible**: Easy to add new buttons or modify existing configs
4. **✅ Auditable**: Complete trail of who changed what and when
5. **✅ Scalable**: Works for 10 UIs or 1000 UIs
6. **✅ Maintainable**: No code changes needed for config updates
7. **✅ Enterprise-Grade**: Matches SAP/Oracle ERP patterns

---

## 🚀 IMPLEMENTATION TIMELINE

| Phase | Task | Estimated Time |
|-------|------|----------------|
| 1 | Create Django models + migrations | 2 hours |
| 2 | Create API endpoints | 2 hours |
| 3 | Enhance MasterToolbar component | 3 hours |
| 4 | Create useToolbarConfig hook | 1 hour |
| 5 | Seed initial data (93 UIs) | 2 hours |
| 6 | Update existing UIs to use hook | 4 hours |
| 7 | Testing + Documentation | 2 hours |
| **TOTAL** | | **16 hours** |

---

## 📝 NEXT STEPS

**Awaiting your approval, Viji:**

1. ✅ Approve this design
2. ✅ Confirm table names and structure
3. ✅ Proceed with implementation

**Ready to execute upon your directive.** 🎯

---

**Document Status**: ⏳ PENDING APPROVAL  
**Last Updated**: 2026-01-09 07:52 IST
