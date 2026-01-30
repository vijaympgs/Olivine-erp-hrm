
# Olivine EnterpriseGPT — Procurement QA Governance & Execution Prompts (Consolidated)

This document consolidates ALL prompts generated today related to:
- Governance conformance
- Phase 0 master data readiness
- Hold / Resume control
- Procurement QA execution (BBP 4.1 → 4.10)

This file is authoritative for agent execution discipline.

---

## 1. Governance Conformance Audit Prompt
Purpose:
Audit steering for:
- business_entities vs company separation
- seed discipline
- architectural locks
- no file-path based governance

Status: COMPLETED & LOCKED

---

## 2. Phase 0 — Master Data Readiness Prompt
Purpose:
Validate master data readiness using existing seed_enterprise_masters.py

Rules:
- Assessment only
- No reseeding
- No fixes during this phase

Status: INITIALLY BLOCKED

---

## 3. Phase 0 — Critical Blocker Resolution Prompt
Scope:
- Fix Company model FieldError: pos_day_opens
- Fix ItemMaster model FieldError: vendorbillline

Rules:
- No blind patches
- No legacy model reintroduction
- domain.company is the sole operational domain

---

## 4. Mandatory HOLD Directive
Trigger:
- Phase 0 blocked
- ORM errors present

Agent actions:
- Stop all testing
- Stop test preparation
- Escalate only
- Track blockers

Status: TERMINAL HOLD ENFORCED

---

## 5. Verification Prep (Read-only)
Correct ORM imports:

```python
from domain.company.models import Company, ItemMaster
from domain.company.models import OperationalSupplier, OperationalCustomer
```

Minimum counts:
- Company ≥1
- Locations ≥2
- Suppliers ≥3
- Items ≥15
- UOMs ≥5

Execution deferred until authorization.

---

## 6. Terminal HOLD Confirmation Prompt
Agent instructed to:
- Remain idle
- Produce no artifacts
- Await explicit resume signal

Status: HOLD LOCKED

---

## 7. Explicit RESUME Directive — Procurement QA
Authorization:
Terminal Hold lifted by human authority

Execution order (LOCKED):
BBP 4.1 → BBP 4.10

Rules:
- ≥10 items per transaction
- Mandatory BBP references
- No governance, schema, or seed changes

Start with:
BBP 4.1 — Purchase Requisition

---

## 8. Final State
Governance: CLOSED  
Phase 0: RESOLVED BY AUTHORITY  
Procurement QA: ACTIVE  

This document is the single consolidated reference for today’s prompts.

Human Authority: Viji  
Agent Role: Executor only
