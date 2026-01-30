# Payments (Vendor Payment Processing) — Test Script Prompt
File to be created by Agent:
**Payments_Processing_test_script.py**

---

## OBJECTIVE

Validate **end-to-end Vendor Payment Processing** behavior covering:
- Payment creation against invoices
- Payment allocation to multiple invoices
- Partial and full payments
- Payment methods (check, wire, ACH, etc.)
- Payment approval workflow
- Payment reversal and cancellation
- Data integrity & Persistence
- Permission enforcement

This test suite must execute critical scenarios using **real reference master data only**.

---

## GLOBAL EXECUTION RULES (MANDATORY)

1. ❌ NO mock data
2. ❌ NO factories, fixtures, or fake generators
3. ✅ USE ONLY existing reference masters from DB:
   - Company
   - Location
   - Supplier
   - Vendor Invoice
   - Bank Account
   - Users / Roles
4. ❌ DO NOT auto-create master data inside tests
5. ✅ FAIL FAST if required master data is missing
6. ✅ Use Django ORM models only
7. ✅ Each test must be transactional and isolated
8. ✅ Follow BBP 4.9 (Payments) rules strictly

---

## TEST SCRIPT STRUCTURE

```python
# file: Payments_Processing_test_script.py

from django.test import TestCase
from django.contrib.auth import get_user_model
from decimal import Decimal
from django.utils import timezone

# TODO: Import Payment specific models and serializers
from procurement.models import (
    VendorPayment,
    PaymentAllocation,
    VendorInvoice,
    Supplier
)

from finance.models import (
    BankAccount,
    PaymentMethod,
    AccountsPayable
)

from master.models import (
    Company, Location
)
```

---

## BASE TEST SETUP (SHARED CONTEXT)

```python
class PaymentsProcessingTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.company = Company.objects.filter(is_active=True).first()
        cls.location = Location.objects.filter(company=cls.company, is_active=True).first()
        cls.supplier = Supplier.objects.filter(is_active=True).first()
        cls.user = get_user_model().objects.filter(is_active=True).first()
        
        # Require approved invoice for payment testing
        cls.invoice = VendorInvoice.objects.filter(
            company=cls.company,
            invoice_status='APPROVED'
        ).first()
        
        cls.bank_account = BankAccount.objects.filter(
            company=cls.company,
            is_active=True
        ).first()
        
        assert cls.company, "Missing active Company master"
        assert cls.location, "Missing active Location master"
        assert cls.supplier, "Missing active Supplier master"
        assert cls.user, "Missing active User"
        assert cls.invoice, "Missing approved Invoice for Payment testing"
        assert cls.bank_account, "Missing active Bank Account"
```

---

## TEST CASES

