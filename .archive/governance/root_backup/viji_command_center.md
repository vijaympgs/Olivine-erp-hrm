# 🧠 Viji Command Center — Single Source of Operational Clarity

> Purpose: Reduce cognitive load, centralize orchestration, and provide one authoritative operational dashboard for Viji across agents, governance, and execution.

---

## 1) Active Rules (Platform Law)
These are the rules currently in force and must be treated as non-negotiable by all agents.

- Governance Canon lives under `.steering/` and overrides conversation memory
- 01practice-v2 = READ-ONLY reference only
- No assumption law: no field, feature, or behavior may be removed or invented
- Refactor ≠ Rewrite; Evolution only, never regression
- Toolbar, permissions, modes must follow governance strictly
- Implementation must pass functional verification (list loads, create works, no regressions)

> This section should be updated only when a new rule becomes LAW.

---

## 2) Current Objectives
What the system is actively working toward right now.

- Stabilize new toolbar rollout across all masters
- Enforce zero-regression policy on refactors
- Align Customer Master with Item Master architecture
- Improve agent discipline (analysis-first, evidence-only)

> This section changes often and reflects current sprint priorities.

---

## 3) Agent Responsibilities
Clear ownership prevents orchestration confusion.

- Viji: Final authority on all decisions
- Mindra: Architecture, governance, orchestration integrity
- Astra: Execution of implementation within governance
- Agent E: HRM + CRM domain ownership (separate onboarding)

> Any confusion about ownership must be resolved here first.

---

## 4) Non-Negotiables Checklist
These must be true for every module, every screen, every change.

- No feature regression allowed
- No skeleton screens for complex masters
- Backend data must always reflect in UI lists
- Create flow must always be tested end-to-end
- Toolbar correctness without functional correctness = FAIL
- No silent deletions of fields, tabs, flows, or logic

> If something feels wrong, this list is usually why.

---

## 5) Open Risks & Fragile Areas
This is not blame. This is awareness.

- Toolbar rollout still inconsistent across modules
- Agents occasionally assume structure instead of inspecting repo
- CRM and HRM modules have weaker enforcement than Retail
- Prompt discipline sometimes degrades over long sessions

> This section is a diagnostic mirror, not a failure report.

---

## 6) Decision Log (High-Level)
Track only important architectural or governance decisions.

- Admin user must always resolve to full permissions at data level
- Item Master must use complex master (_mst_03) pattern
- Customer Master must evolve, not be redesigned
- Functional parity is more important than visual parity

---

## 7) How to Use This Document

- When confused → read this first
- When overloaded → simplify here, not in your head
- When agents drift → point them here
- When new rule is formed → add here deliberately

This document exists to protect your mental energy.
