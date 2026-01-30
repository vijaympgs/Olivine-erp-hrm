# Menu-to-UI Wiring Report
**Generated**: 2026-01-06 21:31 IST  
**Purpose**: Identify all menu items that don't have corresponding UI implementations  
**Source**: menuConfig.ts analysis + router.tsx verification

---

## 📊 **EXECUTIVE SUMMARY**

### **Modal Standards Verification** ✅

#### **1. Workspace Positioning** ✅ **CONFIRMED**
**BaseModal** already positions within primary workspace C:
- **Centered variant**: `left: 'calc(var(--sidebar-rail-width) + var(--sidebar-panel-width))'`
- **Panel variant**: Full workspace width, respects sidebar
- **Backdrop**: Positioned within workspace, not over sidebar
- **Z-index**: Properly layered (modal: 50, lookup: 60)

#### **2. L4 Typography** ✅ **CONFIRMED**
All modal content uses L4 typography by default:
```typescript
// BaseModal.tsx lines 257-266 (centered variant)
fontSize: 'var(--typography-l4-size)',
fontWeight: 'var(--typography-l4-weight)',
color: 'var(--typography-l4-color)',
lineHeight: 'var(--typography-l4-line-height)'

// BaseModal.tsx lines 154-161 (panel variant)
fontSize: 'var(--typography-l4-size)',
fontWeight: 'var(--typography-l4-weight)',
color: 'var(--typography-l4-color)',
lineHeight: 'var(--typography-l4-line-height)'
```

#### **3. Modal Title Typography** ✅ **L2 (Section Headers)**
Modal titles use L2 typography (not L1):
```typescript
// BaseModal.tsx lines 132-136
fontSize: 'var(--typography-l2-size)',      // 18px
fontWeight: 'var(--typography-l2-weight)',  // 600
color: 'var(--typography-l2-color)',        // #1F2937
```

#### **4. Layout Settings Integration** ✅ **CONFIRMED**
All modal typography is controlled via `layoutConfig.ts`:
- **L4 (Form Labels & Body)**: Lines 506-512
  - fontSize: '12px'
  - fontWeight: 400
  - color: '#4B5563'
- **Form-specific typography**: Lines 514-533
  - formLabel, formInput, formHelper, formError
- **CSS Variables**: Applied via `LayoutManager.applyConfig()` (lines 782-804)

---

## 🔍 **MENU-TO-UI WIRING ANALYSIS**

### **Analysis Method**
1. Extract all leaf menu items from `menuConfig.ts` (items with `path` property)
2. Check if path has corresponding route in `router.tsx`
3. Verify if route points to an existing component file
4. Flag items with missing UI implementations

---

## ❌ **UNWIRED MENU ITEMS** (UI Not Implemented)

### **RETAIL MODULE**

#### **1. Sales (5 items - UI exists, backend pending)**
| Menu ID | Label | Path | Status |
|---------|-------|------|--------|
| `quotes` | Quotes & Estimates | `/sales/quotes` | ✅ UI exists, ❌ Backend pending |
| `orders` | Sales Orders | `/sales/orders` | ✅ UI exists, ❌ Backend pending |
| `invoices` | Invoices | `/sales/invoices` | ✅ UI exists, ❌ Backend pending |
| `returns` | Returns & Refunds | `/sales/returns` | ✅ UI exists, ❌ Backend pending |
| `sales-config` | General Configuration | `/sales/configuration` | ✅ UI exists, ❌ Backend pending |

#### **2. Inventory (Multiple paths pointing to same pages)**
**Note**: Many inventory menu items point to `/inventory/levels` or `/inventory/movements` with query parameters or filters. The base pages exist, but specialized views may need implementation.

