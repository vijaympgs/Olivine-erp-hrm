# 6.0 ENTERPRISE POINT OF SALE – MASTER SPECIFICATION

This specification defines the authoritative functional behavior of the
Enterprise POS module. POS is a stateful, audit-critical system operating
at the edge of the enterprise.

------------------------------------------------------------

## 6.1 Terminal Management

### 6.1.1 Business Purpose
Terminal represents a physical POS register/device and defines
what transactions, tenders, peripherals, and policies are allowed
on that device.

Terminal is the **first control boundary** in POS.

---

### 6.1.2 Data Model

Terminal:
- terminal_id
- company_id
- location_id
- terminal_code
- terminal_name
- terminal_type (FIXED, MOBILE, KIOSK)
- is_active
- assigned_department(s)
- hardware_profile (printer, drawer, scanner)
- created_at

Terminal Transaction Settings:
- allowed_transaction_types (sale, return, cash_in, cash_out)
- allow_price_override
- allow_discount
- max_discount_percent

Terminal Tender Mapping:
- tender_type
- min_amount
- max_amount
- allow_refund
- is_enabled

---

### 6.1.3 UI / UX
- Terminal configuration screen (admin only)
- Tab-based configuration:
  - General
  - Transactions
  - Tenders
  - Departments
  - Hardware
- Read-only view for cashiers

---

### 6.1.4 Business Rules
- Terminal must be active to allow Session Open
- All billing behavior is filtered by terminal permissions
- Terminal policies override global defaults

---

### 6.1.5 Validations
- Terminal must belong to a single location
- At least one tender must be enabled
- Disabled terminal cannot be used for billing

---

### 6.1.6 Configuration
- Per-terminal overrides allowed
- Default terminal template supported
- Terminal cloning supported

------------------------------------------------------------

## 6.2 Day Open

### 6.2.1 Business Purpose
Day Open establishes the **business date** and enables POS activity
for the store. All accounting is tied to the business date.

---

### 6.2.2 Data Model
- day_open_id
- location_id
- business_date
- status (OPEN, CLOSED)
- opened_by
- opened_at
- closed_at

---

### 6.2.3 UI / UX
- Dedicated Day Open screen
- Business date selector
- Single “Open Day” action
- Day status banner visible across POS

---

### 6.2.4 Business Rules
- One Day Open per location per business date
- Previous day must be closed
- Business date ≠ system date allowed (configurable)

---

### 6.2.5 Validations
- Block Session Open if Day Open not active
- Block duplicate Day Open

---

### 6.2.6 Configuration
- Enforce calendar date = business date (Yes/No)
- Manager approval for backdated day open

------------------------------------------------------------

## 6.3 Session Open

### 6.3.1 Business Purpose
Session Open establishes **cashier accountability**
and links all activity to a shift.

---

### 6.3.2 Data Model
- session_id
- day_open_id
- cashier_id
- terminal_id
- session_number
- opening_cash
- status (OPEN, TEMP_CLOSED, PERM_CLOSED)
- opened_at
- closed_at

---

### 6.3.3 UI / UX
- Dedicated Session Open screen
- Cashier auto-filled
- Terminal selection
- Opening cash entry

---

### 6.3.4 Business Rules
- Multiple sessions allowed per day
- One active session per cashier per terminal
- Opening cash is mandatory

---

### 6.3.5 Validations
- Block Session Open without Day Open
- Block if terminal already in use

---

### 6.3.6 Configuration
- Allow zero opening cash (Yes/No)
- Enforce cash declaration limits

------------------------------------------------------------

## 6.4 Billing (POS Cockpit)

### 6.4.1 Business Purpose
Billing is the **single operational cockpit** for cashiers.
All transactional actions occur here.

---

### 6.4.2 Data Model

Sale Header:
- sale_id
- session_id
- terminal_id
- receipt_number
- sale_status (OPEN, COMPLETED, VOIDED)
- totals (subtotal, tax, discount, grand_total)

