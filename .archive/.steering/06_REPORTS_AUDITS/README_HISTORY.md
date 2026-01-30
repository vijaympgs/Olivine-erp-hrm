# 🤖 **AI AGENT MANDATORY PROTOCOL**

> [!IMPORTANT]
> **ANY AI AGENT starting a session MUST thoroughly index the [./.steering/](.steering/) directory.**
> This folder is the **SINGLE SOURCE OF TRUTH** for the heart, soul, and architecture of this project.
> **DO NOT PROCEED** until you have read the **[CANONICAL RULESET](./.steering/01_ARCH_GOVERNANCE/CANONICAL_RULESET.md)**.

### 🏛️ **Executive Steering & Governance**

1.  **[CANONICAL RULESET](./.steering/01_ARCH_GOVERNANCE/CANONICAL_RULESET.md)**: ⭐ **MASTER AUTHORITY**. Adhere strictly or risk rejection.
2.  **[Agent Governance](./.steering/01_ARCH_GOVERNANCE/README2_IMPPORTANT_FORAGENTS.md)**: Identity and terminology lock.
3.  **[SPA Architecture](./.steering/01_ARCH_GOVERNANCE/README3_IMPPORTANT_FORAGENTS_SPA_STRUCTURE.md)**: Mandatory frontend standards.
4.  **[Stabilization Checklist](./.steering/01_ARCH_GOVERNANCE/README2_Stabilization_Checklist.md)**: Quality and implementation bounds.
5.  **[Response Contract](./.steering/02_PROMPT_LIBRARY/PROMPT_GUIDE.MD)**: Standard for all agent communications.
6.  **[Retail Feature Tracker](./.steering/04_EXECUTION_PLANS/RETAIL_IMPLEMENTATION_TRACKER.md)**: Live implementation status.

### ⚡ **Quick Start Command**
To immediately initialize the agent and lock all rules, simply type:
> **/start**

## 🚀 **Next Session**
**Last Updated**: 2025-12-23 19:31 IST

### **Current State & Context**
"No OpCo Architecture" is stable. Reusable Transaction Toolbar and Theme Selector are implemented.

### **📝 TODO for Next Session**

#### 1. Procurement Module Refinement
- [ ] **Modal Integration**: Ensure `ProductLookupModal` and `SupplierLookupModal` are fully triggered via the new F1/F3 shortcuts in `PurchaseOrderFormPage.tsx` (presently logged to console).
- [ ] **State Logic**: Finalize `disabledActions` mapping for `REJECTED` and `SUBMITTED` states to ensure the toolbar visually reflects the business rules.
- [ ] **Data Scoping**: Verify that all lookups in the toolbar correctly pass the `currentCompanyId` for multi-tenant isolation.

#### 2. Transaction Toolbar Polish
- [ ] **Sticky Header**: Verify that the toolbar remains fixed at the absolute top of the viewport for long documents.
- [ ] **Hotkey Expansion**: Consider adding `Ctrl+P` (Print) and `Ctrl+S` (Save alias) to the global listener set.
- [ ] **State awareness**: Ensure "Authorize" and "Amend" actions correctly transition based on role permissions (UI logic only).

#### 3. POS & Inventory Alignment
- [ ] **POS Hotkeys**: Align the POS keyboard shortcuts (`Ctrl+K` etc.) to the new enterprise-standard "Product DNA" established by the Transaction Toolbar.
- [ ] **Inventory Lookups**: Integrate the new `Item Lookup (F1)` and `Location Lookup (Shift+F12)` into Stock Entry and Adjustment forms.

#### 4. Background & Theme Compatibility
- [ ] **Dark Mode Audit**: Verify the high-contrast `#f3f2f1` toolbar background correctly toggles or maintains readability in Dark/System modes.

### **🛠️ Recent Changes (Done)**
- [x] **Transaction Toolbar**: Implemented VB.NET inspired header bar with bold icons (18px) and high-contrast styling.
- [x] **Function Key Mapping**: Standardized F1-F12 shortcuts (F1 Item, F3 Supplier, F8 Save).
- [x] **Theme Selector**: Global App-Level Theme (Light, Dark, Auto) integrated into header.
- [x] **Code Sanitization**: Fixed breadcrumb type inference and variable name mismatches.

### 🚀 **Session Context**
*   **[Reference Build (READ-ONLY)](./01practice-v2/)**: Canonical reference. **DO NOT MODIFY.**

---

## 🔐 **Standard Credentials (PERMANENT)**

**AUTHORITATIVE REFERENCE** - These credentials are maintained across all environments:

