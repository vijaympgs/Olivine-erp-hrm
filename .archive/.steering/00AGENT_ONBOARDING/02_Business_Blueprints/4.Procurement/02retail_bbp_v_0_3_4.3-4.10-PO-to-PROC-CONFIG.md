4.3 Purchase Order (PO)
Template Ref: _txn_03 (Medium/Complex Transaction)
4.3.1 Business Purpose
The Purchase Order (PO) is the legally binding commercial document issued to a supplier, confirming agreed quantities, prices, taxes, delivery terms, and payment terms.
Goals:
●	Convert approved internal demand (PR) and/or awarded vendor quotes (RFQ) into a formal purchase commitment.

●	Serve as the anchor document for subsequent processes:

○	Advance Shipment Notice (ASN)

○	Goods Receipt Note (GRN)

○	Supplier Invoice Matching

○	Supplier Returns

○	Payment & Settlement

●	Enforce procurement and financial controls:

○	Budget control (optional integration)

○	Approval workflows (value/role/category-based)

○	Vendor, tax, and contract compliance

●	Support both:

○	Organizations using PR → RFQ → PO

○	Organizations using PR → PO directly

○	Organizations using PO directly (PR & RFQ disabled)

Hybrid behavior (config-driven):
●	PO may be:

○	Created directly (no PR/RFQ) for simple procurement.

○	Created from PR (single or multiple PRs).

○	Created from RFQ award (pre-populated pricing & terms).

●	Config rules can enforce:

○	po_requires_pr for certain categories/locations.

○	po_requires_rfq above spend thresholds.

○	Separate approval tiers for Capex vs Opex vs Services.
4.3.2 Data Model
A) PO Header (purchase_order)
Field	Type	Required	Description
id	UUID	Yes	Primary key
company_id	FK	Yes	Company scope
po_number	String(30)	Yes	Human-readable PO No (per sequence)
po_status	Enum	Yes	DRAFT, PENDING_APPROVAL, APPROVED, SENT_TO_SUPPLIER, PARTIALLY_RECEIVED, FULLY_RECEIVED, CLOSED, CANCELLED
supplier_id	FK (Supplier)	Yes	Supplier to whom PO is issued
supplier_contact_name	String(100)	No	Contact person at supplier
supplier_contact_email	String(200)	No	Email for PO dispatch
ordering_location_id	FK (Location)	Yes	Location/department raising the PO
default_delivery_location_id	FK (Location)	No	Default delivery location for PO lines
currency_code	String(10)	Yes	ISO currency code
po_date	Date	Yes	PO issue date
expected_start_date	Date	No	Services/Capex start date (if applicable)
expected_completion_date	Date	No	For long-running services/projects
payment_terms_code	String(50)	No	Reference to payment terms
incoterms_code	String(20)	No	Incoterms (e.g., EXW, FOB, CIF)
freight_terms	String(100)	No	Who bears freight, any conditions
tax_inclusive	Boolean	Yes	True if prices stored are tax-inclusive
total_gross_amount	Decimal	Yes	Sum of line amounts before discounts/taxes
total_discount_amount	Decimal	Yes	Total discount at header level (if used)
total_tax_amount	Decimal	Yes	Total tax across all lines
total_net_amount	Decimal	Yes	Final payable amount = gross - discounts + tax
linked_rfq_id	FK (RFQ Header)	No	If PO created from RFQ award
linked_rfq_vendor_id	FK (RFQ Vendor)	No	Winning vendor reference (if from RFQ)
created_from_pr_flag	Boolean	Yes	True if PO created from one or more PRs
remarks_internal	Text	No	Internal notes (not sent to supplier)
remarks_to_supplier	Text	No	Free text to appear on PO print/email
approval_required	Boolean	Yes	Derived from config based on value/category
approved_by_user_id	FK (User)	No	User who approved PO
approved_at	DateTime	No	Approval timestamp
cancelled_by_user_id	FK (User)	No	Who cancelled PO
cancelled_at	DateTime	No	Cancelled timestamp
sent_to_supplier_at	DateTime	No	When PO was dispatched to supplier
po_version_no	Integer	Yes	Version number for amendments (start at 1)
is_amendment_of_po_id	FK (PO Header)	No	Reference to original PO for amendments
created_by_user_id	FK (User)	Yes	Creator
created_at	DateTime	Auto	
updated_at	DateTime	Auto	
Note: po_version_no and is_amendment_of_po_id allow for controlled PO amendments; how amendments are managed is further enforced in workflow and validation.
________________________________________
B) PO Line (purchase_order_line)
Each line = one item/variant/service row on the PO.
Field	Type	Required	Description
id	UUID	Yes	Primary key
purchase_order_id	FK (PO Header)	Yes	Link to PO header
line_number	Integer	Yes	Sequential line number on PO
item_id	FK (Item)	Yes	Parent item (for services, can still be a service item)
item_variant_id	FK (Item Variant)	Yes	SKU reference
description_override	String(255)	No	Line description override (for services/Capex)
uom_id	FK (UOM)	Yes	UOM ordered
ordered_qty	Decimal	Yes	Quantity ordered
received_qty	Decimal	Yes	Default 0; updated from GRN
cancelled_qty	Decimal	Yes	Default 0; qty cancelled
unit_price	Decimal	Yes	Unit price (pre-tax or tax-inclusive based on flag)
discount_percent	Decimal	No	Line-level discount %
discount_amount	Decimal	No	Line-level discount value
tax_percent	Decimal	No	Standard tax rate applied
tax_amount	Decimal	No	Tax amount computed for line
line_gross_amount	Decimal	Yes	Qty × unit_price (before discounts/taxes)
line_net_amount	Decimal	Yes	Gross - discount + tax
delivery_location_id	FK (Location)	No	If differs from header default
required_by_date	Date	No	Required delivery date for this line
pr_line_id	FK (PR Line)	No	PR line reference (if fulfilled from PR)
rfq_vendor_quote_line_id	FK (RFQ Vendor Quote)	No	RFQ line reference (if fulfilled from RFQ)
line_status	Enum	Yes	OPEN, PARTIALLY_RECEIVED, FULLY_RECEIVED, CANCELLED
line_remarks_internal	Text	No	Buyer-only notes
line_remarks_to_supplier	Text	No	Supplier-visible notes (line-level)
________________________________________
C) PO–PR Link (purchase_requisition_po_link)
This was already introduced in 4.1 PR; here we reuse it from the PO perspective.
Fields (same table, used bidirectionally):
Field	Type	Required	Description
id	UUID	Yes	Primary key
pr_line_id	FK (PR Line)	Yes	PR line fulfilled
po_id	FK (PO Header)	Yes	PO header
po_line_id	FK (PO Line)	Yes	PO line created
ordered_qty_from_pr	Decimal	Yes	Quantity ordered from PR line
From PO side:
●	Whenever a PO line is created from PR line, an entry is created/updated here.

●	Ensures PR line already_ordered_qty is updated correctly.

________________________________________
D) Config / Control (Conceptual)
Key controls (config / YAML / system params):
●	po_requires_pr (Company, Location, Category, Threshold)

●	po_requires_rfq (Company, Category, Threshold)

●	allow_direct_po_for_categories (list)

●	over_receive_tolerance_percent (e.g. allow receiving up to +5%)

●	price_change_tolerance_percent (allowed % above last purchase or RFQ price before requiring approval)

●	allow_po_amendments_after_grn (Yes/No, and for which fields)

●	po_approval_thresholds (role-based matrix by value/category)

4.3.3 UI / UX Requirements
Screen Name: Purchase Order
 Path: Procurement → Purchase Order
________________________________________
A) PO List
Columns:
●	PO Number

●	PO Date

●	Supplier

●	Ordering Location

●	Status

●	Total Amount

●	Linked RFQ (Yes/No or RFQ Number)

●	Linked PR (Yes/No or count)

●	Last Updated

Filters:
●	Date range (PO Date)

●	Status (DRAFT, PENDING_APPROVAL, APPROVED, SENT_TO_SUPPLIER, etc.)

●	Supplier

●	Location

●	Created By / Approved By

●	Has RFQ? (Yes/No)

●	Has PR? (Yes/No)

Actions:
●	Create PO

●	Open/Edit PO (depending on status/role)

●	Submit for Approval

●	Approve / Reject (for approvers)

●	Send PO to Supplier (email/PDF/export)

●	Cancel PO (with reason)

●	View PO History / Amendments

________________________________________
B) PO Header Form
Sections:
●	General

○	PO Number (auto)

○	PO Date (default to today)

○	Supplier (lookup)

○	Supplier Contact Name / Email

○	Ordering Location

○	Default Delivery Location

○	Currency

●	Commercial Terms

○	Payment Terms

○	Incoterms

○	Freight Terms

○	Tax Inclusive? (Yes/No)

○	Expected Start & Completion Dates (for services/Capex)

●	References

○	Linked RFQ (if any)

○	Linked RFQ Round (optional display)

○	Linked PR(s) (view lines referenced)

○	Contract/Rate Agreement reference (future enhancement)

●	Notes

○	Internal Notes (not printed)

○	Remarks to Supplier (printed on PO/email)

●	System Info (read-only)

○	PO Status

○	Approval Required? (Yes/No)

○	Approved By / At

○	Sent to Supplier At

○	Version No

○	Amendment Of (if this is a revised PO)

________________________________________
C) PO Line Entry
Grid behavior:
Columns:
●	Line No

●	Item Code / Name lookup

●	SKU / Variant

●	Description Override (editable)

●	UOM

●	Ordered Qty

●	Unit Price

●	Discount %

●	Line Gross

●	Tax %

●	Tax Amount

●	Line Net

●	Delivery Location

●	Required By Date

●	PR Reference (if from PR)

●	RFQ Quote Reference (if from RFQ)

●	Line Status

Features:
●	Add line:

○	From Item Master search.

○	From PR line selection: “Add from PR” (filter by location, status, item).

○	From RFQ award: “Import from RFQ” picks awarded vendor lines.

●	Inline validation:

○	Required fields for item, qty, price, UOM.

○	Non-zero ordered quantity.

●	Read-only fields when derived from RFQ:

○	Optionally lock price & terms if config prohibits price override.

●	Totals panel at bottom:

○	Sum of gross, discount, tax, net.

________________________________________
D) Approver View
Approvers see:
●	Summary header (supplier, amount, category, location).

●	Risk flags:

○	Price above last purchase?

○	Vendor risk rating?

○	Missing RFQ despite threshold?

●	Key calculated data:

○	PO value vs approval limit.

○	Budget consumption (if budget module integrated).

Actions:
●	Approve (with optional comment)

●	Reject (reason required)

●	Request Clarification (optional intermediate status in future)

________________________________________
E) Supplier-Facing View (Print / PDF / Email)
PO document includes:
●	Supplier details

●	PO number and date

●	Delivery details

●	Line items with quantities & prices

●	Taxes & totals

●	Payment terms & Incoterms

●	Signature/block text according to company branding

System must support generating:
●	PDF

●	Optional email body with attached PDF

●	Optional export (CSV/Excel) if needed

________________________________________
4.3.4 Validation Rules
Header-level:
●	po_number unique per company.

●	supplier_id required and must reference ACTIVE supplier.

●	ordering_location_id required.

●	po_date cannot be in the future (configurable rule) or earlier than PR/RFQ dates (for linked documents).

●	If po_requires_pr is true for this category/location:

○	At least one line must reference a PR line.

●	If po_requires_rfq is true (threshold/category-based) and RFQ is enabled:

○	PO must reference awarded RFQ data, or user must provide a justification comment and optionally follow an elevated approval flow.

Line-level:
●	At least one line item is required.

●	ordered_qty > 0.

●	ordered_qty + cancelled_qty must be ≥ received_qty.

●	unit_price ≥ 0.

●	When line is linked to RFQ:

○	If price_change_tolerance_percent is configured:

■	PO line price deviation vs RFQ awarded price above tolerance → requires additional approval.

●	When line is linked to PR:

○	ordered_qty_from_pr (sum from PO lines) must not exceed requested_qty on PR line.

●	If line refers to a service item:

○	required_by_date or expected_completion_date should be present.

