# 🎯 RETAIL MODULE - COMPREHENSIVE AUDIT & EXECUTION PLAN
**Session Date**: 2026-01-09 14:20 IST  
**Agent**: Astra  
**Purpose**: Complete Retail Module Implementation

---

## 📊 CURRENT STATE AUDIT

### **1. Toolbar Implementation Status** ✅ **COMPLETE**
- **Backend**: Character-based registry (129 menu items configured)
- **Frontend**: MasterToolbar component integrated in 30+ pages
- **Governance**: `.steering/18_WIRING_CHECKLISTS/` documentation complete
- **Reference**: `toolbar_reference/` toolkit available for all agents

### **2. Sidebar Menu Wiring Status**
Based on `RETAIL_IMPLEMENTATION_TRACKER.md` and `MENU_WIRING_REPORT_2026-01-06.md`:

| Module | Total Items | Wired | Pending | % Complete |
|--------|-------------|-------|---------|------------|
| **Store Ops** | 7 | 7 | 0 | 100% ✅ |
| **Sales** | 5 | 5 (UI) | 0 (Backend ✅) | 100% ✅ |
| **Merchandising** | 9 | 9 | 0 | 100% ✅ |
| **Procurement** | 11 | 11 | 0 | 100% ✅ |
| **Customers** | 3 | 3 | 0 | 100% ✅ |
| **Inventory** | 63 | 21 | 42 | 33% 🚧 |
| **TOTAL RETAIL** | **98** | **56** | **42** | **57%** |

### **3. Command Button Audit** (Toolbar-Only Policy)
**Requirement**: All UIs except POS Billing must use MasterToolbar ONLY (no standalone command buttons)

**Status**: ⚠️ **NEEDS VERIFICATION**
- **Action Required**: Scan all Retail pages for standalone "Add New", "Save", "Cancel" buttons
- **Exception**: POS Billing page can have custom buttons
- **Target**: 100% compliance with toolbar-only policy

---

## 🎯 EXECUTION PLAN - PHASE 4: INVENTORY COMPLETION

### **Priority 1: Inventory Specialized Views** (42 UIs Pending)

#### **Phase 4A: Dashboard & Analytics** (12 UIs) - **6 hours**
| # | Feature | Path | Component | Toolbar Config | Est. Time |
|---|---------|------|-----------|----------------|-----------|
| 1 | Stock by Location | `/inventory/levels/by-location` | `StockByLocationPage.tsx` | `NEVZPM1234RDQX` | 45min |
| 2 | Stock Valuation Dashboard | `/inventory/levels/valuation` | `StockValuationDashboard.tsx` | `NEVPM1234RDX` | 45min |
| 3 | Movement Trends | `/inventory/movements/trends` | `MovementTrendsAnalytics.tsx` | `NEVPM1234RDX` | 45min |
| 4 | Alerts & Notifications | `/inventory/alerts` | `AlertsNotificationsPage.tsx` | `NEVZPM1234RDX` | 45min |
| 5 | Stock by Category | `/inventory/levels/by-category` | `StockByCategoryPage.tsx` | `NEVZPM1234RDQX` | 30min |
| 6 | Stock by Batch/Serial | `/inventory/levels/by-batch` | `StockByBatchSerialPage.tsx` | `NEVZPM1234RDQX` | 30min |
| 7 | Low Stock Alerts | `/inventory/alerts/low-stock` | `LowStockAlertsPage.tsx` | `NEVZPM1234RDX` | 30min |
| 8 | Overstock Alerts | `/inventory/alerts/overstock` | `OverstockAlertsPage.tsx` | `NEVZPM1234RDX` | 30min |
| 9 | Stock Aging Analysis | `/inventory/levels/aging` | `StockAgingAnalysisPage.tsx` | `NEVPM1234RDX` | 45min |
| 10 | Goods Receipt View | `/inventory/movements/receipts` | `GoodsReceiptViewPage.tsx` | `NEVPM1234RDX` | 30min |
| 11 | Goods Issue View | `/inventory/movements/issues` | `GoodsIssueViewPage.tsx` | `NEVPM1234RDX` | 30min |
| 12 | Movement Reports | `/inventory/movements/reports` | `MovementReportsPage.tsx` | `NEPM1234RDX` | 30min |

**Deliverables**:
- ✅ 12 new UI components with MasterToolbar
- ✅ Route registration in `router.tsx`
- ✅ Service integration with existing backend APIs
- ✅ Menu item toolbar configs in Django Admin

