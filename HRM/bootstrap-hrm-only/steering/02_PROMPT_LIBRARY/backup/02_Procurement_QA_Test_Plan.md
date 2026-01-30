# Procurement QA Test Plan (Formal)

## 1. Introduction
This QA Test Plan defines the strategy, scope, and execution approach for validating the Procurement module
aligned with BBP sections **4.1 → 4.10**.

## 2. Objectives
- Validate end-to-end procurement lifecycle
- Ensure data integrity, compliance, and auditability
- Verify configuration-driven behavior

## 3. Scope
Included:
- PR, RFQ, PO, ASN, GRN, Invoice, Returns
- Configuration, Reports, Integrations

Excluded:
- Performance testing
- Security penetration testing

## 4. Test Environment
- Application: Olivine Retail ERP
- Database: PostgreSQL
- Users: Requestor, Approver, Buyer, Receiver, Finance

## 5. Master Data Prerequisites
- 1 Company
- ≥2 Locations
- ≥3 Suppliers
- ≥15 Items
- UOM, Taxes, Users & Roles

## 6. Test Strategy
- Manual functional testing initially
- Automation-ready scripts
- Positive, negative, and edge cases

## 7. Test Execution Phases
- Phase 1: Master validation
- Phase 2: Transaction flow testing
- Phase 3: Exception handling
- Phase 4: Audit & reporting

## 8. Entry & Exit Criteria
Entry:
- Environment ready
- Master data available

Exit:
- All critical test cases passed
- No open blocker defects

## 9. Defect Management
- Severity-based classification
- Root cause analysis
- Retest & closure

## 10. Deliverables
- Test scripts
- Execution reports
- Defect logs
- Sign-off report

## 11. Approval
Approved by:
- QA Lead
- Product Owner
- Architect (Viji)

**Status:** Ready for execution.