Status/Workflow integrity:
●	Cannot submit for approval when:

○	Required header fields are missing.

○	Any line is incomplete.

●	Cannot approve PO with status not in PENDING_APPROVAL.

●	Cannot cancel PO if:

○	Any line is FULLY_RECEIVED (should go through closure process instead).

●	Cannot edit PO lines once:

○	GRN exists for that line (only limited fields allowed per config).

Amendment rules:
●	When PO is amended:

○	Certain fields (vendor, base currency) may be locked.

○	Amendments that affect already received quantities may be blocked or require higher approval.

________________________________________
4.3.5 Workflow
Hybrid, config-driven PO lifecycle:
Default state machine:
●	DRAFT
 → Submit → PENDING_APPROVAL (if approval_required = true)
 → Approve → APPROVED
 → Send to Supplier → SENT_TO_SUPPLIER
 → GRNs posted → PARTIALLY_RECEIVED / FULLY_RECEIVED
 → Close → CLOSED

Alternative paths:
●	DRAFT → Cancel → CANCELLED

●	PENDING_APPROVAL → Reject → DRAFT or REJECTED (config)

●	APPROVED → Cancel (if allowed and no GRN yet) → CANCELLED

Integration with other modules:
●	PR:

○	As PO lines referencing PR are created:

■	purchase_requisition_po_link updated.

■	PR line statuses updated (OPEN → PARTIALLY_ORDERED → FULLY_ORDERED).

■	PR header may move from APPROVED → PARTIALLY_ORDERED → FULLY_ORDERED → CLOSED.

●	RFQ:

○	Once PO is created from awarded RFQ:

■	RFQ header may move to AWARDED and eventually CLOSED.

●	GRN:

○	GRN lines referencing PO lines update:

■	received_qty on PO lines.

■	PO line statuses (OPEN → PARTIALLY_RECEIVED → FULLY_RECEIVED).

■	PO header status (APPROVED/SENT_TO_SUPPLIER → PARTIALLY_RECEIVED → FULLY_RECEIVED → CLOSED).

Amendments:
●	Optionally modeled as:

○	New PO record with is_amendment_of_po_id referencing original.

○	Version numbers to track revision history.

○	Original PO may move to a status like SUPERSEDED (future enhancement).

________________________________________
4.3.6 Module Metadata & Build Steps
Module Metadata
module_type: transaction
complexity: medium_to_complex

template_ref: _txn_03

extension_allowed: true

depends_on:
  - Company
  - Locations
  - Item Master
  - Item Variants
  - Units of Measure
  - Suppliers
  - Purchase Requisition (4.1) [optional linkage]
  - Request for Quotation (4.2) [optional linkage]
  - Users / Roles
  - Procurement Configuration

used_by:
  - ASN (4.4)
  - GRN & QC (4.5)
  - Invoice Matching (4.6)
  - Supplier Returns (4.7)
  - Payments & Settlement (4.8)
  - Vendor Performance (4.9)
  - Procurement Analytics

________________________________________
Build Steps (for AI / Implementation Engine)
You are building a Medium-to-Complex Transaction module for a Retail ERP.

Module: Purchase Order (PO)
Template: _txn_03

Requirements:

1) Backend (Django + DRF):

   Models:
   - purchase_order (header)
   - purchase_order_line (lines)
   - Reuse purchase_requisition_po_link table defined in 4.1
     for PR–PO linkage.

   Serializers:
   - Header + nested lines serializer(s).
   - Lightweight list serializer for PO listing.

   Viewsets & Endpoints:
   - CRUD for PO header & lines with appropriate permissions.
   - Workflow actions:
     - submit_po (DRAFT → PENDING_APPROVAL or APPROVED when no approval needed)
     - approve_po (PENDING_APPROVAL → APPROVED)
     - reject_po (PENDING_APPROVAL → DRAFT/REJECTED as per config)
     - cancel_po (allowed from specific statuses)
     - send_to_supplier (marks as SENT_TO_SUPPLIER + triggers PDF/email generation hook)
   - Integration endpoints:
     - Query APPROVED POs for GRN creation.
     - Query POs by PR or RFQ linkage.

   Business Rules:
   - Enforce validation from section 4.3.4.
   - Enforce configuration behavior (po_requires_pr, po_requires_rfq,
     tolerances, amendment rules).
   - Keep `received_qty` updated via GRN integration (referenced later in 4.5).

2) Frontend (React + Vite + Tailwind):

   Screens:
   - PO List:
     - Columns, filters, and actions as defined in UI section.
     - Status color-coding (badges) and quick filters.
   - PO Edit:
     - Tabs/sections for Header, Lines, References, Notes, System Info.
     - Lines grid with:
       - Add line manually
       - Add from PR
       - Add from RFQ (awarded items)
     - Totals panel for gross, discount, tax, net.
   - Approval View:
     - Compact summary of PO header with risk/exception indicators.
     - Approve/Reject actions with comment.

   Behavior:
   - Lock appropriate fields based on status (e.g. cannot edit supplier
     after approval).
   - Show clear indicators when PO came from PR/RFQ (and enforce
     restrictions like price changes above tolerance).
   - Provide “View Source PR” and “View RFQ” links for traceability.

3) Integration:

   - From PR (4.1):
     - APIs to search and select APPROVED PR lines by location/item.
     - When lines imported:
       - Maintain PR–PO link.
       - Update PR line progress.

   - From RFQ (4.2):
     - APIs to fetch AWARDED RFQ lines for a selected supplier.
     - Pre-populate unit prices, quantities, and terms from
       `rfq_vendor_quote_line`.

   - To GRN (4.5):
     - Provide PO lines as source for GRN creation, ensuring remaining
       receivable quantity is correctly calculated.

   - To Invoice Matching (4.6):
     - Provide confirmed PO prices, quantities, and tax flags.

4) Security & Roles:

   - Define distinct roles:
     - PO Creator / Buyer
     - PO Approver
     - PO Viewer
   - Restrict amendment and cancellation actions to appropriate roles.

Ensure the implementation adheres to the data model, workflows,
validation rules, and UI/UX requirements defined in the Purchase Order
specification.

4.4 Advance Shipment Notice (ASN)
Template Ref: _txn_03 (Medium Transaction, Optional)
4.4.1 Business Purpose
The Advance Shipment Notice (ASN) is a pre-receipt notification from the supplier indicating what is being shipped, in what quantities, and when it will arrive, usually against one or more Purchase Orders (POs).
Goals:
●	Improve receiving efficiency at warehouse/store:

○	Pre-plan space, manpower, and put-away.

●	Enable pre-validation of shipment contents vs PO:

○	Identify over/under shipments before physical arrival.

●	Support integration with:

○	3PL logistics

○	EDI-compatible suppliers

●	Provide an intermediate layer between PO → GRN for:

○	High-volume distribution centers

○	Cross-dock operations

○	Omnichannel fulfillment flows

Hybrid behavior (config-driven):
●	ASN can be:

○	Optional: GRN can be created directly from PO.

○	Mandatory for certain suppliers/categories:

■	e.g., DC inbound, imports, high-value electronics.

●	ASN can be:

○	Created by supplier (via portal/API)

○	Created by internal user (for manual carriers / simple suppliers)

________________________________________
4.4.2 Data Model
A) ASN Header (advance_shipment_notice)
Field	Type	Required	Description
id	UUID	Yes	Primary key
company_id	FK	Yes	Company scope
asn_number	String(30)	Yes	Human-readable ASN No (own sequence or supplier reference)
asn_status	Enum	Yes	DRAFT, PUBLISHED, IN_TRANSIT, ARRIVED, CANCELLED, CLOSED
supplier_id	FK (Supplier)	Yes	Supplier sending shipment
supplier_asn_ref	String(50)	No	Supplier's ASN/Shipment reference
created_by_user_id	FK (User)	Yes	Creator (internal or system user for supplier portal submissions)
shipment_date	Date	Yes	Date goods left supplier
estimated_arrival_date	Date	Yes	Expected arrival date
ship_from_location	String(200)	No	Supplier/DC origin details
ship_to_location_id	FK (Location)	Yes	Store/warehouse/DC receiving
carrier_name	String(100)	No	Transporter/courier name
vehicle_number	String(50)	No	Truck/vehicle/regn number
tracking_number	String(100)	No	AWB/bill/consignment tracking
total_packages	Integer	No	Number of cartons/pallets
gross_weight_kg	Decimal	No	Total shipment weight
remarks	Text	No	Any notes on shipment
created_from_po_flag	Boolean	Yes	True if ASN derived directly from PO(s)
created_at	DateTime	Auto	
updated_at	DateTime	Auto	
________________________________________
B) ASN–PO Link (asn_po_link)
Many ASNs can relate to many POs, but typical scenario: ASN for one or more PO(s) for same supplier & destination.
Field	Type	Required	Description
id	UUID	Yes	Primary key
advance_shipment_notice_id	FK (ASN Header)	Yes	ASN reference
purchase_order_id	FK (PO Header)	Yes	Linked PO header
________________________________________
C) ASN Line (asn_line)
Represents item quantities that supplier indicates are being shipped, usually against PO lines.
Field	Type	Required	Description
id	UUID	Yes	Primary key
advance_shipment_notice_id	FK (ASN Header)	Yes	ASN header
purchase_order_line_id	FK (PO Line)	Yes	Linked PO line
item_id	FK (Item)	Yes	Item master
item_variant_id	FK (Item Variant)	Yes	SKU
uom_id	FK (UOM)	Yes	UOM
shipped_qty	Decimal	Yes	Quantity supplier claims is shipped
expected_arrival_date	Date	No	May override header-level ETA
batch_number	String(50)	No	Supplier’s batch if known
expiry_date	Date	No	For perishable/pharma
serial_numbers_blob	Text	No	JSON or comma list (for serialized items)
line_remarks	Text	No	Any line-level comments
line_status	Enum	Yes	OPEN, PARTIALLY_RECEIVED, FULLY_RECEIVED, CANCELLED
Note: The actual received quantity will be recorded at GRN; ASN is a planned or expected quantity.
________________________________________
D) Config / Control (Conceptual)
●	asn_enabled (Company, Location, Supplier)

●	asn_mandatory_for_grn (Yes/No per supplier/category)

●	asn_allow_over_ship_percent (tolerance vs PO ordered_qty)

●	asn_allow_partial_mapping (ASN may not cover all PO lines)

●	asn_require_tracking_info (Yes/No)

________________________________________
4.4.3 UI / UX Requirements
Screen Name: Advance Shipment Notice
 Path: Procurement → Inbound → ASN
________________________________________
A) ASN List
Columns:
●	ASN Number

●	Supplier

●	Ship From (optionally display)

●	Ship To (Location)

●	Shipment Date

●	Estimated Arrival Date

●	Status

●	Linked PO Count

●	Total Packages (if captured)

Filters:
●	Date range (Shipment or ETA)

●	Status (DRAFT, IN_TRANSIT, ARRIVED, etc.)

●	Supplier

●	Location

●	Linked PO Number

Actions:
●	Create ASN (from PO)

●	View/Edit ASN (status-driven)

●	Mark as In Transit / Arrived

●	Cancel ASN (with reason)

________________________________________
B) ASN Header Form
Sections:
●	Shipment Details

○	ASN Number (auto)

○	Supplier

○	Ship From

○	Ship To Location

○	Shipment Date

○	Estimated Arrival Date

○	Carrier, Vehicle No, Tracking Number

○	Gross Weight, Total Packages

○	Remarks

●	References

○	Linked POs (multi-select)

○	From PO search:

■	Supplier filter

■	Location filter

■	Status filter (APPROVED, SENT_TO_SUPPLIER, PARTIALLY_RECEIVED)

●	System Info (read-only)

○	ASN Status

○	Created By / At

○	Updated At

________________________________________
C) ASN Lines Grid
Columns:
●	PO Number

●	PO Line No

●	Item Code / Name

●	SKU / Variant

●	UOM

●	Ordered Qty (from PO)

●	Already Shipped Qty (from previous ASNs)

●	Shipped Qty (current ASN)

●	Expected Arrival Date

●	Batch No (optional)

●	Expiry Date (optional)

●	Line Remarks

Features:
●	Add lines by:

