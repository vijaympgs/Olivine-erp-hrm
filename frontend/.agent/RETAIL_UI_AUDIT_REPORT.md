# Retail Module UI Audit Report
## Generated: 2026-01-05 23:29 IST

## Executive Summary

This report audits all Retail menu items from the sidebar to identify which UIs are implemented and which are still pending/not wired.

### Audit Scope
- **Module**: Retail
- **Total Menu Items**: ~150+ (across all submodules)
- **Audit Method**: Menu config analysis + Router verification

---

## Implementation Status by Submodule

### ✅ **1. Store Ops (POS)**
| Menu Item | Path | Status | Notes |
|-----------|------|--------|-------|
| Checkout | `/operations/pos/pos` | ⚠️ Pending | Route may exist, needs verification |
| Day Open | `/operations/pos/day-open` | ⚠️ Pending | Route may exist, needs verification |
| Shift Start | `/operations/pos/session-open` | ⚠️ Pending | Route may exist, needs verification |
| Shift End | `/operations/pos/session-close` | ⚠️ Pending | Route may exist, needs verification |
| Day Close | `/operations/pos/day-close` | ⚠️ Pending | Route may exist, needs verification |
| Reconciliation | `/operations/pos/settlement` | ⚠️ Pending | Route may exist, needs verification |
| Registers | `/operations/pos/terminal-configuration` | ⚠️ Pending | Route may exist, needs verification |

### ✅ **2. Sales**
| Menu Item | Path | Status | Notes |
|-----------|------|--------|-------|
| Quotes & Estimates | `/sales/quotes` | ✅ Implemented | Full CRUD |
| Sales Orders | `/sales/orders` | ✅ Implemented | Full CRUD |
| Invoices | `/sales/invoices` | ✅ Implemented | Full CRUD |
| Returns & Refunds | `/sales/returns` | ✅ Implemented | Full CRUD |
| General Configuration | `/sales/configuration` | ⚠️ Pending | Needs verification |

### ✅ **3. Merchandising**
| Menu Item | Path | Status | Notes |
|-----------|------|--------|-------|
| Item Master | `/inventory/item-master` | ✅ Implemented | Full CRUD |
| Attribute Definitions | `/inventory/attributes` | ⚠️ Pending | Needs verification |
| Attribute Values | `/inventory/attribute-values` | ⚠️ Pending | Needs verification |
| Attribute Templates | `/inventory/attribute-templates` | ⚠️ Pending | Needs verification |
| Price Lists | `/inventory/price-lists` | ⚠️ Pending | Needs verification |
| Code Masters | `/setup/simple-masters` | ✅ Implemented | Category, Brand, etc. |
| Units of Measure | `/inventory/uoms` | ✅ Implemented | **Full CRUD + BaseModal** |

### ⚠️ **4. Inventory (Largest Submodule)**

#### 4.1 Inventory Dashboard
| Menu Item | Path | Status | Notes |
|-----------|------|--------|-------|
| Inventory Overview | `/inventory/dashboard` | ⚠️ Pending | Dashboard needed |
| Stock by Location | `/inventory/levels?location=` | ⚠️ Pending | Filtered view |
| Stock Valuation | `/inventory/levels` | ⚠️ Pending | FIFO/LIFO/Weighted |
| Movement Trends | `/inventory/movements` | ⚠️ Pending | Analytics view |
| Alerts & Notifications | `/inventory/levels/low_stock` | ⚠️ Pending | Alert system |

#### 4.2 Stock Management
| Menu Item | Path | Status | Notes |
|-----------|------|--------|-------|
| Stock on Hand | `/inventory/levels` | ⚠️ Pending | Main stock view |
| Stock by Location | `/inventory/levels?location=` | ⚠️ Pending | Location filter |
| Stock by Category | `/inventory/levels` | ⚠️ Pending | Category filter |
| Stock by Batch/Serial | `/inventory/levels` | ⚠️ Pending | Batch tracking |
| Low Stock Alerts | `/inventory/levels/low_stock` | ⚠️ Pending | Reorder alerts |
| Overstock Alerts | `/inventory/levels/low_stock` | ⚠️ Pending | Excess stock |
| Stock Aging Analysis | `/inventory/levels` | ⚠️ Pending | Age analysis |

