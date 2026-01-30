# 🎯 TOOLBAR CONFIGURATION GUIDE (Practical Reference)

**Purpose**: Quick reference to determine the correct `applicable_toolbar_config` string for any screen  
**Last Updated**: 2026-01-09  
**Status**: ⚡ ACTIVE AUTHORITY

---

## 📋 QUICK DECISION TREE

```
Is it a Master Data screen (UOM, Item, Customer, Supplier)?
├─ YES → Is it simple (just list + basic CRUD)?
│  ├─ YES → Use "Masters (Simple)" → NESCKVDXRQF
│  └─ NO → Use "Masters (Advanced)" → NESCKVDXRQFIO (adds Import/Export)
│
└─ NO → Is it a Transaction (PO, SO, Invoice)?
   ├─ YES → Use "Transactions" → NESCKZTJAVPMRDX1234QF
   │
   └─ NO → Is it a Report/Dashboard?
      └─ YES → Use "Reports" → VRXPYQFG

```

---

## 🔤 COMPLETE CHARACTER CODE REFERENCE

| Code | Action | Shortcut | Description | Used In |
|------|--------|----------|-------------|---------|
| **N** | New | F2 | Create new record | Masters, Transactions |
| **E** | Edit | F3 | Edit selected record | Masters, Transactions |
| **S** | Save | F8 | Save changes | Masters, Transactions |
| **C** | Cancel | Esc | Cancel operation | Masters, Transactions |
| **K** | Clear/Reset | F5 | Clear form/filters | Masters, Transactions |
| **V** | View | F7 | View details | Masters (Advanced), Reports |
| **D** | Delete | F4 | Delete record | Masters |
| **X** | Exit | Esc | Exit page | All |
| **R** | Refresh | F9 | Reload data | All |
| **Q** | Search | Ctrl+F | Focus search | All |
| **F** | Filter | Alt+F | Toggle filter panel | Masters, Reports |
| **I** | Import | Ctrl+I | Upload data | Masters (Advanced) |
| **O** | Export | Ctrl+E | Download data | Masters (Advanced), Reports |
| **Y** | Export (Alt) | Ctrl+E | Download data | Reports |
| **L** | Clone | Ctrl+Shift+C | Duplicate record | Transactions |
| **P** | Print | Ctrl+P | Print document | Transactions, Reports |
| **M** | Email | Ctrl+M | Email document | Transactions, Reports |
| **T** | Submit | Alt+S | Submit for approval | Transactions |
| **J** | Reject | Alt+R | Reject document | Transactions |
| **Z** | Authorize | F10 | Approve document | Transactions |
| **A** | Amend | Alt+A | Modify approved doc | Transactions |
| **H** | Hold | Alt+H | Suspend transaction | Transactions |
| **W** | Void | Alt+V | Annul document | Transactions |
| **1** | First | Home | First record | Transactions |
| **2** | Prev | PgUp | Previous record | Transactions |
| **3** | Next | PgDn | Next record | Transactions |
| **4** | Last | End | Last record | Transactions |
| **B** | Notes | Alt+N | Internal notes | Optional |
| **G** | Attach | Alt+U | File attachments | Optional |
| **?** | Help | F1 | Context help | Optional |

---

## 📦 READY-TO-USE CONFIGURATIONS

### 1️⃣ **Masters (Simple)**
**Examples**: UOM, Brands, Categories, Tax Classes, Payment Methods, Reason Codes

**Config String**: `NESCKVDXRQF`

**Breakdown**:
- `N` - New (F2)
- `E` - Edit (F3)
- `S` - Save (F8)
- `C` - Cancel (Esc)
- `K` - Clear (F5)
- `V` - View (F7)
- `D` - Delete (F4)
- `X` - Exit (Esc)
- `R` - Refresh (F9)
- `Q` - Search (Ctrl+F)
- `F` - Filter (Alt+F)

**When to Use**:
- ✅ Simple lookup tables
- ✅ Configuration data
- ✅ No import/export needed
- ✅ No complex workflows

---

### 2️⃣ **Masters (Advanced)**
**Examples**: Item Master, Customers, Suppliers, Locations

**Config String**: `NESCKVDXRQFIO`