○	Selecting from linked PO lines.

●	Auto-calc:

○	Maximum allowed shipped_qty based on:

■	PO ordered_qty and previous ASN shipped_qty (if controlled by config).

●	Show warnings:

○	If shipped_qty > remaining PO qty + tolerance, highlight cell.

________________________________________
4.4.4 Validation Rules
Header-level:
●	asn_number unique per company.

●	supplier_id required and must match supplier of the linked PO(s).

●	ship_to_location_id must match PO delivery location (unless config allows cross-docking).

●	shipment_date must be <= estimated_arrival_date (basic date sanity).

Line-level:
●	purchase_order_line_id must reference a valid PO line where:

○	PO status is APPROVED or SENT_TO_SUPPLIER or PARTIALLY_RECEIVED.

●	shipped_qty > 0.

●	If asn_allow_over_ship_percent is configured:

○	Validate total_shipped_qty_for_po_line ≤ ordered_qty * (1 + tolerance).

●	For batch-managed items:

○	If config requires batch/expiry pre-notification, enforce batch_number and expiry_date not null.

Status/Workflow:
●	Cannot move ASN to IN_TRANSIT without:

○	At least one line.

●	Cannot mark ASN ARRIVED without:

○	Shipment Date and ETA set.

●	Cannot Cancel ASN:

○	If already linked to any posted GRN.

________________________________________
4.4.5 Workflow
Default:
●	DRAFT
 → Publish/Confirm → PUBLISHED
 → Dispatch/Ship → IN_TRANSIT
 → Mark Arrival (optional) → ARRIVED
 → GRN created against ASN → CLOSED (once fully accounted)

Alternative transitions:
●	DRAFT → Cancel → CANCELLED

●	PUBLISHED / IN_TRANSIT → Cancel (only if no GRN yet) → CANCELLED

Integration with GRN:
●	When GRN is created:

○	User may choose source = PO or source = ASN.

○	If from ASN:

■	Default GRN lines are populated from ASN lines.

■	GRN received quantities can be less than or equal to ASN shipped_qty (and potentially more if physical receipt differs – subject to config).

○	ASN line status updates to:

■	PARTIALLY_RECEIVED or FULLY_RECEIVED.

○	ASN may close when all lines are fully received or cancelled.

________________________________________
4.4.6 Module Metadata & Build Steps
Module Metadata
module_type: transaction
complexity: medium

template_ref: _txn_03

extension_allowed: true

depends_on:
  - Company
  - Locations
  - Suppliers
  - Purchase Order (4.3)
  - Users / Roles
  - Procurement/Inbound Config

used_by:
  - GRN & QC (4.5)
  - Inbound Capacity Planning
  - Vendor Performance (on-time shipment vs ETA)

________________________________________
Build Steps (for AI / Implementation Engine)
You are building a Medium Transaction module for a Retail ERP.

Module: Advance Shipment Notice (ASN)
Template: _txn_03

Requirements:

1) Backend (Django + DRF):

   Models:
   - advance_shipment_notice (header)
   - asn_po_link (ASN to PO mapping)
   - asn_line (item-level shipment details)

   Serializers:
   - ASN header with nested lines.
   - List serializer for ASN listing.

   Viewsets & Endpoints:
   - CRUD for ASN header & lines.
   - Workflow actions:
     - publish_asn
     - mark_in_transit
     - mark_arrived
     - cancel_asn
   - Integration endpoints:
     - Load PO lines for ASN creation (by supplier/location/status).
     - Provide ASN lines as source for GRN creation.

   Business Rules:
   - Enforce supplier/location/PO consistency.
   - Enforce shipped quantity & tolerance rules.

2) Frontend (React + Vite + Tailwind):

   Screens:
   - ASN List:
     - Filters, status badges, actions.
   - ASN Edit:
     - Header form (shipment info, references).
     - Lines grid (linked PO lines, shipped qty).

   Behavior:
   - Lock selected PO(s) and supplier on ASN once lines are added.
   - Provide clear warnings on over-ship attempts.

3) Integration:

   - With Purchase Order:
     - Fetch eligible PO lines for a supplier/location.
   - With GRN:
     - Allow GRN creation by selecting ASN and using its lines as default.

4) Security & Roles:

   - ASN Creator / ASN Editor / ASN Viewer.
   - Restrict cancellation and status changes to appropriate roles.

Ensure strict adherence to the data model, validation, and workflow
rules defined in the ASN specification.

________________________________________
4.5 Goods Receipt Note (GRN) + Quality Check (QC)
Template Ref: _txn_03 (Medium/Complex Transaction)
4.5.1 Business Purpose
The Goods Receipt Note (GRN) records the actual physical receipt of goods/services against a Purchase Order (and optionally ASN).
 The Quality Check (QC) sub-process validates whether received items meet quality standards.
Goals:
●	Update inventory with accurate received quantities, batches, and serials.

●	Support 3-way / 4-way matching (PO ↔ ASN ↔ GRN ↔ Invoice).

●	Capture accepted vs rejected quantities, reasons, and QC results.

●	Enable vendor performance and claims (damage, shortage, wrong items).

●	Provide traceability for batch/expiry/serial items (FMCG, pharma, electronics).

Hybrid behavior (config-driven):
●	GRN can be created:

○	Directly from PO (common retail scenario).

○	From ASN (for advanced inbound flows).

●	QC can be:

○	Embedded within GRN (simple)

○	Separate but linked QC document (for heavy QC flows) — we’ll model QC inline but data model ready for extension.

________________________________________
4.5.2 Data Model
A) GRN Header (goods_receipt_note)
Field	Type	Required	Description
id	UUID	Yes	Primary key
company_id	FK	Yes	Company scope
grn_number	String(30)	Yes	Human-readable GRN No
grn_status	Enum	Yes	DRAFT, POSTED, CANCELLED
supplier_id	FK (Supplier)	Yes	Supplier delivering goods
receiving_location_id	FK (Location)	Yes	Store/Warehouse receiving goods
goods_received_date	Date	Yes	Physical receipt date
linked_po_id	FK (PO Header)	Yes	Primary PO reference (multi-PO via lines allowed)
linked_asn_id	FK (ASN Header)	No	If GRN created from ASN
invoice_number	String(50)	No	Supplier invoice number (if provided at receipt)
invoice_date	Date	No	Supplier invoice date
vehicle_number	String(50)	No	Vehicle/truck number
delivery_document_ref	String(50)	No	Delivery challan / packing list ref
remarks	Text	No	General comments
created_by_user_id	FK (User)	Yes	Who created GRN
posted_by_user_id	FK (User)	No	Who finalized/posted GRN
posted_at	DateTime	No	Posting timestamp
created_at	DateTime	Auto	
updated_at	DateTime	Auto	
________________________________________
B) GRN Line (goods_receipt_note_line)
Each line represents received quantity for a PO line (potentially partial).
Field	Type	Required	Description
id	UUID	Yes	Primary key
goods_receipt_note_id	FK (GRN Header)	Yes	Parent GRN
purchase_order_line_id	FK (PO Line)	Yes	PO line reference
asn_line_id	FK (ASN Line)	No	If GRN came via ASN
item_id	FK (Item)	Yes	Item master
item_variant_id	FK (Item Variant)	Yes	SKU
uom_id	FK (UOM)	Yes	UOM
received_qty	Decimal	Yes	Total received qty at dock
accepted_qty	Decimal	Yes	Qty accepted into stock
rejected_qty	Decimal	Yes	Qty rejected; must satisfy received_qty = accepted_qty + rejected_qty
putaway_location_id	FK (Location/Bin)	No	Warehouse location/bin (if WMS integrated)
qc_required	Boolean	Yes	Derived from item/category configuration
qc_status	Enum	Yes	NOT_REQUIRED, PENDING, PASSED, FAILED, OVERRIDDEN
rejection_reason_code	String(50)	No	Reason (damage, short expiry, wrong item, etc.)
rejection_remarks	Text	No	Additional comments
batch_number	String(50)	No	Batch/lot number
expiry_date	Date	No	Expiry date for perishable items
serial_numbers_blob	Text	No	JSON/comma-separated serials
line_remarks	Text	No	General line remarks
________________________________________
C) GRN–Inventory Movement (Conceptual)
Actual inventory movement is usually recorded via:
●	Stock Ledger / Inventory Transaction table (outside this section), using:

○	accepted_qty to increase stock.

○	Optionally mark rejected_qty in blocked, return, or scrap location.

We assume:
●	This module produces inventory movement events to be consumed by Inventory.

________________________________________
D) Config / Control (Conceptual)
●	grn_requires_po = true/false (no-PO receipts allowed? rarely; mostly false)

●	grn_allows_without_asn = true/false

●	qc_required_by_category (e.g. electronics, fresh, pharma)

●	expiry_must_be_at_least_x_days (min remaining shelf-life)

●	allow_receive_over_po_percent (tolerance, e.g., 5%)

●	block_posting_if_qc_pending (true/false per item/category)

________________________________________
4.5.3 UI / UX Requirements
Screen Name: Goods Receipt Note
 Path: Procurement / Inventory → Inbound → GRN
________________________________________
A) GRN List
Columns:
●	GRN Number

●	GRN Date

●	Supplier

●	Receiving Location

●	Linked PO Number

●	Linked ASN (Yes/No or ASN No)

●	Status

●	Created By / Posted By

Filters:
●	Date range (GRN Date)

●	Supplier

●	Location

●	Status (DRAFT, POSTED, CANCELLED)

●	Linked PO / ASN

Actions:
●	Create GRN

○	From PO

○	From ASN

●	View / Edit (DRAFT only)

●	Post GRN

●	Cancel GRN (with reason)

●	Print/Export GRN (for internal record)

________________________________________
B) GRN Header Form
Sections:
●	General

○	GRN Number (auto)

○	Goods Received Date

○	Receiving Location

○	Supplier (inferred from PO)

○	Linked PO (required)

○	Linked ASN (optional)

○	Invoice Number/Date (if known)

○	Vehicle / Delivery Document ref

○	Remarks

●	System Info

○	GRN Status

○	Created By / At

○	Posted By / At

________________________________________
C) GRN Lines Grid
Columns:
●	PO Number

●	PO Line No

●	Item Code / Name

●	SKU

●	UOM

●	PO Ordered Qty

●	Previously Received Qty

●	Remaining Qty

●	Received Qty (input)

●	Accepted Qty (input)

●	Rejected Qty (derived or input)

●	QC Required?

●	QC Status

●	Batch No / Expiry (if applicable)

●	Rejection Reason

●	Line Remarks

Features:
●	Load from:

○	Selected PO (shows remaining quantities).

○	Selected ASN (default from ASN shipped_qty).

●	Auto:

○	Compute remaining_qty = ordered_qty - total_received_so_far.

○	Suggest received_qty from ASN (if used).

●	Inline validations:

○	Rejected+Accepted = Received.

○	Remaining quantities not exceeded beyond tolerance.

________________________________________
D) QC Capture (Inline or Side Panel)
For lines with qc_required = true:
●	QC Status field:

○	PENDING, PASSED, FAILED, OVERRIDDEN.

●	QC input fields (conceptual, can be future extended):

○	QC check list (e.g., packaging, labeling, physical condition).

○	Measured attributes (weight, dimension, etc.).

○	QC remarks.

○	QC done by (user) + date/time.

UI options:
●	Embedded inline in GRN line editor.

●	Or QC modal dialog per line.

________________________________________
4.5.4 Validation Rules
Header-level:
●	grn_number unique per company.

●	receiving_location_id required.

●	goods_received_date cannot be in future (configurable).

●	linked_po_id required unless config allows non-PO GRN.

●	If linked_asn_id present:

○	Supplier in ASN must match Supplier in PO.

○	Location in ASN must match receiving location.

Line-level:
●	Each GRN must have at least one line.

●	received_qty > 0.

●	accepted_qty + rejected_qty = received_qty.

●	received_qty + previous GRN receipts for that PO line must not exceed:

○	ordered_qty * (1 + over_receive_tolerance_percent).

QC-level:
●	If qc_required = true:

○	If block_posting_if_qc_pending = true:

■	Cannot POST GRN while any line with QC required has qc_status = PENDING.