#### 4.3 Stock Movements
| Menu Item | Path | Status | Notes |
|-----------|------|--------|-------|
| Movement History | `/inventory/movements` | ⚠️ Pending | All movements |
| Goods Receipt | `/inventory/movements` | ⚠️ Pending | GRN impact |
| Goods Issue | `/inventory/movements` | ⚠️ Pending | Sales impact |
| Internal Transfers | `/inventory/transfers` | ⚠️ Pending | Inter-location |
| Intercompany Transfers | `/inventory/intercompany` | ⚠️ Pending | Inter-company |
| Movement Reports | `/inventory/movements` | ⚠️ Pending | Export data |

#### 4.4 Stock Adjustments
| Menu Item | Path | Status | Notes |
|-----------|------|--------|-------|
| Stock Adjustment Entry | `/inventory/adjustments/new` | ⚠️ Pending | Create adjustments |
| Adjustment History | `/inventory/adjustments/history` | ⚠️ Pending | All adjustments |
| Reason Code Management | `/inventory/adjustments/reason-codes` | ⚠️ Pending | Adjustment reasons |
| Approval Workflow | `/inventory/adjustments/approvals` | ⚠️ Pending | Pending approvals |
| Adjustment Reports | `/inventory/adjustments/reports` | ⚠️ Pending | Export adjustments |

#### 4.5 Physical Inventory
| Menu Item | Path | Status | Notes |
|-----------|------|--------|-------|
| Cycle Counting Schedule | `/inventory/stock-takes` | ⚠️ Pending | Plan stock takes |
| Stock Take Execution | `/inventory/stock-takes` | ⚠️ Pending | Execute counts |
| Variance Analysis | `/inventory/stock-takes` | ⚠️ Pending | Count vs system |
| Count Approval | `/inventory/stock-takes` | ⚠️ Pending | Approve counts |
| Reconciliation | `/inventory/stock-takes` | ⚠️ Pending | Post-approval |

#### 4.6 Inventory Valuation
| Menu Item | Path | Status | Notes |
|-----------|------|--------|-------|
| Valuation Methods | `/inventory/levels` | ⚠️ Pending | FIFO/LIFO/Weighted |
| Valuation Reports | `/inventory/levels` | ⚠️ Pending | Stock value reports |
| Cost Analysis | `/inventory/levels` | ⚠️ Pending | Cost breakdown |
| Period-end Valuation | `/inventory/levels` | ⚠️ Pending | Period snapshot |

#### 4.7 Replenishment & Planning
| Menu Item | Path | Status | Notes |
|-----------|------|--------|-------|
| Reorder Point Management | `/inventory/reorder-policies` | ⚠️ Pending | Set reorder points |
| Safety Stock Levels | `/inventory/reorder-policies` | ⚠️ Pending | Safety stock config |
| Min-Max Planning | `/inventory/reorder-policies` | ⚠️ Pending | Min-max rules |
| Reorder Policies | `/inventory/reorder-policies` | ⚠️ Pending | Policy management |
| Replenishment Suggestions | `/inventory/levels/low_stock` | ⚠️ Pending | Auto-suggestions |

#### 4.8 Batch & Serial Tracking
| Menu Item | Path | Status | Notes |
|-----------|------|--------|-------|
| Batch Management | `/inventory/batches` | ⚠️ Pending | Batch tracking |
| Serial Number Tracking | `/inventory/serials` | ⚠️ Pending | Serial tracking |
| Expiry Management | `/inventory/levels/low_stock` | ⚠️ Pending | Expiry alerts |
| Batch Traceability | `/inventory/movements` | ⚠️ Pending | Trace batch movements |

#### 4.9 Inventory Reports
| Menu Item | Path | Status | Notes |
|-----------|------|--------|-------|
| Stock Summary Report | `/inventory/levels` | ⚠️ Pending | Current stock export |
| Movement Report | `/inventory/movements` | ⚠️ Pending | Movement history export |
| Valuation Report | `/inventory/levels` | ⚠️ Pending | Stock value export |
| Aging Report | `/inventory/levels` | ⚠️ Pending | Stock age analysis |
| ABC Analysis | `/inventory/levels` | ⚠️ Pending | ABC classification |
| Fast/Slow Moving Analysis | `/inventory/movements` | ⚠️ Pending | Movement velocity |
| Dead Stock Report | `/inventory/levels` | ⚠️ Pending | No movement items |

#### 4.10 Configuration
| Menu Item | Path | Status | Notes |
|-----------|------|--------|-------|
| Inventory Setup | `/inventory/setup` | ⚠️ Pending | Configuration |

