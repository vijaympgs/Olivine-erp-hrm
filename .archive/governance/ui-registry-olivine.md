# UI Registry - Olivine Platform
## Canonical Screen Registration Document
## Version: 2.0.0
## Generated: 2026-01-25
## Status: AUTHORITATIVE
## Source Logic: ui-registry.yaml + menuConfig.ts

---

# REGISTRY PURPOSE

This document is the canonical UI registry for **Olivine Platform**.
All UI lookup, navigation, test mapping, and refactoring MUST consult this registry first.
Filesystem scanning is permitted ONLY when registry lacks an entry.

---

# MODULE: PLATFORM
## Core System & Utilities

### platform.admin.layout
- **name**: Layout Settings
- **module**: Platform
- **route**: /admin/layout-settings
- **menu**: Platform → System Administration → Layout Settings
- **frontend**: frontend/src/pages/admin/LayoutSettingsPage.tsx
- **backend**: unmapped
- **primary_component**: LayoutSettingsPage.tsx
- **test_status**: not_mapped

### platform.admin.pos_rules
- **name**: POS Business Rules
- **module**: Platform
- **route**: /pos/business-rules
- **menu**: Platform → System Administration → POS Business Rules
- **frontend**: unmapped
- **backend**: Retail/backend/pos/business_rules_admin.py
- **primary_component**: POSBusinessRulesPage.tsx
- **test_status**: not_mapped

### platform.tools.filesearch
- **name**: File Search Explorer
- **module**: Platform
- **route**: /admin/file-search
- **menu**: Platform → System Tools → File Search Explorer
- **frontend**: frontend/src/pages/admin/FileSearchExplorerPage.tsx
- **backend**: unmapped
- **primary_component**: FileSearchExplorerPage.tsx
- **test_status**: not_mapped

### platform.tools.backup
- **name**: Backup & Recovery
- **module**: Platform
- **route**: /admin/backup
- **menu**: Platform → System Tools → Backup & Recovery
- **frontend**: frontend/src/pages/admin/BackupPage.tsx
- **backend**: unmapped
- **primary_component**: BackupPage.tsx
- **test_status**: not_mapped

### platform.tools.visual_extractor
- **name**: Visual Extractor
- **module**: Platform
- **route**: /system-tools/visual-extractor
- **menu**: Platform → System Tools → Visual Extractor
- **frontend**: frontend/src/pages/system_tools/visual_extractor/VisualExtractorPage.tsx
- **backend**: unmapped
- **primary_component**: VisualExtractorPage.tsx
- **test_status**: not_mapped

### platform.tools.dataops
- **name**: DataOps Studio
- **module**: Platform
- **route**: /system-tools/dataops-studio
- **menu**: Platform → System Tools → DataOps Studio
- **frontend**: frontend/src/pages/system_tools/dataops_studio/DataOpsStudioPage.tsx
- **backend**: unmapped
- **primary_component**: DataOpsStudioPage.tsx
- **test_status**: not_mapped

### platform.tools.web_console
- **name**: Web Console
- **module**: Platform
- **route**: /system-tools/web-console
- **menu**: Platform → System Tools → Web Console
- **frontend**: frontend/src/pages/system_tools/web_console/WebConsolePage.tsx
- **backend**: unmapped
- **primary_component**: WebConsolePage.tsx
- **test_status**: not_mapped

### platform.tools.html_preview
- **name**: HTML Preview Tool
- **module**: Platform
- **route**: /system-tools/html-preview
- **menu**: Platform → System Tools → HTML Preview Tool
- **frontend**: frontend/src/pages/system_tools/html_preview/HtmlPreviewPage.tsx
- **backend**: unmapped
- **primary_component**: HtmlPreviewPage.tsx
- **test_status**: not_mapped

### platform.tools.wireframe_launchpad
- **name**: Wireframe Launchpad
- **module**: Platform
- **route**: /system-tools/wireframe-launchpad
- **menu**: Platform → System Tools → Wireframe Launchpad
- **frontend**: frontend/src/pages/system_tools/wireframe_launchpad/WireframeLaunchpadPage.tsx
- **backend**: unmapped
- **primary_component**: WireframeLaunchpadPage.tsx
- **test_status**: not_mapped

---

# MODULE: RETAIL
## Store Operations (POS)

### retail.pos.checkout
- **name**: POS Checkout
- **module**: Retail
- **route**: /pos/ui
- **menu**: Retail → Store Ops → Billing → Checkout
- **frontend**: frontend/src/pages/retail/pos/billing/PosPage.tsx
- **backend**: unmapped
- **primary_component**: PosPage.tsx
- **test_status**: not_mapped