| Username | Password     | Role                |
|----------|--------------|---------------------|
| admin    | admin123     | Administrator       |
| boadmin  | boadmin123   | Back Office Manager |
| bouser   | bouser123    | Back Office User    |
| posadmin | posadmin123  | POS Manager         |
| posuser  | posuser123   | POS User            |

**Login URL:** `http://localhost:5173/login`  
**Companies:** MINDRA, RRI  
**Restore:** Run `python set_passwords.py` to reset credentials

📖 **Full Details:** See `STANDARD_CREDENTIALS.md` and `LOGIN_CREDENTIALS.md`

---

## 📋 **Recent Updates**

### ✅ **Completed 2025-12-22 (No OpCo Architecture Validation)**:
1. **No OpCo Architecture Alignment** - Verified complete removal of `OperatingCompany` abstraction
   - Backend: All models (`PurchaseOrder`, `ItemMaster`, etc.) now link directly to `Company`.
   - Frontend: Services (`authService`, `companyService`, `locationService`) updated to use `Company` and `currentCompanyId`.
   - Admin UI: Removed all OpCo-related models; simplified to `Company` and `Location`.
2. **Critical Login & Location Hotfixes**
   - **LoginView Hotfix**: Corrected company lookup to support integer IDs (`isdigit()` check) instead of assuming UUID string length > 30.
   - **Location API Path Fix**: Updated `locationService.ts` to use `/api/auth/user-locations/` (added missing `/auth/` prefix).
   - **Temporary Location Bypass**: Modified `UserLocationListView` to return all active locations for a company, unblocking the UI selection modal.
3. **Seeding Refinement**
   - Successfully executed `seed_refined.py` ensuring all master data adheres to the new hierarchy.
   - Verified `UserCompanyMapping` creation for standard users.

### ✅ **Completed 2025-12-21 (Company Architecture)**:
1. **Company Model Refactoring** - Unified backend company references
   - Refactored `domain.company` and `domain.pos` models to point to canonical `business_entities.Company`
   - Updated `seed_data.py` to use canonical Company/Customer/Supplier models
   - Flushed and re-seeded database with correct hierarchy
   - **Result**: "Single Source of Truth" for Company data established

2. **Admin UI Re-Architecture** - Strict context separation
   - **Licensing App**: Created virtual app for read-only "Business Entity" view (Proxy Model)
   - **Application Companies**: Renamed `domain.company` app label, added "OperationalCompany" Proxy
   - **Benefit**: Clear visual separation of License Owner vs Operating Entity in Admin Sidebar without schema changes

3. **Frontend Service Alignment**
   - Verified `locationService.ts` points to legacy `/api/locations` (correctly wired to BE)
   - Verified `companyService.ts` points to canonical `/api/business/companies`

### ✅ **Completed 2025-12-20 (Late Evening)**:
1. **Sidebar UI Enhancements** - Complete redesign with clean, mobile-app style
   - Larger icons (20px) for all menu levels
   - Subtitles with configurable wrap/truncate behavior
   - ChevronRight (>) indicators for expandable items
   - Dynamic spacing control (compact/normal/comfortable)
   - Proper config integration using centralized layout system
   - Fixed sidebar width to respect layout settings (now uses CSS variables)
   - Fixed Layout Settings page positioning to prevent black area after width changes
2. **Layout Configuration Enhancements** - New user preferences
   - Added `subtitleWrap` setting: 'single-line' (truncate) or 'wrap' (multi-line)
   - Added `menuItemSpacing` setting: 'compact', 'normal', or 'comfortable'
   - Both settings available in Layout Settings page with live preview
3. **Documentation Organization** - Restructured 35 markdown files
   - Created 4 focused folders: `reference/`, `standards/`, `implementation/`, `troubleshooting/`
   - Moved files from root and `docs/` into organized structure
   - Updated README with complete documentation navigation
   - Enhanced `Refer_this_before_new_UI_module.md` with cross-references
   - Created index files and summary documentation
   - **Goal**: Make it easy for AI agents to find relevant docs before development

### ✅ **Completed 2025-12-20 (Evening)**:
1. **Inventory Module Backend** - Complete backend implementation for Inventory Management
   - Created 8 models: StockMovement, StockLevel, ReorderPolicy, StockTransfer, StockTake, StockAdjustment
   - Full DRF API with serializers, views, URLs, admin
   - Custom actions: low_stock, approve, post_transfer, post_stock_take, post_adjustment
   - **Status**: Backend complete, migrations blocked by Django config issue
