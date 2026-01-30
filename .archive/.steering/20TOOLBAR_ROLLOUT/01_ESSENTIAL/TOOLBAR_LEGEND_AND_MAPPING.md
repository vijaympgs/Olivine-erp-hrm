# 🎯 TOOLBAR LEGEND & UI MAPPING

**Single Source of Truth for Toolbar Configuration**  
**Last Updated**: 2026-01-09 18:53 IST

---

## ⚠️ CRITICAL: ARCHITECTURE CLARIFICATION

### **🎯 SINGLE-ENTRY-PER-SCREEN RULE**

**IMPORTANT**: Each screen has **ONE** entry in `ERPMenuItem`, NOT separate entries for "List View" and "Form View"!

---

### **❌ WRONG APPROACH (DO NOT DO THIS)**:
```
ERPMenuItem Entry #1:
  menu_id: "purchase-orders"
  view_type: "LIST_VIEW"  ← WRONG! Don't create this!
  config: "NRQFX"

ERPMenuItem Entry #2:
  menu_id: "PURCHASE_ORDERS"
  view_type: "TRANSACTION"
  config: "NESCKZTJAVPMRDX1234QF"
```

### **✅ CORRECT APPROACH (DO THIS)**:
```
ERPMenuItem (Single Entry):
  menu_id: "PURCHASE_ORDERS"
  view_type: "TRANSACTION"
  config: "NESCKZTJAVPMRDX1234QF"
  
Frontend handles BOTH pages:
  - List page: Uses same config with mode="VIEW"
  - Form page: Uses same config with mode="VIEW|CREATE|EDIT"
```

---

## 📋 **TWO DIFFERENT CONCEPTS**

### **1️⃣ SCREEN TYPE** (Backend - ERPMenuItem.view_type)
What kind of screen this is in the database:

- **MASTER** = Master data screens
  - Example: Item Master, Customer Master, UOM Setup
  - Config: `NESCKVDXRQFIO` (Advanced) or `NESCKVDXRQF` (Simple)
  
- **TRANSACTION** = Transaction/document screens
  - Example: Purchase Order, Sales Order, Invoice
  - Config: `NESCKZTJAVPMRDX1234QF`

- **REPORT** = Report/analysis screens
  - Example: Stock Valuation, Sales Analysis
  - Config: `VRXPYQFG`

- **DASHBOARD** = Dashboard screens
  - Example: Inventory Dashboard, Sales Dashboard
  - Config: Custom

- **CONFIGURATION** = Settings/config screens
  - Example: Company Settings, System Parameters
  - Config: `ESCKXR`

### **2️⃣ UI MODE** (Frontend - MasterToolbar mode prop)
What state the UI is currently in:

- **VIEW Mode** = Reading/viewing records (list or single)
  - List page: Shows New, Refresh, Search, Filter, Exit
  - Form page: Shows Edit, Delete, Print, Authorize, etc.
  - Hides: Save, Cancel, Clear
  
- **CREATE Mode** = Creating a new record
  - Shows: Save, Cancel, Clear, Exit
  - Hides: New, Edit, Delete, Print, etc.
  
- **EDIT Mode** = Editing an existing record
  - Shows: Save, Cancel, Clear, Exit
  - Hides: New, Edit, Delete, Print, etc.

---

## 🎯 **EXAMPLE: PURCHASE ORDER**

### **Backend (Single Entry)**:
```json
{
  "menu_id": "PURCHASE_ORDERS",
  "view_type": "TRANSACTION",
  "config": "NESCKZTJAVPMRDX1234QF"
}
```

### **Frontend Usage**:

**List Page** (`/procurement/purchase-orders`):
```typescript
<MasterToolbar 
  viewId="PURCHASE_ORDERS" 
  mode="VIEW"  // Always VIEW for list pages
/>
// Shows: N, E, R, Q, F, X (subset of full config)
```

**Form Page - Viewing** (`/procurement/orders/123`):
```typescript
<MasterToolbar 
  viewId="PURCHASE_ORDERS" 
  mode="VIEW"
/>
// Shows: E, D, P, M, Z, T, J, A, etc. (different subset)
```