●	For batch-controlled items:

○	batch_number and expiry_date cannot be null.

○	expiry_date must be at least today + min_shelf_life_days if configured.

Status/Workflow:
●	Only DRAFT GRNs can be edited.

●	POSTED GRN:

○	Locked except for limited reversal/cancellation logic as per finance/inventory policy.

●	CANCELLED GRN:

○	If inventory postings already done, must either:

■	Post negative adjustment, or

■	Be blocked — actual reversal handled in separate process.

________________________________________
4.5.5 Workflow
Standard:
●	DRAFT
 → Post GRN → POSTED (inventory updated)

Alternative:
●	DRAFT → Cancel → CANCELLED

Integration:
●	With PO:

○	On POST:

■	Increase received_qty on purchase_order_line.

■	Update PO line status: OPEN → PARTIALLY_RECEIVED → FULLY_RECEIVED.

■	Update PO header status accordingly (e.g., APPROVED → PARTIALLY_RECEIVED → FULLY_RECEIVED → CLOSED).

●	With ASN:

○	If GRN references ASN:

■	Update ASN line status based on accepted quantities.

■	When all ASN lines fully received or cancelled, ASN may be set to CLOSED.

●	With Invoice Matching (4.6):

○	GRN details feed quantity & QC info for 3-way / 4-way matching.

●	With Vendor Performance (4.9):

○	Defect rates, damage reasons, short/over-deliveries all feed into vendor quality KPIs.

________________________________________
4.5.6 Module Metadata & Build Steps
Module Metadata
module_type: transaction
complexity: medium_to_complex

template_ref: _txn_03

extension_allowed: true

depends_on:
  - Company
  - Locations
  - Suppliers
  - Purchase Order (4.3)
  - ASN (4.4) [optional]
  - Users / Roles
  - Item / Variant / UOM
  - Inventory & Stock Ledger (for posting)
  - QC / Quality Rules Config

used_by:
  - Invoice Matching (4.6)
  - Supplier Returns (4.7)
  - Vendor Performance (4.9)
  - Inventory Valuation & Stock Reports

________________________________________
Build Steps (for AI / Implementation Engine)
You are building a Medium-to-Complex Transaction module for a Retail ERP.

Module: Goods Receipt Note (GRN) + Quality Check (QC)
Template: _txn_03

Requirements:

1) Backend (Django + DRF):

   Models:
   - goods_receipt_note (header)
   - goods_receipt_note_line (lines)

   Serializers:
   - GRN header with nested lines.
   - List serializer for GRN listing.

   Viewsets & Endpoints:
   - CRUD for GRN header & lines (DRAFT only).
   - Workflow actions:
     - post_grn (DRAFT → POSTED)
     - cancel_grn (DRAFT → CANCELLED)
   - Integration endpoints:
     - Load PO lines with remaining quantities.
     - Load ASN lines (if GRN created from ASN).

   Business Rules:
   - Enforce quantity validations, tolerance rules, QC dependencies.
   - On POST:
     - Trigger inventory movement events for accepted_qty.
     - Update PO line received_qty and statuses.
     - Update ASN line statuses if linked.

2) Frontend (React + Vite + Tailwind):

   Screens:
   - GRN List:
     - Filters and actions as per spec.
   - GRN Edit:
     - Header form (supplier, PO, dates, documents).
     - Lines grid with:
       - From PO loader.
       - Optionally from ASN.
     - Inline QC flags and fields.

   Behavior:
   - Lock GRN after POST.
   - Clear warnings for over-receipt, missing batch/expiry, QC pending.

3) Integration:

   - Upstream:
     - POs and ASNs as source documents.
   - Downstream:
     - Expose GRN data to Invoice Matching (4.6).
     - Expose QC and rejection reasons to Vendor Performance (4.9).
     - Post inventory movements to Inventory module.

4) Security & Roles:

   - GRN Creator (warehouse/store user).
   - GRN Poster (may be same or different role).
   - GRN Viewer.

Ensure full adherence to the data model, validation rules, and workflow
defined in the GRN + QC specification.

4.6 Supplier Invoice Matching (3-way / 4-way)
Template Ref: _txn_03 (Medium/Complex Transaction)
4.6.1 Business Purpose
Supplier Invoice Matching validates a supplier invoice against what was ordered (PO) and what was received (GRN and QC), before it becomes a payable liability in Finance/AP.
Goals:
●	Prevent overbilling, duplicate billing, and fraud.

●	Ensure that only valid, matched invoices are approved for payment.

●	Support:

○	2-way match: Invoice ↔ PO (for services/recurring)

○	3-way match: Invoice ↔ PO ↔ GRN (standard goods)

○	4-way match: Invoice ↔ PO ↔ GRN ↔ QC (for items requiring QC)

●	Capture and route exceptions:

○	Price variance

○	Quantity variance

○	Tax mismatch

○	Unmatched invoice (no PO/GRN reference)

●	Feed Vendor Performance (billing accuracy) and Payment & Settlement.

Hybrid behavior (config-driven):
●	Matching model can vary by:

○	Company

○	Location / Business Unit

○	Category (Capex, Services, Consumables, Imports)

●	Tolerances can be configured by:

○	Amount (% or absolute)

○	Tax variance

○	Price vs last PO / contract.

________________________________________
4.6.2 Data Model
A) Supplier Invoice Header (supplier_invoice)
Field	Type	Required	Description
id	UUID	Yes	Primary key
company_id	FK	Yes	Company scope
supplier_id	FK (Supplier)	Yes	Supplier issuing invoice
invoice_number	String(50)	Yes	Supplier’s invoice number
invoice_status	Enum	Yes	DRAFT, VALIDATED, MATCHED, EXCEPTION, APPROVAL_PENDING, APPROVED, POSTED, REJECTED, CANCELLED
invoice_date	Date	Yes	Invoice date
posting_date	Date	No	AP posting date (finance integration)
currency_code	String(10)	Yes	Invoice currency
total_invoice_amount	Decimal	Yes	As per invoice document (gross)
total_tax_amount	Decimal	Yes	Total tax on invoice
total_net_amount	Decimal	Yes	Net amount (if needed)
po_id	FK (PO Header)	No	Primary PO this invoice claims to belong to (optional if multi-PO)
grn_id	FK (GRN Header)	No	Optional primary GRN reference
match_type	Enum	Yes	TWO_WAY, THREE_WAY, FOUR_WAY
match_status	Enum	Yes	UNMATCHED, PARTIALLY_MATCHED, FULLY_MATCHED, MATCH_WITH_VARIANCE
match_variance_amount	Decimal	Yes	Total variance amount vs matched reference(s)
match_variance_reason	Text	No	Summary of main variance reasons
payment_terms_code	String(50)	No	Payment terms (default from supplier, can be overridden)
due_date	Date	No	Derived from invoice_date + payment_terms
source_capture_method	Enum	Yes	MANUAL_ENTRY, VENDOR_PORTAL, OCR_UPLOAD, EDI_API
duplicate_check_signature	String(200)	No	Hash derived from supplier+invoice# etc.
duplicate_flag	Boolean	Yes	System-detected potential duplicate
approval_required	Boolean	Yes	Based on value/variance/rules
approved_by_user_id	FK (User)	No	Who approved this invoice for posting/payment
approved_at	DateTime	No	Approval timestamp
rejected_by_user_id	FK (User)	No	If invoice was rejected
rejected_at	DateTime	No	Rejection timestamp
remarks_internal	Text	No	Notes for AP/procurement only
created_by_user_id	FK (User)	Yes	Invoice captured by
created_at	DateTime	Auto	
updated_at	DateTime	Auto	
Note: Multi-PO and multi-GRN linking can be handled via detail/match table below.
________________________________________
B) Supplier Invoice Line (supplier_invoice_line)
Field	Type	Required	Description
id	UUID	Yes	Primary key
supplier_invoice_id	FK (Invoice Header)	Yes	Invoice header
item_id	FK (Item)	No	May be null for non-catalog items
item_variant_id	FK (Item Variant)	No	Same as above
description	String(255)	Yes	Line description from invoice
uom_id	FK (UOM)	No	UOM if structured
qty_invoiced	Decimal	Yes	Quantity as per invoice
unit_price_invoiced	Decimal	Yes	Price per unit as per invoice
line_gross_amount_invoiced	Decimal	Yes	= qty_invoiced × unit_price_invoiced (before tax)
tax_percent_invoiced	Decimal	No	Tax rate applied (if line-wise)
tax_amount_invoiced	Decimal	No	Line tax amount
line_net_amount_invoiced	Decimal	No	Gross + tax or gross - discount + tax
gl_account_code	String(50)	No	For service invoices / non-PO lines
line_remarks	Text	No	Any notes
________________________________________
C) Invoice Match Detail (supplier_invoice_match_detail)
Connects invoice lines to PO/GRN/QC, enabling 2-way/3-way/4-way matching.
Field	Type	Required	Description
id	UUID	Yes	Primary key
supplier_invoice_line_id	FK (Invoice Line)	Yes	Invoice line
purchase_order_line_id	FK (PO Line)	No	For 2/3/4-way match
goods_receipt_note_line_id	FK (GRN Line)	No	For 3/4-way match
qc_status_at_match	Enum	No	NOT_REQUIRED, PENDING, PASSED, FAILED, etc.
matched_qty	Decimal	Yes	Qty considered for matching
matched_unit_price	Decimal	Yes	Reference unit price (from PO/RFQ/Contract)
matched_tax_percent	Decimal	No	Tax rate from PO or master
qty_variance	Decimal	Yes	qty_invoiced - matched_qty
price_variance	Decimal	Yes	unit_price_invoiced - matched_unit_price
tax_variance	Decimal	Yes	tax_invoiced - matched_tax
variance_amount_total	Decimal	Yes	Monetary impact of variances
variance_status	Enum	Yes	WITHIN_TOLERANCE, EXCEEDS_TOLERANCE
variance_reason_code	String(50)	No	Under/over billing, extra charges, tax diff
manual_override_flag	Boolean	Yes	True if user forced override
override_justification	Text	No	Reason for override (if any)
________________________________________
D) Config / Control (Conceptual)
Sample controls:
●	invoice_matching_model per category/location:

○	TWO_WAY, THREE_WAY, FOUR_WAY

●	Tolerances:

○	qty_tolerance_percent

○	price_tolerance_percent

○	tax_tolerance_percent

○	amount_tolerance_absolute

●	auto_match_if_within_tolerance (Yes/No)

●	block_posting_if_qc_failed (Yes/No)

●	block_posting_if_duplicate_flag = true (or require override)

________________________________________
4.6.3 UI / UX Requirements
Screen Name: Supplier Invoice Matching
 Path: Procurement / AP → Supplier Invoices
________________________________________
A) Invoice List
Columns:
●	Invoice Number

●	Invoice Date

●	Supplier

●	PO Number (if any)

●	GRN Number (if any)

●	Status

●	Match Status

●	Variance Amount

●	Created By / Approved By

●	Source (Manual/OCR/Portal/EDI)

Filters:
●	Date range (Invoice Date, Posting Date)

●	Supplier

●	Status (DRAFT, MATCHED, EXCEPTION, etc.)

●	Match Type (2-Way, 3-Way, 4-Way)

●	Has Variance? (Yes/No)

●	Duplicate Flag (Yes/No)

Actions:
●	Capture New Invoice

●	View/Edit (DRAFT/VALIDATED only)

●	Run Auto-Match

●	Send for Approval

●	Approve / Reject

●	Post to Finance (once approved)

________________________________________
B) Invoice Capture Form (Header)
Sections:
●	Invoice Details

○	Supplier (lookup)

○	Invoice Number

○	Invoice Date

○	Currency

○	Invoice Total

○	Tax Total

○	Source Method (Manual/OCR/Portal/EDI)

●	Reference

○	Link to PO(s)

○	Link to GRN(s) (optional)

○	Match Type (auto-suggested by config)

●	System Info

○	Invoice Status

○	Match Status

○	Duplicate Flag

○	Approval Required? (Yes/No)

________________________________________
C) Invoice Lines View
Columns:
●	Line No

●	Description

●	Item Code / SKU (if identified)

