# MASTER LOOKUP EXECUTION PLAN

**Authority**: EnterpriseGPT Governance  
**Date**: 2025-12-24  
**Status**: ⏸️ PHASE 1 READY  
**Canon**: `UI_CANON/LOOKUP_CANON.md`

---

## 🏗️ EXECUTION STRATEGY

We have divided the master lookup implementation into three distinct phases to ensure stability and focus.

**Phase 1** is the IMMEDIATE priority.

### ✅ PHASE 1 — LOOKUP PARITY (IMMEDIATE)
*Goal: Enable standard selection workflows for core retail operations using existing backend models.*

| Master Name | Backend | Action | Priority |
| :--- | :--- | :--- | :--- |
| **Item Variant / SKU** | ✅ Exists | 🔨 Create Lookup | P0 |
| **Item Category** | ✅ Exists | 🔨 Create Lookup | P0 |
| **Brand** | ✅ Exists | 🔨 Create Lookup | P0 |
| **UOM** | ✅ Exists | 🔨 Create Lookup | P0 |
| **Price List** | ✅ Exists | 🔨 Create Lookup | P0 |
| **Company** | ✅ Exists | 🔨 Create Lookup | P1 |
| **User** | ✅ Exists | 🔨 Create Lookup | P1 |
| **Location / Store** | ✅ Exists | 🔨 Enhance to Panel | P2 |
| **Warehouse** | ✅ Exists | 🔨 Enhance to Panel | P2 |

### ⚠️ PHASE 2 — FINANCE & CONTROL (BLOCKED)
*Goal: Solidify financial data selection. Requires Backend Enhancements first.*
*Hold until Phase 1 is complete.*

| Master Name | Backend | Action |
| :--- | :--- | :--- |
| **Chart of Accounts** | ✅ Exists | 🔨 Create Lookup |
| **Ledger Account** | ✅ Exists | 🔨 Create Lookup |
| **Tax Code / GST** | ⚠️ Text | 🏗️ Model Upgrade Required |
| **Payment Term** | ⚠️ Text | 🏗️ Model Upgrade Required |
| **Currency** | ⚠️ Text | 🏗️ Model Upgrade Required |

### 🛑 PHASE 3 — ADVANCED OPS (DEFERRED)
*Goal: Enterprise workflows. Requires major architecture work.*

- Approval Groups, Workflows
- Stock Batches, Serials, Bins
- Document Series, Reasons, Configs

---

## 📋 REFERENCE: LOOKUP CANON
All new lookups MUST strictly adhere to:
1.  **Container**: Use `LookupContainer.tsx`
2.  **Theme**: Match App Header (`#14162A` Gradient)
3.  **UX**: Right-Side Panel, Keyboard Nav, Auto-Focus
