# ARCHITECTURE_PHASE_TASKS.md

This document lists executable tasks for each architecture phase.
Agents must execute ONLY the approved phase.

---

## Phase 1 — Canonicalization & Usage Freeze (SAFE)

- Declare canonical models (Company, Customer, Item, Variant, Employee, Masters)
- Add LEGACY MODEL warnings in non-canonical models
- Fix invalid imports (e.g. POS → non-existent ItemVariant)
- Enforce rule: new code uses canonical models only
- No DB migrations
- No model deletions

Deliverables:
- Clean imports
- System runs without model ambiguity
- Report of touched files

---

## Phase 2 — Compatibility Bridges

- Create adapter services for legacy → canonical models
- Redirect business logic to canonical models
- Keep legacy models read-only
- Remove direct FK usage where conflicting

Deliverables:
- Service-level mappings
- Zero runtime logic using legacy models directly

---

## Phase 3 — Data Alignment (Optional)

- Plan migrations for duplicate tables
- Backfill canonical tables
- Validate reports and aggregates
- Prepare rollback plans

Deliverables:
- Migration scripts
- Validation reports

---

## Phase 4 — Legacy Decommission

- Remove unused legacy models
- Drop obsolete tables
- Clean serializers, admin, tests

Deliverables:
- Reduced schema
- Clean domain boundaries

---

## Phase 5 — Governance & Enforcement

- Add lint rules / checks for canonical imports
- Update onboarding docs
- Lock architecture with CI checks

Deliverables:
- Automated enforcement
- Architecture governance complete