●	UOM

●	Qty Invoiced

●	Unit Price

●	Line Gross

●	Tax %

●	Tax Amount

●	Line Net

●	Matched PO/GRN reference indicator

Features:
●	Auto-suggestion of PO/GRN mapping based on:

○	Supplier, item, quantity, amount, period.

●	Manual line-to-PO/GRN linking when auto-match not possible.

________________________________________
D) Matching View (Core UX)
Dedicated pane/tab:
●	Show for each invoice line:

○	Invoice line values (qty, price, tax)

○	PO line reference:

■	Ordered Qty

■	PO Unit Price

○	GRN line reference:

■	Received Qty

■	Accepted Qty

○	QC Result (for 4-way)

●	Show variance:

○	Qty variance

○	Price variance

○	Tax variance

○	Within/Outside tolerance highlight

●	Actions per line:

○	Accept (within tolerance)

○	Flag as Exception (outside tolerance)

○	Override (if role allows; requires justification)

________________________________________
4.6.4 Validation Rules
Header-level:
●	Supplier + invoice_number combination must be unique (or flagged duplicate).

●	invoice_date must be <= posting date (if posting date used).

●	Total of invoice lines must reconcile with total_invoice_amount and total_tax_amount (allow small rounding difference config).

●	If matching model requires PO:

○	At least one PO is linked or resolvable.

●	If matching model requires GRN:

○	At least one GRN is linked or resolvable.

Line-level:
●	qty_invoiced > 0.

●	If mapped to PO line:

○	qty_invoiced + already_invoiced_qty <= accepted_qty_from_grn * (1 + qty_tolerance_percent).

●	If mapped to GRN line:

○	Finance should not invoice beyond accepted quantity.

●	Price variance vs PO:

○	If beyond tolerance, line flagged as exception; invoice cannot move to MATCHED until resolved.

Matching/Status-level:
●	Invoice cannot be set to MATCHED unless:

○	All lines are either:

■	Matched within tolerance, or

■	Exception is flagged and routed for approval.

●	Cannot POST to Finance unless:

○	Status is APPROVED.

________________________________________
4.6.5 Workflow
Default:
●	DRAFT
 → Validate (auto-match attempt) → VALIDATED
 → If fully matched within tolerance → MATCHED → APPROVAL_PENDING → APPROVED → POSTED

Exception path:
●	VALIDATED → match variance outside tolerance → EXCEPTION
 → Send to approver → APPROVAL_PENDING → APPROVED or REJECTED
 → If approved, can still be POSTED with variances documented.

Rejection path:
●	EXCEPTION / APPROVAL_PENDING → REJECTED (if invoice is disputed with supplier)

Cancellation:
●	DRAFT / VALIDATED → CANCELLED (if captured incorrectly or voided)

________________________________________
4.6.6 Module Metadata & Build Steps
Module Metadata
module_type: transaction
complexity: medium_to_complex

template_ref: _txn_03

extension_allowed: true

depends_on:
  - Company
  - Suppliers
  - Purchase Order (4.3)
  - GRN & QC (4.5)
  - QC Rules (for 4-way)
  - Finance/AP (for posting)
  - Users / Roles
  - Tolerance & Matching Config

used_by:
  - Payments & Settlement (4.8)
  - Vendor Performance (4.9)
  - Tax & Compliance Reporting

________________________________________
Build Steps (for AI / Implementation Engine)
You are building a Medium-to-Complex Transaction module for a Retail ERP.

Module: Supplier Invoice Matching (3-way / 4-way)
Template: _txn_03

Requirements:

1) Backend (Django + DRF):

   Models:
   - supplier_invoice (header)
   - supplier_invoice_line (lines)
   - supplier_invoice_match_detail (matching details)

   Serializers:
   - Invoice header with nested lines.
   - Matching detail serializer.

   Viewsets & Endpoints:
   - Capture invoice (CRUD while in DRAFT).
   - Auto-match endpoint:
     - Tries to match lines to PO/GRN/QC using configured rules.
   - Manual match endpoint:
     - For user-driven mapping.
   - Workflow:
     - validate_invoice
     - mark_matched
     - send_for_approval
     - approve_invoice
     - reject_invoice
     - post_invoice (integration handoff to Finance/AP).

   Business Rules:
   - Enforce uniqueness and tolerance rules.
   - Keep aggregated match_variance_amount up to date.
   - Respect configuration for match type and tolerance per category.

2) Frontend (React + Vite + Tailwind):

   Screens:
   - Invoice List (filters, status indicators).
   - Invoice Capture/Edit:
     - Header + lines + basic references.
   - Matching View:
     - Side-by-side comparison of invoice vs PO vs GRN (+ QC).

   Behavior:
   - Display clear variance warnings.
   - Block approval/posting when rules are violated.
   - Support inline justification capture for overrides.

3) Integration:

   - Upstream:
     - Fetch POs and GRNs for supplier and date window.
   - Downstream:
     - Expose approved, matched invoices to Payments module (4.8).
     - Provide variance data to Vendor Performance (4.9).

4) Security & Roles:

   - Roles:
     - Invoice Capturer
     - Invoice Matcher / Analyst
     - Invoice Approver
     - Finance Poster

Ensure full fidelity with the data, workflow, and validation rules
defined in the Supplier Invoice Matching specification.

________________________________________
4.7 Supplier Returns (RTO – Return to Origin)
Template Ref: _txn_03 (Medium Transaction)
4.7.1 Business Purpose
Supplier Returns (RTO) handles returning goods back to the supplier after they have been received, due to:
●	Quality failures

●	Damages

●	Wrong items / over-delivery

●	Near-expiry or regulatory non-compliance

Goals:
●	Adjust inventory out of stock back to supplier-return pipeline.

●	Provide a formal Supplier Return Note / Debit Note basis:

○	For financial credit

○	For replacement shipments

●	Feed back into:

○	Vendor performance (defect rate, damage rate)

○	Dispute resolution and claims workflow.

Hybrid behavior (config-driven):
●	Returns can be:

○	Immediate at dock (during GRN) or

○	Post-GRN (identified later during put-away or sales).

●	May require:

○	Approval before creating return.

○	Automatic Debit Note generation.

________________________________________
4.7.2 Data Model
A) Supplier Return Header (supplier_return_note)
Field	Type	Required	Description
id	UUID	Yes	Primary key
company_id	FK	Yes	Company scope
return_number	String(30)	Yes	Human-readable return reference
return_status	Enum	Yes	DRAFT, PENDING_APPROVAL, APPROVED, DISPATCHED, CLOSED, CANCELLED
supplier_id	FK (Supplier)	Yes	Supplier to whom stock is returned
originating_location_id	FK (Location)	Yes	Store/Warehouse returning goods
linked_po_id	FK (PO Header)	No	If known
linked_grn_id	FK (GRN Header)	No	Usually required for stock traceability
return_reason_category	Enum	Yes	QUALITY_FAILURE, DAMAGE, WRONG_ITEM, EXCESS_SUPPLY, OTHERS
reference_document_number	String(50)	No	Could be complaint ref, QC ref, claim ID
remarks_internal	Text	No	Internal remarks (not sent to supplier)
remarks_to_supplier	Text	No	Message printed on return note
approval_required	Boolean	Yes	Controlled by config (value/qty)
approved_by_user_id	FK (User)	No	Approver for return
approved_at	DateTime	No	Approval timestamp
dispatch_date	Date	No	Date goods physically shipped back
carrier_name	String(100)	No	Transporter name for return
vehicle_number	String(50)	No	Vehicle/regn number
return_debit_note_number	String(50)	No	Financial debit note reference (if created)
created_by_user_id	FK (User)	Yes	Who created return
created_at	DateTime	Auto	
updated_at	DateTime	Auto	
________________________________________
B) Supplier Return Line (supplier_return_note_line)
Each line represents quantity being returned against specific GRN/PO line.
Field	Type	Required	Description
id	UUID	Yes	Primary key
supplier_return_note_id	FK (Return Header)	Yes	Header ref
goods_receipt_note_line_id	FK (GRN Line)	Yes	From which stock was originally received
purchase_order_line_id	FK (PO Line)	No	Optional if needed for financial link
item_id	FK (Item)	Yes	Item master
item_variant_id	FK (Item Variant)	Yes	SKU
uom_id	FK (UOM)	Yes	UOM
received_qty_from_grn	Decimal	Yes	Qty originally received on GRN line
already_returned_qty	Decimal	Yes	Qty previously returned from this GRN line
return_qty	Decimal	Yes	Qty being returned now
batch_number	String(50)	No	Batch/lot (copied from GRN)
expiry_date	Date	No	Same or updated expiry
serial_numbers_blob	Text	No	JSON/comma-separated serial numbers
reason_code	String(50)	Yes	Detailed reason (e.g., DAMAGE_TRANSIT, WRONG_BARCODE)
line_remarks	Text	No	Additional info
line_status	Enum	Yes	PENDING, DISPATCHED, CLOSED, CANCELLED
expected_credit_amount	Decimal	No	Estimated value to be recovered from supplier
final_credit_amount	Decimal	No	Actual credit note amount (once known)
________________________________________
C) Config / Control (Conceptual)
●	return_requires_grn (true/false; usually true)

●	return_approval_threshold_amount

●	return_allowed_time_window_days (e.g., cannot return after X days from GRN)

●	auto_generate_debit_note (Yes/No; integration with Finance)

●	return_affects_vendor_score (Yes/No; weight in vendor performance)

________________________________________
4.7.3 UI / UX Requirements
Screen Name: Supplier Returns (RTO)
 Path: Procurement / Inventory → Outbound → Supplier Returns
________________________________________
A) Supplier Return List
Columns:
●	Return Number

●	Supplier

●	Originating Location

●	Linked GRN Number

●	Return Reason Category

●	Status

●	Dispatch Date

●	Created By / Approved By

Filters:
●	Date range (Created, Dispatch)

●	Supplier

●	Location

●	Status

●	Reason Category

Actions:
●	Create Return

●	View/Edit (DRAFT / PENDING_APPROVAL)

●	Approve / Reject

●	Mark as Dispatched

●	Close (when financial reconciliation done)

●	Cancel (with reason)

________________________________________
B) Supplier Return Header Form
Sections:
●	General

○	Return Number (auto)

○	Supplier

○	Originating Location

○	Return Reason Category

○	Linked GRN

○	Linked PO (optional)

○	Reference Document (complaint, QC ticket, etc.)

○	Remarks (internal & supplier-facing)

●	Logistics

○	Dispatch Date

○	Carrier

○	Vehicle Number

●	Financial

○	Expected Debit Note No. (if pre-planned)

○	Final Debit Note (once issued by Finance/AP)

________________________________________
C) Supplier Return Lines Grid
Columns:
●	Item Code / Name

●	SKU

●	UOM

●	GRN Number / GRN Line

●	Received Qty (from GRN)

●	Already Returned Qty

●	Return Qty (input)

●	Batch / Expiry

●	Reason Code

●	Expected Credit Amount

●	Line Status

Features:
●	Add lines by:

○	Selecting from GRN lines (filter by supplier/location/date).

●	Show warning when:

○	already_returned_qty + return_qty > received_qty.

●	For batch/serial items:

○	Allow selection of specific serials or batch segments.

________________________________________
4.7.4 Validation Rules
Header-level:
●	return_number unique per company.

●	supplier_id must match supplier of linked GRN/PO.

●	originating_location_id must match receiving location of GRN (unless cross-org allowed by config).

●	If return_requires_grn = true:

○	At least one linked_grn_id and GRN lines on return.

Line-level:
●	return_qty > 0.

●	already_returned_qty + return_qty <= received_qty_from_grn.

●	For batch-managed items:

○	batch_number required.

●	If return_allowed_time_window_days specified:

○	Check GRN date vs current date; prevent or require override beyond allowed window.

Approval:
●	If total expected_credit_amount > return_approval_threshold_amount:

○	Set approval_required = true.

○	Cannot dispatch until approved.

Status/Workflow:
●	Cannot mark return DISPATCHED:

○	If any line has invalid quantity.

○	If approval_required and not approved.

●	Cannot close return:

○	Until financial side processed (either automatically or via manual confirmation).

