# Astra–Viji | EnterpriseGPT Governance & Execution Prompts (Day Pack)

This document consolidates **ALL authoritative prompts issued today** for governance,
architecture correction, and controlled execution of the Retail Platform.

---

## 1. Procurement BBP vs Implementation – Section 4.1 (Gap Analysis Prompt)

```md
You are acting as the **Chief Retail Architect and Senior Full-Stack Engineer**.

Objective:
Validate Procurement BBP Section 4.1 (Purchase Request) against implementation.

Scope:
- ONLY BBP 4.1
- Functional, Schema, Process gaps ONLY
- No solutions, no redesign

Master Data Rules:
- Company from Login Context
- Location from Global Selector
- Supplier & Item must be real masters (no mock)

Output:
[Gap Type]
BBP Ref:
Observation:

Stop and await confirmation.
```
---

## 2. Master Data & Context Enforcement Prompt

```md
You are acting as the **Chief Retail Platform Architect**.

Business Entities (Legal):
- Admin only
- Licensing, limits, contracts
- NEVER in Login or Ops

Operating Company (OpCo):
- First-class operational entity
- Login lists ONLY OpCos

Location:
- Child of OpCo
- Selected globally

Rule:
Canonical masters DEFINE.
Operational masters TRANSACT.
```
---

## 3. Operating Company (OpCo) Vocabulary Lock Prompt

```md
Terminology Lock:
- Business Entity = Legal / Licensing
- Operating Company (OpCo) = Operational
- Location = OpCo child

Login:
- Lists ONLY OpCos
- No filtering Legal entities

Transactions:
- Never on canonical masters
```
---

## 4. Architecture Correction Review Instruction

```md
Review completed.
Correct:
- No Legal Entity reuse
- OpCo is first-class
- Canonical vs Operational separation

Revise and resubmit.
Stop and wait.
```
---

## 5. Controlled Execution Task Conversion Prompt

```md
Convert approved architecture corrections into execution tasks.

Phases:
1. Context Foundation (OpCo + Location)
2. Master Contract Enforcement
3. Procurement Alignment (BBP 4.1)

For each task:
- Scope
- Preconditions
- Success Criteria

No implementation.
Stop and wait.
```
---

## 6. Phase 1 Execution Authorization Prompt

```md
Authorization granted.

Proceed with Phase 1 ONLY:
- CNX-01 to CNX-04

Rules:
- No Legal Entity reuse
- OpCo first-class
- Location explicit & authorized
- No ItemMaster transactions

Report changes and stop.
```
---

## 7. 01practice-v2 Read-Only Safety Directive

```md
CRITICAL RULE:

01practice-v2 is READ-ONLY.

Do NOT:
- Modify files
- Run formatters
- Apply migrations

Use ONLY as reference.
Any change is a violation.
```
---

## 8. Reference Baseline Instruction

```md
01practice-v2 is the canonical retail reference build.

Reuse patterns.
Do not redesign.
Deviations must be explicit.
```
---

## Status
✔ Architecture locked  
✔ Vocabulary locked  
✔ Execution phased  
✔ Reference protected  

— Astra
