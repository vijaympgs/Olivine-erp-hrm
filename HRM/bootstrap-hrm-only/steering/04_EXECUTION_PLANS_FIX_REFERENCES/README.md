# Execution Plans Directory

This directory contains active execution plans and implementation trackers for the Retail ERP Platform.

---

## 📁 Current Files

### **RETAIL_IMPLEMENTATION_TRACKER.md**
**Purpose**: Master tracker for all retail module implementations  
**Status**: Active  
**Scope**: Tracks UI-Model-CRUD-Validation-Persistence-UAT status for:
- Store Operations (POS, Registers, Sessions)
- Sales (Quotes, Orders, Invoices, Returns)
- Merchandising (Catalog, Hierarchy, Variants, Pricing)
- Inventory (Stock Levels, Movements, Transfers, Adjustments)
- Procurement (PR, RFQ, PO, GRN, ASN, Bills, Returns, Payments)
- Customers (Directory, Groups, Loyalty)

**Usage**: Reference this for current implementation status across all modules.

---

### **build-guide.md**
**Purpose**: ELOBS Framework reference for building new modules  
**Status**: Active  
**Scope**: Defines the standard build execution flow:
- **E**xtract: Fields and dependencies from BBP
- **L**ayout: UI structure based on template type
- **O**rganize: Folders and file scaffolding
- **B**uild: Types → Validation → Service → Hook → UI → Routing → Sidebar
- **S**ync: Module with naming and dependency rules

**Usage**: Follow this framework when implementing new modules or features.

---

## 🗑️ Removed Files (2025-12-23)

The following obsolete/completed files were removed during directory cleansing:

- `ADMIN_RESTRUCTURING_PLAN.md` (Completed Dec 22)
- `FULL_OPCO_REMOVAL_PLAN.md` (Completed - OpCo removal done)
- `ARCHITECTURE_PHASE_TASKS.md` (Generic phases, superseded)
- `LOCATION_SELECTOR_IMPLEMENTATION.md` (Old task)
- `agent.blueprints.json` (Incomplete fragment)
- `agent.playbooks.json` (Outdated branding)
- `agent.tasks.json` (Old "Olivine" project tasks)

---

## 📝 Notes

- For module-specific stabilization plans, see `.steering/11_PROCUREMENT_STABILIZATION/`
- For architectural governance, see `.steering/01_ARCH_GOVERNANCE/`
- For design system standards, see `.steering/03_DESIGN_SYSTEM/`

---

**Last Updated**: 2025-12-23