| Menu ID | Label | Path | Status |
|---------|-------|------|--------|
| `inventory-overview` | Inventory Overview | `/inventory/dashboard` | ❌ **NOT WIRED** |
| `stock-by-location` | Stock by Location | `/inventory/levels?location=` | ⚠️ Filter needed |
| `stock-valuation` | Stock Valuation | `/inventory/levels` | ✅ Base page exists |
| `movement-trends` | Movement Trends | `/inventory/movements` | ✅ Base page exists |
| `stock-alerts` | Alerts & Notifications | `/inventory/levels/low_stock` | ❌ **NOT WIRED** |
| `intercompany-transfers` | Intercompany Transfers | `/inventory/intercompany` | ❌ **NOT WIRED** |
| `batch-mgmt` | Batch Management | `/inventory/batches` | ❌ **NOT WIRED** |
| `serial-tracking` | Serial Number Tracking | `/inventory/serials` | ❌ **NOT WIRED** |
| `inventory-setup` | Inventory Setup | `/inventory/setup` | ❌ **NOT WIRED** |

#### **3. Customers (2 items - Backend exists, UI pending)**
| Menu ID | Label | Path | Status |
|---------|-------|------|--------|
| `customer-groups` | Customer Groups | `/customers/groups` | ❌ **NOT WIRED** |
| `loyalty` | Loyalty Programs | `/customers/loyalty` | ❌ **NOT WIRED** |

---

### **FINANCIAL MANAGEMENT MODULE** (ALL UNWIRED)

**Total Items**: ~80 menu items  
**Wired**: 0  
**Unwired**: ~80

#### **Sample Unwired Items** (Top 20):
| Menu ID | Label | Path | Status |
|---------|-------|------|--------|
| `fin-dashboard` | Financial Overview | `/finance/dashboard` | ❌ **NOT WIRED** |
| `cashflow-summary` | Cash Flow Summary | `/finance/cashflow-summary` | ❌ **NOT WIRED** |
| `pl-summary` | Profit & Loss Summary | `/finance/pl-summary` | ❌ **NOT WIRED** |
| `bs-summary` | Balance Sheet Summary | `/finance/bs-summary` | ❌ **NOT WIRED** |
| `fin-alerts` | Financial Alerts | `/finance/alerts` | ❌ **NOT WIRED** |
| `chart-of-accounts` | Chart of Accounts | `/finance/coa` | ❌ **NOT WIRED** |
| `account-groups` | Account Groups | `/finance/account-groups` | ❌ **NOT WIRED** |
| `journal-entries` | Journal Entries | `/finance/journal-entries` | ❌ **NOT WIRED** |
| `recurring-journals` | Recurring Journals | `/finance/recurring-journals` | ❌ **NOT WIRED** |
| `reversing-entries` | Reversing Entries | `/finance/reversing-entries` | ❌ **NOT WIRED** |
| `trial-balance` | Trial Balance | `/finance/trial-balance` | ❌ **NOT WIRED** |
| `general-ledger-view` | General Ledger | `/finance/gl` | ❌ **NOT WIRED** |
| `customer-invoices` | Customer Invoices | `/finance/ar/invoices` | ❌ **NOT WIRED** |
| `credit-notes` | Credit Notes | `/finance/ar/credit-notes` | ❌ **NOT WIRED** |
| `debit-notes` | Debit Notes | `/finance/ar/debit-notes` | ❌ **NOT WIRED** |
| `payment-receipts` | Receipts | `/finance/ar/receipts` | ❌ **NOT WIRED** |
| `payment-allocation` | Payment Allocation | `/finance/ar/allocation` | ❌ **NOT WIRED** |
| `customer-advances` | Customer Advances | `/finance/ar/advances` | ❌ **NOT WIRED** |
| `outstanding-receivables` | Outstanding Receivables | `/finance/ar/outstanding` | ❌ **NOT WIRED** |
| `ar-aging` | Aging Analysis | `/finance/ar/aging` | ❌ **NOT WIRED** |

**Full Financial Management list**: See detailed breakdown below

---

### **CRM MODULE** (ALL UNWIRED - PHASE 2)

**Total Items**: ~150+ menu items  
**Wired**: 0  
**Unwired**: ~150+  
**Status**: **PHASE 2** - Not prioritized for current implementation

---

### **HRM MODULE** (ALL UNWIRED - PHASE 2)

