# Architecture Canonicalization Status

## Phase Tracking

| Phase | Description | Status |
| :--- | :--- | :--- |
| **Phase 1** | **Canonicalization & Usage Freeze** | ✅ **COMPLETED** |
| **Phase 2** | **Compatibility Bridges** | ✅ **COMPLETED** |
| **Phase 3** | **Data Alignment (Safe Mode)** | ✅ **COMPLETED** |
| **Phase 4** | **Soft Decommission** | ✅ **COMPLETED** |
| **Phase 5** | **Governance & Enforcement** | ✅ **COMPLETED** |

*Note: Phase 3 and 4 were executed in "Safe Mode" (no DB schema changes, only application-level guards).*

## Decommissioned Models (Soft)

The following models are flagged `LEGACY_DEPRECATED = True` and have write-blocks enabled:

1.  `backend.domain.company.models.Company`
2.  `backend.domain.company.models.Customer`
3.  `backend.domain.company.models.Supplier`
4.  `backend.domain.user_management.models.Employee`
5.  `backend.domain.master.customer.models.models.Customer`

## Canonical Models (Active)

1.  `backend.domain.business_entities.models.Company`
2.  `backend.domain.business_entities.models.Customer`
3.  `backend.domain.business_entities.models.Supplier`
4.  `backend.hr.models.Employee`