Sale Line:
- item_variant
- qty
- unit_price
- discounts
- taxes

Payment:
- tender_type
- amount
- reference

---

### 6.4.3 UI / UX
Single Billing Workspace supporting:
- Sale / Return / Exchange
- Hold / Resume
- Discounts & overrides
- Multi-tender payment
- Receipt print / reprint
- Close Bill → Settlement

---

### 6.4.4 Business Rules
- Billing allowed only in active session
- All pricing calculated server-side
- Returns must reference original sale (unless policy allows otherwise)

---

### 6.4.5 Validations
- Payment total must equal bill total
- Discount limits enforced
- Block billing after session permanent close

---

### 6.4.6 Configuration
- Discount limits by role
- Return window days
- Receipt mandatory (Yes/No)

------------------------------------------------------------

## 6.5 Settlement

### 6.5.1 Business Purpose
Settlement reconciles **expected vs actual cash**
and finalizes financial accountability for a session.

---

### 6.5.2 Data Model
- settlement_id
- session_id
- expected_cash
- counted_cash
- variance
- status (PENDING, COMPLETED)
- settled_by
- settled_at

---

### 6.5.3 UI / UX
- Dedicated Settlement screen
- Expected cash (read-only)
- Cash count input
- Variance display
- Settle Now / Later actions

---

### 6.5.4 Business Rules
- Settlement may be deferred
- Settlement mandatory before Day End
- Variance must be recorded explicitly

---

### 6.5.5 Validations
- Block Day End if settlement pending
- Block settlement without active session

---

### 6.5.6 Configuration
- Allow settlement deferment (Yes/No)
- Variance tolerance limits
- Manager approval for high variance

------------------------------------------------------------

## 6.6 Session Close

### 6.6.1 Business Purpose
Session Close ends cashier responsibility and locks activity.

---

### 6.6.2 Data Model
- session_status
- closed_at
- closed_by

---

### 6.6.3 UI / UX
- Dedicated Session Close screen
- Session summary
- Temporary / Permanent close option

---

### 6.6.4 Business Rules
- Temporary close allows reopen
- Permanent close is final

---

### 6.6.5 Validations
- Billing blocked after permanent close
- Settlement may still be pending

---

### 6.6.6 Configuration
- Enforce settlement before session close (Yes/No)

------------------------------------------------------------

## 6.7 Day End (Day Close)

### 6.7.1 Business Purpose
Day End finalizes all store operations and closes the business date.

---

### 6.7.2 Data Model
- day_close_id
- business_date
- closed_by
- closed_at
- consolidated_totals

---

### 6.7.3 UI / UX
- Dedicated Day End screen
- Checklist-based validation
- Final Day Close action

---

### 6.7.4 Business Rules
- All sessions must be closed
- All settlements must be completed
- Cash verified and reports generated

---

### 6.7.5 Validations
- Block Day End on any open session
- Block Day End on pending settlement

---

### 6.7.6 Configuration
- Mandatory reports list
- Manager override for exceptional closure

------------------------------------------------------------

## POS MASTER FREEZE

This specification defines the authoritative enterprise POS behavior.
All implementations must conform to this document.


# ENTERPRISE POS – STATE MACHINE SPECIFICATION
(Authoritative Control Layer)

This document defines the explicit state machines governing
POS behavior. UI, APIs, and workflows MUST conform to these rules.

==============================================================

## 1. SALE STATE MACHINE

### 1.1 Sale States

| State | Meaning |
|-----|--------|
| NEW | Sale created, no items yet |
| IN_PROGRESS | Items added / modified |
| ON_HOLD | Temporarily parked sale |
| PAYMENT_IN_PROGRESS | Payment started |
| COMPLETED | Sale finalized |
| VOIDED | Sale cancelled before completion |

---

### 1.2 Allowed Transitions

