
# EnterpriseGPT — Consolidated Governance & Execution Prompt

This document is the SINGLE authoritative prompt for agents working on the Olivine Retail ERP platform.
It consolidates:
1. Business Entities vs Company clarification
2. Seed Data rules
3. Governance & execution discipline established in prior sessions

---

## 1. ARCHITECTURAL TRUTH — BUSINESS ENTITIES vs COMPANY (LOCKED)

- `domain.business_entities` = **LICENSING METADATA ONLY**
  - Company (as tenant anchor)
  - License plans, limits, subscriptions (present/future)
  - Platform / Superuser managed
  - NEVER used for operations

- `domain.company` = **OPERATIONAL REALITY**
  - Company (operational tenant)
  - Location
  - Supplier
  - Customer
  - ItemMaster (canonical)
  - Category, Brand, TaxClass
  - Attributes, UOM, PriceList
  - Used in UI, APIs, transactions

ABSOLUTE RULE:
If a model participates in UI, transactions, or daily operations,
IT MUST LIVE IN `domain.company`.

NO MIXED IMPORTS.
NO EXCEPTIONS.

---

## 2. ITEM CANONICAL DECISION (FINAL)

- Canonical Item model: **ItemMaster**
- `Item` (if present) is LEGACY / DEPRECATED
- NO data migration
- NO table renaming
- Preserve existing `be_*` tables via `Meta.db_table`

Truth:
Stability with real data > speculative refactor.

---

## 3. SEED DATA PROMPT (OPERATIONAL ONLY)

Create or extend MASTER DATA using EXISTING RECORDS where available.
Add new records ONLY to meet required counts.

Minimum anchors:
- Companies: 5
- Locations: 5 per company
- Items (ItemMaster): 200+
- Suppliers: 50+
- Customers: 50+
- Attributes: 20 (with realistic values)

Rules:
- Seed ONLY operational masters
- Import ONLY from `domain.company.models`
- NEVER seed `business_entities`
- Maintain referential integrity
- No transactions, pricing logic, or workflows

---

## 4. GOVERNANCE — FILE & EXECUTION DISCIPLINE

SOURCE OF TRUTH:
- Implementation repo: `retail-erp-platform`
- Reference-only repo: `01practice` (READ-ONLY)

Before ANY change:
- Identify files to be touched
- Explain why
- Confirm no unrelated files are modified

Disallowed:
- Mixed imports
- Silent refactors
- Schema redesign without approval
- Reintroducing removed models

---

## 5. DJANGO ADMIN GOVERNANCE

- business_entities admin:
  - Company ONLY
  - Platform-level access

- company admin:
  - ALL operational masters
  - Application Admin access

No operational model may appear under business_entities admin.

---

## 6. SERIALIZERS & IMPORT HYGIENE

If a model was removed from `business_entities`:
- Its serializer MUST also be removed there
- Serializer MUST live under `domain.company.serializers`

NEVER patch by reintroducing removed models.

---

## 7. STEERING GOVERNANCE

The `.steering/` directory is the SINGLE MEMORY of the system.

Rules:
- Update existing docs before creating new ones
- Record decisions & outcomes, not chat history
- No duplication
- No contradictions
- New agents must understand system state in 10–15 minutes

---

## 8. AUTHORITY MODEL

- Human authority: Viji
- Agent role: EXECUTOR ONLY

If unsure:
STOP.
ASK.
DO NOT GUESS.

---

ACKNOWLEDGEMENT:
By proceeding, you confirm understanding and acceptance of this lock.