**Form Page - Creating** (`/procurement/orders/new`):
```typescript
<MasterToolbar 
  viewId="PURCHASE_ORDERS" 
  mode="CREATE"
/>
// Shows: S, C, K, X
```

**Form Page - Editing** (`/procurement/orders/123/edit`):
```typescript
<MasterToolbar 
  viewId="PURCHASE_ORDERS" 
  mode="EDIT"
/>
// Shows: S, C, K, X
```

---

## 📊 **DJANGO ADMIN vs HTML EXPLORER**

| Field | Django Admin | HTML Explorer | Meaning |
|-------|--------------|---------------|---------|
| **Menu ID** | PURCHASE_ORDERS | PURCHASE_ORDERS | Database identifier |
| **View Type** | TRANSACTION | TRANSACTION | **SCREEN TYPE** (not UI mode!) |
| **Config** | NESCKZTJAVPMRDX1234QF | NESCKZTJAVPMRDX1234QF | Full config string |
| **Route** | /procurement/orders | /procurement/orders | Primary route |

**HTML Explorer ALSO shows**:
- **Total Actions**: All 21 buttons in the config
- **VIEW Mode**: Which buttons show when viewing (18 buttons)
- **CREATE Mode**: Which buttons show when creating (4 buttons)

---

## ✅ **CROSS-CHECKING MADE EASY**

1. **Open HTML Explorer** → Click "Purchase Order"
2. **Note Menu ID**: `PURCHASE_ORDERS`
3. **Open Django Admin** → Search: `PURCHASE_ORDERS`
4. **Compare**: All fields should match!
5. **Verify**: Should see ONLY ONE entry, not separate "List View" entry

---

## 📋 QUICK REFERENCE TABLE

| Screen Type | Config String | Description | Examples |
|-------------|---------------|-------------|----------|
| **Masters (Simple)** | `NESCKVDXRQF` | Basic CRUD | UOM, Brands, Categories, Tax Classes |
| **Masters (Advanced)** | `NESCKVDXRQFIO` | With Import/Export | Item Master, Customers, Suppliers |
| **Transactions** | `NESCKZTJAVPMRDX1234QF` | Full Workflow | Purchase Orders, Sales Orders, Invoices |
| **Reports** | `VRXPYQFG` | Read-only | Stock Valuation, Sales Analysis |
| **Configuration** | `ESCKXR` | Edit-only | Company Settings, System Parameters |
| **Transaction (Simple)** | `NESCKVDXRQF` | No Approval | Stock Adjustments, Stock Transfers |

**Note**: List pages use the same config as their parent screen with `mode="VIEW"`

---

## 🔤 COMPLETE CHARACTER CODE LEGEND

| Code | Action | Shortcut | Icon | Color | Group |
|------|--------|----------|------|-------|-------|
| **N** | New | F2 | ➕ | Blue | CRUD |
| **E** | Edit | F3 | ✏️ | Blue | CRUD |
| **S** | Save | F8 | 💾 | Green | CRUD |
| **C** | Cancel | Esc | ❌ | Gray | CRUD |
| **K** | Clear/Reset | F5 | 🔄 | Amber | CRUD |
| **V** | View | F7 | 👁️ | Indigo | CRUD |
| **D** | Delete | F4 | 🗑️ | Red | CRUD |
| **X** | Exit | Esc | 🚪 | Gray | Navigation |
| **R** | Refresh | F9 | 🔃 | Cyan | Navigation |
| **Q** | Search | Ctrl+F | 🔍 | Gray | Navigation |
| **F** | Filter | Alt+F | ⚡ | Gray | Navigation |
| **I** | Import | Ctrl+I | ⬆️ | Violet | Data |
| **O** | Export | Ctrl+E | ⬇️ | Indigo | Data |
| **Y** | Export (Alt) | Ctrl+E | ⬇️ | Indigo | Data |
| **L** | Clone | Ctrl+Shift+C | 📋 | Blue | Data |
| **Z** | Authorize | F10 | ✅ | Green | Workflow |
| **T** | Submit | Alt+S | 📤 | Blue | Workflow |
| **J** | Reject | Alt+R | 🚫 | Red | Workflow |
| **A** | Amend | Alt+A | 📝 | Orange | Workflow |
| **H** | Hold | Alt+H | ⏸️ | Yellow | Workflow |
| **W** | Void | Alt+V | ⛔ | Red | Workflow |
| **P** | Print | Ctrl+P | 🖨️ | Purple | Document |
| **M** | Email | Ctrl+M | 📧 | Sky | Document |
| **1** | First | Home | ⏮️ | Gray | Navigation |
| **2** | Prev | PgUp | ◀️ | Gray | Navigation |
| **3** | Next | PgDn | ▶️ | Gray | Navigation |
| **4** | Last | End | ⏭️ | Gray | Navigation |
| **B** | Notes | Alt+N | 📝 | Yellow | Tools |
| **G** | Attach | Alt+U | 📎 | Gray | Tools |
| **?** | Help | F1 | ❓ | Blue | Tools |