| From State | Action | To State | Allowed By | Notes |
|----------|-------|---------|-----------|------|
| NEW | Add item | IN_PROGRESS | Cashier |  |
| IN_PROGRESS | Hold sale | ON_HOLD | Cashier |  |
| ON_HOLD | Resume sale | IN_PROGRESS | Cashier | Same session only (configurable) |
| IN_PROGRESS | Start payment | PAYMENT_IN_PROGRESS | Cashier | Locks items |
| PAYMENT_IN_PROGRESS | Payment success | COMPLETED | System | Receipt generated |
| PAYMENT_IN_PROGRESS | Cancel payment | IN_PROGRESS | Cashier | No tender committed |
| IN_PROGRESS | Void sale | VOIDED | Cashier / Manager | Policy-driven |
| NEW | Void sale | VOIDED | Cashier |  |

---

### 1.3 Forbidden Transitions (Hard Blocks)

| Condition | Reason |
|--------|--------|
| Modify items after PAYMENT_IN_PROGRESS | Financial integrity |
| Resume ON_HOLD sale after session close | Accountability |
| Void COMPLETED sale | Must use Return |
| Resume sale from different terminal | Audit control |

---

### 1.4 Failure Handling

- Crash before COMPLETED → Sale remains IN_PROGRESS
- Crash during PAYMENT_IN_PROGRESS → Payment reconciliation required
- Orphan sale auto-marked IN_PROGRESS on recovery

==============================================================

## 2. SESSION STATE MACHINE

### 2.1 Session States

| State | Meaning |
|----|--------|
| OPEN | Active cashier session |
| TEMP_CLOSED | Paused, can reopen |
| PERM_CLOSED | Final, cannot reopen |

---

### 2.2 Allowed Transitions

| From | Action | To | Allowed By | Notes |
|----|-------|---|-----------|------|
| OPEN | Temp close | TEMP_CLOSED | Cashier | Break |
| TEMP_CLOSED | Reopen | OPEN | Cashier | Same cashier |
| OPEN | Permanent close | PERM_CLOSED | Cashier | End of shift |
| TEMP_CLOSED | Permanent close | PERM_CLOSED | Cashier |  |

---

### 2.3 Guard Conditions

| Rule | Enforcement |
|----|------------|
| Cannot PERM_CLOSE with active sale | Block |
| Billing disabled in TEMP_CLOSED | Enforced |
| PERM_CLOSED is immutable | Hard rule |

---

### 2.4 Failure Handling

- Crash during OPEN → Session remains OPEN
- Crash during TEMP_CLOSED → Session recoverable
- Crash after PERM_CLOSED → No impact

==============================================================

## 3. SETTLEMENT STATE MACHINE

### 3.1 Settlement States

| State | Meaning |
|----|--------|
| NOT_STARTED | No settlement attempt |
| PENDING | Deferred settlement |
| IN_PROGRESS | Cash counting started |
| COMPLETED | Settlement finalized |

---

### 3.2 Allowed Transitions

| From | Action | To | Allowed By |
|----|-------|---|-----------|
| NOT_STARTED | Start settlement | IN_PROGRESS | Cashier |
| IN_PROGRESS | Complete settlement | COMPLETED | Cashier |
| IN_PROGRESS | Defer | PENDING | Cashier |
| PENDING | Resume settlement | IN_PROGRESS | Cashier |

---

### 3.3 Blocking Rules

| Condition | Result |
|--------|--------|
| Day End with PENDING settlement | BLOCK |
| Settlement without session | BLOCK |
| Settlement modify after COMPLETED | BLOCK |

---

### 3.4 Variance Rules

| Scenario | Behavior |
|-------|----------|
| Zero variance | Auto-accept |
| Variance within tolerance | Accept |
| Variance beyond tolerance | Manager approval |

==============================================================

## 4. DAY (BUSINESS DATE) STATE MACHINE

### 4.1 Day States

| State | Meaning |
|----|--------|
| NOT_OPENED | No business day |
| OPEN | Active business date |
| CLOSING | Validation in progress |
| CLOSED | Day finalized |