2. **Inventory Module Frontend** - Complete UI pages following Dynamics 365 design
   - Created 6 List pages: Stock Levels, Movements, Transfers, Stock Take, Adjustments, Reorder Policies
   - Dynamics 365-inspired design with Fluent UI patterns
   - Routes registered in router.tsx
   - **Status**: UI complete, ready for testing once migrations resolved
3. **Product Showcase Deck** - Enhanced presentation with 17 slides
   - Captured 11 module screenshots (Login, Dashboard, POS, Sales, Procurement, etc.)
   - PowerPoint-style layout with 16:9 aspect ratio
   - Professional animations and navigation

### ✅ **Completed 2025-12-20 (Morning)**:
1. **Phase 2 Toggle Fix** - Fixed real-time reactivity for "Show Phase 2 Features" toggle
   - Added `layout-config-update` event dispatch in `layoutConfig.ts`
   - Added event listener in `useLayoutConfig.ts` hook
   - Sidebar now updates immediately when toggling Phase 2 without page reload
2. **Event-Driven Configuration** - Improved layout configuration system for same-tab updates
3. **Finance Phase 1 Simplification** - Streamlined Financial Management module
   - Reduced from 20 subgroups (~200 items) to 9 subgroups (~65 items)
   - Moved 11 advanced subgroups to Phase 2 menu
   - Cleaner, more focused menu for core finance operations
   - **Documentation**: [`docs/FINANCE_PHASE1_SIMPLIFICATION.md`](docs/FINANCE_PHASE1_SIMPLIFICATION.md)
4. **Module Visibility Toggles** - Added individual module show/hide controls
   - Toggle visibility for Retail, Finance, CRM, and HRM modules independently
   - Accessible via **System Administration → Layout Settings → Module Visibility**
   - Allows users to focus on specific business areas
   - All modules visible by default

### ✅ **Completed 2025-12-19**:
1. **Menu Reorganization** - Restructured into 4 main modules
2. **Financial Management Module** - Enterprise-grade with 20 subgroups (~200 items)
3. **CRM Module** - Standalone module with 18 subgroups (~180 items)
4. **Page Layout Fixes** - Applied global CSS utility classes to 11 pages
5. **Layout Settings Fix** - Connected LayoutManager properly
6. **Documentation** - Comprehensive guides and implementation summaries
7. **Login Experience** - Redesigned with modern "Console Access" theme, 50/50 split layout, and "flat" aesthetics
8. **Command Palette** - Fixed `Ctrl+K` shortcut, search routing, and visual styling

**📄 Session Handoff**: [`docs/session_handovers/SESSION_HANDOFF_2025-12-19.md`](docs/session_handovers/SESSION_HANDOFF_2025-12-19.md)

---

## 🏗️ **System Architecture**

### **Technology Stack**:
- **Backend**: Django REST Framework with PostgreSQL/SQLite
- **Frontend**: React + TypeScript + Vite
- **Styling**: Tailwind CSS + Custom CSS Variables
- **Database**: PostgreSQL (production) / SQLite (development)

### **Module Structure** (4 Main Modules):

```
📊 Dashboard
─────────────────────────

🏪 MODULE 1: RETAIL OPERATIONS (6 subgroups, ~36 items)
   ├── Point of Sale (POS)
   ├── Sales & Revenue
   ├── Customer Management
   ├── Inventory Management
   ├── Procurement & Purchasing
   └── Master Data

💰 MODULE 2: FINANCIAL MANAGEMENT (9 subgroups, ~65 items - Phase 1 Only)
   ├── Finance Dashboard
   ├── General Ledger
   ├── Accounts Receivable (AR)
   ├── Accounts Payable (AP)
   ├── Cash & Bank
   ├── Payments
   ├── Tax Management (GST, TDS, VAT)
   ├── Financial Reports
   └── Period Closing

🤝 MODULE 3: CUSTOMER RELATIONSHIP MANAGEMENT (18 subgroups, ~180 items)
   ├── CRM Dashboard & Analytics
   ├── Lead Management
   ├── Contact Management
   ├── Account Management
   ├── Opportunity Management
   ├── Sales Pipeline & Forecasting
   ├── Quote & Proposal Management (CPQ)
   ├── Campaign Management
   ├── Email Marketing & Automation
   ├── Customer Service & Support
   ├── Customer Engagement & Communication
   ├── Customer Loyalty & Retention
   ├── Partner & Channel Management
   ├── Sales Enablement
   ├── Analytics & Reporting
   ├── Workflow & Automation
   ├── Integration & Data Management
   └── CRM Configuration & Administration

👥 MODULE 4: HUMAN RESOURCES (14 subgroups, ~60 items)
   ├── HR Dashboard
   ├── Employee Management
   ├── Talent Acquisition
   ├── Compensation & Payroll
   ├── Time & Attendance
   ├── Performance Management
   ├── Learning & Development
   ├── Employee Engagement & Recognition
   ├── Workforce Planning & Analytics
   ├── Compliance & Policies
   ├── Offboarding & Exit Management
   ├── HR Reports & Analytics
   ├── Access & Security
   └── Integrations & Configuration

─────────────────────────
🛡️ System Administration
⚙️ System Configuration
```