> **Agent Instruction**:
> Based on BBP 4.9 and Functional Requirements for **Vendor Payments**:
> 
> **Core Test Cases to Implement:**
> 
> ### PAY-TS-01: Create Payment Against Single Invoice
> - Create payment for approved invoice
> - Set payment amount = invoice amount
> - Select payment method (check/wire/ACH)
> - Verify status = DRAFT
> - Verify invoice linkage
> 
> ### PAY-TS-02: Full Payment
> - Create payment for full invoice amount
> - Verify payment amount = invoice amount
> - Verify invoice status updated to PAID
> - Verify AP balance cleared
> 
> ### PAY-TS-03: Partial Payment
> - Create payment for partial invoice amount
> - Verify payment amount < invoice amount
> - Verify invoice status = PARTIALLY_PAID
> - Verify remaining balance tracked
> 
> ### PAY-TS-04: Multiple Payments Against Single Invoice
> - Create first partial payment
> - Create second payment for remaining amount
> - Verify cumulative payment tracking
> - Verify invoice fully paid after final payment
> 
> ### PAY-TS-05: Payment Allocation to Multiple Invoices
> - Create single payment
> - Allocate to multiple invoices
> - Verify allocation amounts sum to payment total
> - Verify each invoice status updated
> 
> ### PAY-TS-06: Payment Method Selection
> - Create payment with Check method
> - Create payment with Wire Transfer
> - Create payment with ACH
> - Verify method-specific fields captured
> 
> ### PAY-TS-07: Payment Approval Workflow
> - Submit payment (DRAFT → PENDING_APPROVAL)
> - Approve payment (PENDING_APPROVAL → APPROVED)
> - Verify approval required for high-value payments
> - Verify auto-approval for low-value (if configured)
> 
> ### PAY-TS-08: Payment Processing/Execution
> - Approve payment
> - Process payment (APPROVED → PROCESSED)
> - Verify bank account debited
> - Verify payment date recorded
> 
> ### PAY-TS-09: Payment Reversal
> - Process payment
> - Reverse payment
> - Verify status = REVERSED
> - Verify AP balance restored
> - Verify invoice status reverted
> 
> ### PAY-TS-10: Payment Cancellation Before Processing
> - Create and approve payment
> - Cancel before processing
> - Verify status = CANCELLED
> - Verify invoice status unchanged
> 
> ### PAY-TS-11: Over-Payment Handling
> - Attempt payment > invoice amount
> - Verify validation warning/error
> - Verify over-payment recorded as credit (if allowed)
> - Verify supplier credit balance updated
> 
> ### PAY-TS-12: Payment Against Credit Note
> - Create payment
> - Apply credit note to reduce payment
> - Verify net payment amount
> - Verify credit note consumed
> 
> ### PAY-TS-13: Payment Terms Validation
> - Verify payment respects supplier payment terms
> - Verify early payment discount applied (if applicable)
> - Verify late payment penalty calculated
> 
> ### PAY-TS-14: Bank Account Validation
> - Verify payment from correct bank account
> - Verify sufficient balance check (if configured)
> - Verify bank account company context
> 
> ### PAY-TS-15: Payment Reference and Documentation
> - Add payment reference number
> - Attach payment proof/receipt
> - Verify reference uniqueness
> - Verify document linkage
> 
> ### PAY-TS-16: Payment Reconciliation
> - Match payment to bank statement
> - Verify reconciliation status
> - Verify reconciliation date tracking
> 
> ### PAY-TS-17: Company/Supplier Context
> - Verify payment created for correct company
> - Verify payment linked to correct supplier
> - Verify multi-tenancy isolation
> 
> ### PAY-TS-18: Permission Checks
> - Test unauthorized user access
> - Test approval permissions
> - Verify role-based restrictions
> - Test AP clerk vs approver permissions
> 
> ### PAY-TS-19: Invalid Data Validation
> - Zero/negative payment amounts
> - Payment against non-approved invoice
> - Payment without bank account
> - Missing required fields
> 
> ### PAY-TS-20: Audit Trail Verification
> - Verify created_at, updated_at timestamps
> - Verify created_by, updated_by user tracking
> - Verify status change history
> - Verify approval audit trail
> - Verify reversal audit trail

---

## AGENT EXECUTION INSTRUCTION (LOCKED)

**Run Task:** Payments (Vendor Payment Processing) — Test Automation

- Create `Payments_Processing_test_script.py` in `backend/domain/procurement/payments/tests/`
- Implement PAY-TS-01 through PAY-TS-20 exactly as defined
- Enforce real master dependency
- Do not simplify or shortcut validations
- Follow BBP 4.9 strictly
- Ensure tests cover: Full/Partial payments, Multiple allocations, Payment methods, Approval workflow, Reversal, AP integration

**Acceptance Criteria:**
- All 20 test cases pass
- No mock data used
- Real master data validated before execution
- Payment allocation logic verified
- AP balance updates validated
- Bank account integration tested
- Proper error handling for missing data
- Transaction isolation maintained

**Critical Integration Points:**
- Invoice → Payment linkage
- Payment → AP balance update
- Payment → Bank account debit
- Payment → Supplier credit tracking
- Payment → Reconciliation

**Business Logic to Validate:**
- Payment Amount: Payment Amount ≤ Invoice Outstanding Amount (unless over-payment allowed)
- Allocation: Sum(Allocation Amounts) = Payment Amount
- AP Impact: AP Balance = Previous Balance - Payment Amount

Failure to meet any rule = test suite rejection.