---

### 4.2 Allowed Transitions

| From | Action | To | Allowed By |
|----|-------|---|-----------|
| NOT_OPENED | Day Open | OPEN | Manager |
| OPEN | Initiate Day End | CLOSING | Manager |
| CLOSING | All checks pass | CLOSED | System |
| CLOSING | Validation fail | OPEN | System |

---

### 4.3 Mandatory Checks at CLOSING

| Check | Must Pass |
|----|----------|
| All sessions PERM_CLOSED | YES |
| All settlements COMPLETED | YES |
| Cash verified | YES |
| Mandatory reports generated | YES |

---

### 4.4 Failure Handling

- Crash during CLOSING → Resume checks
- Partial close NOT allowed
- CLOSED is immutable

==============================================================

## 5. TERMINAL STATE MACHINE

### 5.1 Terminal States

| State | Meaning |
|----|--------|
| ACTIVE | Can be used |
| INACTIVE | Disabled |
| MAINTENANCE | Temporarily blocked |

---

### 5.2 Rules

- Session Open allowed only on ACTIVE terminals
- MAINTENANCE blocks billing but allows settlement
- INACTIVE blocks all operations

==============================================================

## 6. CROSS-STATE INTEGRITY RULES (CRITICAL)

| Rule | Enforcement |
|----|------------|
| Sale must belong to OPEN session | Hard |
| Session must belong to OPEN day | Hard |
| Settlement must belong to session | Hard |
| Day Close blocks everything | Hard |

==============================================================

## 7. AUDIT GUARANTEES

- Every state transition is recorded as:
  - Previous state
  - New state
  - User
  - Timestamp
  - Terminal
  - Reason (if applicable)
- No state rollback after financial finalization

==============================================================

## STATE MACHINE FREEZE

This document defines the canonical POS state behavior.
All UI, APIs, and integrations MUST conform to this control layer.

# ENTERPRISE POS – FAILURE & EDGE CASE SPECIFICATION
(Control, Recovery, and Exception Handling)

This document defines how the POS system behaves under failures,
exceptions, and abnormal operating conditions. These rules are
mandatory for enterprise-grade POS behavior.

==============================================================

## 1. FAILURE CLASSIFICATION MODEL

All POS failures are classified into one of the following categories:

1. Power Failure
2. Network Failure
3. Application Crash
4. Peripheral Failure
5. Human Error
6. Data Conflict / Corruption
7. Policy Violation

Each failure category has predefined recovery rules.

==============================================================

## 2. POWER FAILURE SCENARIOS

### 2.1 Power Loss During Billing (Before Payment)

State at failure:
- Sale State: IN_PROGRESS
- Session State: OPEN

Expected Behavior:
- Sale remains IN_PROGRESS
- No receipt generated
- No inventory movement posted
- On restart, cashier can:
  - Resume sale
  - Void sale

Forbidden:
- Auto-completing sale
- Auto-voiding sale

---

### 2.2 Power Loss During Payment

State at failure:
- Sale State: PAYMENT_IN_PROGRESS

Expected Behavior:
- Sale locked for modification
- Payment marked as UNCONFIRMED
- On restart:
  - POS must reconcile payment status
  - If payment confirmed by gateway → COMPLETE sale
  - If payment failed → revert to IN_PROGRESS

Audit Requirement:
- Payment reconciliation event recorded

---

### 2.3 Power Loss After Sale Completion

State at failure:
- Sale State: COMPLETED

Expected Behavior:
- Sale remains COMPLETED
- Receipt can be reprinted
- Inventory already adjusted
- No duplicate posting allowed

==============================================================

## 3. NETWORK FAILURE SCENARIOS

### 3.1 Network Loss During Billing (Online Mode)

Expected Behavior:
- If offline mode allowed:
  - Continue billing
  - Mark sale as OFFLINE
- If offline not allowed:
  - Block new sales
  - Allow session close (policy-based)