---

## � **Documentation Organization**

Our documentation is organized into focused folders for easy navigation:

### **📚 Core Documentation** (Root)
- **[README.md](./README.md)** - This file, project overview and quick start
- **[RETAIL_IMPLEMENTATION_TRACKER.md](./RETAIL_IMPLEMENTATION_TRACKER.md)** - Implementation status tracker

### **📖 Reference** ([`docs/reference/`](./docs/reference/))
Essential guides to consult before development:
- **[Refer This Before New UI Module](./docs/reference/Refer_this_before_new_UI_module.md)** - ⭐ **START HERE** for all UI/module work
- [Sidebar Quick Reference](./docs/reference/SIDEBAR_QUICK_REFERENCE.md)
- [Section C Migration Guide](./docs/reference/SECTION_C_MIGRATION_GUIDE.md)
- [Layout Configuration System](./docs/reference/LAYOUT_CONFIGURATION_SYSTEM.md)
- [Menu Tree Structure](./docs/reference/MENU_TREE_STRUCTURE.md)
- [POS Implementation Guide](./docs/reference/POS_IMPLEMENTATION_GUIDE.md)
- [Accordion Implementation Guide](./docs/reference/ACCORDION_IMPLEMENTATION_GUIDE.md)

### **📐 Standards** ([`docs/standards/`](./docs/standards/))
Development standards and best practices:
- [UI Layout Terminology](./docs/standards/UI_LAYOUT_TERMINOLOGY.md)
- [Olivine Sidebar Enhancement Prompt](./docs/standards/OLIVINE_SIDEBAR_ENHANCEMENT_PROMPT.md)
- [Final UI Steps](./docs/standards/FINAL_UI_STEPS.md)

### **🚀 Implementation** ([`docs/implementation/`](./docs/implementation/))
Module implementation plans and status:
- CRM, Financial Management, Inventory, Procurement
- Menu reorganization, Layout simplification
- Phase 2 & 3 implementations

### **🔧 Troubleshooting** ([`docs/troubleshooting/`](./docs/troubleshooting/))
Fixes, issues, and resolution guides:
- AppHeader, Font consistency, Page positioning
- Migration issues, Layout settings refinements

### **📋 Business Process Blueprints** ([`docs/bbp/`](./docs/bbp/))
Detailed business process specifications:
- POS, Procurement, Inventory modules
- Standards and compliance requirements

### **🔍 Other Folders**
- **[`docs/specifications/`](./docs/specifications/)** - Technical specifications
- **[`docs/steering/`](./docs/steering/)** - Project steering documents
- **[`docs/fixes/`](./docs/fixes/)** - Bug fixes and patches
- **[`docs/templates/`](./docs/templates/)** - Document templates

---

## �📚 **Documentation Hub**

### **🎯 Implementation Guides**:

#### **Menu & Navigation**:
- [`docs/MENU_REORGANIZATION_COMPLETE.md`](docs/MENU_REORGANIZATION_COMPLETE.md) - Complete menu restructuring
- [`docs/MENU_REORGANIZATION_PROPOSAL.md`](docs/MENU_REORGANIZATION_PROPOSAL.md) - Original proposal
- [`docs/MENU_TREE_STRUCTURE.md`](docs/MENU_TREE_STRUCTURE.md) - **Visual tree structure** (Complete hierarchy)
- [`docs/RETAIL_IMPLEMENTATION_TRACKER.md`](docs/RETAIL_IMPLEMENTATION_TRACKER.md) - **Retail Implementation Tracker** (New)

#### **Financial Management**:
- [`docs/FINANCIAL_MANAGEMENT_IMPLEMENTATION_COMPLETE.md`](docs/FINANCIAL_MANAGEMENT_IMPLEMENTATION_COMPLETE.md) - Complete implementation
- [`docs/FINANCIAL_MANAGEMENT_MENU_PROPOSAL.md`](docs/FINANCIAL_MANAGEMENT_MENU_PROPOSAL.md) - Original proposal
- **Inspiration**: Tally (P1), NetSuite (P2), SAP (P3)
- **Features**: 20 subgroups, ~200 items, GST/TDS compliance, Multi-currency, ASC 606

