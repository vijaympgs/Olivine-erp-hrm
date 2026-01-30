# POS Vertical: Pharmacy (Retail / Chain / Hospital)

**Reference**: GoFrugal, LS Pharma, Marg ERP  
**Parent**: [roadmap_pos.md](./roadmap_pos.md)

## 💊 Feature Checklist (Functional Specification)

### 1. Regulatory Compliance & Controls (India Focus)
- [ ] **Schedule H/H1/X Handling**:
  - Mandatory prompt for **Doctor Name**, **Registration No**, and **Patient Details**.
  - Restrict sale without these fields.
  - Auto-generation of Schedule H1 Register reports.
  - Doctor-wise and Drug-wise Schedule H1 reporting.
  - Monthly statutory export (PDF / Excel).
  - Immutable audit log for Schedule overrides (User, Date, Terminal).
- [ ] **Narcotics (NRx) Control**:
  - Strict audit trail for Psychotropic substances.
  - Manager Authorization override for high-risk drugs.
  - Dual authorization workflow (Cashier + Pharmacist/Manager).
  - Repeated purchase detection for same Patient / Doctor.
- [ ] **Expiry Management (Critical)**:
  - **FEFO (First Expiry First Out)**: System auto-picks the batch expiring earliest.
  - **Expiry Blocking**: Hard stop at POS if item is expired or within "Near Expiry" buffer (e.g., 30 days).
  - **Non-Returnable Logic**: Flag items that cannot be returned (Cold chain, cut strips).
  - Configurable near-expiry window (15 / 30 / 60 days).
  - Manager override with mandatory reason capture.
  - Near-expiry alerts and dashboard for store managers.

### 2. Intelligent Search & Substitution
- [ ] **Search by Content (Salt/Composition)**:
  - Search "Paracetamol 500mg" -> Lists Crocin, Dolo, Calpol, Generic.
  - Phonetic and spelling-tolerant search.
  - Strength and dosage based filtering.
- [ ] **Substitute / Generic Logic**:
  - "Brand X Out of Stock" -> "Show Substitutes with same Salt".
  - **Margin Opportunity**: Highlight generic/private-label alternatives with higher margin.
  - Doctor restriction flag (No substitution).
  - Branded vs Generic margin comparison.
- [ ] **Drug Interaction Alerts** (Advanced):
  - Alert if Drug A and Drug B have known adverse interaction.
  - Allergy Alerts (if Patient History exists).
  - Pharmacist acknowledgment required.
  - Override reason logging.

### 3. Inventory & Rack Management
- [ ] **Rack/Bin Location**:
  - Print exact Rack/Shelf number on Receipt/Picklist.
  - "Storage Type" tagging: Fridge (2-8°C), Cabinet, Lock & Key.
  - Rack-wise stock aging visibility.
  - Cold-chain compliance warnings.
- [ ] **Batch Management**:
  - Strict Batch Tracking (MRP, Expiry, Ptr, Pts).
  - Handling "Cut Strips" (Selling 4 tablets out of 10).
  - Batch-level margin tracking.
  - Loose tablet reconciliation during stock audit.

### 4. Prescription (Rx) Management
- [ ] **Digital Prescription**:
  - Scan/Upload Rx Image via Webcam or Mobile.
  - Link Rx Image to Bill for audit.
  - Multiple Rx images per bill.
  - Secure retrieval for inspections.
- [ ] **Refill Management** (CRM):
  - Mark Bill as "Chronic" (Diabetes/BP).
  - Auto-calculate next refill date.
  - SMS/WhatsApp Reminder.
  - Missed refill follow-ups.
  - Chronic patient refill history.

### 5. Hospital Pharmacy Specifics
- [ ] **IPD vs OPD Billing**:
  - OPD: Cash/Card carry-out.
  - IPD: Credit Bill to Patient Bed/UHID.
  - Ward-wise medicine consumption.
  - Bed transfer handling.
- [ ] **Insurance / TPA**:
  - Capture TPA details.
  - Split Bill: "Patient Pay" vs "Insurance Pay".
  - TPA-wise claim-ready invoices.
  - Approval-required medicine flagging.

### 6. Specialized Sales
- [ ] **FMCG / General Items**:
  - Mixed basket support (Medicines + Shampoo).
  - Different tax logic (GST 12/18% vs Exempt).
  - Mixed return handling.
  - Margin floor enforcement.