________________________________________
4.7.5 Workflow
Standard:
●	DRAFT
 → Submit → PENDING_APPROVAL (if approval_required)
 → Approve → APPROVED
 → Dispatch → DISPATCHED
 → Close (once credit note processed / resolved) → CLOSED

Alternative:
●	If no approval required:

○	DRAFT → APPROVED directly on submit.

Cancellation:
●	DRAFT / PENDING_APPROVAL / APPROVED → CANCELLED (with reason).

●	After DISPATCHED, cancellation path depends on config and may require reverse movement.

Inventory integration:
●	On DISPATCH:

○	Inventory movement event to reduce stock at originating location.

○	Potential movement to “In-Transit to Supplier” virtual location.

Finance integration:
●	On CLOSED:

○	Ensure debit note/credit is linked against supplier account.

Vendor performance:
●	Each return line contributes to:

○	Damage rate

○	Wrong shipment rate

○	Quality failure metrics.

________________________________________
4.7.6 Module Metadata & Build Steps
Module Metadata
module_type: transaction
complexity: medium

template_ref: _txn_03

extension_allowed: true

depends_on:
  - Company
  - Locations
  - Suppliers
  - GRN & QC (4.5)
  - Purchase Order (4.3) [optional]
  - Inventory Movement Engine
  - Users / Roles
  - Return / Claims Configuration

used_by:
  - Vendor Performance & Compliance (4.9)
  - Inventory Valuation & Stock Adjustments
  - Dispute & Claims Management

________________________________________
Build Steps (for AI / Implementation Engine)
You are building a Medium Transaction module for a Retail ERP.

Module: Supplier Returns (RTO)
Template: _txn_03

Requirements:

1) Backend (Django + DRF):

   Models:
   - supplier_return_note (header)
   - supplier_return_note_line (lines)

   Serializers:
   - Header with nested lines.
   - List serializer for returns.

   Viewsets & Endpoints:
   - CRUD while in DRAFT.
   - Workflow actions:
     - submit_return
     - approve_return
     - reject_return
     - dispatch_return
     - close_return
     - cancel_return

   Business Rules:
   - Enforce quantity validations against GRN lines.
   - Enforce approval and time-window rules.
   - Trigger inventory movement events at dispatch.

2) Frontend (React + Vite + Tailwind):

   Screens:
   - Return List view with filters and status.
   - Return Edit:
     - Header (supplier, location, reasons).
     - Lines grid (select from GRN lines).
     - Logistics info (dispatch details).
   - Approval View with summary of returned amounts.

   Behavior:
   - Block dispatch if not approved where required.
   - Show warnings for over-return or old GRNs.

3) Integration:

   - Upstream:
     - GRN and PO lines as source for return.
   - Downstream:
     - Provide return info to Finance for debit note creation.
     - Feed into Vendor Performance (4.9).
     - Adjust inventory via stock movement.

4) Security & Roles:

   - Return Creator
   - Return Approver
   - Return Dispatcher
   - Return Viewer

Ensure conformance with the data model, workflow, and validation
rules defined in the Supplier Returns specification.

4.8 Payments & Settlement
Template Ref: _txn_03 (Medium/Complex Transaction)
4.8.1 Business Purpose
The Payments & Settlement module manages how approved supplier invoices are converted into actual payments, including:
●	Standard invoice payments

●	Part-payments and adjustments

●	Early payment discounts

●	Retentions and milestone payments

●	Settlements against debit notes or credit notes

Goals:
●	Ensure only approved, matched invoices (from 4.6) are paid.

●	Optimize cash flow and working capital via:

○	Payment scheduling

○	Discount programs

○	Prioritization rules.

●	Maintain a clear audit trail:

○	What invoice was paid?

○	When?

○	From which bank account?

●	Support different payment modes:

○	Bank transfer (NEFT/RTGS/ACH/SWIFT)

○	Cheque

○	Manual settlements (offline).

Hybrid behavior (config-driven):
●	Payments can be processed:

○	Per invoice (single-payment mode)

○	Via Payment Runs/Batches (group payments by date/supplier/bank).

●	Settlement model can:

○	Auto-apply credit notes and debit notes.

○	Support partial payments and multi-invoice settlement for a single payment.

________________________________________
4.8.2 Data Model
A) Payment Batch Header (supplier_payment_batch)
Represents one logical “payment run” (e.g., weekly payment cycle).
Field	Type	Required	Description
id	UUID	Yes	Primary key
company_id	FK	Yes	Company scope
batch_number	String(30)	Yes	Payment batch ID
batch_status	Enum	Yes	DRAFT, READY_FOR_REVIEW, APPROVAL_PENDING, APPROVED, EXECUTED, PARTIALLY_EXECUTED, CANCELLED
batch_date	Date	Yes	Logical batch/run date
payment_date	Date	No	Intended payment date
bank_account_id	FK (Bank Account)	Yes	Bank account used for this run
total_batch_amount	Decimal	Yes	Sum of planned payments in batch
currency_code	String(10)	Yes	Currency (usually company base)
created_by_user_id	FK (User)	Yes	Creator
reviewed_by_user_id	FK (User)	No	Optional reviewer before approval
approved_by_user_id	FK (User)	No	Approver for payment run
approved_at	DateTime	No	Approval timestamp
executed_by_user_id	FK (User)	No	Who triggered actual payment file/API
executed_at	DateTime	No	Execution timestamp
remarks_internal	Text	No	Internal notes for AP/Finance
created_at	DateTime	Auto	
updated_at	DateTime	Auto	
________________________________________
B) Supplier Payment (supplier_payment)
Represents one supplier-level payment instruction, possibly covering multiple invoices.
Field	Type	Required	Description
id	UUID	Yes	Primary key
supplier_payment_batch_id	FK (Payment Batch)	No	Optional; may also support ad-hoc payment (no batch)
company_id	FK	Yes	Company scope
supplier_id	FK (Supplier)	Yes	Supplier being paid
payment_reference_number	String(50)	Yes	Internal payment ref (can store bank UTR later)
payment_status	Enum	Yes	PLANNED, PENDING_EXECUTION, EXECUTED, FAILED, CANCELLED
payment_mode	Enum	Yes	BANK_TRANSFER, CHEQUE, MANUAL_SETTLEMENT, OTHER
bank_account_id	FK (Bank Account)	Yes	From which account money goes out
payment_currency_code	String(10)	Yes	Currency used
payment_amount	Decimal	Yes	Total amount paid to supplier
early_payment_discount_taken	Decimal	Yes	Total discount benefit taken (if any)
FX_rate_applied	Decimal	No	For foreign currency payments
payment_execution_ref	String(100)	No	UTR/transaction ID from bank
payment_value_date	Date	No	Actual settlement date at bank
remarks_internal	Text	No	Internal notes on payment
created_by_user_id	FK (User)	Yes	Creator
executed_by_user_id	FK (User)	No	Execution user
created_at	DateTime	Auto	
updated_at	DateTime	Auto	
________________________________________
C) Payment–Invoice Link (supplier_payment_invoice_link)
Connects payments to invoices and credit/debit notes.
Field	Type	Required	Description
id	UUID	Yes	Primary key
supplier_payment_id	FK (Supplier Payment)	Yes	Payment header
supplier_invoice_id	FK (Supplier Invoice)	Yes	Invoice settled (4.6)
gross_invoice_amount	Decimal	Yes	Original invoice value
credit_notes_adjusted_amount	Decimal	Yes	Total credit applied against this invoice
discount_taken_amount	Decimal	Yes	Early payment or other discount
net_payable_amount	Decimal	Yes	Net payable after above adjustments
amount_paid	Decimal	Yes	Actual paid amount (can be partial)
remaining_balance_after_payment	Decimal	Yes	Outstanding after this payment
settlement_type	Enum	Yes	FULL, PARTIAL, ADVANCE, FINAL
Note: Credit/debit notes may be modeled as special supplier_invoice entries or separate financial documents; this link handles netting logic conceptually.
________________________________________
D) Config / Control (Conceptual)
●	auto_select_invoices_due_within_days (e.g. 7 days)

●	payment_run_requires_approval (Yes/No; possibly threshold-based)

●	min_discount_percent_to_take_early_payment (e.g. >1% only)

●	max_invoices_per_payment (for UI constraints)

●	block_payment_if_invoice_status != APPROVED (true/false)

●	partial_payment_allowed (Yes/No; and when)

________________________________________
4.8.3 UI / UX Requirements
Screen Name(s):
●	Payment Run / Batch

●	Supplier Payments

Path: Finance / AP → Payments & Settlement
________________________________________
A) Payment Batch List
Columns:
●	Batch Number

●	Batch Date

●	Payment Date (planned/executed)

●	Bank Account

●	Total Amount

●	Status

●	Created By / Approved By / Executed By

Filters:
●	Date range

●	Status

●	Bank account

●	Created By / Approved By

Actions:
●	Create New Batch

●	View/Edit Batch

●	Submit for Approval

●	Approve Batch

●	Execute Batch (export bank file / trigger API)

●	Cancel Batch (if not executed)

________________________________________
B) Payment Batch Detail
Sections:
●	Header

○	Batch No, Date

○	Bank Account

○	Payment Date

○	Status

○	Remarks

●	Invoice Selection Panel

○	Filter invoices by:

■	Supplier

■	Due date range

■	Status = APPROVED

■	With/without discount eligibility

○	Multi-select invoices.

●	Selected Payments Grid

○	Supplier

○	Invoice Number

○	Invoice Date

○	Invoice Amount

○	Due Date

○	Suggested Payment Amount

○	Discount available? (Yes/No, discount amount)

○	Discount taken (checkbox or amount)

○	Net Payable

○	Included in Batch? (flag)

Totals section:
●	Sum of all net payable by supplier

●	Sum of batch total

________________________________________
C) Supplier Payment View
For each supplier_payment:
●	Supplier details (name, ID, bank info).

●	Payment amount and mode.

●	Linked invoices:

○	Invoice No, Amount, Paid Amount, Remaining Balance.

Actions:
●	Mark as Executed (if not using automatic bank integration).

●	Edit remarks.

●	View payment advice.

________________________________________
D) Payment Advice / Supplier Communication
Generate and store:
●	Payment Advice PDF / Email with:

○	Paid invoices list

○	Amounts

○	Any deductions (discounts, returns, debit notes)

○	Payment reference (UTR, cheque no, etc.)

________________________________________
4.8.4 Validation Rules
Header-level (Batch):
●	batch_number unique per company.

●	bank_account_id required.

●	payment_date cannot be in the past (or allowed with warning, per config).

●	Batch cannot move to APPROVAL_PENDING or APPROVED:

○	If no supplier_payment entries exist.

○	If any linked invoices are no longer in APPROVED status.

Supplier Payment-level:
●	payment_amount > 0.

●	payment_currency_code consistent with invoice or properly converted (FX handled upstream or by Finance).

●	For each linked invoice:

○	amount_paid ≤ net_payable_amount.

●	If partial_payment_allowed = false:

○	amount_paid must equal net_payable_amount (for full settlement).

Posting/Execution:
●	Cannot EXECUTE payment:

○	If batch/individual payment not APPROVED (where approval_required = true).

●	Cannot mark payment as EXECUTED twice.

________________________________________
4.8.5 Workflow
Batch-level:
●	DRAFT
 → Review → READY_FOR_REVIEW (optional intermediate)
 → Submit for Approval → APPROVAL_PENDING
 → Approve → APPROVED
 → Execute (bank file/API or manual) → EXECUTED

Alternative:
●	DRAFT → CANCELLED

●	APPROVAL_PENDING → REJECTED (and optionally back to DRAFT)

Supplier Payment-level:
●	PLANNED → PENDING_EXECUTION (once batch is approved)

●	PENDING_EXECUTION → EXECUTED (on confirm/payment file success)

●	PENDING_EXECUTION → FAILED (if bank rejects; can be retried or cancelled)

Integration with 4.6 Supplier Invoice:
●	Once payment is executed:

○	Update invoice’s paid amount and outstanding.

○	If fully paid:

■	Invoice status may move to PAID.

●	Retention and milestone scenarios:

○	Only portion of invoice may be included in payment.

