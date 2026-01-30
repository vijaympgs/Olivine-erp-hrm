# Test Script Generation Plan - Remaining Components

**Date**: 2025-12-27  
**Status**: 3/11 Complete (27%)  
**Remaining**: 8 test scripts  

---

## ✅ COMPLETED (3/11)

| Component | BBP | Test Cases | File | Status |
|-----------|-----|------------|------|--------|
| Purchase Requisition | 4.1 | 10 | `pr/tests/test_4_1_purchase_requisition.py` | ✅ DONE |
| Request for Quotation | 4.2 | 21 | `rfq/tests/test_4_2_request_for_quotation.py` | ✅ DONE |
| Purchase Orders | 4.3 | 12 | `po/tests/test_4_3_purchase_order.py` | ✅ DONE |

**Total Completed**: 43 test cases

---

## ⏳ PENDING (8/11)

### Core Procurement (4 scripts)

#### 1. ASN - Advance Shipment Notice (BBP 4.5)
- **File**: `backend/domain/procurement/asn/tests/test_4_5_advance_shipment_notice.py`
- **Test Cases**: 18 (ASN-TS-01 to ASN-TS-18)
- **Prompt**: `.steering/13TEST_PLANS/TEST_SCRIPT_CREATE_PROMPTS/4.5_Advance_Shipment_Notice_test_script_prompt.md`
- **Key Tests**:
  - ASN creation against PO
  - Full/Partial shipments
  - Multiple ASNs per PO
  - GRN pre-population
  - ASN-GRN variance tracking
  - Delivery date management
- **Menu ID**: `asns`

#### 2. GRN - Goods Receipts (BBP 4.6)
- **File**: `backend/domain/procurement/grn/tests/test_4_6_goods_receipts.py`
- **Test Cases**: 14 (GRN-TS-01 to GRN-TS-14)
- **Prompt**: `.steering/13TEST_PLANS/TEST_SCRIPT_CREATE_PROMPTS/4.6_Goods_Receipts_test_script_prompt.md`
- **Key Tests**:
  - GRN creation against PO/ASN
  - Full/Partial receipts
  - Quality inspection workflow
  - Inventory updates
  - Batch/Serial number tracking
  - Rejection handling
- **Menu ID**: `receipts`

#### 3. Invoice Matching (BBP 4.7)
- **File**: `backend/domain/procurement/invoice/tests/test_4_7_invoice_matching.py`
- **Test Cases**: 18 (INV-TS-01 to INV-TS-18)
- **Prompt**: `.steering/13TEST_PLANS/TEST_SCRIPT_CREATE_PROMPTS/4.7_Invoice_Matching_test_script_prompt.md`
- **Key Tests**:
  - 2-way matching (PO vs Invoice)
  - 3-way matching (PO vs GRN vs Invoice)
  - Price/Quantity variance detection
  - Tolerance configuration
  - Approval workflow for variances
  - AP integration
- **Menu ID**: `bills`

#### 4. Purchase Returns (BBP 4.8)
- **File**: `backend/domain/procurement/returns/tests/test_4_8_purchase_returns.py`
- **Test Cases**: 20 (RET-TS-01 to RET-TS-20)
- **Prompt**: `.steering/13TEST_PLANS/TEST_SCRIPT_CREATE_PROMPTS/4.8_Purchase_Returns_test_script_prompt.md`
- **Key Tests**:
  - Return creation against GRN
  - Return reasons tracking
  - Approval workflow
  - Inventory adjustments
  - Debit note generation
  - Replacement vs Refund
- **Menu ID**: `purchase-returns`

---

### Supporting Components (4 scripts)

#### 5. Vendors (Master Data)
- **File**: `backend/domain/master/tests/test_vendors_master_data.py` OR `backend/domain/company/tests/test_vendors_master_data.py`
- **Test Cases**: 18 (VEN-TS-01 to VEN-TS-18)
- **Prompt**: `.steering/13TEST_PLANS/TEST_SCRIPT_CREATE_PROMPTS/Vendors_Master_Data_test_script_prompt.md`
- **Key Tests**:
  - Vendor CRUD operations
  - Contact management
  - Payment terms configuration
  - Tax configuration
  - Vendor classification
  - Multi-location mapping
