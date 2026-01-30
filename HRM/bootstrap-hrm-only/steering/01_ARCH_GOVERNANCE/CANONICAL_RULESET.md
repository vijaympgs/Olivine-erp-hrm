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