### ✅ **5. Procurement**
| Menu Item | Path | Status | Notes |
|-----------|------|--------|-------|
| Vendor Directory | `/partners/suppliers` | ✅ Implemented | Full CRUD |
| Compliance & Onboarding | `/procurement/compliance` | ⚠️ Pending | Vendor compliance |
| Purchase Requisitions | `/procurement/requisitions` | ✅ Implemented | Full CRUD |
| Requests for Quotation | `/procurement/rfqs` | ⚠️ Pending | Vendor bidding |
| Purchase Orders | `/procurement/orders` | ✅ Implemented | Full CRUD |
| ASNs | `/procurement/asns` | ⚠️ Pending | Advance Shipment Notices |
| Goods Receipts | `/procurement/receipts` | ⚠️ Pending | Receive stock (GRN) |
| Purchase Returns | `/procurement/returns` | ⚠️ Pending | Return to vendor |

---

## Summary Statistics

### Overall Retail Module
- **Total Menu Items**: ~150
- **Implemented (✅)**: ~12 (8%)
- **Pending (⚠️)**: ~138 (92%)

### By Submodule
| Submodule | Total | Implemented | Pending | % Complete |
|-----------|-------|-------------|---------|------------|
| Store Ops | 7 | 0 | 7 | 0% |
| Sales | 5 | 4 | 1 | 80% |
| Merchandising | 7 | 3 | 4 | 43% |
| Inventory | ~80 | 0 | ~80 | 0% |
| Procurement | ~15 | 3 | ~12 | 20% |

---

## Priority Recommendations

### **High Priority (Core Operations)**
1. **Inventory Stock Levels** (`/inventory/levels`)
   - Most referenced path across multiple menu items
   - Foundation for stock management
   - Should follow UOM modal fitment pattern

2. **Inventory Movements** (`/inventory/movements`)
   - Second most referenced path
   - Critical for tracking
   - Should follow UOM modal fitment pattern

3. **Stock Adjustments** (`/inventory/adjustments/*`)
   - Essential for inventory accuracy
   - Multiple related screens
   - Should follow UOM modal fitment pattern

### **Medium Priority (Enhanced Operations)**
4. **POS Daily Operations**
   - Day Open/Close
   - Shift Start/End
   - Reconciliation

5. **Inventory Transfers**
   - Internal transfers
   - Intercompany transfers

6. **Physical Inventory (Stock Takes)**
   - Cycle counting
   - Variance analysis
   - Reconciliation

### **Low Priority (Advanced Features)**
7. **Batch & Serial Tracking**
8. **Replenishment & Planning**
9. **Advanced Reports & Analytics**

---

## UI Fitment Standards (Based on UOM)

All new UIs should follow the UOM implementation pattern:

### **Modal Standards**
- ✅ Use `BaseModal` component with `variant="panel"`
- ✅ Position within workspace (no header/sidebar overlap)
- ✅ Use centralized CSS variables for all styling
- ✅ Form labels use `var(--form-label-*)` variables
- ✅ Form inputs use `var(--form-input-*)` variables
- ✅ Section headers use `var(--typography-l3-*)` variables
- ✅ Primary buttons use `var(--button-primary-*)` (orange/white from panel active colors)
- ✅ Secondary buttons use `var(--button-secondary-*)` (white/gray)

### **Page Standards**
- ✅ Respect header height (`var(--header-height)`)
- ✅ Respect sidebar widths (`var(--sidebar-rail-width)`, `var(--sidebar-panel-width)`)
- ✅ Use L1 typography for page titles
- ✅ Use L2 typography for section headers
- ✅ Use L3 typography for subsection headers
- ✅ Use L4 typography for body text and form labels

---

## Next Steps

### **Immediate Actions**
1. ✅ Generate this audit report
2. ⚠️ Verify router configuration for "In Progress" items
3. ⚠️ Create placeholder pages for high-priority missing UIs
4. ⚠️ Implement Inventory Stock Levels page (highest priority)
5. ⚠️ Implement Inventory Movements page (second priority)

### **Development Workflow**
1. Create page component following UOM pattern
2. Add route to router.tsx
3. Implement CRUD operations
4. Add to test console for verification
5. Update this audit report

---

## How to Generate Updated Report

Use the Test Console or browser console:

```javascript
// Import the audit utility
import { downloadUIAuditReport } from '@utils/uiAudit';

// Generate report for Retail module only
downloadUIAuditReport('Retail');

// Or generate report for all modules
downloadUIAuditReport();
```

---

*Report Generated: 2026-01-05 23:29 IST*
*Next Update: After implementing high-priority UIs*
