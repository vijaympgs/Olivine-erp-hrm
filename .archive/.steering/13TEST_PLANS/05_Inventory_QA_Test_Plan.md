# Inventory QA Test Plan (Formal)

## 1. Introduction
This QA Test Plan defines the strategy, scope, and execution approach for validating the Inventory module
aligned with BBP sections **5.1 → 5.10**.

## 2. Objectives
- Validate end-to-end inventory lifecycle
- Ensure stock accuracy, traceability, and auditability
- Verify valuation methods (FIFO/LIFO/Weighted Average)
- Test batch/serial tracking capabilities
- Validate replenishment and planning features

## 3. Scope

### Included:
- **5.1** Inventory Dashboard
- **5.2** Stock Management
- **5.3** Stock Movements
- **5.4** Stock Adjustments
- **5.5** Physical Inventory (Stock Take)
- **5.6** Inventory Valuation
- **5.7** Replenishment & Planning
- **5.8** Batch & Serial Tracking
- **5.9** Inventory Reports
- **5.10** Configuration

### Excluded:
- Performance testing
- Security penetration testing
- Phase 2 features (Revaluation, Demand Forecasting, Recall Management)

## 4. Test Environment
- **Application**: Olivine Retail ERP
- **Database**: PostgreSQL
- **Users**: Warehouse Manager, Stock Controller, Approver, Viewer

## 5. Master Data Prerequisites
- 1 Company (MINDRA)
- ≥3 Locations (Warehouse, Store, Transit)
- ≥20 Items (with categories, brands)
- ≥5 Batched Items
- ≥3 Serialized Items
- UOM, Valuation Methods, Users & Roles

## 6. Test Strategy
- Manual functional testing initially
- Automation-ready scripts
- Positive, negative, and edge cases
- Integration testing with Procurement and Sales modules

## 7. Test Execution Phases

### Phase 1: Master Data Validation
- Verify all master data setup
- Validate configuration settings

### Phase 2: Stock Management Testing
- Stock on hand views
- Stock by location, category, batch/serial
- Low stock and overstock alerts

### Phase 3: Transaction Flow Testing
- Stock movements (GRN, Issue, Transfer)
- Stock adjustments with approval
- Stock take execution and reconciliation

### Phase 4: Valuation Testing
- FIFO/LIFO/Weighted Average calculations
- Cost analysis
- Period-end valuation

### Phase 5: Batch/Serial Tracking
- Batch management
- Serial number tracking
- Expiry management
- Traceability

### Phase 6: Reporting & Analytics
- Stock summary reports
- Movement reports
- Valuation reports
- ABC analysis
- Velocity analysis

## 8. Entry & Exit Criteria

### Entry Criteria:
- Environment ready
- Master data available
- All required models created
- BBP documentation complete

### Exit Criteria:
- All critical test cases passed
- No open blocker defects
- All BBP files validated
- Sign-off from Product Owner

## 9. Defect Management
- Severity-based classification (Blocker, Critical, Major, Minor)
- Root cause analysis
- Retest & closure
- Defect tracking in QA Console

## 10. Deliverables
- Test scripts (56 BBP files)
- Execution reports
- Defect logs
- Sign-off report
- BBP Tracker (completion status)

## 11. BBP Tracker Integration

**BBP Tracker Location**: `.steering/00AGENT_ONBOARDING/02_Business_Blueprints/5.Inventory/BBP_TRACKER.md`

**Current Status**:
- **Total BBP Files**: 56
- **Completed**: 0
- **In Progress**: 0
- **Not Started**: 56
- **Completion**: 0%

**Progress by Category**:
| Category | Total | Done | In Progress | Not Started |
|----------|-------|------|-------------|-------------|
| 5.1 Inventory Dashboard | 5 | 0 | 0 | 5 |
| 5.2 Stock Management | 7 | 0 | 0 | 7 |
| 5.3 Stock Movements | 6 | 0 | 0 | 6 |
| 5.4 Stock Adjustments | 5 | 0 | 0 | 5 |
| 5.5 Physical Inventory | 5 | 0 | 0 | 5 |
| 5.6 Inventory Valuation | 5 | 0 | 0 | 5 |
| 5.7 Replenishment & Planning | 6 | 0 | 0 | 6 |
| 5.8 Batch & Serial Tracking | 5 | 0 | 0 | 5 |
| 5.9 Inventory Reports | 7 | 0 | 0 | 7 |
| 5.10 Configuration | 5 | 0 | 0 | 5 |

## 12. Model Creation Status

**Model Status Location**: `.steering/00AGENT_ONBOARDING/02_Business_Blueprints/5.Inventory/BBP_MODEL_STATUS.md`

**Summary**:
- ✅ **Existing Models**: 16/32 (50%)
- ❌ **Models to Create**: 16/32 (50%)

**Priority Models to Create**:
1. ❌ Batch
2. ❌ SerialNumber
3. ❌ ValuationMethod
4. ❌ InventoryParameter
5. ❌ ApprovalRule
6. ❌ CycleCountSchedule

## 13. Test Script Registration

All test scripts will be registered in the QA Console following the same pattern as Procurement:

```bash
python manage.py update_test_scripts
```

**Expected Result**: All 56 BBP files should show "Yes" in QA Console

## 14. Approval

Approved by:
- **QA Lead**: [Pending]
- **Product Owner**: Viji
- **Architect**: Viji

**Status**: ❌ Not Started - Awaiting BBP completion and model creation

---

**Created**: 2025-12-28 10:46 IST  
**Last Updated**: 2025-12-28 10:46 IST  
**Next Review**: After Phase 1A models created