### retail.pos.day_open
- **name**: Day Open
- **module**: Retail
- **route**: /operations/pos/day-open
- **menu**: Retail → Store Ops → Daily Operations → Day Open
- **frontend**: frontend/src/pages/retail/pos/day_open/DayOpenPage.tsx
- **backend**: unmapped
- **primary_component**: DayOpenPage.tsx
- **test_status**: not_mapped

### retail.pos.session_open
- **name**: Shift Start
- **module**: Retail
- **route**: /operations/pos/session-open
- **menu**: Retail → Store Ops → Daily Operations → Shift Start
- **frontend**: frontend/src/pages/retail/pos/session/SessionOpenPage.tsx
- **backend**: unmapped
- **primary_component**: SessionOpenPage.tsx
- **test_status**: not_mapped

## Merchandising & Master Data

### retail.master.items
- **name**: Item Master
- **module**: Retail
- **route**: /inventory/item-master
- **menu**: Retail → Merchandising → Product Catalog → Item Master
- **frontend**: frontend/src/pages/inventory/ItemMasterPage.tsx
- **backend**: unmapped
- **primary_component**: ItemMasterPage.tsx
- **test_status**: not_mapped

### retail.master.suppliers
- **name**: Supplier Master
- **module**: Retail
- **route**: /partners/suppliers
- **menu**: Retail → Procurement → Vendor Management → Supplier Master
- **frontend**: frontend/src/pages/partners/SupplierMasterPage.tsx
- **backend**: unmapped
- **primary_component**: SupplierMasterPage.tsx
- **test_status**: not_mapped

### retail.test.console
- **name**: Test Console
- **module**: Retail
- **route**: /test-console
- **menu**: Retail → Test Console
- **frontend**: frontend/src/pages/TestConsolePage.tsx
- **backend**: unmapped
- **primary_component**: TestConsolePage.tsx
- **test_status**: not_mapped

## Inventory Management

### inventory.dashboard
- **name**: Inventory Dashboard
- **module**: Retail
- **route**: /inventory/dashboard
- **menu**: Retail → Inventory → Dashboard
- **frontend**: frontend/src/pages/inventory/InventoryDashboard.tsx
- **backend**: unmapped
- **primary_component**: InventoryDashboard.tsx
- **test_status**: not_mapped

### inventory.stock.levels
- **name**: Stock on Hand
- **module**: Retail
- **route**: /inventory/levels
- **menu**: Retail → Inventory → Stock Management → Stock on Hand
- **frontend**: frontend/src/pages/inventory/StockLevelListPage.tsx
- **backend**: unmapped
- **primary_component**: StockLevelListPage.tsx
- **test_status**: not_mapped

---

# MODULE: FINANCIAL MANAGEMENT
## Accounting & Finance (BBP)

### finance.dashboard
- **name**: Finance Dashboard
- **module**: Finance
- **route**: /finance/dashboard
- **menu**: Finance → Dashboard
- **frontend**: frontend/src/pages/finance/FinanceDashboardPage.tsx
- **backend**: unmapped
- **primary_component**: FinanceDashboardPage.tsx
- **test_status**: not_mapped

### finance.setup.coa
- **name**: Chart of Accounts
- **module**: Finance
- **route**: /finance/setup/coa
- **menu**: Finance → Setup → Core Financial Setup → Chart of Accounts
- **frontend**: frontend/src/pages/finance/ChartOfAccountsPage.tsx
- **backend**: unmapped
- **primary_component**: ChartOfAccountsPage.tsx
- **test_status**: not_mapped

---

# MODULE: CRM
## Customer Relationship Management (BBP)

### crm.dashboard
- **name**: CRM Dashboard
- **module**: CRM
- **route**: /crm/dashboard
- **menu**: CRM → Dashboard
- **frontend**: frontend/src/pages/crm/CRMDashboardPage.tsx
- **backend**: unmapped
- **primary_component**: CRMDashboardPage.tsx
- **test_status**: not_mapped

---

# MODULE: HRM
## Human Resources (BBP)

### hrm.dashboard
- **name**: HR Dashboard
- **module**: HRM
- **route**: /hr/dashboard
- **menu**: HR → Dashboard
- **frontend**: HRM/frontend/src/pages/Dashboard.tsx
- **backend**: unmapped
- **primary_component**: Dashboard.tsx
- **test_status**: not_mapped

### hrm.employee.directory
- **name**: Employee Directory
- **module**: HRM
- **route**: /hr/employees
- **menu**: HR → Employee Management → Employee Directory
- **frontend**: HRM/frontend/src/pages/EmployeeDirectory.tsx
- **backend**: unmapped
- **primary_component**: EmployeeDirectory.tsx
- **test_status**: not_mapped