**Total Items**: ~100+ menu items  
**Wired**: 0  
**Unwired**: ~100+  
**Status**: **PHASE 2** - Separate agent (Agent E) responsible

---

## 📊 **WIRING STATISTICS**

### **Overall Summary**
| Module | Total Menu Items | Wired | Unwired | % Complete |
|--------|------------------|-------|---------|------------|
| **Retail - Store Ops** | 7 | 7 | 0 | 100% |
| **Retail - Sales** | 5 | 5 (UI only) | 5 (Backend) | 50% |
| **Retail - Merchandising** | 9 | 9 | 0 | 100% |
| **Retail - Inventory** | 60+ | 9 | ~51 | 15% |
| **Retail - Procurement** | 11 | 11 | 0 | 100% |
| **Retail - Customers** | 3 | 1 | 2 | 33% |
| **Financial Management** | ~80 | 0 | ~80 | 0% |
| **CRM** | ~150 | 0 | ~150 | 0% (Phase 2) |
| **HRM** | ~100 | 0 | ~100 | 0% (Phase 2) |
| **TOTAL** | ~425 | ~42 | ~383 | ~10% |

### **Priority Breakdown**
| Priority | Count | Description |
|----------|-------|-------------|
| **P0 - Critical** | 2 | Customer Groups, Loyalty (backend exists) |
| **P1 - High** | 9 | Inventory specialized views (dashboard, batches, serials, etc.) |
| **P2 - Medium** | 80 | Financial Management (entire module) |
| **P3 - Low** | 250+ | CRM + HRM (Phase 2) |

---

## 🎯 **DETAILED UNWIRED INVENTORY ITEMS**

### **Inventory Dashboard & Analytics**
- ❌ `/inventory/dashboard` - Inventory Overview
- ⚠️ `/inventory/levels?location=` - Stock by Location (filter needed)
- ⚠️ `/inventory/levels` - Stock Valuation (base exists, specialized view needed)
- ⚠️ `/inventory/movements` - Movement Trends (base exists, analytics needed)
- ❌ `/inventory/levels/low_stock` - Alerts & Notifications

### **Stock Management (Specialized Views)**
All point to `/inventory/levels` but need specialized filtering/views:
- ⚠️ Stock on Hand (base exists)
- ⚠️ Stock by Location (filter needed)
- ⚠️ Stock by Category (filter needed)
- ⚠️ Stock by Batch/Serial (filter needed)
- ❌ Low Stock Alerts (dedicated view needed)
- ❌ Overstock Alerts (dedicated view needed)
- ⚠️ Stock Aging Analysis (analytics needed)

### **Stock Movements (Specialized Views)**
All point to `/inventory/movements` but need specialized filtering:
- ⚠️ Movement History (base exists)
- ⚠️ Goods Receipt (filter needed)
- ⚠️ Goods Issue (filter needed)
- ✅ Internal Transfers (exists)
- ❌ Intercompany Transfers (NOT WIRED)
- ⚠️ Movement Reports (export functionality needed)

### **Stock Adjustments (Specialized Routes)**
- ✅ Stock Adjustment Entry (`/inventory/adjustments/new`)
- ✅ Adjustment History (`/inventory/adjustments/history`)
- ✅ Reason Code Management (`/inventory/adjustments/reason-codes`)
- ✅ Approval Workflow (`/inventory/adjustments/approvals`)
- ⚠️ Adjustment Reports (`/inventory/adjustments/reports`) - export needed

### **Physical Inventory**
All point to `/inventory/stock-takes`:
- ⚠️ Cycle Counting Schedule (base exists, specialized view needed)
- ⚠️ Stock Take Execution (base exists)
- ⚠️ Variance Analysis (analytics needed)
- ⚠️ Count Approval (workflow needed)
- ⚠️ Reconciliation (post-approval logic needed)