#### **CRM Module**:
- [`docs/CRM_IMPLEMENTATION_COMPLETE.md`](docs/CRM_IMPLEMENTATION_COMPLETE.md) - Complete implementation
- [`docs/CRM_MODULE_PROPOSAL.md`](docs/CRM_MODULE_PROPOSAL.md) - Original proposal
- **Inspiration**: Salesforce (P1), HubSpot (P2), Microsoft Dynamics 365 (P3)
- **Features**: 18 subgroups, ~180 items, Lead-to-Cash, Marketing Automation, CPQ

#### **UI/UX & Layout**:
- [`docs/GLOBAL_PAGE_POSITIONING_FIX.md`](docs/GLOBAL_PAGE_POSITIONING_FIX.md) - Page layout standardization
- [`docs/PAGE_POSITIONING_UPDATES_SUMMARY.md`](docs/PAGE_POSITIONING_UPDATES_SUMMARY.md) - Implementation summary
- [`docs/FONT_CONSISTENCY_UPDATE.md`](docs/FONT_CONSISTENCY_UPDATE.md) - Font standardization
- [`docs/fixes/LAYOUT_SETTINGS_NOT_APPLYING_FIX.md`](docs/fixes/LAYOUT_SETTINGS_NOT_APPLYING_FIX.md) - Layout settings fix

#### **POS System**:
- [`docs/POS_IMPLEMENTATION_GUIDE.md`](docs/POS_IMPLEMENTATION_GUIDE.md) - POS implementation
- [`docs/POS_IMPROVEMENTS_PLAN.md`](docs/POS_IMPROVEMENTS_PLAN.md) - Enhancement roadmap
- [`docs/fixes/POS_CART_HEADER_ALIGNMENT_FIX.md`](docs/fixes/POS_CART_HEADER_ALIGNMENT_FIX.md) - Alignment fixes

#### **Master Pages**:
- [`docs/MASTER_PAGES_VERIFICATION.md`](docs/MASTER_PAGES_VERIFICATION.md) - Master page verification

---

## 🎨 **Frontend Architecture**

### **Key Files**:
- **Menu Configuration**: `frontend/src/app/menuConfig.ts` (4 modules, ~500+ items)
- **Global Styles**: `frontend/src/styles/layout.css` (CSS variables, utility classes)
- **Layout Manager**: `frontend/src/config/layoutConfig.ts` (Dynamic layout configuration)
- **Main Entry**: `frontend/src/main.tsx` (App initialization)

### **CSS Utility Classes** (New):
```css
.page-container          /* Standard pages (max-width: 1280px) */
.page-container-full     /* Full-width pages */
.page-container-scroll   /* Scrollable pages */
.page-spacing            /* Spacing only */
```

### **CSS Variables**:
```css
--header-height: 64px
--statusbar-height: 48px
--sidebar-width: 256px
--font-family: 'Inter', sans-serif
```

### **Pages Updated** (11 pages):
1. `AttributeSetup.tsx`
2. `AttributeValueSetup.tsx`
3. `LocationSetup.tsx`
4. `PriceListSetup.tsx`
5. `ProductAttributeTemplateSetup.tsx`
6. `UOMSetup.tsx`
7. `ItemMasterSetup.tsx`
8. `CustomerSetup.tsx`
9. `SupplierSetup.tsx`
10. `EmployeeListPage.tsx`
11. `DashboardPage.tsx`

---

## 🔧 **Development Standards**

### **Ruleset & Guidelines**:
- [`ruleset/CODING_STANDARDS.md`](ruleset/CODING_STANDARDS.md) - Code quality standards
- [`ruleset/DEVELOPMENT_WORKFLOW.md`](ruleset/DEVELOPMENT_WORKFLOW.md) - Development process
- [`ruleset/UI_UX_GUIDELINES.md`](ruleset/UI_UX_GUIDELINES.md) - Design standards

### **Specifications**:
- [`docs/specifications/CENTRALIZED_CSS_CONFIG.md`](docs/specifications/CENTRALIZED_CSS_CONFIG.md) - CSS architecture
- [`docs/specifications/EMPLOYEE_FORM_SPEC.md`](docs/specifications/EMPLOYEE_FORM_SPEC.md) - Form standards
- [`docs/steering/prompt_ui_standard.md`](docs/steering/prompt_ui_standard.md) - UI prompts

---

## 🚀 **Quick Start**