---

### 3.2 Network Loss During Payment (Card / UPI)

Expected Behavior:
- Payment enters PENDING_CONFIRMATION
- Sale locked
- No retry without reconciliation
- Cashier cannot cancel blindly

---

### 3.3 Network Loss During Settlement

Expected Behavior:
- Settlement cannot be completed
- Settlement may be saved as IN_PROGRESS
- Day End must be blocked until settlement is finalized

==============================================================

## 4. APPLICATION CRASH SCENARIOS

### 4.1 Crash During Session Open

Expected Behavior:
- Session not created unless fully committed
- On restart:
  - Either no session exists
  - Or session exists in OPEN state

---

### 4.2 Crash During Settlement Completion

Expected Behavior:
- Settlement marked IN_PROGRESS
- On restart:
  - Resume settlement
  - No duplicate settlement allowed

---

### 4.3 Crash During Day End

Expected Behavior:
- Day enters CLOSING state
- On restart:
  - Resume validation checks
  - Day must end in OPEN or CLOSED
  - Partial close not allowed

==============================================================

## 5. PERIPHERAL FAILURE SCENARIOS

### 5.1 Receipt Printer Failure

Expected Behavior:
- Sale completion not blocked
- Receipt marked as NOT_PRINTED
- Reprint allowed later
- Digital receipt fallback (if configured)

---

### 5.2 Cash Drawer Failure

Expected Behavior:
- Billing allowed
- Settlement allowed
- Drawer-open event logged as FAILED
- Manual override may be required

---

### 5.3 Barcode Scanner Failure

Expected Behavior:
- Manual item search enabled
- No impact on sale integrity

==============================================================

## 6. HUMAN ERROR SCENARIOS

### 6.1 Cashier Logs Out Mid-Sale

Expected Behavior:
- Sale auto-held
- Sale cannot be resumed by another cashier
  unless override policy allows

---

### 6.2 Cashier Attempts Day End

Expected Behavior:
- Blocked
- Error: Unauthorized operation

---

### 6.3 Wrong Cash Count Entered

Expected Behavior:
- Variance calculated
- No auto-correction
- Manager approval if variance exceeds tolerance

==============================================================

## 7. DATA CONFLICT & CORRUPTION

### 7.1 Duplicate Receipt Numbers

Expected Behavior:
- Impossible by design
- If detected:
  - Block posting
  - Raise critical system alert

---

### 7.2 Offline vs Online Sale Conflict

Expected Behavior:
- Offline sale retains local authority
- Central system reconciles, never overwrites
- Conflict flagged for review

==============================================================

## 8. POLICY VIOLATION HANDLING

### 8.1 Discount Limit Exceeded

Expected Behavior:
- Prompt for manager override
- Log override reason

---

### 8.2 Return Outside Allowed Window

Expected Behavior:
- Block return
- Allow override only if policy permits

==============================================================

## 9. FORCED OPERATIONS (EXCEPTIONAL)

### 9.1 Forced Session Close

Allowed Only When:
- Cashier unavailable
- Manager intervention

Effects:
- Session marked FORCE_CLOSED
- Settlement still required

---

### 9.2 Forced Day End

Allowed Only When:
- Extreme conditions (store closure, disaster)

Effects:
- Day marked FORCE_CLOSED
- All exceptions logged
- Mandatory audit review required

==============================================================

## 10. OFFLINE-SPECIFIC RULES

Allowed Offline:
- New sale
- Hold / Resume
- Cash payments

Not Allowed Offline:
- Settlement
- Day End
- Returns (unless cached sale exists)

==============================================================

## 11. AUDIT & FORENSICS GUARANTEES

For every failure:
- Event type recorded
- State before and after recorded
- User and terminal recorded
- Recovery action recorded

No silent failure allowed.

==============================================================

## FAILURE SPEC FREEZE

This document defines mandatory POS behavior under failure and
exception conditions. All implementations MUST comply.