#### **Phase 4B: Physical Inventory** (6 UIs) - **4 hours**
| # | Feature | Path | Component | Toolbar Config | Est. Time |
|---|---------|------|-----------|----------------|-----------|
| 13 | Cycle Count Schedule | `/inventory/stock-takes/schedule` | `CycleCountSchedulePage.tsx` | `NESCKPVDXRTJZ` | 45min |
| 14 | Stock Take Execution | `/inventory/stock-takes/execute` | `StockTakeExecutionPage.tsx` | `NESCKPVDXRTJZ` | 45min |
| 15 | Variance Analysis | `/inventory/stock-takes/variance` | `VarianceAnalysisPage.tsx` | `NEVPM1234RDX` | 30min |
| 16 | Count Approval | `/inventory/stock-takes/approvals` | `CountApprovalPage.tsx` | `NEVZPM1234RDTJX` | 45min |
| 17 | Reconciliation | `/inventory/stock-takes/reconciliation` | `ReconciliationPage.tsx` | `NESCKPVDXRTJZ` | 45min |
| 18 | Stock Take Reports | `/inventory/stock-takes/reports` | `StockTakeReportsPage.tsx` | `NEPM1234RDX` | 30min |

#### **Phase 4C: Replenishment & Planning** (4 UIs) - **3 hours**
| # | Feature | Path | Component | Toolbar Config | Est. Time |
|---|---------|------|-----------|----------------|-----------|
| 19 | Safety Stock Levels | `/inventory/reorder/safety-stock` | `SafetyStockPage.tsx` | `NESCKPVDXRQ` | 45min |
| 20 | Min-Max Planning | `/inventory/reorder/min-max` | `MinMaxPlanningPage.tsx` | `NESCKPVDXRQ` | 45min |
| 21 | Reorder Policies | `/inventory/reorder/policies` | `ReorderPoliciesPage.tsx` | `NESCKPVDXRQ` | 45min |
| 22 | Replenishment Suggestions | `/inventory/reorder/suggestions` | `ReplenishmentSuggestionsPage.tsx` | `NEVPM1234RDX` | 45min |

#### **Phase 4D: Batch & Serial Tracking** (2 UIs) - **2 hours**
| # | Feature | Path | Component | Toolbar Config | Est. Time |
|---|---------|------|-----------|----------------|-----------|
| 23 | Expiry Management | `/inventory/batches/expiry` | `ExpiryManagementPage.tsx` | `NEVZPM1234RDX` | 60min |
| 24 | Batch Traceability | `/inventory/batches/trace` | `BatchTraceabilityPage.tsx` | `NEVPM1234RDX` | 60min |

#### **Phase 4E: Inventory Reports** (7 UIs) - **4 hours**
| # | Feature | Path | Component | Toolbar Config | Est. Time |
|---|---------|------|-----------|----------------|-----------|
| 25 | Stock Summary Report | `/inventory/reports/stock-summary` | `StockSummaryReportPage.tsx` | `NEPM1234RDX` | 30min |
| 26 | Movement Report | `/inventory/reports/movements` | `MovementReportPage.tsx` | `NEPM1234RDX` | 30min |
| 27 | Valuation Report | `/inventory/reports/valuation` | `ValuationReportPage.tsx` | `NEPM1234RDX` | 30min |
| 28 | Aging Report | `/inventory/reports/aging` | `AgingReportPage.tsx` | `NEPM1234RDX` | 30min |
| 29 | ABC Analysis | `/inventory/reports/abc-analysis` | `ABCAnalysisPage.tsx` | `NEVPM1234RDX` | 45min |
| 30 | Fast/Slow Moving | `/inventory/reports/velocity` | `VelocityAnalysisPage.tsx` | `NEVPM1234RDX` | 45min |
| 31 | Dead Stock Report | `/inventory/reports/dead-stock` | `DeadStockReportPage.tsx` | `NEVPM1234RDX` | 45min |