○	Remaining becomes future liability.

________________________________________
4.8.6 Module Metadata & Build Steps
Module Metadata
module_type: transaction
complexity: medium_to_complex

template_ref: _txn_03

extension_allowed: true

depends_on:
  - Company
  - Suppliers
  - Supplier Invoice Matching (4.6)
  - Bank Accounts / Treasury
  - Users / Roles
  - Payment Configuration (tolerances, approval rules)

used_by:
  - Vendor Performance (4.9) - for payment behavior metrics
  - Cash Flow & Treasury Planning
  - Financial Ledger / AP

________________________________________
Build Steps (for AI / Implementation Engine)
You are building a Medium-to-Complex Transaction module for a Retail ERP.

Module: Payments & Settlement
Template: _txn_03

Requirements:

1) Backend (Django + DRF):

   Models:
   - supplier_payment_batch
   - supplier_payment
   - supplier_payment_invoice_link

   Serializers:
   - Batch with nested supplier_payment and rollup amounts.
   - Payment with nested invoice links.

   Viewsets & Endpoints:
   - CRUD for payment batches (up to APPROVAL_PENDING).
   - Actions:
     - submit_batch_for_approval
     - approve_batch
     - reject_batch
     - execute_batch
   - For individual payments:
     - create_ad_hoc_payment (optional)
     - mark_payment_executed
     - mark_payment_failed

   Integration:
   - Query `supplier_invoice` records with status `APPROVED` and not fully paid.
   - Update invoices’ paid/outstanding amounts.
   - Provide hooks to generate:
     - Bank files (e.g., CSV, XML, etc.)
     - Payment advice export.

2) Frontend (React + Vite + Tailwind):

   Screens:
   - Payment Batch List
   - Payment Batch Detail:
     - Header + invoice selection + payment summary.
   - Payment Detail:
     - View supplier payment with linked invoices.

   Behavior:
   - Respect status-based edit locks.
   - Clearly highlight discount-taking options and net payable amounts.

3) Security & Roles:

   - Roles:
     - Payment Batch Creator
     - Payment Approver
     - Payment Executor
     - Payment Viewer

Ensure all validation and workflows conform to the spec above.

________________________________________
4.9 Vendor Performance & Compliance
Template Ref: _analytic_01 (Analytical / Composite Module)
4.9.1 Business Purpose
The Vendor Performance & Compliance module aggregates data across the entire Source-to-Pay cycle to provide:
●	Performance scoring on:

○	Cost

○	Quality

○	Delivery

○	Billing accuracy

○	Service responsiveness

●	Compliance monitoring on:

○	Legal/tax documents (GST, registrations, certificates)

○	Contract adherence

○	Audit flags

●	Actionable insights:

○	Preferred supplier ranking

○	Watchlist and blacklist candidates

○	Supplier improvement programs

Goals:
●	Move from transactional procurement to data-driven supplier management.

●	Provide objective metrics for:

○	Allocation of spend

○	Contract renewal/termination

○	Negotiation leverage

○	Risk mitigation.

________________________________________
4.9.2 Conceptual Data Model
This module is primarily analytical and read-heavy, but we define a staging layer for snapshots and events.
A) Vendor Performance Snapshot (vendor_performance_snapshot)
Aggregated by Vendor + Period (e.g., month/quarter).
Field	Type	Required	Description
id	UUID	Yes	Primary key
company_id	FK	Yes	Company scope
supplier_id	FK (Supplier)	Yes	Vendor
period_start_date	Date	Yes	Period start (e.g., 1st of month)
period_end_date	Date	Yes	Period end
total_pos_value	Decimal	Yes	PO value issued during period
total_grn_value	Decimal	Yes	Accepted GRN value
total_returns_value	Decimal	Yes	Value of supplier returns (RTO)
total_invoices_value	Decimal	Yes	Invoiced amount
total_disputes_count	Integer	Yes	Billing or quality disputes
late_delivery_count	Integer	Yes	Deliveries beyond SLA
on_time_delivery_percent	Decimal	Yes	Calculated OTIF/OTD metric
qc_fail_count	Integer	Yes	Lines failed QC
qc_fail_percent	Decimal	Yes	QC fail % of total inspected lines
invoice_mismatch_count	Integer	Yes	Invoices with variance/exceptions
avg_invoice_match_variance	Decimal	Yes	Avg variance amount per exception invoice
avg_payment_delay_days	Decimal	No	From invoice due date vs actual payment (optional two-way metric)
vendor_rating_cost	Decimal	Yes	Sub-score 0–100
vendor_rating_quality	Decimal	Yes	Sub-score 0–100
vendor_rating_delivery	Decimal	Yes	Sub-score 0–100
vendor_rating_compliance	Decimal	Yes	Sub-score 0–100
vendor_rating_service	Decimal	Yes	Sub-score 0–100
vendor_overall_score	Decimal	Yes	Weighted combined score 0–100
performance_band	Enum	Yes	ELITE, APPROVED, CONDITIONAL, UNDER_WATCH, BLOCKED_CANDIDATE
notes_internal	Text	No	Comments from procurement for that period
created_at	DateTime	Auto	Snapshot creation time
Snapshots may be generated monthly/quarterly by a scheduled job, not necessarily via UI transaction.
________________________________________
B) Vendor Compliance Record (vendor_compliance_record)
Captures regulatory and contractual compliance events.
Field	Type	Required	Description
id	UUID	Yes	Primary key
company_id	FK	Yes	Company scope
supplier_id	FK (Supplier)	Yes	Vendor
compliance_type	Enum	Yes	GST_REG, ISO_CERT, FOOD_SAFETY, ESG, CONTRACT_SLA, OTHERS
document_reference	String(100)	No	Certificate/contract reference
valid_from_date	Date	No	Valid from (if applicable)
valid_to_date	Date	No	Valid to (if applicable)
last_verified_at	DateTime	No	Last verification timestamp
last_verified_by_user_id	FK (User)	No	Who verified compliance
compliance_status	Enum	Yes	VALID, EXPIRED, PENDING_VERIFICATION, REVOKED
risk_level	Enum	Yes	LOW, MEDIUM, HIGH, CRITICAL
remarks	Text	No	Notes
________________________________________
C) Vendor Performance Event (Conceptual) (vendor_performance_event)
Optional but useful per incident basis, e.g.:
●	Late delivery

●	QC fail

●	Invoice mismatch

●	Return to supplier

Field	Type	Required	Description
id	UUID	Yes	Primary key
company_id	FK	Yes	Company
supplier_id	FK (Supplier)	Yes	Vendor
event_type	Enum	Yes	DELIVERY_LATE, QC_FAIL, RETURN, INVOICE_DISPUTE, PAYMENT_DELAY, etc.
reference_module	String(50)	Yes	PO, GRN, INVOICE, RETURN, PAYMENT, etc.
reference_id	UUID	Yes	ID of transaction (PO/GRN/invoice/return)
event_date	DateTime	Yes	When event occurred
value_impact	Decimal	No	Monetary impact (if applicable)
severity	Enum	Yes	LOW, MEDIUM, HIGH, CRITICAL
notes	Text	No	Additional context
This can be populated automatically from 4.3–4.8 processes.
________________________________________
D) Config / Control (Conceptual)
●	vendor_scoring_weights per dimension:

○	cost, quality, delivery, compliance, service.

●	vendor_elite_threshold_score (e.g., >90).

●	vendor_approved_threshold_score (e.g., >75).

●	Rules for:

○	When to flag vendor as UNDER_WATCH.

○	When to recommend blocklist.

●	vendor_review_frequency (e.g., monthly/quarterly/annually).

________________________________________
4.9.3 UI / UX Requirements
Screen Name(s):
●	Vendor Performance Dashboard

●	Vendor Scorecard

●	Vendor Compliance Monitor

Path: Procurement → Vendor Management → Performance & Compliance
________________________________________
A) Vendor Performance Dashboard
Views:
●	Summary Widgets:

○	No. of Active Vendors

○	No. of Elite / Approved / Under Watch / Blocked candidates

○	Spend by Vendor Tier

●	Top Vendors:

○	By spend

○	By score

●	Risk Overview:

○	Vendors with high return rate

○	Vendors with high QC failure

Filters:
●	Time range (period)

●	Category (e.g., FMCG, Electronics, Capex, Services)

●	Region / Location

●	Vendor tier/band

________________________________________
B) Vendor Scorecard (Per Vendor)
Sections:
●	Header

○	Vendor name, code

○	Primary contact

○	Category tags

○	Overall score + band (Elite/Approved/etc.)

●	KPIs & Metrics

○	Cost:

■	Price competitiveness vs category average

○	Delivery:

■	OTIF / on-time delivery %

■	Late delivery count

○	Quality:

■	QC failure %

■	Return rate as % of delivered value

○	Billing:

■	Invoice mismatch count

■	Typical variance magnitude

○	Payments (from vendor perspective):

■	Average payment delay (optional fairness metric)

●	Trend Charts

○	Score over time (line chart)

○	QC fail % over time

○	Returns value over time

●	Events Timeline

○	Significant events (major rejection, escalated disputes, compliance expiry).

________________________________________
C) Vendor Compliance View
Per vendor view:
●	List of all vendor_compliance_record entries:

○	Compliance type

○	Valid from/to

○	Status (valid/expired/pending)

○	Risk level

●	Alerts:

○	Upcoming expiring certifications (within X days)

○	Already expired docs.

Global compliance board:
●	Vendors with critical compliance issues.

●	Quick actions:

○	Open vendor master

○	Notify responsible buyer/compliance manager (conceptually).

________________________________________
4.9.4 Scoring & Business Rules
Scoring model:
For each vendor & period:
●	vendor_rating_cost (0–100)

●	vendor_rating_quality

●	vendor_rating_delivery

●	vendor_rating_compliance

●	vendor_rating_service

Each rating computed from associated metrics, e.g.:
●	Delivery:

○	If OTIF ≥ 95% → 90+ score.

○	If OTIF between 80–95% → 70–90.

○	If OTIF < 80% → penalized heavily.

●	Quality:

○	Based on QC failure rate and return rate.

●	Billing:

○	Invoice dispute frequency & variance.

Overall score:
vendor_overall_score =
   cost_weight           * vendor_rating_cost
 + quality_weight        * vendor_rating_quality
 + delivery_weight       * vendor_rating_delivery
 + compliance_weight     * vendor_rating_compliance
 + service_weight        * vendor_rating_service

Classification:
●	ELITE → score ≥ 90

●	APPROVED → 75 ≤ score < 90

●	CONDITIONAL → 60 ≤ score < 75

●	UNDER_WATCH → 40 ≤ score < 60

●	BLOCKED_CANDIDATE → score < 40 or critical compliance failures

Exact weight and threshold values are configurable.
________________________________________
4.9.5 Workflow (Analytical & Governance)
This module is mostly batch/scheduled job driven:
1.	Periodic Performance Job (e.g., monthly):

○	Aggregate data from:

■	POs (4.3)

■	GRNs + QC (4.5)

■	Invoice Matching (4.6)

■	Returns (4.7)

■	Payments (4.8)

○	Compute metrics & scores.

○	Insert or update vendor_performance_snapshot.

2.	Compliance Monitoring Job:

○	Evaluate vendor_compliance_record:

■	Detect expired or soon-to-expire records.

○	Raise alerts and update statuses.

3.	Governance Actions:

○	Procurement Head can:

■	Mark vendor as “Do Not Use / Blocked Candidate”.

■	Put vendor “Under Watch”.

■	Approve vendor improvement plan.

________________________________________
4.9.6 Module Metadata & Build Steps
Module Metadata
module_type: analytics
complexity: medium_to_complex

template_ref: _analytic_01

extension_allowed: true

depends_on:
  - Suppliers
  - RFQ (4.2)
  - Purchase Order (4.3)
  - GRN & QC (4.5)
  - Invoice Matching (4.6)
  - Supplier Returns (4.7)
  - Payments & Settlement (4.8)
  - Compliance Master / Documents
  - Users / Roles

used_by:
  - Strategic Sourcing
  - Category Management
  - Risk & Compliance
  - Vendor Onboarding / Offboarding Decisions