# ENTERPRISE POS – INTERFACE CONTRACT SPECIFICATION
(POS ↔ Inventory ↔ Finance ↔ Audit)

This document defines the authoritative contracts between the POS system
and downstream enterprise systems. These contracts are immutable and
govern data ownership, timing, and reconciliation.

==============================================================

## 1. CORE PRINCIPLE (NON-NEGOTIABLE)

POS is the **system of record** for:
- Sales transactions
- Returns transactions
- Cash movements
- Settlement outcomes

Downstream systems (Inventory, Finance, Reporting) are
**systems of consumption**, not correction.

No downstream system may:
- Modify POS-originated financial facts
- Recalculate POS totals
- Re-sequence POS documents

==============================================================

## 2. POS → INVENTORY CONTRACT

### 2.1 Ownership

POS owns:
- Quantity sold
- Quantity returned
- Transaction timestamp
- Business date
- Terminal and session reference

Inventory consumes POS events to adjust stock.

---

### 2.2 Events Emitted by POS

#### A) SALE_COMPLETED

Emitted when:
- Sale state transitions to COMPLETED

Payload (logical):
- sale_id
- business_date
- location_id
- terminal_id
- item_variant_id
- quantity_sold
- uom
- sale_timestamp
- receipt_number

Inventory Behavior:
- Reduce on-hand quantity
- Record stock movement as POS_SALE
- Never recalculate quantity

---

#### B) RETURN_COMPLETED

Emitted when:
- Return transaction is completed

Payload:
- return_id
- original_sale_id
- business_date
- location_id
- item_variant_id
- quantity_returned
- return_timestamp

Inventory Behavior:
- Increase on-hand quantity OR
- Route to non-sellable bucket (policy-driven)
- Record stock movement as POS_RETURN

---

### 2.3 Forbidden Inventory Actions

Inventory MUST NOT:
- Reject a valid POS event due to stock shortage
- Alter quantities received from POS
- Retroactively change stock for past business dates

---

### 2.4 Offline Considerations

- Offline POS sales generate LOCAL events
- On sync:
  - Inventory accepts events in POS business-date order
  - Conflicts flagged, not auto-resolved

==============================================================

## 3. POS → FINANCE / ACCOUNTING CONTRACT

### 3.1 Ownership

POS owns:
- Gross sales
- Discounts
- Taxes
- Payment breakdown
- Cash variances
- Business date

Finance consumes POS results for posting.

---

### 3.2 Financial Events from POS

#### A) SALE_FINANCIAL_POST

Emitted when:
- Sale is COMPLETED

Payload:
- sale_id
- business_date
- gross_amount
- discount_amount
- tax_amount
- net_amount
- tender_breakdown

Finance Behavior:
- Post revenue
- Post tax
- Post receivable / cash
- Use POS numbers as-is

---

#### B) RETURN_FINANCIAL_POST

Emitted when:
- Return is COMPLETED

Finance Behavior:
- Reverse revenue
- Reverse tax
- Post refund liability

---

#### C) SETTLEMENT_COMPLETED

Emitted when:
- Settlement state transitions to COMPLETED

Payload:
- session_id
- business_date
- expected_cash
- counted_cash
- variance_amount
- variance_reason

Finance Behavior:
- Post cash-in-hand
- Post cash variance (gain/loss)
- Never recompute variance

---

### 3.3 Forbidden Finance Actions

Finance MUST NOT:
- Recalculate tax or discount
- Change business date
- Aggregate across days before Day End
- Post without POS settlement completion

==============================================================

## 4. POS → DAY END / CONSOLIDATION CONTRACT

### 4.1 Day End Authority

POS is authoritative for:
- Day Open
- Day Close
- Day totals

Day End is a **hard boundary**.

---

### 4.2 Day End Emission

#### DAY_CLOSED Event

Payload:
- business_date
- location_id
- total_sales
- total_returns
- total_cash
- total_non_cash
- total_variance