### **Prerequisites**:
- Python 3.9+
- Node.js 18+
- PostgreSQL (for production)

### **Backend Setup**:
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### **Frontend Setup**:
```bash
cd frontend
npm install
npm run dev
```

### **Access**:
- Frontend: `http://localhost:5173`
- Backend API: `http://localhost:8000`
- Admin Panel: `http://localhost:8000/admin`

---

## 📊 **Module Statistics**

| Module | Subgroups | Menu Items | Depth | Status |
|--------|-----------|------------|-------|--------|
| **Retail Operations** | 6 | ~36 | 3 | ✅ Complete |
| **Financial Management (Phase 1)** | 9 | ~65 | 3 | ✅ Complete |
| **CRM** | 18 | ~180 | 4 | ✅ Complete |
| **Human Resources** | 14 | ~60 | 3 | ✅ Complete |
| **System-Wide** | 2 | ~10 | 2 | ✅ Complete |
| **Phase 2 (Advanced)** | 3 | ~21 | 3 | ✅ Complete |
| **TOTAL** | **52** | **~372** | 4 | ✅ |

---

## 🎯 **Enterprise Features**

### **Financial Management** (Inspired by Tally + NetSuite + SAP):
- ✅ Complete GL, AR, AP, Bank Management
- ✅ GST/TDS/VAT compliance (India)
- ✅ Multi-currency & FX management
- ✅ Fixed assets & depreciation
- ✅ Cost accounting & job costing
- ✅ Budgeting & forecasting
- ✅ Revenue recognition (ASC 606)
- ✅ Treasury & cash management
- ✅ Period-end closing & audit trail
- ✅ 30+ standard financial reports

### **CRM** (Inspired by Salesforce + HubSpot + Dynamics 365):
- ✅ Lead-to-Cash automation
- ✅ Sales pipeline & forecasting
- ✅ Marketing automation
- ✅ Email campaigns & sequences
- ✅ Customer service & support
- ✅ Loyalty & retention programs
- ✅ CPQ (Configure, Price, Quote)
- ✅ Partner & channel management
- ✅ 360° customer view
- ✅ AI-powered insights

### **Retail Operations**:
- ✅ POS system with offline mode
- ✅ **Inventory management** (Backend & Frontend complete, migrations blocked)
- ✅ Procurement & purchasing
- ✅ Multi-location support
- ✅ Pricing & promotions
- ✅ Returns & refunds

### **Human Resources**:
- ✅ Employee lifecycle management
- ✅ Payroll & compensation
- ✅ Time & attendance
- ✅ Performance management
- ✅ Learning & development
- ✅ Recruitment & onboarding

---

## 🔌 **Integration Capabilities**

### **Financial Integrations**:
- Bank integration
- Payment gateways
- Tax portals (GST, TDS)
- Accounting systems

### **CRM Integrations**:
- Email (Gmail, Outlook)
- Calendar sync
- Social media (LinkedIn, Twitter, Facebook)
- WhatsApp messaging
- Telephony (CTI)
- E-commerce platforms
- Marketing automation tools

### **General Integrations**:
- API management
- Webhooks
- Data import/export
- Third-party apps

---

## 📁 **Project Structure**

```
retail-erp-platform/
├── backend/                    # Django REST API
│   ├── domain/                # Business logic modules
│   ├── erp_core/              # Django project settings
│   └── requirements.txt       # Python dependencies
│
├── frontend/                   # React + TypeScript
│   ├── src/
│   │   ├── app/               # App configuration
│   │   │   └── menuConfig.ts  # Menu structure (4 modules)
│   │   ├── config/            # Configuration files
│   │   │   └── layoutConfig.ts # Layout manager
│   │   ├── modules/           # Feature modules
│   │   │   ├── pos/          # POS system
│   │   │   └── ...
│   │   ├── pages/             # Page components
│   │   │   ├── admin/        # Admin pages
│   │   │   ├── hr/           # HR pages
│   │   │   └── ...
│   │   ├── styles/            # Global styles
│   │   │   └── layout.css    # Layout utilities
│   │   ├── ui/                # UI components
│   │   └── main.tsx           # App entry point
│   └── package.json           # Node dependencies
│
├── docs/                       # Documentation
│   ├── fixes/                 # Bug fix documentation
│   ├── specifications/        # Technical specs
│   ├── steering/              # Project guidance
│   ├── FINANCIAL_MANAGEMENT_IMPLEMENTATION_COMPLETE.md
│   ├── CRM_IMPLEMENTATION_COMPLETE.md
│   ├── GLOBAL_PAGE_POSITIONING_FIX.md
│   └── ...
│
├── ruleset/                    # Development standards
│   ├── CODING_STANDARDS.md
│   ├── DEVELOPMENT_WORKFLOW.md
│   └── UI_UX_GUIDELINES.md
│
└── README.md                   # This file
```