#### **Phase 4F: Valuation** (4 UIs) - **3 hours**
| # | Feature | Path | Component | Toolbar Config | Est. Time |
|---|---------|------|-----------|----------------|-----------|
| 32 | Valuation Methods | `/inventory/valuation/methods` | `ValuationMethodsPage.tsx` | `NESCKPVDXRQ` | 45min |
| 33 | Valuation Reports | `/inventory/valuation/reports` | `ValuationReportsPage.tsx` | `NEPM1234RDX` | 45min |
| 34 | Cost Analysis | `/inventory/valuation/cost-analysis` | `CostAnalysisPage.tsx` | `NEVPM1234RDX` | 45min |
| 35 | Period-end Valuation | `/inventory/valuation/period-end` | `PeriodEndValuationPage.tsx` | `NEVPM1234RDX` | 45min |

#### **Phase 4G: Miscellaneous** (7 UIs) - **4 hours**
| # | Feature | Path | Component | Toolbar Config | Est. Time |
|---|---------|------|-----------|----------------|-----------|
| 36 | Adjustment Reports | `/inventory/adjustments/reports` | `AdjustmentReportsPage.tsx` | `NEPM1234RDX` | 30min |
| 37 | Intercompany Config | `/inventory/intercompany/config` | `IntercompanyConfigPage.tsx` | `NESCKPVDXRQ` | 45min |
| 38 | Transfer Templates | `/inventory/transfers/templates` | `TransferTemplatesPage.tsx` | `NESCKPVDXRQ` | 45min |
| 39 | Inventory Audit Trail | `/inventory/audit-trail` | `InventoryAuditTrailPage.tsx` | `NEVPM1234RDX` | 45min |
| 40 | Stock Reservations | `/inventory/reservations` | `StockReservationsPage.tsx` | `NESCKPVDXRTJZ` | 45min |
| 41 | Inventory Forecasting | `/inventory/forecasting` | `InventoryForecastingPage.tsx` | `NEVPM1234RDX` | 45min |
| 42 | Inventory KPIs | `/inventory/kpis` | `InventoryKPIsPage.tsx` | `NEVPM1234RDX` | 30min |

---

## 📋 IMPLEMENTATION CHECKLIST (Per UI)

### **For Each Component**:
- [ ] Create component file in `retail/frontend/inventory/pages/`
- [ ] Import MasterToolbar from `@ui/components/MasterToolbarConfigDriven`
- [ ] Implement `getToolbarMode()` function (VIEW/EDIT/CREATE)
- [ ] Implement `handleToolbarAction()` switch statement
- [ ] Add `viewId` prop matching Django Admin menu_id
- [ ] Register route in `frontend/src/app/router.tsx`
- [ ] Verify toolbar config in Django Admin (`ERPMenuItem`)
- [ ] Test all toolbar actions (New, Edit, Save, Cancel, etc.)
- [ ] Verify no standalone command buttons exist
- [ ] Test keyboard shortcuts (F2-F12)

---

## 🎯 SUCCESS CRITERIA

### **Phase 4 Complete When**:
- ✅ All 42 Inventory UIs created and wired
- ✅ All routes registered in `router.tsx`
- ✅ All toolbar configs set in Django Admin
- ✅ 100% toolbar-only compliance (no command buttons)
- ✅ All keyboard shortcuts functional
- ✅ Retail Module = **100% UI Complete**

---

## ⏱️ TIME ESTIMATE

| Phase | UIs | Estimated Time |
|-------|-----|----------------|
| 4A: Dashboard & Analytics | 12 | 6 hours |
| 4B: Physical Inventory | 6 | 4 hours |
| 4C: Replenishment | 4 | 3 hours |
| 4D: Batch & Serial | 2 | 2 hours |
| 4E: Reports | 7 | 4 hours |
| 4F: Valuation | 4 | 3 hours |
| 4G: Miscellaneous | 7 | 4 hours |
| **TOTAL** | **42** | **26 hours** |

**Recommended Approach**: Execute in 3-4 sessions of 6-8 hours each

---

## 📝 NEXT STEPS

1. **Immediate**: Review and confirm this execution plan
2. **Session 1**: Phase 4A (Dashboard & Analytics) - 12 UIs, 6 hours
3. **Session 2**: Phase 4B + 4C (Physical + Replenishment) - 10 UIs, 7 hours
4. **Session 3**: Phase 4D + 4E (Batch + Reports) - 9 UIs, 6 hours
5. **Session 4**: Phase 4F + 4G (Valuation + Misc) - 11 UIs, 7 hours
6. **Final**: Command button audit & cleanup

---

**Prepared By**: Astra  
**Date**: 2026-01-09 14:20 IST  
**Status**: ⏳ **AWAITING APPROVAL**