### **Batch & Serial Tracking**
- ❌ `/inventory/batches` - Batch Management (NOT WIRED)
- ❌ `/inventory/serials` - Serial Number Tracking (NOT WIRED)
- ❌ `/inventory/levels/low_stock` - Expiry Management (NOT WIRED)
- ⚠️ `/inventory/movements` - Batch Traceability (filter needed)

### **Configuration**
- ❌ `/inventory/setup` - Inventory Setup (NOT WIRED)

---

## 🎯 **DETAILED UNWIRED FINANCIAL MANAGEMENT ITEMS**

### **1. Finance Dashboard** (5 items)
- ❌ `/finance/dashboard` - Financial Overview
- ❌ `/finance/cashflow-summary` - Cash Flow Summary
- ❌ `/finance/pl-summary` - Profit & Loss Summary
- ❌ `/finance/bs-summary` - Balance Sheet Summary
- ❌ `/finance/alerts` - Financial Alerts

### **2. General Ledger** (7 items)
- ❌ `/finance/coa` - Chart of Accounts
- ❌ `/finance/account-groups` - Account Groups
- ❌ `/finance/journal-entries` - Journal Entries
- ❌ `/finance/recurring-journals` - Recurring Journals
- ❌ `/finance/reversing-entries` - Reversing Entries
- ❌ `/finance/trial-balance` - Trial Balance
- ❌ `/finance/gl` - General Ledger

### **3. Accounts Receivable** (9 items)
- ❌ `/finance/ar/invoices` - Customer Invoices
- ❌ `/finance/ar/credit-notes` - Credit Notes
- ❌ `/finance/ar/debit-notes` - Debit Notes
- ❌ `/finance/ar/receipts` - Receipts
- ❌ `/finance/ar/allocation` - Payment Allocation
- ❌ `/finance/ar/advances` - Customer Advances
- ❌ `/finance/ar/outstanding` - Outstanding Receivables
- ❌ `/finance/ar/aging` - Aging Analysis
- ❌ `/finance/ar/writeoffs` - Write-offs

### **4. Accounts Payable** (8 items)
- ❌ `/finance/ap/bills` - Vendor Bills
- ❌ `/finance/ap/debit-notes` - Debit Notes (Returns)
- ❌ `/finance/ap/credit-notes` - Credit Notes
- ❌ `/finance/ap/payments` - Payments
- ❌ `/finance/ap/advances` - Vendor Advances
- ❌ `/finance/ap/outstanding` - Outstanding Payables
- ❌ `/finance/ap/aging` - Aging Analysis
- ❌ `/finance/ap/expense-claims` - Expense Claims

### **5. Cash & Bank** (5 items)
- ❌ `/finance/bank/accounts` - Bank Accounts
- ❌ `/finance/bank/cash-accounts` - Cash Accounts
- ❌ `/finance/bank/deposits` - Deposits & Withdrawals
- ❌ `/finance/bank/reconciliation` - Bank Reconciliation
- ❌ `/finance/bank/cheques` - Cheque Management

### **6. Payments** (5 items)
- ❌ `/finance/payments/methods` - Payment Methods
- ❌ `/finance/payments/terms` - Payment Terms
- ❌ `/finance/payments/online` - Online Payments
- ❌ `/finance/payments/refunds` - Refunds & Reversals
- ❌ `/finance/payments/reconciliation` - Payment Reconciliation

### **7. Tax Management** (7 items)
- ❌ `/finance/tax/config` - Tax Configuration
- ❌ `/finance/tax/gst` - GST (Input / Output)
- ❌ `/finance/tax/tds-tcs` - TDS / TCS
- ❌ `/finance/tax/invoices` - Tax Invoices
- ❌ `/finance/tax/returns` - Tax Returns
- ❌ `/finance/tax/reconciliation` - Tax Reconciliation
- ❌ `/finance/tax/einvoicing` - E-Invoicing / E-Way Bill