---

## 🗺️ RETAIL MODULE UI MAPPING

### **Inventory Module**

| Screen | Type | Config | Status |
|--------|------|--------|--------|
| UOM Setup | Masters (Simple) | `NESCKVDXRQF` | ✅ COMPLETE |
| Reason Codes | Masters (Simple) | `NESCKVDXRQF` | ✅ COMPLETE |
| Item Master | Masters (Advanced) | `NESCKVDXRQFIO` | ✅ COMPLETE |
| Categories | Masters (Simple) | `NESCKVDXRQF` | ✅ COMPLETE |
| Brands | Masters (Simple) | `NESCKVDXRQF` | ✅ COMPLETE |
| Attributes | Masters (Simple) | `NESCKVDXRQF` | ✅ COMPLETE |
| Stock Valuation | Reports | `VRXPYQFG` | ✅ COMPLETE |
| Stock Adjustment | Transaction (Simple) | `NESCKVDXRQF` | ✅ COMPLETE |

### **Procurement Module**

| Screen | Type | Config | Status |
|--------|------|--------|--------|
| Purchase Requisition | Transactions | `NESCKZTJAVPMRDX1234QF` | ✅ COMPLETE |
| Purchase Order | Transactions | `NESCKZTJAVPMRDX1234QF" | ✅ COMPLETE |
| Supplier Master | Masters (Advanced) | `NESCKVDXRQFIO` | ✅ COMPLETE |
| Goods Receipt | Transactions | `NESCKZTJAVPMRDX1234QF` | ✅ COMPLETE |

### **Sales Module**

| Screen | Type | Config | Status |
|--------|------|--------|--------|
| Sales Order | Transactions | `NESCKZTJAVPMRDX1234QF` | ✅ COMPLETE |
| Sales Invoice | Transactions | `NESCKZTJAVPMRDX1234QF` | ✅ COMPLETE |
| Sales Quote | Transactions | `NESCKZTJAVPMRDX1234QF` | ✅ COMPLETE |
| Customer Master | Masters (Advanced) | `NESCKVDXRQFIO` | ✅ COMPLETE |

### **POS Module**

| Screen | Type | Config | Status |
|--------|------|--------|--------|
| POS Day Open/Close | List View | `NRQFX` | ✅ COMPLETE |
| POS Settlement | List View | `NRQFX` | ✅ COMPLETE |
| POS Billing | Transaction | `NESCKVDXRQFZTJAHO` | ⚠️ EXCLUDED |

---

## 🛠️ THE "GOLDEN RULE" FOR CONFIGURATIONS

### **🎯 ONE ENTRY PER SCREEN**

**Critical Rule**: Each screen has **ONE** entry in `ERPMenuItem` with **ONE** configuration string.

### **How It Works**:

1. **Backend (ERPMenuItem)**:
   - Create ONE entry per screen
   - Set the FULL configuration string (e.g., `NESCKZTJAVPMRDX1234QF`)
   - Example: Purchase Order has ONE entry with `view_type: TRANSACTION`

2. **Frontend (MasterToolbar)**:
   - **List Page**: Uses same `viewId`, sets `mode="VIEW"`
   - **Form Page**: Uses same `viewId`, sets `mode` based on state (VIEW/CREATE/EDIT)
   
3. **MasterToolbar Component**:
   - Takes the FULL config string from backend
   - Filters buttons based on `mode` prop
   - **VIEW mode**: Hides S, C, K (Save, Cancel, Clear)
   - **CREATE/EDIT mode**: Hides N, E, V, D, R, etc. (New, Edit, View, Delete, Refresh)

### **Example: Purchase Orders**

**Backend (Single Entry)**:
```json
{
  "menu_id": "PURCHASE_ORDERS",
  "view_type": "TRANSACTION",
  "config": "NESCKZTJAVPMRDX1234QF"
}
```

**Frontend Usage**:
```typescript
// List page (/procurement/purchase-orders)
<MasterToolbar viewId="PURCHASE_ORDERS" mode="VIEW" />
// Shows: N, E, R, Q, F, X (subset for list view)