**Breakdown**:
- All from "Masters (Simple)" PLUS:
- `I` - Import (Ctrl+I) - Bulk upload
- `O` - Export (Ctrl+E) - Bulk download

**When to Use**:
- ✅ Large datasets
- ✅ Bulk operations needed
- ✅ Data migration required
- ✅ Excel integration needed

**Optional Additions**:
- Add `L` for Clone if duplication is common
- Add `B` for Notes if comments are needed
- Add `G` for Attachments if files are needed

---

### 3️⃣ **Transactions (Standard)**
**Examples**: Purchase Orders, Sales Orders, Invoices, Goods Receipts

**Config String**: `NESCKZTJAVPMRDX1234QF`

**Breakdown**:
- `N` - New (F2)
- `E` - Edit (F3)
- `S` - Save (F8)
- `C` - Cancel (Esc)
- `K` - Clear (F5)
- `Z` - Authorize (F10)
- `T` - Submit (Alt+S)
- `J` - Reject (Alt+R)
- `A` - Amend (Alt+A)
- `V` - View (F7)
- `P` - Print (Ctrl+P)
- `M` - Email (Ctrl+M)
- `R` - Refresh (F9)
- `D` - Delete (F4)
- `X` - Exit (Esc)
- `1` - First (Home)
- `2` - Prev (PgUp)
- `3` - Next (PgDn)
- `4` - Last (End)
- `Q` - Search (Ctrl+F)
- `F` - Filter (Alt+F)

**When to Use**:
- ✅ Document-based workflows
- ✅ Approval processes
- ✅ Status transitions (Draft → Submitted → Approved)
- ✅ Audit trail required

**Optional Additions**:
- Add `H` for Hold if suspension is needed
- Add `W` for Void if annulment is needed
- Add `L` for Clone if duplication is common
- Add `B` for Notes
- Add `G` for Attachments

---

### 4️⃣ **Transactions (Simplified)**
**Examples**: Stock Adjustments, Stock Transfers (no approval workflow)

**Config String**: `NESCKVDXRQF`

**Breakdown**:
- Same as "Masters (Simple)"
- Use when no approval workflow is needed

**When to Use**:
- ✅ Internal operations
- ✅ No approval required
- ✅ Direct posting
- ❌ No Submit/Authorize/Reject

---

### 5️⃣ **Reports & Dashboards**
**Examples**: Stock Valuation, Sales Analysis, Aging Reports

**Config String**: `VRXPYQFG`

**Breakdown**:
- `V` - View (F7)
- `R` - Refresh (F9)
- `X` - Exit (Esc)
- `P` - Print (Ctrl+P)
- `Y` - Export (Ctrl+E)
- `Q` - Search (Ctrl+F)
- `F` - Filter (Alt+F)
- `G` - Settings (Alt+O)

**When to Use**:
- ✅ Read-only screens
- ✅ Data visualization
- ✅ No editing capability
- ✅ Export/print focused

---

### 6️⃣ **Configuration Screens**
**Examples**: Company Settings, System Parameters, User Preferences

**Config String**: `ESCKXR`

**Breakdown**:
- `E` - Edit (F3)
- `S` - Save (F8)
- `C` - Cancel (Esc)
- `K` - Clear (F5)
- `X` - Exit (Esc)
- `R` - Refresh (F9)

**When to Use**:
- ✅ Settings pages
- ✅ No New/Delete (single record)
- ✅ Edit-only mode

---

## 🎨 REAL-WORLD EXAMPLES

### Example 1: UOM Setup
**Screen Type**: Masters (Simple)  
**Config**: `NESCKVDXRQF`  
**Reasoning**: Simple lookup table, no import/export needed

### Example 2: Item Master
**Screen Type**: Masters (Advanced)  
**Config**: `NESCKVDXRQFIO`  
**Reasoning**: Large dataset, needs bulk import/export

### Example 3: Purchase Order
**Screen Type**: Transactions (Standard)  
**Config**: `NESCKZTJAVPMRDX1234QF`  
**Reasoning**: Full workflow with approval process

### Example 4: Stock Movement
**Screen Type**: Transactions (Simplified)  
**Config**: `NESCKVDXRQF`  
**Reasoning**: Internal operation, no approval needed