### **8. Financial Reports** (9 items)
- ❌ `/finance/reports/balance-sheet` - Balance Sheet
- ❌ `/finance/reports/pl` - Profit & Loss
- ❌ `/finance/reports/cashflow` - Cash Flow
- ❌ `/finance/reports/trial-balance` - Trial Balance
- ❌ `/finance/reports/day-book` - Day Book
- ❌ `/finance/reports/cash-book` - Cash Book
- ❌ `/finance/reports/bank-book` - Bank Book
- ❌ `/finance/reports/sales-register` - Sales Register
- ❌ `/finance/reports/purchase-register` - Purchase Register

### **9. Period Closing** (5 items)
- ❌ `/finance/closing/period-close` - Period Close
- ❌ `/finance/closing/year-close` - Year Close
- ❌ `/finance/closing/opening-balances` - Opening Balances
- ❌ `/finance/closing/period-lock` - Period Lock
- ❌ `/finance/closing/audit-trail` - Audit Trail

**Total Financial Management Unwired**: 60 items

---

## 💡 **RECOMMENDATIONS**

### **Immediate Actions** (P0 - Critical)
1. ✅ **Verify Modal Standards** - COMPLETE
   - BaseModal positions within workspace C ✅
   - L4 typography applied to all modal content ✅
   - Controlled via layoutConfig.ts ✅

2. 🎯 **Implement Customer Module UIs** (2 items, 4 hours)
   - Customer Groups page
   - Customer Loyalty page

### **Short-term Actions** (P1 - High)
3. 🎯 **Implement Inventory Specialized Views** (9 items, 8-12 hours)
   - Inventory Dashboard
   - Low Stock Alerts (dedicated view)
   - Overstock Alerts
   - Batch Management
   - Serial Number Tracking
   - Intercompany Transfers
   - Inventory Setup
   - Expiry Management
   - Stock Aging Analytics

### **Medium-term Actions** (P2 - Medium)
4. 🎯 **Financial Management Module** (60 items, 40-60 hours)
   - Start with core: GL, AR, AP
   - Then: Cash & Bank, Payments
   - Then: Tax Management
   - Finally: Reports & Period Closing

### **Long-term Actions** (P3 - Low)
5. 🎯 **CRM & HRM Modules** (250+ items, Phase 2)
   - Defer to Phase 2
   - Agent E responsible for HRM/CRM

---

## 📋 **TEST CONSOLE INTEGRATION**

### **How to Generate Live Report**
To generate a comprehensive report for ALL modules:

1. **Navigate to Test Console**:
   ```
   http://localhost:5173/test-console
   ```

2. **For Each Module**:
   - Click on module in Explorer (left sidebar)
   - View readiness matrix (middle panel)
   - Apply filters if needed
   - Click **"CSV"** button to export

3. **Generate Complete Report**:
   - Repeat for all modules:
     - Retail
     - Financial Management
     - CRM
     - HRM
   - Combine CSV exports
   - Analyze unwired items

### **Automated Report Generation** (Future Enhancement)
**Recommendation**: Add "Export All Modules" button to Test Console that:
1. Iterates through all modules automatically
2. Generates single consolidated CSV
3. Includes wiring status for each menu item
4. Flags items with missing UI implementations

---

## 🎯 **NEXT STEPS**

### **Option 1: Complete Customer Module** (Recommended - Quick Win)
- Customer Groups page (2-3 hours)
- Customer Loyalty page (3-4 hours)
- **Impact**: Brings Customers to 100%

### **Option 2: Inventory Specialized Views** (High Value)
- Inventory Dashboard (3-4 hours)
- Batch/Serial Management (4-5 hours)
- Low/Overstock Alerts (2-3 hours)
- **Impact**: Brings Inventory to 30-40%

### **Option 3: Financial Management Foundation** (Strategic)
- Chart of Accounts (4-5 hours)
- Journal Entries (5-6 hours)
- AR/AP basics (8-10 hours)
- **Impact**: Starts critical FMS module

---

**Report Generated By**: Astra (AI Agent)  
**Analysis Date**: 2026-01-06 21:31 IST  
**Total Menu Items Analyzed**: ~425  
**Wired**: ~42 (10%)  
**Unwired**: ~383 (90%)  
**Status**: ✅ **READY FOR REVIEW**