Downstream Behavior:
- Lock postings for the business date
- No further entries allowed for that date

---

### 4.3 Immutability Rule

Once DAY_CLOSED is emitted:
- No POS transaction may be added
- No inventory adjustment may backdate
- No finance posting may alter totals

Corrections require:
- Explicit adjustment documents
- Separate business date

==============================================================

## 5. POS → AUDIT / EVENT LEDGER CONTRACT

### 5.1 Event Immutability

Every POS action emits an event:
- Sale state change
- Session state change
- Settlement state change
- Day state change
- Override action
- Failure recovery action

Events are:
- Append-only
- Time-ordered
- Never deleted

---

### 5.2 Audit Payload Minimum

Each event records:
- Event type
- Previous state
- New state
- User
- Terminal
- Timestamp
- Business date
- Reason (if applicable)

Audit systems consume events as facts.

==============================================================

## 6. ERROR & REJECTION HANDLING

### 6.1 Downstream Rejection

If Inventory or Finance rejects an event:
- POS does NOT roll back
- Event marked as DELIVERY_FAILED
- Retry mechanism engaged
- Alert raised

Financial truth remains with POS.

---

### 6.2 Partial Delivery

- Inventory posted but Finance failed:
  - Finance retry required
- Finance posted but Inventory failed:
  - Inventory retry required

No cross-system rollback allowed.

==============================================================

## 7. CROSS-SYSTEM CONSISTENCY RULES

| Rule | Enforcement |
|----|------------|
| POS business date is authoritative | Hard |
| POS receipt number is final | Hard |
| POS totals are final | Hard |
| Downstream systems are consumers | Hard |

==============================================================

## 8. ENTERPRISE GUARANTEES

With this contract:
- POS can operate offline
- Inventory remains accurate
- Finance remains auditable
- Corrections are explicit, not silent

==============================================================

## INTERFACE CONTRACT FREEZE

This document defines the immutable enterprise contract
between POS and downstream systems.

All integrations MUST comply.


# ENTERPRISE POS – OFFLINE SYNC & CONFLICT RESOLUTION SPECIFICATION
(Authoritative Design Contract)

This document defines how the POS system operates during offline conditions,
how data is persisted locally, how synchronization occurs, and how conflicts
are detected and resolved without violating financial integrity.

==============================================================

## 1. CORE OFFLINE PRINCIPLES (NON-NEGOTIABLE)

1. POS MUST operate without network connectivity.
2. Offline data is NOT temporary data — it is authoritative local truth.
3. Financial facts are NEVER overwritten during sync.
4. Conflicts are resolved by rules, not guesswork.
5. Human intervention is required for ambiguous financial conflicts.

==============================================================

## 2. OFFLINE CAPABILITY MATRIX

| POS Capability | Offline Allowed | Notes |
|---------------|----------------|------|
| Day Open | ❌ | Must be online |
| Session Open | ✅ | Allowed after Day Open |
| Billing (Sale) | ✅ | Core offline function |
| Hold / Resume | ✅ | Same terminal only |
| Cash Payments | ✅ | Always allowed |
| Card / UPI | ⚠️ | Only if terminal supports offline auth |
| Returns | ⚠️ | Only if original sale cached |
| Settlement | ❌ | Must be online |
| Session Close | ✅ | Allowed |
| Day End | ❌ | Must be online |

==============================================================

## 3. LOCAL OFFLINE DATA MODEL (EDGE LEDGER)

Each terminal maintains a **Local POS Ledger** containing:

### 3.1 Locally Stored Entities
- Sale
- Sale Line
- Payment
- Return
- Cash Movement
- Session
- POS Events

### 3.2 Local Identifiers
- Every entity has:
  - Local UUID (immutable)
  - Global UUID (assigned on sync, if needed)

Local UUIDs are NEVER regenerated.

==============================================================

## 4. OFFLINE TRANSACTION BEHAVIOR