### Example 5: Stock Valuation Report
**Screen Type**: Reports  
**Config**: `VRXPYQFG`  
**Reasoning**: Read-only, export/print focused

### Example 6: Company Settings
**Screen Type**: Configuration  
**Config**: `ESCKXR`  
**Reasoning**: Single record, edit-only

---

## 🔧 HOW TO APPLY

### Step 1: Identify Screen Type
Use the decision tree at the top to classify your screen.

### Step 2: Choose Base Config
Pick the appropriate ready-to-use configuration string.

### Step 3: Customize (Optional)
Add optional characters based on specific needs:
- Add `L` if Clone is needed
- Add `B` if Notes are needed
- Add `G` if Attachments are needed
- Add `H` if Hold is needed
- Add `W` if Void is needed

### Step 4: Update Backend
Set the `applicable_toolbar_config` field in `ERPMenuItem`:

```python
ERPMenuItem.objects.filter(menu_id='your_menu_id').update(
    applicable_toolbar_config='NESCKVDXRQF'
)
```

### Step 5: Verify Frontend
Ensure `viewId` matches `menu_id`:

```typescript
<MasterToolbar
  viewId="your_menu_id"
  mode={mode}
  onAction={handleAction}
/>
```

---

## 📊 CONFIGURATION MATRIX

| Screen Type | Config String | Length | Complexity |
|-------------|---------------|--------|------------|
| Masters (Simple) | `NESCKVDXRQF` | 11 | ⭐ Low |
| Masters (Advanced) | `NESCKVDXRQFIO` | 13 | ⭐⭐ Medium |
| Transactions (Standard) | `NESCKZTJAVPMRDX1234QF` | 21 | ⭐⭐⭐ High |
| Transactions (Simplified) | `NESCKVDXRQF` | 11 | ⭐ Low |
| Reports | `VRXPYQFG` | 8 | ⭐ Low |
| Configuration | `ESCKXR` | 6 | ⭐ Low |

---

## ⚠️ COMMON MISTAKES TO AVOID

1. ❌ **Don't add workflow actions to Masters**
   - Masters don't need Submit/Authorize/Reject
   - Use `NESCKVDXRQF` not `NESCKZTJA...`

2. ❌ **Don't add CRUD to Reports**
   - Reports are read-only
   - Use `VRXPYQFG` not `NESCKVDXRQF`

3. ❌ **Don't forget Exit**
   - Always include `X` for Exit
   - Users need a way to leave the page

4. ❌ **Don't mix character codes**
   - Use `O` for Export, not `Y` (unless Reports)
   - Use `Z` for Authorize, not `A` (A is Amend)

5. ❌ **Don't add Import/Export to simple Masters**
   - Only add `IO` if bulk operations are truly needed
   - Keeps toolbar clean for simple screens

---

## 🎓 LEARNING PATH

### Beginner
Start with these 3 configs:
1. `NESCKVDXRQF` - Masters (Simple)
2. `VRXPYQFG` - Reports
3. `ESCKXR` - Configuration

### Intermediate
Add these 2 configs:
4. `NESCKVDXRQFIO` - Masters (Advanced)
5. `NESCKZTJAVPMRDX1234QF` - Transactions

### Advanced
Customize by adding optional characters:
- `L` (Clone), `B` (Notes), `G` (Attach), `H` (Hold), `W` (Void)

---

## 📞 QUICK HELP

**Question**: "Which config for Customer Master?"  
**Answer**: `NESCKVDXRQFIO` (Masters - Advanced, needs import/export)

**Question**: "Which config for Tax Class?"  
**Answer**: `NESCKVDXRQF` (Masters - Simple, no import/export)

**Question**: "Which config for Sales Order?"  
**Answer**: `NESCKZTJAVPMRDX1234QF` (Transactions - Standard, full workflow)

**Question**: "Which config for Stock Report?"  
**Answer**: `VRXPYQFG` (Reports, read-only)

**Question**: "Which config for System Settings?"  
**Answer**: `ESCKXR` (Configuration, edit-only)

---

**Last Updated**: 2026-01-09 17:21 IST  
**Maintained By**: Astra (ERP Platform Development Owner)  
**Status**: ⚡ ACTIVE AUTHORITY