________________________________________
Build Steps (for AI / Implementation Engine)
You are building an Analytical/Composite module for a Retail ERP.

Module: Vendor Performance & Compliance
Template: _analytic_01

Requirements:

1) Backend (Django + DRF):

   Models:
   - vendor_performance_snapshot
   - vendor_compliance_record
   - (optional) vendor_performance_event

   Services / Jobs:
   - Periodic job to aggregate KPIs and compute scores per vendor + period.
   - Job to scan and update compliance statuses (valid/expired/etc.).

   APIs:
   - Get vendor performance snapshot list (with filters).
   - Get detailed scorecard for a specific vendor.
   - Get compliance records and alerts.

2) Frontend (React + Vite + Tailwind):

   Screens:
   - Vendor Performance Dashboard.
   - Vendor Scorecard:
     - KPIs, charts, events timeline.
   - Compliance Board:
     - Expiring/expired compliance docs.
     - Vendor risk summary.

   Behavior:
   - Interactive filters by period/category/location.
   - Drill-down from dashboard to vendor-level detail.

3) Integration:

   - Read-only integration from transactional modules (4.2–4.8).
   - Optional feedback loop to:
     - Vendor master (flagging under-watch/blocked).
     - RFQ and PO (e.g., prevent awarding to blocked vendors).

4) Security & Roles:

   - Roles:
     - Procurement Analyst
     - Category Manager
     - Procurement Head
     - Compliance Officer (read/write on compliance records)

Ensure that the aggregation logic and KPIs remain consistent with
metrics described in the Vendor Performance & Compliance specification.


4.1 PR → 4.2 RFQ → 4.3 PO → 4.4 ASN → 4.5 GRN+QC → 4.6 Invoice Matching → 4.7 Supplier Returns → 4.8 Payments → 4.9 Vendor Performance & Compliance → 4.10 Config/Masters (which we already partly covered earlier).

4.10 Procurement Configuration & Master Data Governance

4.10 is really about
Think of 4.10 Procurement Configuration & Master Data Governance as:
“The control panel and rules layer that tells all the transaction modules in Section 4 how to behave.”
It does not introduce new core entities like Item or Supplier, but instead defines:
●	Which procurement steps are enabled/disabled

●	What is mandatory vs optional

●	Tolerances, thresholds, and rules used by:

○	4.1 PR

○	4.2 RFQ

○	4.3 PO

○	4.4 ASN

○	4.5 GRN + QC

○	4.6 Invoice Matching

○	4.7 Supplier Returns

○	4.8 Payments

In other words:
●	Your Masters (Supplier, Item, Location, etc.) = Who/What we buy from.

●	4.10 Config & Governance = How we run procurement (process, rules, flows).

So it centralizes all the config flags we’ve been referencing:
●	pr_enabled, pr_required_for_po

●	rfq_enabled, rfq_mandatory_threshold_amount

●	po_requires_pr, po_requires_rfq

●	asn_enabled, asn_mandatory_for_grn

●	over_receive_tolerance_percent, price_tolerance_percent

●	qc_required_by_category, expiry_must_be_at_least_x_days

●	invoice_matching_model

●	return_allowed_time_window_days

●	etc.

Rather than scattering them in multiple specs, 4.10:
●	Documents them in one place

●	Gives them a proper data model (config tables)

●	Ensures your ERP can behave as “simple retail” or “enterprise-grade” just by flipping config.

Template Ref: _cfg_01 (Configuration Module)
4.10.1 Business Purpose
The Procurement Configuration & Master Data Governance module defines how all procurement transactions (4.1–4.9) behave, without changing core masters (Supplier, Item, Location, etc.).
Goals:
●	Centralize process behavior and tolerance rules:

○	Which steps are active (PR, RFQ, ASN, etc.).

○	Which steps are mandatory or optional.

○	Matching & QC rules, approval thresholds.

●	Allow the same product to serve:

○	Small retailers (direct PO, minimal controls).

○	Mid/Large enterprises (full PR–RFQ–PO–ASN–GRN–Invoice–Payment chain).

●	Provide governance over:

○	Who can change configuration.

○	Audit of when rules changed (and by whom).

This module does not introduce new core entity masters; it references and controls how existing masters and transactions are used.
________________________________________
4.10.2 Data Model (Conceptual Configuration Tables)
These are logical config entities; physical implementation can be SQL tables, JSON config, or a mix.
A) Procurement Process Settings (procurement_process_setting)
Controls step enablement and mandatory rules.
Field	Type	Required	Description
id	UUID	Yes	Primary key
company_id	FK	Yes	Company scope
location_id	FK (Location)	No	Optional override per location
category_code	String(50)	No	Optional override per category
pr_enabled	Boolean	Yes	Show/hide PR (4.1)
pr_required_for_po	Boolean	Yes	Hard rule: PO must reference PR?
pr_approval_required	Boolean	Yes	Approval workflow required for PR?
rfq_enabled	Boolean	Yes	RFQ (4.2) allowed?
rfq_mandatory_threshold	Decimal	No	Amount above which RFQ is mandatory
po_requires_pr	Boolean	Yes	PO must link PR in this context?
po_requires_rfq	Boolean	Yes	PO must link RFQ award in this context?
asn_enabled	Boolean	Yes	ASN (4.4) enabled?
asn_mandatory_for_grn	Boolean	Yes	GRN must come via ASN?
non_po_grn_allowed	Boolean	Yes	Allow GRN without PO (exceptions)?
created_at	DateTime	Auto	
updated_at	DateTime	Auto	
________________________________________
B) Tolerance Settings (procurement_tolerance_setting)
Numeric thresholds for matching & receiving.
Field	Type	Required	Description
id	UUID	Yes	Primary key
company_id	FK	Yes	Company scope
category_code	String(50)	No	Optional per category
over_receive_tolerance_percent	Decimal	No	Max GRN over PO qty (e.g., 5%)
qty_tolerance_percent_invoice	Decimal	No	Max qty over GRN accepted for invoicing
price_tolerance_percent	Decimal	No	Max price delta vs PO/RFQ
tax_tolerance_percent	Decimal	No	Max tax variance vs expected
amount_tolerance_absolute	Decimal	No	Absolute currency amount tolerance
return_allowed_time_window_days	Integer	No	Max days post-GRN to initiate supplier return
created_at	DateTime	Auto	
updated_at	DateTime	Auto	
________________________________________
C) Matching & QC Configuration (matching_qc_setting)
Controls matching logic (2/3/4-way) and QC requirements.
Field	Type	Required	Description
id	UUID	Yes	Primary key
company_id	FK	Yes	Company scope
category_code	String(50)	No	Category-specific
invoice_matching_model	Enum	Yes	TWO_WAY, THREE_WAY, FOUR_WAY
qc_required_by_default	Boolean	Yes	If QC is required for this category
block_grn_post_if_qc_pending	Boolean	Yes	Prevent posting GRN if QC not completed
expiry_min_days_remaining	Integer	No	Min days shelf-life at receipt
block_invoice_if_qc_failed	Boolean	Yes	Prevent matching invoice if QC failed
created_at	DateTime	Auto	
updated_at	DateTime	Auto	
________________________________________
D) Approval Matrix (procurement_approval_matrix)
Defines who approves which transaction at what threshold.
Field	Type	Required	Description
id	UUID	Yes	Primary key
company_id	FK	Yes	Company scope
module_code	Enum	Yes	PR, PO, RFQ_AWARD, INVOICE, PAYMENT_BATCH, RETURN
category_code	String(50)	No	Optional per category
min_amount	Decimal	Yes	Lower bound inclusive
max_amount	Decimal	Yes	Upper bound inclusive
approver_role_code	String(50)	Yes	Role (Proc Manager, Finance Head, etc.)
approval_level	Integer	Yes	1, 2, 3… for multi-level approval
sequential_approval_required	Boolean	Yes	Sequential vs parallel approvals
created_at	DateTime	Auto	
updated_at	DateTime	Auto	
________________________________________
E) Vendor & Item Governance (Pointers Only)
You already have Supplier, Item, Item Variant, UOM, etc. in v0.3.
 4.10 can store procurement-specific governance attributes without redefining those cores. These can be extensions or views:
Examples:
●	Vendor-level:

○	Allowed categories

○	Risk rating

○	Blocked_for_new_po (bool)

●	Item-level:

○	Default procurement type (Make/Buy/Drop-ship)

○	QC_required flag

○	Approved vendor list reference (linking to Supplier)

These can be implemented as:
●	Extensions to your existing item/supplier masters or

●	Separate mapping tables like item_procurement_profile, supplier_procurement_profile.

________________________________________
4.10.3 UI / UX Requirements
Screen Name: Procurement Configuration
 Path: Admin / Configuration → Procurement
A) Process Configuration Screen
Sections:
●	Grid by:

○	Company

○	Location

○	Category

Columns:
●	PR Enabled?

●	PR Required for PO?

●	RFQ Enabled?

●	RFQ Mandatory Threshold

●	ASN Enabled?

●	GRN Without PO Allowed?

●	Matching Model (2/3/4-way)

Actions:
●	Add new rule row

●	Override rule for specific location/category

●	View effective rule (resolved by priority: location > category > company)

________________________________________
B) Tolerances & Matching
Screen to define:
●	Over-receipt tolerance

●	Price/Tax tolerance

●	Return time window

UI:
●	Filter by category

●	Inline edit fields

●	Show where-used indicator (modules impacted).

________________________________________
C) Approval Matrix Maintenance
Screen for managing approval rules:
●	Filters:

○	Module (PR/PO/etc.)

○	Category

○	Role

●	Grid:

○	Module

○	Category

○	Min Amount

○	Max Amount

○	Approver Role

○	Level

○	Sequential? (Yes/No)

Approval view integration:
●	Approvers can see why they’re being asked to approve (which rule triggered).

________________________________________
4.10.4 Governance & Validation Rules
●	Changes to procurement configuration must:

○	Be restricted to config/admin roles.

○	Have full audit trail (who, what, when).

●	Rule resolution algorithm (conceptual):

○	For each transaction (PR/PO/RFQ/etc.), system determines:

■	Company

■	Location

■	Category

○	Then finds the most specific applicable config:

■	Location + Category

■	Location

■	Category

■	Company-level default

●	Prevent contradictory configs:

○	E.g., pr_enabled = false and pr_required_for_po = true for same scope.

●	Validate that:

○	Approval matrix covers required ranges (no gaps where approvals would be ambiguous).

________________________________________
4.10.5 Module Metadata & Build Steps
Module Metadata
module_type: configuration
complexity: medium

template_ref: _cfg_01

extension_allowed: true

depends_on:
  - Company
  - Locations
  - Categories
  - Suppliers
  - Items / Variants
  - Users / Roles

used_by:
  - PR (4.1)
  - RFQ (4.2)
  - PO (4.3)
  - ASN (4.4)
  - GRN & QC (4.5)
  - Invoice Matching (4.6)
  - Supplier Returns (4.7)
  - Payments & Settlement (4.8)
  - Vendor Performance (4.9)

________________________________________
Build Steps (for AI / Implementation Engine)
You are building a Configuration module for a Retail ERP.

Module: Procurement Configuration & Governance
Template: _cfg_01

Requirements:

1) Backend (Django + DRF):

   Models:
   - procurement_process_setting
   - procurement_tolerance_setting
   - matching_qc_setting
   - procurement_approval_matrix

   Services:
   - Rule resolution service:
     - Given (company, location, category, module), compute effective
       config and approval rules.
   - Audit logging for config changes.

   APIs:
   - CRUD for configuration models (restricted to admin roles).
   - Read-only "get effective settings" API consumed by transactional
     modules.

2) Frontend (React + Vite + Tailwind):

   Screens:
   - Process configuration maintenance.
   - Tolerance and matching settings.
   - Approval matrix.

   Behavior:
   - Prevent conflicting rule combinations.
   - Provide preview of "effective" rules for a sample scenario
     (company/location/category).

3) Security & Roles:

   - Restrict write access to configuration to:
     - System Admin
     - Procurement Admin
   - Transactional modules should only **read** from these settings.

Ensure no duplication of core masters (supplier/item), and treat
this module as the centralized control layer for Section 4
procurement behavior.