---

## 🐛 **Known Issues & Fixes**

### **Fixed**:
- ✅ Layout settings not applying (localStorage key mismatch) - **FULLY RESOLVED** - [`docs/fixes/LAYOUT_SETTINGS_FIX_SUMMARY.md`](docs/fixes/LAYOUT_SETTINGS_FIX_SUMMARY.md)
- ✅ POS header alignment issues - [`docs/fixes/POS_CART_HEADER_ALIGNMENT_FIX.md`](docs/fixes/POS_CART_HEADER_ALIGNMENT_FIX.md)
- ✅ Page content hidden under header - [`docs/GLOBAL_PAGE_POSITIONING_FIX.md`](docs/GLOBAL_PAGE_POSITIONING_FIX.md)
- ✅ Font inconsistency across pages - [`docs/FONT_CONSISTENCY_UPDATE.md`](docs/FONT_CONSISTENCY_UPDATE.md)
- ✅ Sidebar parent menu incorrectly highlighted - [`docs/fixes/SIDEBAR_PARENT_ACTIVE_FIX.md`](docs/fixes/SIDEBAR_PARENT_ACTIVE_FIX.md)
- ✅ Sidebar flat design update - [`docs/fixes/SIDEBAR_FLAT_DESIGN_UPDATE.md`](docs/fixes/SIDEBAR_FLAT_DESIGN_UPDATE.md)
- ✅ Layout settings integration (Subtitles, Header) - [`docs/fixes/LAYOUT_CONFIG_INTEGRATION.md`](docs/fixes/LAYOUT_CONFIG_INTEGRATION.md)
- ✅ Login Page Overhaul (Modern Split Layout, Access ID/Passkey)
- ✅ Command Palette Fix (Recursive Search, Ctrl+K)

### **Pending**:
- ⏳ **Resolve Inventory module migrations** (Django app registry config)
- ⏳ Implement placeholder pages for new Financial Management items
- ⏳ Implement placeholder pages for new CRM items
- ⏳ Build reporting engine for 30+ financial reports
- ⏳ Integrate tax portals (GST, TDS)
- ⏳ Setup email integration (Gmail, Outlook)
- ⏳ Implement CPQ (Configure, Price, Quote)

---

## 🎯 **Next Steps**

### **Immediate Priorities**:
1. **Resolve Inventory migrations** (see `RETAIL_IMPLEMENTATION_TRACKER.md` for details)
2. **Test Inventory UI** once migrations are resolved
3. **Create placeholder pages** for Financial Management module
4. **Create placeholder pages** for CRM module
5. **Implement core financial modules** (GL, AR, AP)
6. **Implement core CRM modules** (Leads, Contacts, Opportunities)

### **Short-term Goals**:
1. Implement financial reporting engine
2. Build CRM analytics dashboard
3. Integrate tax portals (GST, TDS)
4. Setup marketing automation workflows
5. Implement CPQ functionality
6. Build mobile sales app

### **Long-term Vision**:
1. AI-powered insights and predictions
2. Advanced analytics and BI
3. Multi-tenant support
4. Mobile apps (iOS, Android)
5. Offline-first architecture
6. Real-time collaboration

---

## 📖 **Reference Documentation**

### **For Future Sessions**:

#### **Menu Structure**:
- File: `frontend/src/app/menuConfig.ts`
- 4 main modules: Retail, Financial, CRM, HRM
- Total: ~486 menu items across 60 subgroups
- Depth: Up to 4 levels

#### **Layout System**:
- File: `frontend/src/styles/layout.css`
- CSS Variables: `--header-height`, `--statusbar-height`, `--sidebar-width`
- Utility Classes: `.page-container`, `.page-container-full`, `.page-container-scroll`
- Layout Manager: `frontend/src/config/layoutConfig.ts`

#### **Module Implementations**:
1. **Financial Management**: 20 subgroups, Tally/NetSuite/SAP inspired
2. **CRM**: 18 subgroups, Salesforce/HubSpot/Dynamics 365 inspired
3. **Retail Operations**: 6 subgroups, POS-focused
4. **HRM**: 14 subgroups, comprehensive HR suite