### 4.1 Sale Creation (Offline)

When offline:
- Sale created locally
- Sale marked OFFLINE = TRUE
- Receipt number generated from local sequence
- Inventory impact recorded locally

Sale State Rules:
- IN_PROGRESS → COMPLETED allowed
- VOID allowed before COMPLETED
- COMPLETED sale is immutable

---

### 4.2 Payments (Offline)

Cash:
- Always allowed
- Cash ledger updated locally

Non-Cash:
- Allowed only if terminal supports offline authorization
- Marked as OFFLINE_AUTH
- Must be reconciled on sync

---

### 4.3 Returns (Offline)

Allowed only if:
- Original sale exists in local cache
- Return window policy allows

Otherwise:
- Block return
- Prompt to retry online

==============================================================

## 5. SYNC TRIGGER & MODES

### 5.1 Sync Triggers
- Network restored
- Manual sync initiated
- Scheduled background sync

---

### 5.2 Sync Modes

1. **Incremental Sync**
   - Only unsynced events
2. **Recovery Sync**
   - After crash or partial failure
3. **Forced Sync**
   - Manager-initiated

==============================================================

## 6. SYNC ORDER (CRITICAL)

Events MUST sync in this order:

1. POS Events
2. Sessions
3. Sales
4. Payments
5. Returns
6. Cash Movements

Business date order MUST be preserved.

==============================================================

## 7. CONFLICT DETECTION TYPES

### 7.1 Duplicate Transaction Conflict

Detected When:
- Same receipt number
- Same terminal + timestamp collision

Resolution:
- POS local copy wins
- Central marks duplicate as CONFLICT_RECORDED
- Manual review required

---

### 7.2 Inventory Quantity Conflict

Detected When:
- Offline sale causes stock to go negative centrally

Resolution:
- Inventory accepts POS event
- Negative stock allowed temporarily
- Replenishment required (no rollback)

---

### 7.3 Payment Reconciliation Conflict

Detected When:
- Offline card payment cannot be confirmed

Resolution:
- Sale remains COMPLETED
- Payment marked UNCONFIRMED
- Finance flags as exception
- Manual settlement required

---

### 7.4 Business Date Conflict

Detected When:
- Offline sales belong to closed business date centrally

Resolution:
- POS business date remains authoritative
- Central system reopens date logically (shadow posting)
- Audit flag raised

==============================================================

## 8. CONFLICT RESOLUTION RULES (TRUTH HIERARCHY)

Truth Authority Order:
1. POS Terminal (local)
2. Store POS Aggregation
3. Central Systems

Rules:
- Never overwrite POS financial facts
- Never auto-adjust totals
- Corrections require explicit adjustment documents

==============================================================

## 9. PARTIAL SYNC FAILURE HANDLING

### Scenario:
- Inventory sync succeeds
- Finance sync fails

Behavior:
- Finance events retried
- No rollback of inventory
- Alert raised

Same rule applies vice versa.

==============================================================

## 10. DATA CORRUPTION & RECOVERY

### 10.1 Local Data Corruption

Behavior:
- Lock billing immediately
- Allow view-only mode
- Force recovery sync
- Manual intervention required

---

### 10.2 Central Rejection

Behavior:
- POS retries delivery
- Marks event as DELIVERY_FAILED
- Does NOT alter local state

==============================================================

## 11. AUDIT & FORENSICS (MANDATORY)

Every offline action records:
- Offline flag
- Local timestamp
- Sync timestamp
- Sync result
- Conflict flags (if any)

Audit systems must be able to answer:
- What happened offline?
- When did it sync?
- Was it altered?

==============================================================

## 12. OFFLINE EXIT CONDITIONS

POS is considered fully ONLINE only when:
- All local events synced
- No pending conflicts
- All financial events acknowledged

==============================================================

## OFFLINE SPEC FREEZE

This document defines the authoritative offline and sync behavior
of the Enterprise POS system.

All implementations MUST comply.
