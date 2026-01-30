# Architecture Governance Guide

## 1. Core Principles
To ensure system stability and prepare for the final migration, the following architectural rules are enforced:

1.  **Canonical Models Only**: New code must use the "Canonical" models defined in `domain.business_entities` and `hr`.
2.  **Legacy Freeze**: The "Legacy" models in `domain.company` and `domain.user_management` are strictly **Read-Only** for creation.
3.  **Bridge Pattern**: Usage of legacy models is permitted ONLY via the `LegacyBridge` service or within the `domain.pos` (legacy) module.

## 2. Model Classification

| Entity | Canonical Model (USE THIS) | Legacy Model (DO NOT USE) |
| :--- | :--- | :--- |
| **Company** | `domain.business_entities.Company` | `domain.company.Company` |
| **Customer** | `domain.business_entities.Customer` | `domain.company.Customer` <br> `master.customer.Customer` |
| **Supplier** | `domain.business_entities.Supplier` | `domain.company.Supplier` |
| **Employee** | `backend.hr.Employee` | `domain.user_management.Employee` |
| **Item** | `domain.business_entities.ItemMaster` | `domain.company.Item` (Use `ItemVariant` instead) |

**Note**: `domain.company.ItemVariant` is currently considered Canonical for SKU-level operations as it has no counterpart in Business Entities.

## 3. The Legacy Bridge
To resolve interactions between new logic (Canonical) and old logic (Legacy), use the `LegacyBridge`:

```python
from common.legacy_bridge import LegacyBridge

# Get Canonical from Legacy
canonical = LegacyBridge.get_canonical_company(legacy_company_id)

# Get Legacy from Canonical
legacy = LegacyBridge.get_legacy_company(canonical_company_id)
```

## 4. Operational Constraints
*   **Creation Blocked**: Attempting to create a new instance of a Legacy model via `save()` will raise a `ValidationError`.
*   **Existing Data**: Existing legacy records can be updated if necessary (maintenance), but this should be avoided.

## 5. Automated Enforcement
An architecture linting script is available to catch forbidden imports. This runs in CI/CD.

**Run Linter:**
```bash
python scripts/arch_lint.py
```

*Status: POS Module is currently excluded from strict enforcement as it undergoes refactoring.*