#### **Key Decisions Made**:
- ✅ CRM as separate top-level module (not under Retail)
- ✅ Master Data under Retail Operations
- ✅ Reports split into module-specific sections
- ✅ Global CSS utility classes for consistent layout
- ✅ LayoutManager for dynamic configuration

---

## 🤝 **Contributing**

### **Development Workflow**:
1. Check [`ruleset/DEVELOPMENT_WORKFLOW.md`](ruleset/DEVELOPMENT_WORKFLOW.md)
2. Follow [`ruleset/CODING_STANDARDS.md`](ruleset/CODING_STANDARDS.md)
3. Adhere to [`ruleset/UI_UX_GUIDELINES.md`](ruleset/UI_UX_GUIDELINES.md)
4. Document changes in `docs/`

### **Code Standards**:
- TypeScript for frontend
- Python (Django) for backend
- Tailwind CSS + Custom CSS Variables
- Component-based architecture
- API-first design

---

## 🎯 **Next Steps & Priorities**

### **🔴 CRITICAL - High Priority**:
1. **Inventory Module Backend Migration** - BLOCKED
   - **Issue**: Django model migrations failing due to app registry configuration
   - **Error**: `RuntimeError: Model class ... doesn't declare an explicit app_label...`
   - **Impact**: Backend complete but cannot persist data, frontend ready but cannot test
   - **Action Required**: Fix Django app configuration in `backend/domain/inventory/apps.py`
   - **Status**: 🔴 **BLOCKING** - Must resolve before proceeding
   - **Reference**: [`docs/implementation/INVENTORY_IMPLEMENTATION_STATUS.md`](./docs/implementation/INVENTORY_IMPLEMENTATION_STATUS.md)

### **🟡 HIGH - Next Session**:
2. **Inventory Module Integration** (After migration fix)
   - Connect frontend pages to backend APIs
   - Test all CRUD operations
   - Implement form pages (Transfer, Stock Take, Adjustment)
   - End-to-end testing with real data

3. **Inventory Module Completion**
   - Stock movement tracking validation
   - Reorder policy automation
   - Stock take reconciliation
   - Approval workflows for adjustments

### **🟢 MEDIUM - Future Sessions**:
4. **Procurement Module** - Forms and workflows
5. **Sales Module** - Order processing enhancements
6. **Reports & Analytics** - Dashboard widgets

### **📋 Documentation Needed**:
- Session handoff document for Inventory work
- Migration troubleshooting guide
- Inventory module user guide

---

## 📞 **Support & Resources**

### **Documentation**:
- All docs in `docs/` directory
- Implementation guides for each module
- Fix documentation in `docs/fixes/`
- Specifications in `docs/specifications/`

### **Key Contacts**:
- Project Lead: [Your Name]
- Backend Team: [Team Info]
- Frontend Team: [Team Info]

---

## 📝 **Version History**

### **v2.0.0** (2025-12-19):
- ✅ Complete menu reorganization (4 modules)
- ✅ Enterprise-grade Financial Management (20 subgroups)
- ✅ Standalone CRM module (18 subgroups)
- ✅ Global page layout fixes (11 pages)
- ✅ Layout settings fix
- ✅ Comprehensive documentation

### **v1.0.0** (Previous):
- Initial ERP platform
- Basic POS system
- Inventory management
- HR module foundation

---

## 📄 **License**

[Your License Here]

---

**Last Updated**: 2025-12-22 20:40:30 IST  
**Maintained By**: Development Team  
**Status**: ✅ Active Development  
**Next Review**: 2025-12-21


**Execution Rule:***

Additional execution rule:

For any changes or implementations during Phase 1 (Context Foundation),
refer to **01practice-v2** as the canonical baseline for retail platform patterns.

- Reuse established approaches where applicable
- Align naming, flow, and structure with 01practice-v2
- Do NOT redesign patterns that already exist there
- Deviations must be explicitly justified

01practice-v2 is the reference build for:
- Retail login patterns
- Company / Location context handling
- Foundational master usage

Critical execution constraint:

The folder **01practice-v2/** is a READ-ONLY reference implementation.

Rules:
1. Do NOT modify, refactor, rename, reformat, or touch any files under 01practice-v2/.
2. Do NOT run migrations, formatting, or auto-fixes in this folder.
3. Do NOT copy files from 01practice-v2 and modify them in place.
4. 01practice-v2 is for REFERENCE ONLY.

Usage guidance:
- Study patterns, flows, and structures in 01practice-v2.
- Re-implement or adapt patterns ONLY in the active platform codebase.
- Any deviation from 01practice-v2 patterns must be explicitly stated.

Any change inside 01practice-v2, even accidental, is considered a critical violation.