- **Menu ID**: `suppliers`

#### 6. Payments
- **File**: `backend/domain/procurement/payments/tests/test_payments_processing.py` OR `backend/domain/finance/tests/test_payments_processing.py`
- **Test Cases**: 20 (PAY-TS-01 to PAY-TS-20)
- **Prompt**: `.steering/13TEST_PLANS/TEST_SCRIPT_CREATE_PROMPTS/Payments_Processing_test_script_prompt.md`
- **Key Tests**:
  - Payment creation against invoices
  - Full/Partial payments
  - Payment allocation
  - Payment methods
  - Approval workflow
  - Payment reversal
- **Menu ID**: `payments`

#### 7. Compliance
- **File**: `backend/domain/procurement/compliance/tests/test_compliance_management.py`
- **Test Cases**: 20 (COMP-TS-01 to COMP-TS-20)
- **Prompt**: `.steering/13TEST_PLANS/TEST_SCRIPT_CREATE_PROMPTS/Compliance_Management_test_script_prompt.md`
- **Key Tests**:
  - Compliance requirement definition
  - Document upload/verification
  - Expiry tracking
  - Alert generation
  - PO blocking for non-compliance
  - Reporting
- **Menu ID**: `compliance`

#### 8. Configuration
- **File**: `backend/domain/procurement/tests/test_configuration_management.py` OR `backend/domain/config/tests/test_configuration_management.py`
- **Test Cases**: 20 (CFG-TS-01 to CFG-TS-20)
- **Prompt**: `.steering/13TEST_PLANS/TEST_SCRIPT_CREATE_PROMPTS/Configuration_Management_test_script_prompt.md`
- **Key Tests**:
  - Approval rules configuration
  - Tolerance settings
  - Numbering sequences
  - Email templates
  - System defaults
  - Configuration hierarchy
- **Menu ID**: `procurement-config`

---

## 📊 SUMMARY

| Category | Scripts | Test Cases | Status |
|----------|---------|------------|--------|
| **Completed** | 3 | 43 | ✅ |
| **Core Pending** | 4 | 70 | ⏳ |
| **Supporting Pending** | 4 | 78 | ⏳ |
| **TOTAL** | 11 | 191 | 27% |

---

## 🚀 GENERATION INSTRUCTIONS

### For Each Script:

1. **Open the prompt file** (e.g., `4.5_Advance_Shipment_Notice_test_script_prompt.md`)
2. **Copy the entire content**
3. **Paste to AI agent** (Claude, ChatGPT, etc.)
4. **AI generates the test script**
5. **Save to specified file path**
6. **Run**: `python manage.py update_test_scripts` (or use "Refresh Scripts" button)
7. **Verify in QA Console** (should show "Yes")

### Batch Generation Command:

```bash
# After generating all scripts, update database
cd backend
python manage.py update_test_scripts

# Or use QA Console "Refresh Scripts" button
```

---

## 📝 NOTES

- All prompts are **self-contained** and don't require conversation history
- Each prompt follows the **same template structure**
- All scripts use **real master data only** (no mocks/factories)
- All scripts are **BBP-compliant**
- Scripts can be generated **in any order**
- Use **"Refresh Scripts"** button after creating new scripts

---

## ✅ NEXT SESSION CHECKLIST

1. [ ] Generate ASN test script (18 test cases)
2. [ ] Generate GRN test script (14 test cases)
3. [ ] Generate Invoice Matching test script (18 test cases)
4. [ ] Generate Purchase Returns test script (20 test cases)
5. [ ] Generate Vendors test script (18 test cases)
6. [ ] Generate Payments test script (20 test cases)
7. [ ] Generate Compliance test script (20 test cases)
8. [ ] Generate Configuration test script (20 test cases)
9. [ ] Update database with all script paths
10. [ ] Execute all tests via QA Console
11. [ ] Document results in TEST_EXECUTION_HISTORY.md

---

**Last Updated**: 2025-12-27 22:12 IST  
**Progress**: 3/11 scripts (27%)  
**Remaining Work**: 148 test cases across 8 scripts
