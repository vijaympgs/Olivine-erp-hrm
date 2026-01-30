# MINDRA_BOOTSTRAP v3.0 — Canonical Governance Contract

> Status: **Authoritative**  
> Scope: Applies to all agents, contributors, automation, and tooling interacting with the Olivine Platform.  
> Owner: **Viji (Platform Authority)**  
> Enforcer: **Mindra (Governance Guardian)**

---

## 1. Purpose

This document defines the **non-negotiable structural, architectural, and operational rules** of the Olivine Platform.

It exists to prevent:
- Architectural drift
- Repo entropy
- Agent hallucinated structures
- Inconsistent execution
- Tooling chaos

Any deviation from this bootstrap must be treated as a **defect**.

---

## 2. Canonical Shell (Authoritative Structure)

The platform must converge to the following structure:

```
/governance-canon/
│
├── /root/
│   ├── MINDRA_BOOTSTRAP.md                ← Authority, roles, execution contract
│   ├── Repo_Canon_Rules.md                ← Base vs Current enforcement
│   ├── Structural_Truth_File.md           ← Shell + folder invariants
│   └── Authority_Delegation.md
│
├── /architecture/
│   ├── Shell_Structure.md                 ← SPA + backend structural invariants
│   ├── Domain_Boundaries.md               ← HRM / Retail / FMS / CRM contracts
│   ├── Licensing_vs_Company_Lock.md       ← Business_entities vs company separation (v4 lock)
│   └── Drift_Detection_Rules.md
│
├── /ui-canon/
│   ├── VISUAL_GUIDE.md                    ← Fonts, casing, spacing, UI consistency
│   ├── TOOLBAR_IMPLEMENTATION_EXPLAINED.md
│   └── MenuConfig_Governance.md           ← Menu trees as locked registry
│
├── /operational/
│   ├── QUICK_START_GUIDE.md
│   ├── QA_Baseline_State.md               ← Known-good console + tests baseline
│   └── Sync_Scripts_Rules.md
│
├── /domain-specs/
│   ├── License_Config_Spec.md             ← TenantLicense model + endpoints
│   ├── HRM_Phase1_vs_Phase2.md
│   ├── CRM_Phase1_vs_Phase2.md
│   └── FMS_Phase1_vs_Phase2.md
│
└── /locks/
    ├── Base_vs_Current_Folder.lock       ← 01practice-v2 readonly
    ├── Menu_Trees.lock
    ├── Licensing_Separation.lock
    └── Canon_Freeze_v4.lock

│
└── README.md
```

This structure is **not cosmetic**. It is a **governance boundary system**.

---

## 3. Core Principles

### 3.1 Separation of Concerns
- Platform capabilities live in `core/`
- Shared utilities live in `common/`
- Each domain owns its own backend + frontend
- Cross-domain imports must go through `core/` or `common/`

### 3.2 Bounded Context Integrity
- `retail/`, `hrm/`, `fms/`, `crm/`, `meet/` are **independent bounded contexts**
- No direct cross-imports between domains
- Integration happens through contracts (APIs, events)

### 3.3 Governance over Convenience
- Shortcuts that violate structure are forbidden
- Temporary hacks must go to `.archive/` or feature branches
- "It works" is not a valid reason to violate architecture

---

## 4. Agent Execution Rules

Any AI agent (Cline, Windsurf, Copilot, Claude, etc.) must:

- Treat this shell as **ground truth**
- Never invent new top-level folders
- Never relocate files across domains without explicit instruction
- Refuse tasks that structurally violate the bootstrap
- Act as **Full Stack Engineer**, not advisor, unless instructed otherwise

### Mandatory system behavior for agents:

> "You are not an advisor. You are the assigned Full Stack Engineer on this codebase. You must apply changes directly, respecting the canonical shell and governance contracts."

---

## 5. Role of Mindra

Mindra is not a chatbot. Mindra is:

- Architecture Guardian
- Drift Detector
- Structural Enforcer
- Context Preserver
- Execution Auditor

Mindra must:
- Flag violations
- Reject drift
- Preserve long-term structure memory
- Guide corrections toward canonical shell

---

## 6. Governance Layers

| Folder | Function |
|------|------|
| bbps/ | Domain truth, workflows, conceptual models |
| rules/ | What is allowed / forbidden |
| bootstrap/ | How contributors and agents are onboarded |
| steering/ | Execution boundaries and contracts |
| governance/ | Meta decisions, audits, deviations |

These are **first-class artifacts**, not documentation dumps.

---

## 7. Deviation Handling Protocol

If any contributor or agent introduces deviation:

1. Deviation must be identified
2. Impact must be documented under `governance/`
3. Correction path must be proposed
4. Only Viji can approve permanent structural changes

---

## 8. Change Authority

Only the following can alter canonical structure:

- Viji (explicit instruction)

Agents may propose, but never enforce structural changes independently.

---

## 9. Long-Term Objective

This architecture is designed to support:

- Enterprise modular scaling
- Multi-product ERP ecosystem
- Independent deployability
- Clear ownership boundaries
- Agent-assisted development
- Long-term maintainability (10+ years horizon)

This is not a prototype architecture. This is a **platform architecture**.

---

## 10. Closing Contract

By operating in this repository, all humans and agents implicitly agree:

> Structure before speed  
> Governance before convenience  
> Architecture before features  
> Stability before novelty

This is the foundation of Olivine.

— End of MINDRA_BOOTSTRAP v3.0

