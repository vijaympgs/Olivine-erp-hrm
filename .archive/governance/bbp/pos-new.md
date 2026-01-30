# POS Blueprint - Business Requirements & Implementation Plan

**Created:** 01-Nov-2025 14:32:00 IST  
**Last Updated:** 04-Nov-2025 03:39:48 IST  
**Purpose:** Single source of truth for all POS requirements, analysis, and implementation

---

## 🎯 Table of Contents

1. [Confirmed Workflow](#confirmed-workflow)
2. [Industry Analysis](#industry-analysis)
3. [Business Requirements](#business-requirements)
4. [Technical Requirements](#technical-requirements)
5. [Architecture & Scalability](#architecture--scalability)
6. [Implementation Status](#implementation-status)
7. [Pending Items](#pending-items)

---

## ✅ Confirmed Workflow

### **Workflow:** Day Open → Session Open → Billing → Settlement → Session Close → Day Close

**Menu Order:**
```
1. Terminal Configuration (Setup only)
2. Day Open (Store-level, once per business day)
3. Session Open (Cashier-level, multiple per day)
4. Billing (Repeatable)
5. Settlement (Deferrable - "Now" or "Later")
6. Session Close (End cashier shift)
7. Day Close (End business day - includes settlement validation)
```

**Notes:**
- "Billing Close" is NOT a menu item - it's the Billing→Settlement navigation
- "Float details" is integrated into Session Open
- Settlement can be deferred, but MUST be completed before Day Close
- Cashiers can continue billing without completing settlement

---

## 🔍 Industry Analysis

### **Market Leaders Researched**

#### **1. SAP Retail POS (SAP CAR)**
**Workflow:**
```
Day Open (Store Level) → Session Open (Cashier Level) → 
Terminal Opening → Billing → Settlement → Session Close → Day Close
```
**Key Concept:** Two-tier hierarchy (Store → Cashier)

#### **2. Oracle Retail (RMS/XStore)**
**Workflow:**
```
Day Open (Business Date) → Cashier Login/Session Open → 
Cash Drawer Setup → Billing → Settlement → Session Close → Day Close
```
**Key Concept:** Business date management

#### **3. TCS OmniStore Retail**
**Workflow:**
```
Store Day Open → Register Session Open → 
Cash Float Setup → Billing → Settlement → Register Close → Store Day Close
```
**Key Concept:** Store → Register hierarchy

#### **4. Square/Square POS**
**Workflow:**
```
Location Day Open (Optional) → Employee Session → 
Cash Drawer Setup → Billing → Shift Close → Day Close
```
**Key Concept:** Optional Day Open for SMBs

#### **5. Toast/PayPal POS**
**Workflow:**
```
Manager Day Start → Staff Shift Open → 
Cash Handling → Billing → Cash Out → Shift Close → Day End
```
**Key Concept:** Manager-initiated day start

### **Industry Standard Recommendation: APPROACH 2**
- Day Open established as store-level, once-per-day operation
- Session Open for cashier-level, shift-based operations
- Two-tier hierarchy for scalability and auditing
- Business date management for compliance

---

## 📋 Business Requirements

### **1. Day Open**
- **Frequency:** Once per business day per location
- **Who:** Store Manager / Authorized User
- **Purpose:**
  - Establish business/accounting date
  - Reset document sequences
  - Initialize day operations
- **Validation:** None (first operation)
- **Status:** ✅ Complete

### **2. Session Open**
- **Frequency:** Once per cashier shift
- **Who:** Cashier / POS User
- **Purpose:**
  - Start cashier's session
  - Set opening float (cash balance)
  - Allocate terminal
- **Validation:** Requires active Day Open
- **Status:** ✅ Complete

### **3. Billing**
- **Frequency:** Multiple per session
- **Who:** Cashier
- **Purpose:**
  - Process customer transactions
  - Accept payments
  - Generate receipts
- **Navigation:** Close button → Settlement page
- **Status:** ✅ Complete

### **4. Settlement**
- **Frequency:** Optional (can be deferred)
- **Who:** Cashier
- **Purpose:**
  - Reconcile transactions
  - Count cash
  - Calculate differences
- **Options:**
  - "Settle Now" → Complete immediately
  - "Later" → Deferred to Day Close
- **Constraint:** Can continue billing without settlement, but MUST be completed before Day Close
- **Status:** ✅ Complete

### **5. Session Close**
- **Frequency:** End of cashier's shift
- **Who:** Cashier
- **Purpose:**
  - Finalize cashier's session
  - Consolidate session data
- **Modes:** Temporary (can reopen) or Permanent (final close)
- **Status:** ✅ Complete

### **6. Day Close**
- **Frequency:** Once per business day
- **Who:** Store Manager / Authorized User
- **Purpose:**
  - Finalize all business day activities
  - Consolidate sales across sessions
  - Generate reports, backup data
- **Validations:**
  - ✅ All sessions closed
  - ✅ **All settlements completed** (critical - no "Later" pending)
  - ✅ Reports generated
  - ✅ Backup completed
  - ✅ Cash counted
  - ✅ Inventory verified
- **Status:** ✅ Complete

---

## 🔧 Technical Requirements

### **Backend Models**

#### **DayOpen** ✅
- Business date management
- Document sequence initialization
- Location-scoped (one per business date)
- `next_sale_number`, `next_session_number`

#### **DayClose** ✅
- Day end consolidation
- Checklist validation
- Settlement verification (blocks if pending)
- Sales/transactions aggregation

#### **POSSession** ✅
- Cashier session tracking
- Opening/closing cash
- Settlement status (`pending`/`completed`)
- Close modes (temporary/permanent)

#### **Sale** ✅
- Transaction records
- Linked to location, terminal, session
- Multiple sale types

#### **Payment** ✅
- Payment tracking per sale
- Multiple payment methods
- Status tracking

#### **Terminal** ✅
- Terminal configuration
- Location/department mapping
- System settings
- Hardware configuration (JSON)

#### **TerminalTransactionSetting** ✅
- Transaction type permissions
- Printer template assignments
- Per-terminal configuration

#### **TerminalTenderMapping** ✅
- Tender type limits
- Min/max values
- Allow/deny permissions

#### **TerminalDepartmentMapping** ✅
- Department access control
- Category restrictions
- Per-terminal configuration

---

## 🏗️ Architecture & Scalability

### **Current Architecture**

**Database:**
- **HO DB:** SQLite (for now, masters/settings/reports)
- **Store DB:** Not yet implemented (POS transactions)
- **Planned:** MySQL/PostgreSQL for Store DB

**Technology Stack:**
- **Backend:** Django 5.0.1 + DRF
- **Frontend:** React 18 + Vite
- **Database:** SQLite (currently)
- **Authentication:** JWT
- **API:** RESTful

**Offline Mode:**
- **Planned:** IndexedDB for offline billing
- **Sync:** Bidirectional with conflict resolution

### **Scalability Analysis**

#### **Current Limitations:**
1. **SQLite:** Single writer limitation (not suitable for multi-terminal)
2. **Monolithic:** Single Django app (all modules in one)
3. **No microservices:** Everything in one backend
4. **No caching:** No Redis/Memcached
5. **No load balancing:** Single server deployment

#### **Scaling Recommendations:**
1. **Database Layer:**
   - ✅ Add database router for multi-DB support
   - ✅ Implement read replicas for HO DB
   - ✅ Store DB per location (MySQL/PostgreSQL)
   - ✅ Connection pooling

2. **Application Layer:**
   - ✅ Add caching layer (Redis)
   - ✅ Implement Celery for async tasks
   - ✅ API rate limiting
   - ✅ Background jobs for sync

3. **Microservices Transition (Future):**
   - POS Service (billing, settlement)
   - Inventory Service (stock management)
   - Master Data Service (products, customers)
   - Reporting Service (analytics, consolidation)
   - Sync Service (bidirectional sync)

4. **Model Extensibility:**
   - ✅ JSONField for flexible data
   - ✅ Abstract base models
   - ✅ Plugin architecture for preferences
   - ✅ Configurable fields (via settings)

### **Future Enhancements:**
1. **Microservices:** Separate POS, Inventory, Master Data services
2. **Event-driven:** Message queue for async processing
3. **Horizontal scaling:** Load balancer + multiple app servers
4. **CDN:** Static asset delivery
5. **Monitoring:** APM, logging, alerting

---

## ✅ Implementation Status

### **Phase 1: Backend Models & APIs**
- ✅ DayOpen model, serializer, ViewSet, URLs
- ✅ DayClose model, serializer, ViewSet, URLs
- ✅ POSSession updates (settlement status)
- ✅ Sale updates (location, terminal)
- ✅ Terminal model with all fields
- ✅ TerminalTransactionSetting model
- ✅ TerminalTenderMapping model
- ✅ TerminalDepartmentMapping model
- ✅ All migrations applied
- **Progress:** 95%

### **Phase 2: Frontend UI**
- ✅ Session Open page
- ✅ Billing page
- ✅ Settlement page (with "Now"/"Later")
- ✅ Session Close page
- ✅ Terminal Configuration (5-tab dialog)
- ⏳ Day Open page
- ⏳ Day Close page with checklist
- **Progress:** 65%

### **Phase 3: Integration**
- ✅ Day Open → Session Open validation
- ✅ Billing → Settlement navigation
- ⏳ Document sequence generation from Day Open
- ⏳ Settlement validation in Day Close UI
- **Progress:** 60%

### **Overall Progress:** 🎯 **70%**

---

## ⏳ Pending Items

### **Priority 1 (Critical):**
1. ✅ ~~Day Open backend~~ 
2. ✅ ~~Day Close backend with settlement validation~~ 
3. ⏳ Day Open UI page
4. ⏳ Day Close UI with checklist
5. ⏳ Menu order update (add Day Open first)

### **Priority 2 (Important):**
1. ⏳ Document sequence integration
2. ⏳ Pending settlements indicator
3. ⏳ Offline billing with IndexedDB
4. ⏳ Bidirectional sync mechanism

### **Priority 3 (Enhancement):**
1. ⏳ Multi-DB support
2. ⏳ Terminal preferences MVP
3. ⏳ Reporting consolidation
4. ⏳ Performance optimization

---

## 📚 References

### **Key Documents:**
- `50_POS_WORKFLOW_ANALYSIS.md` - Industry research, workflow decision
- `51_TERMINAL_PREFERENCES_RESEARCH.md` - Terminal settings research
- `55_POS_ACTION_PLAN.md` - Detailed implementation plan
- `28_TERMINAL_PNG_ANALYSIS.md` - Terminal UI requirements
- `31_SQLITE_ENTERPRISE_VIABILITY_ANALYSIS.md` - Database strategy

### **User Clarifications:**
- Settlement deferment allowed, but required before Day Close
- Billing Close is navigation, not menu item
- Float details integrated in Session Open
- Workflow confirmed: Day Open → Session Open → Billing → Settlement → Session Close → Day Close

---

**Status:** This document is the authoritative source for POS requirements and implementation. All future decisions should reference this document.

---

## ✅ **SESSION ACKNOWLEDGEMENT (02-Nov-2025 18:15:03 IST)**

**Status:** Requirements frozen as per 01-Nov-2025 - Following exactly as documented ✅
- All clarifications from 01-Nov-2025 discussions acknowledged
- No deviations from frozen workflow
- UAT fixes completed (Issues #3, #4)

1️⃣ Day Open (DayOpenPage.jsx)
#	Feature	Description
1.1	Business date selection	Date picker for establishing business day
1.2	Notes input	Optional notes for day open
1.3	Active day detection	Check if day already open (blocks duplicate open)
1.4	Open day action	POST to /day-opens/open/
1.5	Close day shortcut	Quick close from Day Open page
1.6	Read-only identity tiles	User code, user name, location
1.7	Error handling	Location not assigned, timeout, network errors
1.8	Theme integration	Dynamic theme color from API
2️⃣ Session Open (SessionOpenPage.jsx)
#	Feature	Description
2.1	Identity tiles (read-only)	User Code, User Name, Location, Sale Date, Session No, Session Start Date/Time
2.2	Hostname-based terminal auto-detection	Resolve hostname (localStorage → backend → fingerprint), match to system_name
2.3	Terminal dropdown	Manual terminal selection if auto-detect fails
2.4	Float amount input	Opening cash balance (editable)
2.5	Session number preview	Auto-generated from Day Open sequence
2.6	Active day open check	Blocks session open if no active day
2.7	Terminal open session check	Detects if terminal already has open session
2.8	Open session action	POST to /pos-sessions/start/
2.9	Continue to POS	Navigate to billing after session start
2.10	Location from user profile	No location selection (derived from logged-in user)
3️⃣ POS Desktop / Billing (POSDesktop.jsx — 191KB, ~5000 lines)
Layout Structure (per your reference doc)
Section	ID	Description
1	section-1-top-bar	Header: customer selector, current time
2	section-2-main-content	70/30 split: left product area, right transaction area
2.1	panel-2.1-left-product-area	Cart items list (100% of left panel)
2.1.1	sub-section-2.1.1-cart-items-list	Cart table with header
2.2	panel-2.2-right-transaction-area	Product lookup OR cart view
2.2.0	sub-section-2.2.0-customer-details	Customer icon, info, search
2.2.1	sub-section-2.2.1-totals	Last Bill, Total Items, Sub Total, Discount, Round off, TOTAL
2.2.3	sub-section-2.2.3-pos-functions	18 POS function buttons (F1-F12 + Alt/Ctrl combos)
3	section-3-status-bar	POS session display, operator info
Billing Features
#	Feature	Description
3.1	Product search	Search by name, SKU, barcode
3.2	Barcode scanner support	Auto-add product on scan + Enter
3.3	Quick quantity	Type number before scan = quantity multiplier
3.4	Cart management	Add, remove, update quantity, clear cart
3.5	Customer selection	Walk-in or search existing customer
3.6	Quick customer add	Create new customer inline
3.7	Line item discount	Per-item discount
3.8	Bill discount	Percentage discount on total
3.9	Price override	Change item price (with permission)
3.10	Tax override	Override tax rate
3.11	Transaction notes	Add notes to bill
3.12	Suspend sale	Save current cart as draft
3.13	Resume sale	Load suspended sale
3.14	Refund handling	Process returns
3.15	Exchange handling	Item exchange flow
3.16	Payment dialog	Multi-tender payment (cash, card, UPI, wallet)
3.17	Quick cash buttons	Preset amounts ($20, $50, $100, etc.)
3.18	Change calculation	Auto-calculate change due
3.19	Receipt preview	Bill preview before print
3.20	Print receipt	Thermal/standard receipt printing
3.21	Bill query	Search past bills
3.22	Reprint	Reprint previous receipt
3.23	Settlement shortcut	Navigate to settlement
3.24	Force quit	Emergency close with confirmation
3.25	Session gating	Blocks billing if no active session
3.26	IndexedDB caching	Offline-capable product/session cache
3.27	Quick item creation	Create new product on-the-fly
Keyboard Shortcuts (useKeyboardShortcuts.js)
Shortcut	Action
F1	Help
F2	Focus search
F3	Customer
F4	Discount
F5	Resume
F6	Suspend
F8 / F12	Checkout
F9	Clear cart
Ctrl+N	New sale
Ctrl+S	Suspend
Ctrl+R	Resume
Ctrl+D	Discount
Ctrl+Q	Quantity
Ctrl+X	Clear cart
Ctrl+I	Toggle section identifiers
Escape	Cancel/close dialog
Section Identifiers (Ctrl+I toggle)
Semi-transparent overlay numbers on each section
Helps training and debugging
Toggleable via showIdentifiers state
4️⃣ Settlement (SettlementModuleV2.jsx, SettlementConsole/)
#	Feature	Description
4.1	Denomination counting	INR denominations (₹2000 → ₹1)
4.2	Expected vs actual cash	Auto-calculate expected from session sales
4.3	Variance calculation	Difference + variance reason selection
4.4	Settlement reasons	Dropdown from /pos-masters/settlement-reasons/
4.5	Interim settlements	Partial cash pickups during session
4.6	Manager sign-off	Manager name, notes, confirmation
4.7	Settlement history	View past settlements
4.8	Validation pre-conditions	Block if suspended bills or partial transactions
4.9	Session transaction list	Show all sales for session
4.10	Adjustments	Add/remove manual adjustments
5️⃣ Session Close (SessionClosePage.jsx)
#	Feature	Description
5.1	Close mode selection	Temporary vs Permanent
5.2	Temporary close	Can re-logon with authorization
5.3	Permanent close	Final close, sales consolidated
5.4	Read-only session summary	User, location, terminal, dates, float
5.5	Confirmation dialog	Confirm before close
5.6	Session validation	Blocks if no open session
5.7	Navigate to Session Open	If no session found
6️⃣ Day Close (DayClosePage.jsx)
#	Feature	Description
6.1	Checklist validation	All sessions closed, settlements completed, reports generated, backup done, cash counted, inventory verified
6.2	Settlement summary	Aggregate expected/counted/variance for all sessions
6.3	Session recap table	List all closed sessions for the day
6.4	Active day detection	Blocks if no active day
6.5	Close day action	POST to /day-opens/{id}/close/
6.6	Error handling	Timeout, network, validation errors
7️⃣ Shared Components (components/)
Component	Description
Cart.jsx	Cart display component
CartItem.jsx	Individual cart item row
CustomerSelector.jsx	Customer search/select dialog
QuickCustomerForm.jsx	Inline customer creation
ProductSearch.jsx	Product search with barcode support
PaymentDialog.jsx	Multi-tender payment flow
Receipt.jsx	Receipt preview/print
SuspendedSalesDialog.jsx	Resume suspended sales
KeyboardShortcutsHelp.jsx	F1 help dialog
SessionDialog.jsx	Session info dialog
QuickAccessPanel.jsx	Quick action panel
8️⃣ Services Required
Service	Purpose
terminalService.js	Terminal CRUD + hostname identification
sessionManager.js	Session state management + IndexedDB
shiftManager.js	Shift state management
transactionManager.js	Transaction tracking
productManager.js	Product cache
salesService.js	Sales API
customerService.js	Customer API
payModeService.js	Payment methods
currencyService.js	Currency denominations
businessRulesService.js	POS business rules
indexedDBManager.js	Offline storage
itemMasterService.js	Product/item master
Migration Scope Summary
Category	Files	Estimated Effort
Workflow Pages	6 pages	High
Shared Components	11 components	Medium
Hooks	1 hook	Low
Services	12 services	Medium (some already exist)
Layout/Identifiers	1 system	Low
❓ Questions for You Before Migration
Do you want all 6 workflow steps migrated? (Day Open, Session Open, Billing, Settlement, Session Close, Day Close)
POSDesktop vs POSBillingEnhanced: There are multiple billing variants. Confirm using POSDesktop.jsx (the 191KB full-featured version)?
Settlement version: Use SettlementModuleV2.jsx or SettlementConsole/ (component-based)?
IndexedDB/offline support: Include offline caching or defer?
Any features to exclude from the above list?
Please review and confirm which features/pages to include, and I'll begin the migration.

Feedback submitted






Code

Claude Opus 4.5 (Thinking)


Drop to add to Cascade