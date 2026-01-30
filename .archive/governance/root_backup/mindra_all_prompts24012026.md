# Mindra --- Consolidated Prompts (24012026)

This document consolidates all major operational prompts provided in
this conversation into a single reference artifact.

------------------------------------------------------------------------

## 1. Astra --- POS Phase 2 System Study & Vertical Extensibility Directive

``` text
STOP LOOPING. SWITCH TO DIRECT FIX MODE.
... (directive on POS architecture, single POS screen, vertical extensibility via config, impact analysis, etc.)
```

------------------------------------------------------------------------

## 2. Astra --- POS Business Rules Like-to-Like Replication Directive

``` text
ASTRA — IMPLEMENTATION DIRECTIVE: POS BUSINESS RULES (LIKE-TO-LIKE REPLICATION)
... (replicate 01practice-v2 UI/behavior exactly into Olivine System Admin POS Business Rules)
```

------------------------------------------------------------------------

## 3. Astra --- POS Business Rules Restructure (UI + Backend + Seed Data)

``` text
ASTRA — POS BUSINESS RULES RESTRUCTURE (UI + BACKEND + SEED DATA) — AUTHORITATIVE
... (collate rules from MDs + JSX, backend-driven rules, seed data, strict UI parity)
```

------------------------------------------------------------------------

## 4. Astra --- Modular Architecture Aware Refactor Prompt

``` text
ASTRA — POS BUSINESS RULES RESTRUCTURE (MODULAR ARCHITECTURE AWARE)
... (do NOT collapse components, preserve architecture, refactor behavior only)
```

------------------------------------------------------------------------

## 5. Build Error Fix Prompt (idb import / Vite)

``` text
STOP LOOPING. SWITCH TO DIRECT FIX MODE.
Fix missing dependency: npm install idb in correct workspace.
Verify node_modules/idb exists and build passes.
```

------------------------------------------------------------------------

## 6. Final Backend + Seed-Aware Business Rules Directive

``` text
ASTRA — POS BUSINESS RULES RESTRUCTURE (UI + BACKEND + SEED DATA)
... (rule schema: code, name, vertical, category, rule_type, default, validation, persistence)
```

------------------------------------------------------------------------

## Notes

-   All prompts are governance-grade, designed to prevent loops and
    enforce deterministic execution.
-   UI parity with 01practice-v2 is a recurring invariant.
-   Architecture preservation is mandatory (no flattening).
-   Backend-driven rule metadata + seed data is enforced.

------------------------------------------------------------------------

*End of consolidated artifact.*