// Form page - viewing (/procurement/orders/123)
<MasterToolbar viewId="PURCHASE_ORDERS" mode="VIEW" />
// Shows: E, D, P, M, Z, T, J, A, etc. (subset for form view)

// Form page - creating (/procurement/orders/new)
<MasterToolbar viewId="PURCHASE_ORDERS" mode="CREATE" />
// Shows: S, C, K, X

// Form page - editing (/procurement/orders/123/edit)
<MasterToolbar viewId="PURCHASE_ORDERS" mode="EDIT" />
// Shows: S, C, K, X
```

### **✅ Benefits**:
- No duplicate entries in database
- No risk of accidentally deactivating list view
- Single source of truth per screen
- Frontend controls button visibility based on context

---

## 🎨 MODE-BASED VISIBILITY RULES

### **1. VIEW Mode** (Looking at a record)
*   **Logical Goal**: Allow navigation, workflow actions, and data operations.
*   **Included Chars**: `N`, `E`, `V`, `P`, `M`, `R`, `D`, `Y`, `I`, `Q`, `F`, `1,2,3,4`, `Z,T,J,H,O,A,W`, `?`, `X`

### **2. CREATE / EDIT Mode** (Modifying a record)
*   **Logical Goal**: Focus purely on saving or cancelling the current action.
*   **Included Chars**: `S`, `C`, `K`, `X`, `?`, `B`, `G` (Notes/Attach)
*   **Hidden Chars**: All others (Edit, Delete, Workflow, Navigation) are hidden to prevent data corruption.

---

## 📊 CONFIGURATION BREAKDOWN

### Masters (Simple): `NESCKVDXRQF`
```
N - New (F2)
E - Edit (F3)
S - Save (F8)
C - Cancel (Esc)
K - Clear (F5)
V - View (F7)
D - Delete (F4)
X - Exit (Esc)
R - Refresh (F9)
Q - Search (Ctrl+F)
F - Filter (Alt+F)
```

### Masters (Advanced): `NESCKVDXRQFIO`
```
All from Masters (Simple) PLUS:
I - Import (Ctrl+I)
O - Export (Ctrl+E)
```

### Transactions: `NESCKZTJAVPMRDX1234QF`
```
N - New (F2)
E - Edit (F3)
S - Save (F8)
C - Cancel (Esc)
K - Clear (F5)
Z - Authorize (F10)
T - Submit (Alt+S)
J - Reject (Alt+R)
A - Amend (Alt+A)
V - View (F7)
P - Print (Ctrl+P)
M - Email (Ctrl+M)
R - Refresh (F9)
D - Delete (F4)
X - Exit (Esc)
1 - First (Home)
2 - Prev (PgUp)
3 - Next (PgDn)
4 - Last (End)
Q - Search (Ctrl+F)
F - Filter (Alt+F)
```

### Reports: `VRXPYQFG`
```
V - View (F7)
R - Refresh (F9)
X - Exit (Esc)
P - Print (Ctrl+P)
Y - Export (Ctrl+E)
Q - Search (Ctrl+F)
F - Filter (Alt+F)
G - Settings (Alt+O)
```

### Configuration: `ESCKXR`
```
E - Edit (F3)
S - Save (F8)
C - Cancel (Esc)
K - Clear (F5)
X - Exit (Esc)
R - Refresh (F9)
```

---

**Status**: ⚡ ACTIVE AUTHORITY  
**Owner**: Astra (ERP Platform Development)
