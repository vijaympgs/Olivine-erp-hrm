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
1. ✅ ~~Day Open backend~~ Complete
2. ✅ ~~Day Close backend with settlement validation~~ Complete
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

