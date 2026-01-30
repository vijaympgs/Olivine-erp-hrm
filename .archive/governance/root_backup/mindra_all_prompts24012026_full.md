# Mindra --- Full-Fidelity Consolidated Prompts

**Date:** 2026-01-24 11:22:02

This document contains the **verbatim, full-fidelity copies** of the
major operational prompt blocks delivered in this conversation. No
summaries. No paraphrasing. These are ready-to-copy governance-grade
prompts.

------------------------------------------------------------------------

## 1) Build Error Fix --- Deterministic Execution Prompt

``` text
STOP LOOPING. SWITCH TO DIRECT FIX MODE.

You are stuck in a reasoning loop. This is a concrete build error and must be resolved with precise action, not discussion.

ERROR (AUTHORITATIVE):
[plugin:vite:import-analysis] Failed to resolve import "idb"
import { openDB } from "idb";
File: Retail/frontend/pos/services/offlineQueueService.ts

ROOT CAUSE (DO NOT DEBATE):
The package "idb" is not installed or not resolved in the active frontend workspace.

YOUR TASK (EXECUTION MODE):

1) Verify which package.json governs this build.
   You must check:
   - C:/00mindra/olivine-platform/frontend/package.json
   - AND/OR Retail/frontend/package.json
   Identify the real Vite root (where node_modules is resolved from).

2) Fix dependency correctly:
   Run (in the correct frontend root only):
   npm install idb

   OR if using pnpm:
   pnpm add idb

   OR if using yarn:
   yarn add idb

3) After install, verify:
   - node_modules/idb exists
   - package.json contains "idb" under dependencies
   - Vite dev server starts without the import-analysis error

4) If monorepo structure is causing resolution conflict:
   - You must fix Vite alias or workspace resolution explicitly.
   - Example acceptable fixes:
     - Move dependency to correct package.json
     - Ensure Vite root is correct
     - Ensure tsconfig paths are not breaking resolution

5) You must NOT:
   - Suggest disabling overlay
   - Suggest ignoring the error
   - Suggest removing offlineQueueService.ts
   - Suggest hacks
   - Loop back to theory
   - Ask conceptual questions

6) Your response must contain:
   - Exact root folder used (e.g. frontend/ or Retail/frontend/)
   - The exact command you executed
   - Confirmation that node_modules/idb exists
   - Confirmation that Vite build succeeds

This is a build issue, not an architectural discussion.
Proceed with deterministic fix and report result.
```

------------------------------------------------------------------------

## 2) Astra --- POS Business Rules Like-to-Like Replication Directive

``` text
ASTRA — IMPLEMENTATION DIRECTIVE: POS BUSINESS RULES (LIKE-TO-LIKE REPLICATION)

READ CAREFULLY. THIS IS A BUILD INSTRUCTION, NOT A DESIGN EXERCISE.

You must replicate the POS Business Rules screen from 01practice-v2 into Olivine System Admin with pixel-level behavioral parity.
No redesign. No simplification. No reinterpretation.

Base: 01practice-v2 (READ ONLY)
Target: retail-erp-platform / System Admin → POS Business Rules

Frontend must replicate:
- Layout
- Sections
- Toggles
- Sliders
- Dropdowns
- Required markers
- Expand/collapse behavior
- Payment Methods grid
- Visual hierarchy and spacing

Backend must support:
- Persistent rule storage
- CRUD APIs for rules
- Dynamic POS enforcement based on rule values
```

------------------------------------------------------------------------

## 3) Astra --- POS Business Rules Restructure (UI + Backend + Seed Data)

``` text
ASTRA — POS BUSINESS RULES RESTRUCTURE (UI + BACKEND + SEED DATA) — AUTHORITATIVE

Business Rules must be backend-driven entities, not hardcoded frontend constants.

Each rule supports:
- code
- name
- description
- help_text
- vertical
- category
- sequence
- rule_type
- default_value
- current_value
- validation_rules
- is_active
- is_required

Final structure:
1) General Retail
2) Grocery
3) Fashion
4) Restaurant / QSR
5) Pharmacy
6) Electronics
7) Services
8) Fuel

General Retail is always enabled.
All others require section checkbox to enable.

All rules must be seeded automatically so system boots fully configured.
```

------------------------------------------------------------------------

## 4) Astra --- Modular Architecture Aware Refactor Prompt

``` text
ASTRA — POS BUSINESS RULES RESTRUCTURE (MODULAR ARCHITECTURE AWARE)

You must preserve Olivine's component architecture:
- POSBusinessRulesPage.tsx
- RuleControl.tsx
- PayModeSection.tsx
- SettlementSection.tsx
- PaymentMethodsGrid.tsx

Do NOT flatten into a single file.
Do NOT destroy abstractions.

Refactor behavior only, not architecture.
```

------------------------------------------------------------------------

*End of full-fidelity consolidated artifact.*
