# AGENT E ONBOARDING - COMPLETE REFERENCE
## HRM & CRM Module Development

**Generated**: 2026-01-04 19:50 IST
**Purpose**: Consolidated onboarding document for Agent E
**Read Order**: Sequential (01-10)

---

## TABLE OF CONTENTS

1. [01_Onboarding_Context.md](#file-01) - Context & Status
2. [02_Architecture_Rules.md](#file-02) - Architecture Rules
3. [03_Development_Standards.md](#file-03) - Development Standards
4. [04_Frontend_UI_Canon.md](#file-04) - Frontend UI Canon
5. [05_CANONICAL_RULESET.md](#file-05) - Canonical Ruleset
6. [06_ARCHITECTURAL_LOCK_REFERENCE.md](#file-06) - Architectural Lock Reference
7. [07_governance.md](#file-07) - Governance
8. [08_typography.md](#file-08) - Typography
9. [09_LOOKUP_CANON.md](#file-09) - Lookup Canon
10. [10_EMPLOYEE_UI_REFERENCE.md](#file-10) - Employee UI Reference

---

## ⚠️ AGENT E SPECIAL INSTRUCTIONS - SIMPLIFIED COMPANY HANDLING

**Context**: To avoid confusion with Licensing vs App Companies and Location complexity, use this simplified approach for HRM/CRM development:

### 🎯 SIMPLIFIED RULE FOR AGENT E:

**For ALL HRM and CRM models (Employee, Customer, Lead, Contact, Opportunity, etc.):**

1. **Add a `company` field** to every model:
   ```python
   company = models.CharField(max_length=10, default="001")
   ```

2. **Use default value "001"** for all records during development

3. **Why this approach?**
   - Avoids confusion about Company vs BusinessEntity vs Location
   - Simplifies development and testing
   - Migration to proper Company ForeignKey will happen later when integrating into main platform

4. **What this means:**
   - Don't worry about `from domain.business_entities.models import Company`
   - Don't worry about Location relationships
   - Don't worry about multi-tenancy during initial development
   - Just use `company = "001"` everywhere

5. **When you copy HRM/CRM to main platform:**
   - Viji will handle the migration from `CharField` to proper `ForeignKey(Company)`
   - Your focus: Build great HRM/CRM functionality with consistent UI

### ✅ Example Model Pattern for Agent E:

```python
class Employee(models.Model):
    employee_code = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    company = models.CharField(max_length=10, default="001")  # ← Use this
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    # ... other fields
```

```python
class Customer(models.Model):
    customer_code = models.CharField(max_length=20, unique=True)
    customer_name = models.CharField(max_length=200)
    email = models.EmailField()
    company = models.CharField(max_length=10, default="001")  # ← Use this
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    # ... other fields
```

**This is a temporary simplification for Agent E's development environment. Ignore the complex Company/Location architecture in the rest of this document - it's for the main platform integration later.**

---

## 🏗️ DEVELOPMENT STRATEGY: ENTERPRISE SHELL & APP ISOLATION

**Concept**: You are building standalone modules (HRM, CRM) that will be plugged into the main **Olivine Enterprise Shell** later.

### 1. The Shell Architecture
The core platform (`erp-platform/`) provides the "Turnkey Shell":
- **Retail** (Existing - do not touch)
- **Common** (Auth, Tenants, Permissions, Global Masters)
- **FMS** (Future)

**Your Deployment Targets:**
- **HRM/** (Start here)
- **CRM/** (Follows HRM)

### 2. Isolation Strategy
- **Develop in Isolation**: Build your modules as independent Django/React apps.
- **Simplified Dependencies**: Do NOT depend on Retail or FMS logic.
- **Simplified Models**: Use `company = "001"` (CharField) as per the instructions above.

### 3. Integration Plan (The "Snap-In")
Once your module is mature:
1.  **Copy**: The entire `hrm/` or `crm/` folder is copied into the Shell's `apps/` directory.
2.  **Wire Up**: We map your simple `company` field to the Shell's real `Company` tenant.
3.  **Enable**: We add your URLs to the main `urls.py`.

**✅ YOUR JOB:** Build a robust, beautiful module inside its own folder. Don't worry about the Shell's complexity.

---





-
<a name="file-01"></a>
## FILE: 01_Onboarding_Context.md



# ONBOARDING FOR AGENT E: STEP 1 - Context & Status

## 👋 WELCOME: Olivine Retail ERP Platform - HRM & CRM Module Development

You are **Agent E**, responsible for developing **HRM (Human Resource Management)** and **CRM (Customer Relationship Management)** modules for the **Olivine Retail ERP Platform**, a multi-tenant, enterprise-grade management system.

**Your Focus Areas:**
1. **HRM**: Employee Management, Payroll, Attendance, Leave, Performance
2. **CRM**: Customer Management, Leads, Contacts, Opportunities, Sales Pipeline

---

## 🎯 PRIMARY GOALS

1. **Strict Architecture**: Clean separation between "Canonical Masters" (Global Definitions) and "Operational Data" (Transactions/Per-Company).
2. **No "OperatingCompany" Model**: We use a `Company` model for operations. "Business Entity" is strictly for licensing/admin only.
3. **Enterprise UI**: VB.NET-inspired, keyboard-heavy, high-density UI using React + Tailwind + Vite.
4. **Backend Integrity**: Django DRF with strict service layers and domain separation.
5. **UI Consistency**: Match the Employee Master UI patterns exactly for all CRM forms.

---

## 📅 CURRENT STATUS

**Agent E Scope**: HRM & CRM Module Development
**HRM Status**: Employee Master UI completed (reference implementation)
**CRM Status**: Ready to begin (Customer, Lead, Contact, Opportunity)

### 🎯 IMMEDIATE OBJECTIVE
Build CRM module forms following the exact UI patterns established in the Employee Master implementation.

### 📋 YOUR TASK LIST
1. **Study Reference Implementation**
   - Review `10_EMPLOYEE_UI_REFERENCE.md` for complete UI patterns
   - Understand tab structure, styling, validation patterns
   - Note the 2-column grid layout and form field conventions

2. **CRM Module Development**
   - Customer Master (similar to Employee Master)
   - Lead Management (simpler, fewer tabs)
   - Contact Management (with Company relationship)
   - Opportunity/Pipeline Management

3. **UI Consistency Requirements**
   - Use identical Tailwind classes from Employee Master
   - Maintain 2-column grid layout (`grid grid-cols-2 gap-6`)
   - Follow exact header pattern (photo/logo + name + code + status)
   - Use same validation and error display patterns

---

## 🛠️ TECH STACK

- **Frontend**: React 18, TypeScript, Tailwind CSS, Lucide Icons, Vite
- **Backend**: Python 3.10+, Django 4+, Django REST Framework (DRF)
- **Database**: PostgreSQL (Production), SQLite (Dev)
- **Architecture**: Modular Monolith (Domains: HRM, CRM, Retail, FMS)

---

## ⚠️ CRITICAL "DO NOTs"

1. **Do NOT edit `01practice-v2`**: This is a read-only reference codebase.
2. **Do NOT create "OperatingCompany" models**: We removed this abstraction. Use `Company`.
3. **Do NOT mix Business Entity and Company**: 
   - `BusinessEntity` = Admin/Billing only
   - `Company` = Actual tenant where users log in and work
4. **Do NOT deviate from Employee Master UI patterns**: Match styling exactly.
5. **Do NOT create custom lookup components**: Always use `LookupContainer.tsx`.

---

## 🎨 UI PATTERN REFERENCE

**Employee Master** is your reference implementation. Study it carefully:
- File: `10_EMPLOYEE_UI_REFERENCE.md`
- Source: `frontend/core/ui_canon/frontend/ui/components/employee/EmployeeForm.tsx`

**Key Patterns to Replicate:**
- Header: Photo + Name + Code + Status Badge
- Tabs: Conditional rendering based on `activeSection`
- Grid: Always `grid grid-cols-2 gap-6`
- Labels: Always `block font-medium mb-1`
- Inputs: Always `w-full rounded border px-3 py-2`
- Errors: Always `text-red-600 text-xs mt-1`

---

## 📚 NEXT STEPS

1. Read files 01-10 in sequence
2. Study `10_EMPLOYEE_UI_REFERENCE.md` thoroughly
3. Begin with Customer Master form (adapt Employee patterns)
4. Follow ELOBS workflow: Extract → Layout → Organize → Build → Sync

---

**Welcome aboard, Agent E! Let's build world-class HRM & CRM modules.** 🚀




-
<a name="file-02"></a>
## FILE: 02_Architecture_Rules.md



# ONBOARDING FOR AGENTS: STEP 2 - Architecture Rules

## 🔒 THE RULE (NON-NEGOTIABLE)

```
business_entities = LICENSING METADATA ONLY
company = OPERATIONAL MASTERS ONLY
```

**NO EXCEPTIONS. NO INTERPRETATION.**

---

## 📋 OPERATIONAL MODELS (Use domain.company)

### Canonical Models in `domain.company.models`:

| Model | Purpose | DB Table | Records |
|-------|---------|----------|---------|
| `Category` | Product categories | `be_category` | 7 |
| `Brand` | Product brands | `be_brand` | 21 |
| `TaxClass` | Tax classifications | `be_tax_class` | 5 |
| `ItemMaster` | **CANONICAL ITEM MODEL** | `be_item_master` | 302 |
| `OperationalSupplier` | Suppliers (alias: `Supplier`) | `be_supplier` | 145 |
| `OperationalCustomer` | Customers (alias: `Customer`) | `be_customer` | 170 |
| `Location` | Store/warehouse locations | `be_location` | 28 |
| `Attribute` | Product attributes | `be_attribute` | - |
| `AttributeValue` | Attribute values | `be_attribute_value` | - |
| `UnitOfMeasure` | Units of measure | `be_uom` | - |
| `PriceList` | Price lists | `be_price_list` | - |

---

## ✅ CORRECT IMPORT PATTERNS

### ✅ Seeds, APIs, Services, Admin:
```python
from domain.business_entities.models import Company  # ONLY for licensing
from domain.company.models import (
    ItemMaster,
    Category,
    Brand,
    TaxClass,
    Location,
    OperationalSupplier as Supplier,
    OperationalCustomer as Customer,
    # ... other operational models
)
```

### ❌ WRONG (DO NOT DO THIS):
```python
# ❌ NEVER import operational models from business_entities
from domain.business_entities.models import (
    ItemMaster,  # ❌ WRONG
    Supplier,    # ❌ WRONG
    Customer,    # ❌ WRONG
    Category,    # ❌ WRONG
)
```

---

## 🚫 DEPRECATED MODELS

### In `domain.company.models`:
- ❌ `Item` - DEPRECATED (use `ItemMaster`)
- ❌ `Supplier` (legacy) - DEPRECATED (use `OperationalSupplier`)
- ❌ `Customer` (legacy) - DEPRECATED (use `OperationalCustomer`)

### In `domain.business_entities.models`:
- ⚠️ Operational models still exist but are DEPRECATED
- ⚠️ DO NOT USE - they will be removed in future cleanup

---

## 📊 ITEM MODEL DECISION

**CANONICAL ITEM MODEL**: `ItemMaster` (domain.company)

| Model | Status | Records | Purpose |
|-------|--------|---------|---------|
| `ItemMaster` | ✅ CANONICAL | 302 | **USE THIS** |
| `Item` | ❌ DEPRECATED | 0 | Legacy, will be removed |

**Why ItemMaster?**
- Has actual data (302 records)
- Used by procurement, inventory, POS
- Seed script uses it
- Extensive relationships

---

## 🔧 AFFECTED MODULES

### Updated Files:
1. `backend/domain/company/models.py` - Added operational models
2. `backend/domain/company/views.py` - Updated imports
3. `seed/seed_enterprise_masters.py` - Updated imports

### Modules Using ItemMaster:
- ✅ Procurement (`domain.procurement`)
- ✅ Inventory (`domain.inventory`)
- ✅ POS (`domain.pos`)
- ✅ Sales (`domain.sales`)

---

## 🎯 VERIFICATION COMMANDS

### Check Model Location:
```python
from domain.company.models import ItemMaster, OperationalSupplier
print(f"ItemMaster app: {ItemMaster._meta.app_label}")  # Should be 'company'
print(f"ItemMaster table: {ItemMaster._meta.db_table}")  # Should be 'be_item_master'
print(f"ItemMaster count: {ItemMaster.objects.count()}")  # Should be 302
```

### Check API Endpoints:
```bash
curl http://localhost:8000/api/suppliers/?status=ACTIVE
curl http://localhost:8000/api/items/
```

---

## 📝 FUTURE CLEANUP TASKS

1. **Remove deprecated models from `business_entities/models.py`**
   - Category, Brand, TaxClass, ItemMaster, Supplier, Customer
   - LOW RISK (not used anywhere)

2. **Remove legacy models from `company/models.py`**
   - Legacy Item, Supplier, Customer
   - MEDIUM RISK (check for any remaining references)

3. **Update Django Admin**
   - Register operational models in `company/admin.py`
   - Remove from `business_entities/admin.py`

---

## 🚨 CRITICAL REMINDERS

1. **NEVER** import operational models from `business_entities`
2. **ALWAYS** use `ItemMaster` (not `Item`)
3. **ALWAYS** use `OperationalSupplier`/`OperationalCustomer` (aliased as Supplier/Customer)
4. **Company** is the ONLY model that should be in `business_entities` (for licensing)
5. **NO** table renaming (keep `be_*` prefixes)
6. **NO** data migration needed (same tables)

---

## 📞 ESCALATION

If you encounter:
- Imports from `business_entities` for operational models
- References to deprecated `Item` model
- Confusion about which model to use

**STOP. ASK. DO NOT GUESS.**




-
<a name="file-03"></a>
## FILE: 03_Development_Standards.md



# ONBOARDING FOR AGENTS: STEP 3 - Development Standards

## 📜 CANONICAL RULESET: Olivine Retail ERP Platform
**Single Source of Truth for Governance, Architecture, and Execution**

---

## 🏛️ 1. ARCHITECTURAL GOVERNANCE (NON-NEGOTIABLE)
*Source: .steering/01_ARCH_GOVERNANCE/README2_IMPPORTANT_FORAGENTS.md, .steering/01_ARCH_GOVERNANCE/README2_Stabilization_Checklist.md*

### **Terminology & Entity Lock**
- **Business Entity (Legal)**: Top-level legal oversight. Admin-only. NEVER used in Login or Transactions.
- **Company (Operational)**: First-class operational entity. Login lists ONLY Companies. All transactions (PO, RFQ, etc.) bind to `Company`.
- **Location**: Child of Company. Selected globally via the Global Selector.
- **OpCo Removal**: The abstraction "OperatingCompany" has been fully removed. Use `Company` directly.

### **Governance Flags & Access Control**
- **🔒 Platform Only**: A GOVERNANCE FLAG (not a data category).
  - **WHO**: Records can be created/modified ONLY by Platform Superusers.
  - **PURPOSE**: Defines tenant boundaries and protects core identity from business-level access.
  - **NOT Licensing**: Does not mean record is licensing data, auto-created, or non-operational.
  - **Company Status**: Company IS the operational tenant and participates in ALL transactions, even though it is "Platform Only" (managed via admin-only).
- **Licensing vs. Governance**: 
  - Licensing validates **QUANTITY** (how many Companies MAY exist).
  - Governance (Platform Only) validates **AUTHORITY** (who MAY edit them).
  - Confusing these two violates the core architecture.

### **Data Access & Scoping rules**
- **Queryset Isolation**: All backend ViewSets must strictly filter by the active user's `currentCompanyId`.
- **Location Integrity**: Requesting/Delivery locations must be validated against the Document Header's Company.
- **User Context**: Creator/Modifier fields MUST be auto-populated from `request.user`; never trust frontend input for authorship.

### **Master Data Enforcement**
- **Canonical vs. Operational**: Input Canonical IDs (`item_id`, `uom_id`); Backend resolves to Operational binding if required.
- **Hard References**: Store Foreign Keys to Operational entities (`CompanyItem`) where applicable, or bind directly to `Company` and `ItemMaster`.
- **Reference Build Protection**: `01practice-v2` / `02practice` are **READ-ONLY**. Do NOT modify any files in these directories mid-session.

---

## ⚙️ 2. BACKEND & API STANDARDS
*Source: .steering/01_ARCH_GOVERNANCE/system-rules.md, backend/domain patterns*

### **Business Logic Separation (Mandatory)**
- **models.py**: Data structure and persistence ONLY.
- **services.py / business_rules/**: Authoritative business logic and validation. 
- **views.py**: Thin orchestration (Request/Response wiring only).
- **selectors.py**: Optimized read-only queries (KPIs, availability).

### **DRF Router Registration**
- **Explicit Basename**: Always specify the `basename` in `router.register`.
  - *Correct*: `router.register(r'rfqs', RFQViewSet, basename='rfq')`
  - *Why*: Prevents `AssertionError` when ViewSets use `get_queryset()` or lack a static `queryset` attribute.

### **Action-Driven Workflows**
- **Status Transitions**: Explicitly handle status changes (`DRAFT` -> `SUBMITTED`) via `@action` endpoints, not generic `PATCH` updates.
- **Validation**: Enforce business rules (e.g., "At least one line item required") before allowing transitions.

---

## ⚡ 3. EXECUTION FLOW (ELOBS)
*Source: .steering/01_ARCH_GOVERNANCE/agent.olivine_ruleset.md*

Every AI task must follow the **ELOBS** sequence:
1.  **E (Extract)**: Read BBP fields, relationships, and business rules first.
2.  **L (Layout)**: Determine the module structure (Simple vs. Complex Master/Transaction).
3.  **O (Organize)**: Scaffolding files in `src/modules/<module>/`.
4.  **B (Build)**: Sequence: Types → Schema → Services → Hooks → UI → Routing → Sidebar.
5.  **S (Sync)**: Cross-check against BBP and canonical references.

---

## 📖 4. DESIGN & TYPOGRAPHY (STRICT)
*Source: .steering/03_DESIGN_SYSTEM/typography.md*

- **Primary Font**: `Inter`, sans-serif (No overrides).
- **Weights**: 400 (Regular), 500 (Medium), 600 (Semibold).
- **Scale**: Title (20-22px), Body (13-14px), Table/Label (12-13px).
- **Table Numerics**: Must use tabular numerals (`font-feature-settings: "tnum"`).

---

## 🤖 5. RESPONSE CONTRACT & EXECUTION
*Source: .steering/02_PROMPT_LIBRARY/PROMPT_GUIDE.MD, .steering/02_PROMPT_LIBRARY/EXECUTION_CONTRACT.md*

- **Architect Mode**: Responses must be precise, authoritative, and implementation-safe.
- **Execution Contract**: Adhere strictly to the **[EXECUTION CONTRACT](../02_PROMPT_LIBRARY/EXECUTION_CONTRACT.md)** for all UI-only implementation tasks.
- **Output Format**: Expert guidance must be delivered in a SINGLE fenced prompt block.
- **Verdict Priority**: Every review MUST start with **APPROVED**, **APPROVED WITH NOTES**, or **REJECTED**.

---

## 🧪 6. QUALITY & TESTING STANDARDS
*Source: .steering/09_QUALITY_GOVERNANCE/TESTING_STANDARDS.md*

- **Correctness Properties**: Define formal invariants (Consistency, Preservation, Merging) for any complex state or logic.
- **Dual Testing**: Combine Unit Tests (Edge cases) with Property-Based Testing (Universal invariants, 100+ iterations).
- **Traceability**: Every task must map to a Requirement ID and every test must reference a Property.




-
<a name="file-04"></a>
## FILE: 04_Frontend_UI_Canon.md



# ONBOARDING FOR AGENTS: STEP 4 - Frontend & UI Canon

## SPA STRUCTURE (Mandatory)

This structure is optimized for:
- Vite + React + TypeScript
- Tailwind CSS
- Enterprise-scale modular growth

### src/ (Application Source Root)
All runtime SPA code **must live inside `src/`**.

```
src/
├── app/          # Global providers (Auth, Layout). NO business logic.
├── modules/      # Domain-Driven Modules (One folder per domain).
├── components/   # Shared UI (Buttons, Inputs, Tables). Props only.
├── services/     # API Infrastructure (Auth, HTTP).
├── store/        # Global State (Zustand/Redux).
├── styles/       # Tailwind + Global CSS.
├── hooks/        # Shared Hooks.
├── utils/        # Formatters, Validators.
```

### Module Design (src/modules/)
Each business domain mirrors backend domains.
```
src/modules/procurement/
├── pages/        # Route screens
├── components/   # Module-specific UI
├── services/     # Module-specific API calls
├── hooks/        # Module-specific logic
├── types.ts      # Domain interfaces
└── index.ts      # Public API
```

---

## 🎨 UI CANON: LOOKUPS & MODALS (Strict)

**RULE**: Lookups are an extension of Sidebar + App Header, NOT independent island components.

**IMPLEMENTATION**: All lookups **MUST use `LookupContainer.tsx`**.

### Compliance Checklist:
1.  **Theme Identity**: Header uses EXACT SAME background gradient (`#14162A` → `#101223`) and Brand Color (`#22D3EE`) as the App Header.
2.  **Typography**: Use `Inter`. No custom fonts.
3.  **Interaction**: Keyboard-first (Escape closes, Auto-focus search).
4.  **Reusability**: Use generic `LookupContainer`. Do not build custom modal shells.

### Usage Example:
```typescript
import { LookupContainer } from '../../ui/components/LookupContainer';

export const ProductLookupModal = ({ isOpen, onClose, onSelect }) => (
  <LookupContainer
    isOpen={isOpen}
    onClose={onClose}
    title="Product Lookup"
    icon={<Package size={20} />} // Lucide icon
    searchBar={/* ... */}
  >
    {/* Results Table */}
  </LookupContainer>
);
```

### ❌ PROHIBITIONS:
- ❌ Use `bg-[#0078d4]` or hardcoded blues.
- ❌ Create custom modal headers that ignore the theme.
- ❌ Mix light headers with dark sidebar themes.

---

## VB.NET STYLE TOOLBAR
All "Document" pages (PO, Invoice, etc.) must use the `TransactionToolbar`.
- **Location**: Fixed at the top (Sticky).
- **Style**: High contrast, functional buttons.
- **Shortcuts**: Map F-keys (F1-F12) to actions where possible.

## TYPOGRAPHY
- **Primary Font**: `Inter`.
- **Weights**: 400 (Regular), 500 (Medium), 600 (SemiBold).
- **Numbers**: Use `tnum` (Tabular Numerals) for all data grids.

## NON-NEGOTIABLE RULES
1. One module = one domain.
2. No circular imports.
3. No cross-module component access (use shared `components/` if needed).
4. Pages never talk directly to HTTP (use `services/`).




-
<a name="file-05"></a>
## FILE: 05_CANONICAL_RULESET.md



# 📜 CANONICAL RULESET: Olivine Retail ERP Platform
**Single Source of Truth for Governance, Architecture, and Execution**

---

## 🏛️ 1. ARCHITECTURAL GOVERNANCE (NON-NEGOTIABLE)
*Source: .steering/01_ARCH_GOVERNANCE/README2_IMPPORTANT_FORAGENTS.md, .steering/01_ARCH_GOVERNANCE/README2_Stabilization_Checklist.md*

### **Terminology & Entity Lock**
- **Business Entity (Legal)**: Top-level legal oversight. Admin-only. NEVER used in Login or Transactions.
- **Company (Operational)**: First-class operational entity. Login lists ONLY Companies. All transactions (PO, RFQ, etc.) bind to `Company`.
- **Location**: Child of Company. Selected globally via the Global Selector.
- **OpCo Removal**: The abstraction "OperatingCompany" has been fully removed. Use `Company` directly.

### **Governance Flags & Access Control**
- **🔒 Platform Only**: A GOVERNANCE FLAG (not a data category).
  - **WHO**: Records can be created/modified ONLY by Platform Superusers.
  - **PURPOSE**: Defines tenant boundaries and protects core identity from business-level access.
  - **NOT Licensing**: Does not mean record is licensing data, auto-created, or non-operational.
  - **Company Status**: Company IS the operational tenant and participates in ALL transactions, even though it is "Platform Only" (managed via admin-only).
- **Licensing vs. Governance**: 
  - Licensing validates **QUANTITY** (how many Companies MAY exist).
  - Governance (Platform Only) validates **AUTHORITY** (who MAY edit them).
  - Confusing these two violates the core architecture.

### **Data Access & Scoping rules**
- **Queryset Isolation**: All backend ViewSets must strictly filter by the active user's `currentCompanyId`.
- **Location Integrity**: Requesting/Delivery locations must be validated against the Document Header's Company.
- **User Context**: Creator/Modifier fields MUST be auto-populated from `request.user`; never trust frontend input for authorship.

### **Master Data Enforcement**
- **Canonical vs. Operational**: Input Canonical IDs (`item_id`, `uom_id`); Backend resolves to Operational binding if required.
- **Hard References**: Store Foreign Keys to Operational entities (`CompanyItem`) where applicable, or bind directly to `Company` and `ItemMaster`.
- **Reference Build Protection**: `01practice-v2` / `02practice` are **READ-ONLY**. Do NOT modify any files in these directories mid-session.

---

## ⚙️ 2. BACKEND & API STANDARDS
*Source: .steering/01_ARCH_GOVERNANCE/system-rules.md, backend/domain patterns*

### **Business Logic Separation (Mandatory)**
- **models.py**: Data structure and persistence ONLY.
- **services.py / business_rules/**: Authoritative business logic and validation. 
- **views.py**: Thin orchestration (Request/Response wiring only).
- **selectors.py**: Optimized read-only queries (KPIs, availability).

### **DRF Router Registration**
- **Explicit Basename**: Always specify the `basename` in `router.register`.
  - *Correct*: `router.register(r'rfqs', RFQViewSet, basename='rfq')`
  - *Why*: Prevents `AssertionError` when ViewSets use `get_queryset()` or lack a static `queryset` attribute.

### **Action-Driven Workflows**
- **Status Transitions**: Explicitly handle status changes (`DRAFT` -> `SUBMITTED`) via `@action` endpoints, not generic `PATCH` updates.
- **Validation**: Enforce business rules (e.g., "At least one line item required") before allowing transitions.

---

## 🎨 3. FRONTEND SPA ARCHITECTURE
*Source: .steering/01_ARCH_GOVERNANCE/README3_IMPPORTANT_FORAGENTS_SPA_STRUCTURE.md, docs/reference/Refer_this_before_new_UI_module.md*

### **Directory Structure (src/)**
- `app/`: Global providers and layout logic (No business/API logic).
- `modules/`: Domain-driven logic (Pages, Components, Services, Hooks, Types).
- `components/`: Shared, domain-agnostic UI (Props-driven only, no API calls).
- `services/`: Shared infrastructure (Auth, HTTP client).

### **Module Design Patterns**
- **One Module = One Domain**: Follow backend domain boundaries.
- **Service Isolation**: Pages must never talk directly to HTTP. Always use a dedicated Service.
- **No Circular Imports**: Strictly enforced separation between modules.
- **UI State**: Use `AuthContext` for `currentCompanyId` and `currentLocationId`.

### **Design Aesthetics**
- **Premium Enterprise UI**: Use modern typography (Inter), subtle gradients, and high-contrast headers.
- **VB.NET Inspired Toolbar**: Standardized `TransactionToolbar` for all document-level pages (F1-F12 shortcuts).
- **Sticky Layouts**: The AppHeader and TransactionToolbar must remain fixed at the top.

---

## ⚡ 4. EXECUTION FLOW (ELOBS)
*Source: .steering/01_ARCH_GOVERNANCE/agent.olivine_ruleset.md*

Every AI task must follow the **ELOBS** sequence:
1.  **E (Extract)**: Read BBP fields, relationships, and business rules first.
2.  **L (Layout)**: Determine the module structure (Simple vs. Complex Master/Transaction).
3.  **O (Organize)**: Scaffolding files in `src/modules/<module>/`.
4.  **B (Build)**: Sequence: Types → Schema → Services → Hooks → UI → Routing → Sidebar.
5.  **S (Sync)**: Cross-check against BBP and canonical references.

---

## 📖 5. DESIGN & TYPOGRAPHY (STRICT)
*Source: .steering/03_DESIGN_SYSTEM/typography.md*

- **Primary Font**: `Inter`, sans-serif (No overrides).
- **Weights**: 400 (Regular), 500 (Medium), 600 (Semibold).
- **Scale**: Title (20-22px), Body (13-14px), Table/Label (12-13px).
- **Table Numerics**: Must use tabular numerals (`font-feature-settings: "tnum"`).

---

## 🤖 6. RESPONSE CONTRACT & EXECUTION
*Source: .steering/02_PROMPT_LIBRARY/PROMPT_GUIDE.MD, .steering/02_PROMPT_LIBRARY/EXECUTION_CONTRACT.md*

- **Architect Mode**: Responses must be precise, authoritative, and implementation-safe.
- **Execution Contract**: Adhere strictly to the **[EXECUTION CONTRACT](../02_PROMPT_LIBRARY/EXECUTION_CONTRACT.md)** for all UI-only implementation tasks.
- **Output Format**: Expert guidance must be delivered in a SINGLE fenced prompt block.
- **Verdict Priority**: Every review MUST start with **APPROVED**, **APPROVED WITH NOTES**, or **REJECTED**.

---

## 🧪 7. QUALITY & TESTING STANDARDS
*Source: .steering/09_QUALITY_GOVERNANCE/TESTING_STANDARDS.md*

- **Correctness Properties**: Define formal invariants (Consistency, Preservation, Merging) for any complex state or logic.
- **Dual Testing**: Combine Unit Tests (Edge cases) with Property-Based Testing (Universal invariants, 100+ iterations).
- **Traceability**: Every task must map to a Requirement ID and every test must reference a Property.

---

**Last Synchronized**: 2025-12-23  
**Status**: ⚡ ACTIVE AUTHORITY




-
<a name="file-06"></a>
## FILE: 06_ARCHITECTURAL_LOCK_REFERENCE.md



# ARCHITECTURAL LOCK - QUICK REFERENCE

## 🔒 THE RULE (NON-NEGOTIABLE)

```
business_entities = LICENSING METADATA ONLY
company = OPERATIONAL MASTERS ONLY
```

**NO EXCEPTIONS. NO INTERPRETATION.**

---

## 📋 OPERATIONAL MODELS (Use domain.company)

### Canonical Models in `domain.company.models`:

| Model | Purpose | DB Table | Records |
|-------|---------|----------|---------|
| `Category` | Product categories | `be_category` | 7 |
| `Brand` | Product brands | `be_brand` | 21 |
| `TaxClass` | Tax classifications | `be_tax_class` | 5 |
| `ItemMaster` | **CANONICAL ITEM MODEL** | `be_item_master` | 302 |
| `OperationalSupplier` | Suppliers (alias: `Supplier`) | `be_supplier` | 145 |
| `OperationalCustomer` | Customers (alias: `Customer`) | `be_customer` | 170 |
| `Location` | Store/warehouse locations | `be_location` | 28 |
| `Attribute` | Product attributes | `be_attribute` | - |
| `AttributeValue` | Attribute values | `be_attribute_value` | - |
| `UnitOfMeasure` | Units of measure | `be_uom` | - |
| `PriceList` | Price lists | `be_price_list` | - |

---

## ✅ CORRECT IMPORT PATTERNS

### ✅ Seeds, APIs, Services, Admin:
```python
from domain.business_entities.models import Company  # ONLY for licensing
from domain.company.models import (
    ItemMaster,
    Category,
    Brand,
    TaxClass,
    Location,
    OperationalSupplier as Supplier,
    OperationalCustomer as Customer,
    # ... other operational models
)
```

### ❌ WRONG (DO NOT DO THIS):
```python
# ❌ NEVER import operational models from business_entities
from domain.business_entities.models import (
    ItemMaster,  # ❌ WRONG
    Supplier,    # ❌ WRONG
    Customer,    # ❌ WRONG
    Category,    # ❌ WRONG
)
```

---

## 🚫 DEPRECATED MODELS

### In `domain.company.models`:
- ❌ `Item` - DEPRECATED (use `ItemMaster`)
- ❌ `Supplier` (legacy) - DEPRECATED (use `OperationalSupplier`)
- ❌ `Customer` (legacy) - DEPRECATED (use `OperationalCustomer`)

### In `domain.business_entities.models`:
- ⚠️ Operational models still exist but are DEPRECATED
- ⚠️ DO NOT USE - they will be removed in future cleanup

---

## 📊 ITEM MODEL DECISION

**CANONICAL ITEM MODEL**: `ItemMaster` (domain.company)

| Model | Status | Records | Purpose |
|-------|--------|---------|---------|
| `ItemMaster` | ✅ CANONICAL | 302 | **USE THIS** |
| `Item` | ❌ DEPRECATED | 0 | Legacy, will be removed |

**Why ItemMaster?**
- Has actual data (302 records)
- Used by procurement, inventory, POS
- Seed script uses it
- Extensive relationships

---

## 🔧 AFFECTED MODULES

### Updated Files:
1. `backend/domain/company/models.py` - Added operational models
2. `backend/domain/company/views.py` - Updated imports
3. `seed/seed_enterprise_masters.py` - Updated imports

### Modules Using ItemMaster:
- ✅ Procurement (`domain.procurement`)
- ✅ Inventory (`domain.inventory`)
- ✅ POS (`domain.pos`)
- ✅ Sales (`domain.sales`)

---

## 🎯 VERIFICATION COMMANDS

### Check Model Location:
```python
from domain.company.models import ItemMaster, OperationalSupplier
print(f"ItemMaster app: {ItemMaster._meta.app_label}")  # Should be 'company'
print(f"ItemMaster table: {ItemMaster._meta.db_table}")  # Should be 'be_item_master'
print(f"ItemMaster count: {ItemMaster.objects.count()}")  # Should be 302
```

### Check API Endpoints:
```bash
curl http://localhost:8000/api/suppliers/?status=ACTIVE
curl http://localhost:8000/api/items/
```

---

## 📝 FUTURE CLEANUP TASKS

1. **Remove deprecated models from `business_entities/models.py`**
   - Category, Brand, TaxClass, ItemMaster, Supplier, Customer
   - LOW RISK (not used anywhere)

2. **Remove legacy models from `company/models.py`**
   - Legacy Item, Supplier, Customer
   - MEDIUM RISK (check for any remaining references)

3. **Update Django Admin**
   - Register operational models in `company/admin.py`
   - Remove from `business_entities/admin.py`

---

## 🚨 CRITICAL REMINDERS

1. **NEVER** import operational models from `business_entities`
2. **ALWAYS** use `ItemMaster` (not `Item`)
3. **ALWAYS** use `OperationalSupplier`/`OperationalCustomer` (aliased as Supplier/Customer)
4. **Company** is the ONLY model that should be in `business_entities` (for licensing)
5. **NO** table renaming (keep `be_*` prefixes)
6. **NO** data migration needed (same tables)

---

## 📞 ESCALATION

If you encounter:
- Imports from `business_entities` for operational models
- References to deprecated `Item` model
- Confusion about which model to use

**STOP. ASK. DO NOT GUESS.**

**Authority**: Viji  
**Agent Role**: Executor ONLY

---

**Last Updated**: 2025-12-23  
**Status**: LOCKED - NO CHANGES WITHOUT APPROVAL




-
<a name="file-07"></a>
## FILE: 07_governance.md



# EnterpriseGPT UI Canon — Transaction Toolbar & Theming

This document consolidates all approved prompts for implementing
the **Enterprise Transaction Header Toolbar**, **Global Theme Selector**,
and **Lookup Shortcut Enhancements**.

Use this file as a **single source of truth** for AI agents, UI engineers,
and governance reviews.

---

## AGENT PROMPT — Enterprise Transaction Header Toolbar + Global Theme Selector

You are implementing core UI infrastructure for an EnterpriseGPT application.

This includes:
1) A reusable Transaction Header Toolbar for all transaction pages
2) A Global App-Level Theme Selector in the main application header

DO NOT implement backend logic or individual action handlers.
Focus strictly on UI, behavior contracts, states, accessibility, and theming.

---

## PART A — TRANSACTION HEADER TOOLBAR

### A1. Purpose

Replace bottom Save / Submit buttons with a compact, Excel / VB.NET–style
toolbar embedded directly into the transaction page header.

Applies to:
PR, PO, GRN, Invoice, Journal, and all transactional screens.

---

### A2. Placement & Structure

- Render inside the transaction page header
- Positioned directly below the transaction title and status (Draft, Approved, etc.)
- Single-line horizontal toolbar
- Always visible (no scroll dependency)
- Bottom Save / Submit buttons must be removed entirely

Actions (fixed order, icon-only):

New, Edit, Save, Clear, Cancel, Clone, View, Submit, Authorize, Amend

Icons only; no text labels under icons  
Text appears only via tooltip

---

### A3. Function Keys (Mandatory)

- New            → F2  
- Edit           → F4  
- Save           → F8  
- Clear / Reset  → F5  
- Cancel         → Esc  
- Clone          → F6  
- View           → F7  
- Submit / Post  → F9  
- Authorize      → F10  
- Amend / Revise → Ctrl + D  

Keyboard shortcuts must work anywhere within the transaction page,
including when focus is inside form fields.

---

### A4. State → Action Enable Matrix

**Draft**
- Enabled: New, Edit, Save, Clear, Cancel, Clone, View, Submit
- Disabled: Authorize, Amend

**Submitted**
- Enabled: View, Cancel
- Conditional: Authorize (role-based)
- Disabled: New, Edit, Save, Clear, Clone, Amend

**Approved / Authorized**
- Enabled: View, Amend
- Disabled: New, Edit, Save, Clear, Cancel, Clone, Submit, Authorize

**Cancelled**
- Enabled: View, Clone
- Disabled: All others

Disabled actions must remain visible but muted.

---

### A5. Visual Style (VB / VB.NET Soul, Modernized)

- Compact toolbar height: ~40–44px
- Soft rectangular buttons (6–8px radius)
- Subtle bevel / pressed-in active state
- Thin vertical separators between action groups
- Icons monochrome by default
- Accent color on hover / active only
- No Material UI or mobile-first styling

Grouping:

[ New | Edit | Save ] | [ Clear | Cancel ] | [ Clone | View ] | [ Submit | Authorize | Amend ]

---

### A6. Design Tokens (Reference)

**Spacing**
- Toolbar padding: px-3 py-1.5
- Button size: h-8 w-8
- Icon size: 16–18px
- Gap between buttons: gap-1
- Group separator margin: mx-2

**Radius**
- Button radius: rounded-md

**Typography (Tooltips)**
- text-xs
- font-medium

**Transitions**
- transition-colors transition-shadow duration-150 ease-out

---

### A7. Accessibility & Keyboard Rules

- All buttons must be focusable via Tab
- Subtle visible focus ring required
- Tooltips accessible via keyboard focus
- Icons must include aria-label
- Esc always prioritizes Cancel when enabled
- Disabled actions must not be focusable
- Keyboard shortcuts must not conflict with browser defaults

---

## PART B — GLOBAL APP-LEVEL THEME SELECTOR

### B1. Purpose

Introduce a global theme selector that controls the entire application UI.

Theme changes must apply via a full UI refresh
without losing page or transaction state.

---

### B2. Placement

- Located in the main Application Header
- Right-aligned near user profile / settings
- Visible across all modules (Retail, POS, FMS, HRM, CRM)

---

### B3. Theme Options

Exactly three options:

- Light
- Dark
- System (default)

System theme:
- Follows OS preference
- Evaluated on application load only

---

### B4. Selection & Refresh Behavior

- Selecting a theme updates state immediately
- Application performs a full UI refresh
- No logout
- No route reset
- No transaction data loss
- Current page and form state must be preserved

---

### B5. Persistence Contract

- Theme preference must persist:
  - Page reload
  - Browser restart
  - Logout / login
- User preference overrides system default

---

### B6. Visual Style

- Minimal control (icon toggle or compact dropdown)
- No persistent text labels
- Tooltip indicates current theme:
  - “Theme: Light”
  - “Theme: Dark”
  - “Theme: System”
- Must not dominate the header visually

---

### B7. Interaction Rules

- Fully keyboard accessible
- Focus-visible compliant
- Must not interfere with transaction function keys
- No automatic theme switching unless user explicitly selects

---

## PART C — TOOLBAR ENHANCEMENT: LOOKUP SHORTCUTS

### C1. Purpose

Provide fast, keyboard-driven access to commonly used master lookups
directly from the transaction header toolbar.

Designed to mimic classic desktop ERP lookup behavior.

---

### C2. Lookup Shortcuts (Canonical)

- Customer Lookup
- Supplier Lookup
- Item Lookup
- Location Lookup

(Future-extensible: Warehouse, Tax, Price List, Ledger)

Icons only; no labels.

---

### C3. Placement & Grouping

- Appear within the same transaction header toolbar
- Positioned after core CRUD actions and before workflow actions
- Separated by a thin vertical divider

Recommended grouping:

[ Core CRUD ] | [ Reset / Cancel ] | [ Clone / View ] | [ Lookups ] | [ Workflow ]

---

### C4. Function Keys (Lookups)

- Customer Lookup  → F11
- Supplier Lookup  → Shift + F11
- Item Lookup      → F12
- Location Lookup  → Shift + F12

Shortcuts must:
- Work anywhere within the transaction page
- Be shown in tooltips
- Not conflict with CRUD keys

Tooltip example:
“Item Lookup (F12)”

---

### C5. Visual Style

- Same size, spacing, and style as other toolbar icons
- Monochrome default
- Accent color on hover
- Utility-focused appearance (not primary actions)

---

### C6. Enable / Disable Behavior

- Lookup shortcuts must support enable/disable via user permissions
- Disabled lookups:
  - Remain visible
  - Appear muted
  - Are non-focusable
- Permission logic not implemented (UI-only contract)

---

### C7. Accessibility & State Awareness

- Enabled lookups keyboard accessible
- Disabled lookups not focusable
- aria-label required for all icons
- Typically enabled in Draft / Edit states
- May be disabled in Approved / Cancelled states (UI indication only)

---

## OUT OF SCOPE (GLOBAL)

- No backend wiring
- No API calls
- No per-action business logic
- No permission enforcement logic
- No lookup popup or search implementation
- No per-module theming
- No animation-heavy transitions

---

## DELIVERABLE

A cohesive EnterpriseGPT UI foundation consisting of:

1. A VB-inspired, modern Transaction Header Toolbar
2. Global keyboard-first CRUD and workflow actions
3. Integrated master-data lookup shortcuts
4. A global App Header Theme Selector with full refresh behavior

This UI must feel like a **modern evolution of classic desktop ERP systems**,
optimized for **power users, speed, and transactional density**.


EnterpriseGPT_UI_Canon_Toolbar_Theme_HRM.md
md
Copy code
# EnterpriseGPT UI Canon
## Transaction Toolbar • Global Theme • Lookups • HRM Forms

This document is the **single source of truth** for implementing
EnterpriseGPT UI standards across modules, with special focus on:

- Transaction Header Toolbar (VB / VB.NET–inspired)
- Global App-Level Theme Selector
- Lookup Shortcuts
- HRM Form Implementation Standards

This file is **agent-ready**, **governance-safe**, and **non-ambiguous**.

---

# PART 1 — TRANSACTION HEADER TOOLBAR (CORE CANON)

## AGENT PROMPT — Enterprise Transaction Header Toolbar

You are implementing a reusable Enterprise Transaction Header Toolbar
for all transaction pages (PR, PO, GRN, Invoice, Journal, HRM Masters, etc.).

This toolbar replaces traditional bottom Save / Submit buttons
and is inspired by classic VB / VB.NET desktop ERP toolbars,
modernized for EnterpriseGPT.

DO NOT implement backend logic or individual action handlers.
Focus strictly on UI, behavior contracts, states, accessibility, and theming.

---

## 1. PLACEMENT & STRUCTURE

- Render inside the transaction page header
- Positioned directly below the transaction title and status
- Single-line horizontal toolbar
- Always visible (no scroll dependency)
- Bottom Save / Submit buttons must be removed entirely

Actions (fixed order, icon-only):

New, Edit, Save, Clear, Cancel, Clone, View, Submit, Authorize, Amend

Icons only  
Text appears only via tooltip

---

## 2. FUNCTION KEYS (MANDATORY)

- New            → F2
- Edit           → F4
- Save           → F8
- Clear / Reset  → F5
- Cancel         → Esc
- Clone          → F6
- View           → F7
- Submit / Post  → F9
- Authorize      → F10
- Amend / Revise → Ctrl + D

Keyboard shortcuts must work anywhere within the page,
including when focus is inside form fields.

---

## 3. STATE → ACTION ENABLE MATRIX

### Draft
- Enabled: New, Edit, Save, Clear, Cancel, Clone, View, Submit
- Disabled: Authorize, Amend

### Submitted
- Enabled: View, Cancel
- Conditional: Authorize (role-based)
- Disabled: New, Edit, Save, Clear, Clone, Amend

### Approved / Authorized
- Enabled: View, Amend
- Disabled: New, Edit, Save, Clear, Cancel, Clone, Submit, Authorize

### Cancelled
- Enabled: View, Clone
- Disabled: All others

Disabled actions must remain visible but muted.

---

## 4. VISUAL STYLE (VB / VB.NET SOUL)

- Toolbar height: ~40–44px
- Soft rectangular buttons (6–8px radius)
- Subtle bevel / pressed-in active state
- Thin vertical separators between groups
- Icons monochrome by default
- Accent color on hover / active
- No Material UI or mobile-first patterns

Grouping:

[ New | Edit | Save ] | [ Clear | Cancel ] | [ Clone | View ] | [ Submit | Authorize | Amend ]

---

## 5. DESIGN TOKENS (REFERENCE)

Spacing:
- Toolbar padding: px-3 py-1.5
- Button size: h-8 w-8
- Icon size: 16–18px
- Gap: gap-1
- Group margin: mx-2

Typography (tooltips):
- text-xs
- font-medium

Transitions:
- transition-colors transition-shadow duration-150 ease-out

---

## 6. ACCESSIBILITY & KEYBOARD

- All enabled buttons focusable via Tab
- Subtle visible focus ring required
- Tooltips accessible via keyboard focus
- aria-label required for icons
- Esc always prioritizes Cancel
- Disabled actions not focusable

---

# PART 2 — LOOKUP SHORTCUTS (TOOLBAR ENHANCEMENT)

## AGENT PROMPT — Lookup Shortcuts

Enhance the existing Transaction Header Toolbar
by introducing global Lookup Shortcuts for master data.

DO NOT redesign or remove existing toolbar actions.

---

## 1. LOOKUP SET (CANONICAL)

- Customer Lookup
- Supplier Lookup
- Item Lookup
- Location Lookup

(Future-extensible: Warehouse, Tax, Ledger, Price List)

Icons only.

---

## 2. PLACEMENT

[ Core CRUD ] | [ Reset / Cancel ] | [ Clone / View ] | [ Lookups ] | [ Workflow ]

Separated by thin vertical divider.

---

## 3. FUNCTION KEYS (LOOKUPS)

- Customer Lookup  → F11
- Supplier Lookup  → Shift + F11
- Item Lookup      → F12
- Location Lookup  → Shift + F12

Displayed in tooltips.

---

## 4. ENABLE / DISABLE RULES

- Lookup icons must support enable/disable via permissions
- Disabled lookups:
  - Remain visible
  - Muted appearance
  - Non-focusable

Permission logic not implemented (UI-only contract).

---

## 5. ACCESSIBILITY & STATE

- Enabled lookups keyboard accessible
- Disabled lookups not focusable
- aria-label required
- Typically enabled in Draft / Edit
- May be disabled in Approved / Cancelled

---

# PART 3 — GLOBAL APP-LEVEL THEME SELECTOR

## AGENT PROMPT — Global Theme Selector

Implement a global Theme Selector in the main Application Header
that controls the entire app UI.

Theme change must apply via full UI refresh.

---

## 1. PLACEMENT

- App Header (topmost)
- Right-aligned near profile/settings
- Visible across all modules

---

## 2. THEME OPTIONS

Exactly three:

- Light
- Dark
- System (default)

System:
- Follows OS preference
- Evaluated on app load only

---

## 3. BEHAVIOR

- Selecting a theme updates immediately
- Full UI refresh applied
- No logout
- No route reset
- No data loss
- Page & form state preserved

---

## 4. PERSISTENCE

- Theme persisted per user
- Survives reload, browser restart, logout/login
- User preference overrides system

---

## 5. VISUAL STYLE

- Minimal control (icon toggle / compact dropdown)
- No persistent text labels
- Tooltip:
  - Theme: Light
  - Theme: Dark
  - Theme: System

---

## 6. INTERACTION

- Keyboard accessible
- Focus-visible compliant
- Must not interfere with transaction function keys
- No auto-switching during session

---

# PART 4 — HRM FORM IMPLEMENTATION CANON

## AGENT PROMPT — HRM Forms (EnterpriseGPT)

You are implementing HRM forms aligned with EnterpriseGPT UI standards.

DO NOT invent patterns.
DO NOT redesign layouts.
EXECUTE this canon exactly.

---

## 1. TECH STACK

Frontend:
- React
- TypeScript
- Vite
- Tailwind CSS
- Lucide Icons

Backend (context):
- Python
- Django
- Django REST Framework

---

## 2. FOLDER STRUCTURE (MANDATORY)

spa/olivine-app-core/src/
├── modules/hrm/
│ ├── pages/
│ ├── models/
│ ├── services/
│ └── routes.ts
│
├── ui/components/
│ ├── form/
│ └── toolbar/
│
└── theme/

yaml
Copy code

Reuse common components.
No duplication.

---

## 3. PAGE LAYOUT STANDARD

App Header  
Module Header  
Transaction Header (with Toolbar)  
Form Body (sectioned, grid-based)

❌ No bottom Save buttons  
✅ Toolbar only

---

## 4. FORM DESIGN STYLE

- Grid layout (2–3 columns)
- Sectioned via FormSection
- Labels above inputs
- Dense, professional spacing

Sections example:
- Basic Information
- Employment Details
- Organization Mapping
- Payroll / Statutory
- Status & Metadata

---

## 5. STYLE CANON (TAILWIND)

Inputs:
- h-9
- rounded-md
- border-slate-300

Labels:
- text-xs
- font-medium
- text-slate-600

Section headers:
- text-sm
- font-semibold

---

## 6. MODELING STYLE

- One model per entity
- Typed fields
- Backend-aligned names
- Explicit enums & dates
- Workflow-ready states

---

## 7. LOOKUPS IN HRM

- Department
- Role
- Manager
- Location

Use platform lookup patterns.
No embedded logic.

---

## 8. ACCESSIBILITY

- Full keyboard navigation
- Logical tab order
- aria-labels
- Clear read-only mode

---

## OUT OF SCOPE (GLOBAL)

- No backend logic
- No API wiring
- No permission enforcement
- No modal logic
- No custom styling overrides

---

## FINAL DELIVERABLE

A unified EnterpriseGPT UI foundation that:
- Feels like classic desktop ERP
- Is keyboard-first
- Is scalable across Retail, HRM, FMS, POS
- Is modern, clean, and enterprise-grade


You are an execution-only engineering agent working on the Olivine Retail ERP platform.

This prompt is authoritative and overrides default assistant behavior.

────────────────────────────────────────
1. SOURCE OF TRUTH
────────────────────────────────────────
- Implementation repository: retail-erp-platform (ONLY)
- Reference / learning repository: 01practice (READ-ONLY, NEVER MODIFY)

If an example exists in 01practice:
→ Treat it as conceptual guidance only
→ Re-implement cleanly inside retail-erp-platform

────────────────────────────────────────
2. RULESET OBLIGATION
────────────────────────────────────────
Before writing or modifying any code, you MUST:

- Refer to the existing RULESET documents provided in this workspace, including:
  • Sidebar & Navigation rules
  • UI / UX consistency rules
  • DRF backend rules
  • Domain-driven module rules
  • File-touch and folder-discipline rules

If a rule exists:
→ FOLLOW IT STRICTLY
→ DO NOT reinterpret or redesign

If a rule is missing or ambiguous:
→ STOP and ASK for clarification
→ DO NOT assume or invent standards

────────────────────────────────────────
3. FILE TOUCH DISCIPLINE (CRITICAL)
────────────────────────────────────────
You MUST explicitly state:
- Which files will be touched
- Why each file is required
- Confirm no unrelated files are modified

Allowed actions:
- Modify existing files
- Add new files ONLY in approved folders
- Extend existing patterns

Disallowed actions:
- Arbitrary refactors
- Moving files without approval
- Cross-module leakage
- Silent changes

────────────────────────────────────────
4. UI / SIDEBAR / NEW SCREEN RULES
────────────────────────────────────────
For any of the following:
- Sidebar changes
- New UI screens
- Enhancements to existing UI
- Theme, layout, or navigation updates

You MUST:
- Follow existing sidebar structure and menu config
- Respect module boundaries (Retail, POS, HRM, FMS, CRM)
- Use approved Tailwind tokens, fonts, spacing, and icon rules
- Maintain keyboard accessibility and dark/light theme parity
- Avoid visual experimentation unless explicitly requested

Any UI change must:
- Match the current design language
- Be incremental, not disruptive
- Preserve existing routes and permissions

────────────────────────────────────────
5. NEW MODULE / FEATURE ADDITION
────────────────────────────────────────
When adding a new module or feature:
- Follow the established folder structure
- Use domain-driven naming
- Register routes explicitly
- Register permissions explicitly
- Do NOT copy-paste from another module blindly

You must explain:
- Where the module fits in the architecture
- How it integrates with existing modules
- What configuration, if any, is required

────────────────────────────────────────
6. BUG FIXES & REFACTORING
────────────────────────────────────────
For fixes:
- Identify root cause
- Apply the smallest possible fix
- Do NOT “clean up” unrelated code
- Do NOT modernize unless asked

For refactoring:
- Proceed ONLY with explicit instruction
- Provide before/after clarity

────────────────────────────────────────
7. OUTPUT EXPECTATION
────────────────────────────────────────
Every response MUST include:
1. Confirmation that rulesets were referenced
2. List of files to be touched
3. Exact changes to be made (no ambiguity)
4. Assurance that no scope creep occurred

────────────────────────────────────────
8. AUTHORITY MODEL
────────────────────────────────────────
- Human authority: Viji (final decision)
- Agent role: Executor only

You do NOT:
- Redesign architecture
- Introduce new patterns
- Self-approve deviations

You DO:
- Execute precisely as instructed
- Ask when unsure
- Preserve long-term system integrity

Acknowledge this contract before proceeding with any task.


You are an execution-only engineering agent for the Olivine Retail ERP.

This prompt enforces FILELIST AWARENESS.
You MUST align all actions strictly to the existing repository structure.

────────────────────────────────────────
1. REPOSITORY CONTEXT (MANDATORY)
────────────────────────────────────────
Primary implementation repository:
- retail-erp-platform

Reference-only repository:
- 01practice (READ-ONLY, NEVER MODIFY)

You must mentally load and respect the existing filelist and structure
as established in prior work on this project.

────────────────────────────────────────
2. BACKEND FILELIST DISCIPLINE (DJANGO / DRF)
────────────────────────────────────────
Backend root:
- backend/

Core boundaries:
- backend/erp_core/        → settings, root urls, app wiring ONLY
- backend/domain/          → ALL business domains live here
  - procurement/
  - retail/
  - hrm/
  - fms/
  - crm/
  - common/ (shared domain logic only)

Rules:
- New business logic → backend/domain/<module>/
- urls.py:
  - erp_core/urls.py → top-level include ONLY
  - domain/<module>/urls.py → router & endpoint registration
- ViewSets live inside:
  - domain/<module>/views/
- Models live inside:
  - domain/<module>/models/
- Serializers live inside:
  - domain/<module>/serializers/

Do NOT:
- Add domain logic in erp_core
- Cross-import between domains casually
- Bypass routers or permission layers

────────────────────────────────────────
3. FRONTEND FILELIST DISCIPLINE (SPA / REACT)
────────────────────────────────────────
Frontend root:
- spa/olivine-app-core/src/

Key folders:
- modules/        → Module-level pages (Retail, POS, HRM, etc.)
- ui/components/  → Reusable UI components (buttons, layouts, tables)
- ui/layout/      → AppHeader, Sidebar, PageContainer
- config/         → menu config, permissions, feature flags
- theme/          → Tailwind tokens, theme definitions

Rules:
- Sidebar changes → ui/layout/Sidebar + config/menu*
- Header/theme changes → ui/layout/AppHeader + theme/
- New screen/page → modules/<module>/
- Shared UI → ui/components/

Do NOT:
- Hardcode UI inside modules that belongs to ui/components
- Duplicate sidebar or header logic
- Introduce new layout patterns without approval

────────────────────────────────────────
4. SIDEBAR & NAVIGATION ENFORCEMENT
────────────────────────────────────────
Sidebar is a GOVERNED surface.

Rules:
- Menu structure comes from config files ONLY
- Icons, labels, shortcuts follow approved sidebar ruleset
- Enable/disable via permissions, not conditional JSX hacks
- No inline styling; Tailwind tokens only
- No visual experimentation unless explicitly requested

Any sidebar task MUST state:
- Which menu config file is touched
- Which layout component is touched
- Confirmation that routing & permissions remain intact

────────────────────────────────────────
5. NEW MODULE ADDITION (FRONTEND + BACKEND)
────────────────────────────────────────
When adding a new module:
Backend:
- Create under backend/domain/<new_module>/
- Add urls.py, views/, models/, serializers/
- Register explicitly in erp_core/urls.py

Frontend:
- Create under modules/<new_module>/
- Add menu entry via config
- Hook permissions explicitly

You must explain:
- Why the module is separate
- How it aligns with existing modules
- What files are added vs reused

────────────────────────────────────────
6. FIXES & ENHANCEMENTS
────────────────────────────────────────
For any fix or enhancement:
- Identify exact file(s) involved
- Apply minimal change
- Preserve folder boundaries
- Avoid “while I’m here” refactors

If a fix touches:
- Sidebar
- Layout
- Domain routing
→ Extra caution and explicit confirmation required

────────────────────────────────────────
7. RESPONSE FORMAT (NON-NEGOTIABLE)
────────────────────────────────────────
Before implementation, you MUST respond with:

1. Files to be touched (exact paths)
2. Reason for each file
3. Confirmation of rule adherence
4. Statement that no other files will be modified

No assumptions.
No silent changes.
No scope expansion.

────────────────────────────────────────
8. AUTHORITY & EXECUTION MODE
────────────────────────────────────────
- Final authority: Viji
- Agent role: Precise executor

If something feels unclear:
→ ASK
Do NOT invent patterns.
Do NOT optimize beyond instructions.

Acknowledge this filelist-aware contract before proceeding.

You are an execution-only engineering agent for the Olivine Retail ERP.

This prompt enforces FILELIST AWARENESS.
You MUST align all actions strictly to the existing repository structure.

────────────────────────────────────────
1. REPOSITORY CONTEXT (MANDATORY)
────────────────────────────────────────
Primary implementation repository:
- retail-erp-platform

Reference-only repository:
- 01practice (READ-ONLY, NEVER MODIFY)

You must mentally load and respect the existing filelist and structure
as established in prior work on this project.

────────────────────────────────────────
2. BACKEND FILELIST DISCIPLINE (DJANGO / DRF)
────────────────────────────────────────
Backend root:
- backend/

Core boundaries:
- backend/erp_core/        → settings, root urls, app wiring ONLY
- backend/domain/          → ALL business domains live here
  - procurement/
  - retail/
  - hrm/
  - fms/
  - crm/
  - common/ (shared domain logic only)

Rules:
- New business logic → backend/domain/<module>/
- urls.py:
  - erp_core/urls.py → top-level include ONLY
  - domain/<module>/urls.py → router & endpoint registration
- ViewSets live inside:
  - domain/<module>/views/
- Models live inside:
  - domain/<module>/models/
- Serializers live inside:
  - domain/<module>/serializers/

Do NOT:
- Add domain logic in erp_core
- Cross-import between domains casually
- Bypass routers or permission layers

────────────────────────────────────────
3. FRONTEND FILELIST DISCIPLINE (SPA / REACT)
────────────────────────────────────────
Frontend root:
- spa/olivine-app-core/src/

Key folders:
- modules/        → Module-level pages (Retail, POS, HRM, etc.)
- ui/components/  → Reusable UI components (buttons, layouts, tables)
- ui/layout/      → AppHeader, Sidebar, PageContainer
- config/         → menu config, permissions, feature flags
- theme/          → Tailwind tokens, theme definitions

Rules:
- Sidebar changes → ui/layout/Sidebar + config/menu*
- Header/theme changes → ui/layout/AppHeader + theme/
- New screen/page → modules/<module>/
- Shared UI → ui/components/

Do NOT:
- Hardcode UI inside modules that belongs to ui/components
- Duplicate sidebar or header logic
- Introduce new layout patterns without approval

────────────────────────────────────────
4. SIDEBAR & NAVIGATION ENFORCEMENT
────────────────────────────────────────
Sidebar is a GOVERNED surface.

Rules:
- Menu structure comes from config files ONLY
- Icons, labels, shortcuts follow approved sidebar ruleset
- Enable/disable via permissions, not conditional JSX hacks
- No inline styling; Tailwind tokens only
- No visual experimentation unless explicitly requested

Any sidebar task MUST state:
- Which menu config file is touched
- Which layout component is touched
- Confirmation that routing & permissions remain intact

────────────────────────────────────────
5. NEW MODULE ADDITION (FRONTEND + BACKEND)
────────────────────────────────────────
When adding a new module:
Backend:
- Create under backend/domain/<new_module>/
- Add urls.py, views/, models/, serializers/
- Register explicitly in erp_core/urls.py

Frontend:
- Create under modules/<new_module>/
- Add menu entry via config
- Hook permissions explicitly

You must explain:
- Why the module is separate
- How it aligns with existing modules
- What files are added vs reused

────────────────────────────────────────
6. FIXES & ENHANCEMENTS
────────────────────────────────────────
For any fix or enhancement:
- Identify exact file(s) involved
- Apply minimal change
- Preserve folder boundaries
- Avoid “while I’m here” refactors

If a fix touches:
- Sidebar
- Layout
- Domain routing
→ Extra caution and explicit confirmation required

────────────────────────────────────────
7. RESPONSE FORMAT (NON-NEGOTIABLE)
────────────────────────────────────────
Before implementation, you MUST respond with:

1. Files to be touched (exact paths)
2. Reason for each file
3. Confirmation of rule adherence
4. Statement that no other files will be modified

No assumptions.
No silent changes.
No scope expansion.

────────────────────────────────────────
8. AUTHORITY & EXECUTION MODE
────────────────────────────────────────
- Final authority: Viji
- Agent role: Precise executor

If something feels unclear:
→ ASK
Do NOT invent patterns.
Do NOT optimize beyond instructions.

Acknowledge this filelist-aware contract before proceeding.



# EnterpriseGPT — Consolidated Governance & Execution Prompt

This document is the SINGLE authoritative prompt for agents working on the Olivine Retail ERP platform.
It consolidates:
1. Business Entities vs Company clarification
2. Seed Data rules
3. Governance & execution discipline established in prior sessions

---

## 1. ARCHITECTURAL TRUTH — BUSINESS ENTITIES vs COMPANY (LOCKED)

- `domain.business_entities` = **LICENSING METADATA ONLY**
  - Company (as tenant anchor)
  - License plans, limits, subscriptions (present/future)
  - Platform / Superuser managed
  - NEVER used for operations

- `domain.company` = **OPERATIONAL REALITY**
  - Company (operational tenant)
  - Location
  - Supplier
  - Customer
  - ItemMaster (canonical)
  - Category, Brand, TaxClass
  - Attributes, UOM, PriceList
  - Used in UI, APIs, transactions

ABSOLUTE RULE:
If a model participates in UI, transactions, or daily operations,
IT MUST LIVE IN `domain.company`.

NO MIXED IMPORTS.
NO EXCEPTIONS.

---

## 2. ITEM CANONICAL DECISION (FINAL)

- Canonical Item model: **ItemMaster**
- `Item` (if present) is LEGACY / DEPRECATED
- NO data migration
- NO table renaming
- Preserve existing `be_*` tables via `Meta.db_table`

Truth:
Stability with real data > speculative refactor.

---

## 3. SEED DATA PROMPT (OPERATIONAL ONLY)

Create or extend MASTER DATA using EXISTING RECORDS where available.
Add new records ONLY to meet required counts.

Minimum anchors:
- Companies: 5
- Locations: 5 per company
- Items (ItemMaster): 200+
- Suppliers: 50+
- Customers: 50+
- Attributes: 20 (with realistic values)

Rules:
- Seed ONLY operational masters
- Import ONLY from `domain.company.models`
- NEVER seed `business_entities`
- Maintain referential integrity
- No transactions, pricing logic, or workflows

---

## 4. GOVERNANCE — FILE & EXECUTION DISCIPLINE

SOURCE OF TRUTH:
- Implementation repo: `retail-erp-platform`
- Reference-only repo: `01practice` (READ-ONLY)

Before ANY change:
- Identify files to be touched
- Explain why
- Confirm no unrelated files are modified

Disallowed:
- Mixed imports
- Silent refactors
- Schema redesign without approval
- Reintroducing removed models

---

## 5. DJANGO ADMIN GOVERNANCE

- business_entities admin:
  - Company ONLY
  - Platform-level access

- company admin:
  - ALL operational masters
  - Application Admin access

No operational model may appear under business_entities admin.

---

## 6. SERIALIZERS & IMPORT HYGIENE

If a model was removed from `business_entities`:
- Its serializer MUST also be removed there
- Serializer MUST live under `domain.company.serializers`

NEVER patch by reintroducing removed models.

---

## 7. STEERING GOVERNANCE

The `.steering/` directory is the SINGLE MEMORY of the system.

Rules:
- Update existing docs before creating new ones
- Record decisions & outcomes, not chat history
- No duplication
- No contradictions
- New agents must understand system state in 10–15 minutes

---

## 8. AUTHORITY MODEL

- Human authority: Viji
- Agent role: EXECUTOR ONLY

If unsure:
STOP.
ASK.
DO NOT GUESS.

---

ACKNOWLEDGEMENT:
By proceeding, you confirm understanding and acceptance of this lock.




-
<a name="file-08"></a>
## FILE: 08_typography.md



OLIVINE TYPOGRAPHY RULES (AUTHORITATIVE)

1. FONT FAMILY
- Primary font: Inter
- Fallbacks:
  'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif
- Only ONE font family is allowed across the application.
- No per-component or per-module font overrides.

2. FONT WEIGHTS (STRICT)
- Regular: 400
- Medium: 500
- Semibold: 600
- Do NOT use 300, 700, or higher.
- Bold text must be rare and intentional.

3. FONT SIZES (ERP-OPTIMIZED SCALE)
- Page Title: 20–22px (600)
- Section Title: 14–15px (600)
- Body Text: 13–14px (400)
- Form Label: 12–13px (500)
- Helper / Subtitle Text: 12px (400)
- Table Text: 13px (400)

4. LINE HEIGHTS
- Titles: 1.2
- Body & Labels: 1.4
- Helper / Subtitle Text: 1.5
- Line-height must never be below 1.4 for body text.

5. SIDEBAR TYPOGRAPHY
- Section Header:
  - 12px, 600, line-height 1.4
- Menu Item Label:
  - 13–14px, 500, line-height 1.4
- Menu Item Subtitle:
  - 12px, 400, line-height 1.5
- Label and subtitle MUST be aligned on the same left text axis.
- Label and subtitle MUST live in the same text container.
- Subtitle must start directly under the label text, not under icons.

6. FORMS (EMPLOYEE, MASTER FORMS)
- Section Title:
  - 14–15px, 600
- Field Label:
  - 12–13px, 500
- Input Text:
  - 13–14px, 400
- Helper / Error Text:
  - 12px, 400
- Inputs must NOT be bold.
- Helper text must NOT be smaller than 12px.

7. TABLES & NUMERIC DATA
- Table Header:
  - 12px, 600
- Table Cell Text:
  - 13px, 400
- Numeric columns must use tabular numerals.
- Enable:
  font-feature-settings: "tnum";
- Tables must feel visually quieter than forms.

8. SPACING & RHYTHM
- Maintain consistent vertical spacing between:
  - Label → Input
  - Label → Subtitle
- No arbitrary spacing per component.
- Typography rhythm must be consistent across modules.

9. ACCESSIBILITY & TONE
- Avoid overly light gray text for subtitles.
- No italics for helper text.
- Typography must remain readable for long working hours.

10. NON-NEGOTIABLE RULE
- Typography is token-driven, not component-driven.
- Any deviation must update the typography tokens first.


/* =========================================================
   OLIVINE TYPOGRAPHY DESIGN TOKENS (AUTHORITATIVE)
   ========================================================= */

/* ---------- CSS VARIABLES (GLOBAL) ---------- */
:root {
  /* Font Family */
  --font-family-primary: 'Inter', system-ui, -apple-system,
    BlinkMacSystemFont, 'Segoe UI', sans-serif;

  /* Font Weights */
  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;

  /* Font Sizes */
  --font-size-page-title: 20px;
  --font-size-section-title: 14px;
  --font-size-body: 13px;
  --font-size-label: 12px;
  --font-size-helper: 12px;
  --font-size-table: 13px;

  /* Line Heights */
  --line-height-tight: 1.2;
  --line-height-normal: 1.4;
  --line-height-relaxed: 1.5;

  /* Letter Spacing */
  --letter-spacing-normal: 0;
}

/* ---------- GLOBAL BASE ---------- */
body {
  font-family: var(--font-family-primary);
  font-size: var(--font-size-body);
  font-weight: var(--font-weight-regular);
  line-height: var(--line-height-normal);
}

/* ---------- SIDEBAR ---------- */
.sidebar-section-title {
  font-size: var(--font-size-label);
  font-weight: var(--font-weight-semibold);
  line-height: var(--line-height-normal);
}

.sidebar-item-label {
  font-size: var(--font-size-body);
  font-weight: var(--font-weight-medium);
  line-height: var(--line-height-normal);
}

.sidebar-item-subtitle {
  font-size: var(--font-size-helper);
  font-weight: var(--font-weight-regular);
  line-height: var(--line-height-relaxed);
}

/* ---------- FORMS ---------- */
.form-section-title {
  font-size: var(--font-size-section-title);
  font-weight: var(--font-weight-semibold);
  line-height: var(--line-height-tight);
}

.form-label {
  font-size: var(--font-size-label);
  font-weight: var(--font-weight-medium);
  line-height: var(--line-height-normal);
}

.form-input,
.form-select,
.form-textarea {
  font-size: var(--font-size-body);
  font-weight: var(--font-weight-regular);
  line-height: var(--line-height-normal);
}

.form-helper-text,
.form-error-text {
  font-size: var(--font-size-helper);
  font-weight: var(--font-weight-regular);
  line-height: var(--line-height-relaxed);
}

/* ---------- TABLES ---------- */
.table-header {
  font-size: var(--font-size-label);
  font-weight: var(--font-weight-semibold);
  line-height: var(--line-height-normal);
}

.table-cell {
  font-size: var(--font-size-table);
  font-weight: var(--font-weight-regular);
  line-height: var(--line-height-normal);
  font-feature-settings: "tnum";
}

/* =========================================================
   TYPESCRIPT TOKENS (for React / MUI / Design System)
   ========================================================= */

export const typographyTokens = {
  fontFamily: {
    primary:
      "'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
  },

  fontWeight: {
    regular: 400,
    medium: 500,
    semibold: 600,
  },

  fontSize: {
    pageTitle: "20px",
    sectionTitle: "14px",
    body: "13px",
    label: "12px",
    helper: "12px",
    table: "13px",
  },

  lineHeight: {
    tight: 1.2,
    normal: 1.4,
    relaxed: 1.5,
  },

  numeric: {
    fontFeatureSettings: "tnum",
  },
};

/* =========================================================
   NON-NEGOTIABLE RULE
   =========================================================
   - Components must consume these tokens.
   - No hardcoded font sizes, weights, or families.
   - Any typography change must update tokens first.
   ========================================================= */




-
<a name="file-09"></a>
## FILE: 09_LOOKUP_CANON.md



# LOOKUP UI CANON - IMPLEMENTATION COMPLETE

**Date**: 2025-12-23  
**Status**: ✅ ENFORCED  
**Applies To**: ALL lookup modals in Olivine/EnterpriseGPT

---

## 🎯 CANON SUMMARY

**RULE**: Lookups are an extension of Sidebar + App Header, NOT independent components.

**IMPLEMENTATION**: All lookups MUST use `LookupContainer.tsx`

---

## ✅ COMPLIANCE CHECKLIST

### 1. Theme Identity ✅
- [x] Lookup header uses SAME background as App Header
- [x] Lookup header uses SAME gradient (`#14162A` → `#101223`)
- [x] Lookup icons use SAME brand color (`#22D3EE`)
- [x] Lookup text uses SAME colors as Header
- [x] NO bright blue headers
- [x] NO hardcoded colors

### 2. Structure ✅
- [x] Shared `LookupContainer` component created
- [x] All lookups use the container
- [x] Consistent header layout
- [x] Consistent search bar placement
- [x] Consistent results area

### 3. Typography & Icons ✅
- [x] Uses Lucide icons (same as Sidebar)
- [x] Same font family as App Header
- [x] Same font weights
- [x] Consistent icon sizing

### 4. Interaction ✅
- [x] Keyboard-first (Escape closes)
- [x] Auto-focus on search input
- [x] Hover states match Sidebar
- [x] Click to select

### 5. Theme Awareness ✅
- [x] Uses `useLayoutConfig` hook
- [x] Reads theme from config
- [x] NO hardcoded colors
- [x] Adapts to light/dark/auto

### 6. Reusability ✅
- [x] Single `LookupContainer` component
- [x] All lookups use it
- [x] Lookups differ ONLY in data + columns
- [x] NOT in look & feel

---

## 📁 FILES CREATED/MODIFIED

### Created:
1. ✅ `frontend/src/ui/components/LookupContainer.tsx`
   - Canonical lookup shell
   - Theme-aware
   - Matches App Header exactly

### Refactored:
2. ✅ `frontend/src/ui/components/SupplierLookupModal.tsx`
   - Removed hardcoded `bg-[#0078d4]`
   - Now uses `LookupContainer`
   - Matches App Header theme

3. ✅ `frontend/src/ui/components/ProductLookupModal.tsx`
   - Removed hardcoded `backgroundColor: '#0078d4'`
   - Now uses `LookupContainer`
   - Matches App Header theme

---

## 🎨 THEME EXTRACTION

### From App Header Config:
```typescript
// Header Background
headerBgStyle: 'gradient'
headerGradientStart: '#14162A'
headerGradientEnd: '#101223'

// Brand Colors
brandColor: '#22D3EE' (cyan)
iconColor: '#6F7396' (muted purple-gray)
```

### Applied To Lookups:
```typescript
// Lookup Header
background: linear-gradient(to bottom, #14162A, #101223)
icon color: #22D3EE
text color: #FFFFFF
close button color: #6F7396

// Lookup Body
background: white
hover: gray-50
border: gray-100
```

---

## 🚀 USAGE GUIDE

### For Future Lookups:

```typescript
import { LookupContainer } from './LookupContainer';
import { YourIcon } from 'lucide-react';

export const YourLookupModal = ({ isOpen, onClose, onSelect }) => {
  // Your state and logic here
  
  const searchBar = (
    <div className="relative">
      <Search className="absolute left-3 top-2.5 text-gray-400" size={16} />
      <input
        type="text"
        placeholder="Search..."
        className="w-full pl-9 pr-3 py-2 border border-gray-300 rounded-sm text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
    </div>
  );

  const resultsContent = (
    <div>
      {/* Your results here */}
    </div>
  );

  return (
    <LookupContainer
      isOpen={isOpen}
      onClose={onClose}
      title="Your Lookup"
      icon={<YourIcon size={20} />}
      searchBar={searchBar}
    >
      {resultsContent}
    </LookupContainer>
  );
};
```

---

## ❌ PROHIBITIONS

### DO NOT:
- ❌ Use `bg-[#0078d4]` or any hardcoded blue
- ❌ Use `backgroundColor: '#0078d4'` in style props
- ❌ Create custom lookup headers
- ❌ Ignore `LookupContainer`
- ❌ Use bright brand colors in lookup body
- ❌ Mix light header with dark sidebar
- ❌ Style lookups independently

### DO:
- ✅ Always use `LookupContainer`
- ✅ Use theme tokens from `useLayoutConfig`
- ✅ Match App Header colors exactly
- ✅ Keep lookups visually consistent
- ✅ Test in light AND dark themes

---

## 🧪 VERIFICATION

### Visual Check:
1. Open any lookup (Supplier, Item, etc.)
2. Compare header color to App Header
3. Should be SAME dark gradient
4. Should NOT be bright blue

### Code Check:
```bash
# Search for violations
grep -r "bg-\[#0078d4\]" frontend/src/ui/components/*Lookup*.tsx
grep -r "backgroundColor.*0078d4" frontend/src/ui/components/*Lookup*.tsx

# Should return NO results
```

---

## 📊 BEFORE vs AFTER

### BEFORE (WRONG):
```tsx
// ❌ Hardcoded bright blue
<div className="... bg-[#0078d4] text-white">
  <Search size={20} />
  <h2>Supplier Lookup</h2>
</div>
```

### AFTER (CORRECT):
```tsx
// ✅ Uses LookupContainer with theme colors
<LookupContainer
  title="Supplier Lookup"
  icon={<Search size={20} />}
  // Header automatically matches App Header
/>
```

---

## ✅ SUCCESS CRITERIA

A user should feel that:
- ✅ Lookup belongs to the same product as Sidebar
- ✅ Lookup feels like a native ERP panel
- ✅ Switching between modules does NOT change lookup look
- ✅ Lookup header matches App Header exactly
- ✅ All lookups look identical (except data)

**If any lookup looks visually different from another, the implementation is WRONG.**

---

## 🔒 ENFORCEMENT

This canon is **LOCKED** and **NON-NEGOTIABLE**.

Any future lookup MUST:
1. Use `LookupContainer`
2. Match App Header theme
3. Follow the structure defined here

**NO EXCEPTIONS.**

---

**Canon Established**: 2025-12-23  
**Enforced By**: Antigravity Agent  
**Authority**: Viji (Product Owner)  
**Status**: ✅ ACTIVE




-
<a name="file-10"></a>
## FILE: 10_EMPLOYEE_UI_REFERENCE.md



# 11_EMPLOYEE_UI_CANON.md
## Employee Master UI Reference - Pattern for CRM Module Development

**Purpose**: This document extracts the exact UI patterns, styling, and component structure from the Employee Master implementation to serve as a reference for Agent E when building CRM modules (Customer, Lead, Contact, Opportunity forms).

**Source Files**:
- `frontend/core/ui_canon/frontend/ui/components/employee/EmployeeForm.tsx` (1009 lines)
- `frontend/core/ui_canon/frontend/ui/components/employee/EmployeeFormStandalone.tsx`
- `frontend/src/pages/hr/EmployeeMasterPage.tsx`

---

## 1. Visual Overview (from employee_master_all_tabs.jpg)

### Tab Structure
The Employee Master form uses a **tabbed interface** with the following sections:
1. **Summary** - Read-only overview of all employee data
2. **Personal** - Personal information (name, DOB, gender, marital status)
3. **Employment** - Employment details (joining date, type, designation, department)
4. **Organization** - Organization structure (business unit, location, reporting manager)
5. **Contact** - Contact information (email, mobile, address)
6. **Statutory** - Compliance data (PAN, Aadhaar, PF, ESI)
7. **Compensation** - Salary information (CTC, pay grade)

### Layout Pattern
- **Header Section**: Photo + Name + Employee Code + Status Badge
- **Tab Navigation**: Horizontal tabs below header
- **Form Content**: 2-column grid layout for form fields
- **Action Buttons**: Save/Cancel at bottom (handled by parent component)

---

## 2. Component Architecture

### File Structure
```
frontend/
├── core/ui_canon/frontend/ui/components/employee/
│   ├── EmployeeForm.tsx              # Core tabbed form (1009 lines)
│   ├── EmployeeFormStandalone.tsx    # Wrapper with toolbar
│   ├── EmployeeLayout.tsx            # Page layout
│   ├── EmployeeContextPanel.tsx      # Sidebar panel
│   ├── EmployeeList.tsx              # List view
│   └── EmployeeLifecycleNav.tsx      # Navigation
└── src/pages/hr/
    └── EmployeeMasterPage.tsx        # Page component
```

### Component Hierarchy
```tsx
EmployeeMasterPage
└── EmployeeFormStandalone
    └── EmployeeForm (with activeSection prop)
        ├── Header (photo + name + status)
        ├── Tab Content (conditional rendering based on activeSection)
        │   ├── Summary Tab
        │   ├── Personal Tab
        │   ├── Employment Tab
        │   ├── Organization Tab
        │   ├── Contact Tab
        │   ├── Statutory Tab
        │   └── Compensation Tab
        └── Form Actions (submit/cancel)
```

### Props Pattern
```typescript
interface EmployeeFormProps {
  initialData?: EmployeeFormData;
  onSubmit: (data: FormData) => void;
  onCancel: () => void;
  isSubmitting: boolean;
  activeSection: string;  // Controls which tab is displayed
}
```

---

## 3. Styling Canon (Extracted from Actual Code)

### Form Container
```tsx
className="space-y-8 max-w-4xl w-full mx-auto px-6 py-8 bg-white rounded-md shadow-md font-primary"
```

### Header Section
```tsx
// Header Container
className="flex items-center space-x-6 border-b pb-4"

// Photo (if exists)
className="h-20 w-20 rounded-full object-cover"

// Photo Placeholder
className="h-20 w-20 rounded-full bg-gray-300 flex items-center justify-center text-gray-600"

// Name
className="text-xl font-bold"

// Employee Code
className="font-mono text-sm text-gray-500"

// Status Badge (Active)
className="inline-block px-2 py-1 mt-1 font-semibold rounded text-xs uppercase bg-green-100 text-green-800"

// Status Badge (Inactive)
className="inline-block px-2 py-1 mt-1 font-semibold rounded text-xs uppercase bg-gray-300 text-gray-600"
```

### Section Headers
```tsx
// Main Section Header
className="font-semibold text-lg border-b pb-2 mb-4"

// Subsection Header (in Summary tab)
className="font-semibold text-md mb-3 text-gray-700"
```

### Form Fields (2-Column Grid)
```tsx
// Grid Container
className="grid grid-cols-2 gap-6"

// Individual Field Container
<div>
  <label className="block font-medium mb-1">Field Label *</label>
  <input
    className="w-full rounded border px-3 py-2 border-gray-300"
    // Error state:
    className="w-full rounded border px-3 py-2 border-red-500"
  />
  {/* Error Message */}
  <p className="text-red-600 text-xs mt-1">{errorMessage}</p>
</div>
```

### Input Field Styles
```tsx
// Text Input
className="w-full rounded border border-gray-300 px-3 py-2"

// Text Input (Error State)
className="w-full rounded border px-3 py-2 border-red-500"

// Read-Only Input
className="w-full rounded border border-gray-300 px-3 py-2 bg-gray-100"

// Select Dropdown
className="w-full rounded border border-gray-300 px-3 py-2"

// Date Input
className="w-full rounded border border-gray-300 px-3 py-2"

// Textarea
className="w-full rounded border border-gray-300 px-3 py-2"
```

### Summary Tab (Read-Only Display)
```tsx
// Summary Container
className="space-y-6"

// Summary Grid
className="grid grid-cols-2 gap-4 text-sm"

// Label
className="font-medium text-gray-600"

// Value
className="text-gray-900"

// Full-Width Field (e.g., Address)
className="col-span-2"
```

---

## 4. Typography Standards

### Font Weights
- **Labels**: `font-medium`
- **Section Headers**: `font-semibold`
- **Employee Code**: `font-mono`
- **Status Badge**: `font-semibold`

### Text Sizes
- **Name**: `text-xl`
- **Section Headers**: `text-lg`
- **Subsection Headers**: `text-md`
- **Employee Code**: `text-sm`
- **Form Labels**: (default, ~14px)
- **Summary Labels/Values**: `text-sm`
- **Error Messages**: `text-xs`
- **Status Badge**: `text-xs uppercase`

### Text Colors
- **Primary Text**: `text-gray-900`
- **Secondary Text**: `text-gray-600`
- **Muted Text**: `text-gray-500`
- **Error Text**: `text-red-600`
- **Active Status**: `text-green-800`
- **Inactive Status**: `text-gray-600`

---

## 5. Tab Implementation Patterns

### Tab 1: Summary (Read-Only Overview)
```tsx
{activeSection.toLowerCase() === 'summary' && (
  <section>
    <h3 className="font-semibold text-lg border-b pb-2 mb-4">Employee Summary</h3>
    <div className="space-y-6">
      {/* Personal Information Summary */}
      <div>
        <h4 className="font-semibold text-md mb-3 text-gray-700">Personal Information</h4>
        <div className="grid grid-cols-2 gap-4 text-sm">
          <div>
            <span className="font-medium text-gray-600">Full Name:</span>
            <p className="text-gray-900">{formData.first_name} {formData.last_name}</p>
          </div>
          <div>
            <span className="font-medium text-gray-600">Date of Birth:</span>
            <p className="text-gray-900">{formData.date_of_birth || 'Not provided'}</p>
          </div>
        </div>
      </div>
      {/* Repeat for other subsections */}
    </div>
  </section>
)}
```

### Tab 2: Personal (Editable Form)
```tsx
{activeSection.toLowerCase() === 'personal' && (
  <section>
    <h3 className="font-semibold text-lg border-b pb-2 mb-4">Personal Information</h3>
    <div className="grid grid-cols-2 gap-6">
      {/* Text Input with Validation */}
      <div>
        <label className="block font-medium mb-1">First Name *</label>
        <input
          name="first_name"
          type="text"
          value={formData.first_name}
          onChange={handleChange}
          className={`w-full rounded border px-3 py-2 ${
            formErrors.first_name ? 'border-red-500' : 'border-gray-300'
          }`}
        />
        {formErrors.first_name && (
          <p className="text-red-600 text-xs mt-1">{formErrors.first_name}</p>
        )}
      </div>

      {/* Date Input */}
      <div>
        <label className="block font-medium mb-1">Date of Birth</label>
        <input
          name="date_of_birth"
          type="date"
          value={formData.date_of_birth || ''}
          onChange={handleChange}
          className="w-full rounded border border-gray-300 px-3 py-2"
        />
      </div>

      {/* Select Dropdown */}
      <div>
        <label className="block font-medium mb-1">Gender</label>
        <select
          name="gender"
          value={formData.gender || ''}
          onChange={handleChange}
          className="w-full rounded border border-gray-300 px-3 py-2"
        >
          <option value="">Select gender</option>
          {genderOptions.map((opt) => (
            <option key={opt.value} value={opt.value}>
              {opt.label}
            </option>
          ))}
        </select>
      </div>

      {/* Read-Only Field */}
      <div>
        <label className="block font-medium mb-1">Employee Code</label>
        <input
          name="employee_code"
          type="text"
          value={formData.employee_code}
          readOnly
          className="w-full rounded border border-gray-300 px-3 py-2 bg-gray-100"
        />
      </div>
    </div>
  </section>
)}
```

---

## 6. Data Model Pattern

```typescript
interface EmployeeFormData {
  // Identity
  employee_code: string;
  first_name: string;
  last_name: string;
  
  // Personal
  date_of_birth?: string;
  gender?: "M" | "F" | "O";
  marital_status?: "single" | "married" | "divorced" | "widowed";
  
  // Employment
  date_of_joining?: string;
  employment_type?: "full_time" | "part_time" | "contract" | "intern";
  designation?: string;
  department?: string;
  
  // Organization
  business_unit?: string;
  location?: string;
  reporting_manager?: number | null;
  
  // Contact
  email: string;
  mobile_number?: string;
  address?: string;
  
  // Statutory
  pan?: string;
  aadhaar?: string;
  pf_number?: string;
  esi_number?: string;
  
  // Compensation
  ctc?: number;
  pay_grade?: string;
  
  // Status
  status: "active" | "inactive";
  created_at?: string;
  updated_at?: string;
  
  // Media
  photo?: File | string | null;
}
```

---

## 7. Validation Pattern

```typescript
const validate = (): boolean => {
  const errors: FormErrors = {};
  
  // Required field validation
  if (!formData.employee_code.trim()) {
    errors.employee_code = "Employee Code is required";
  }
  if (!formData.first_name.trim()) {
    errors.first_name = "First Name is required";
  }
  
  // Email validation
  if (!formData.email.trim()) {
    errors.email = "Email is required";
  } else if (!/^[\w-.]+@[\w-]+\.[a-z]{2,}$/i.test(formData.email)) {
    errors.email = "Invalid email address";
  }
  
  // Phone validation
  if (formData.mobile_number && !/^\+?[\d\s-]{7,15}$/.test(formData.mobile_number)) {
    errors.mobile_number = "Invalid mobile number";
  }
  
  setFormErrors(errors);
  return Object.keys(errors).length === 0;
};
```

---

## 8. Replication Guide for CRM Modules

### For Customer Master Form:
1. **Replace Employee-specific fields** with Customer fields:
   - `employee_code` → `customer_code`
   - `first_name/last_name` → `customer_name` or `contact_person`
   - `department/designation` → `industry/company_size`
   - `date_of_joining` → `customer_since`

2. **Keep the same tab structure**:
   - Summary (read-only overview)
   - Basic Info (name, code, type)
   - Contact Details (email, phone, address)
   - Business Info (industry, revenue, employees)
   - Preferences (payment terms, credit limit)
   - Documents (attachments, contracts)

3. **Maintain exact styling**:
   - Use the same className patterns
   - Keep 2-column grid layout
   - Use identical header structure (photo → logo)
   - Keep status badge pattern (active/inactive → active/prospect/inactive)

### For Lead/Contact Forms:
- **Lead**: Simpler version with fewer tabs (Basic, Contact, Qualification, Notes)
- **Contact**: Similar to Employee but with Company relationship field
- **Opportunity**: Add pipeline/stage-specific fields

### Key Patterns to Replicate:
1. **Header**: Always show photo/logo + name + code + status
2. **Tabs**: Use conditional rendering based on `activeSection`
3. **Grid**: Always `grid grid-cols-2 gap-6` for form fields
4. **Labels**: Always `block font-medium mb-1`
5. **Inputs**: Always `w-full rounded border px-3 py-2`
6. **Errors**: Always `text-red-600 text-xs mt-1`
7. **Summary**: Always read-only with `grid grid-cols-2 gap-4 text-sm`

---

## 9. Color Palette (Extracted)

### Backgrounds
- Form: `bg-white`
- Read-only input: `bg-gray-100`
- Photo placeholder: `bg-gray-300`
- Active status: `bg-green-100`
- Inactive status: `bg-gray-300`

### Borders
- Default: `border-gray-300`
- Error: `border-red-500`
- Section divider: `border-b`

### Text
- Primary: `text-gray-900`
- Secondary: `text-gray-600`
- Muted: `text-gray-500`
- Error: `text-red-600`
- Success (active): `text-green-800`

---

## 10. Spacing Standards

### Form Spacing
- Form container: `space-y-8` (32px vertical spacing between sections)
- Form padding: `px-6 py-8` (24px horizontal, 32px vertical)
- Grid gap: `gap-6` (24px between fields)
- Summary grid gap: `gap-4` (16px in read-only view)

### Component Spacing
- Header padding: `pb-4` (16px bottom padding)
- Section header: `pb-2 mb-4` (8px bottom padding, 16px bottom margin)
- Label margin: `mb-1` (4px bottom margin)
- Error margin: `mt-1` (4px top margin)
- Photo spacing: `space-x-6` (24px horizontal spacing)

---

## 11. Accessibility Patterns

### Required Fields
- Mark with asterisk (*) in label
- Validate on submit
- Show error message below field
- Change border color to red on error

### Read-Only Fields
- Use `readOnly` attribute
- Apply `bg-gray-100` background
- Keep border visible

### Form Submission
- Disable submit during processing
- Show loading state
- Display toast notifications for success/error

---

**End of Employee UI Canon**

**For Agent E**: Use this document as your reference when building Customer, Lead, Contact, and Opportunity forms in the CRM module. Match the styling, structure, and patterns exactly to ensure UI consistency across HRM and CRM modules.




Agent E, please read 
C:\00mindra\olivine-erp-platform.steering\16_ONBOARDING\ONBOARD_COMPLETE.md
 carefully from beginning to end. It contains your complete onboarding, architectural rules, and the new simplified development strategy for HRM/CRM. Follow it strictly."

You are good to go! Good luck with the handoff! 🎉