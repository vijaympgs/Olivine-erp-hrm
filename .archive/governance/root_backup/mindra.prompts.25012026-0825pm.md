# Mindra Prompts Log

## File: mindra.prompts.25012026-0825pm.md

## Date: 2026-01-25

This document consolidates the user's key prompts and instructions from
the session started on 25 Jan 2026. Purpose: allow clean continuity when
starting a new session.

------------------------------------------------------------------------

## Core User Constraints (Must Always Apply)

-   All responses must stay strictly within **Olivine-platform
    context**.
-   No generic ERP language unless user explicitly asks (no "generally",
    "typically", "best practice").
-   Prompts intended for agents must be delivered as **SCCB (Single
    Copyable Code Block)**.
-   The assistant operates as **Chief Architect for Olivine**.
-   Username reference when needed: `viji.m.olivine.venture`.

------------------------------------------------------------------------

## User Direction: QA & Test Console Artifacts

User clarified operational model:

1.  Mindra must produce:
    -   Full UI tracker for all Retail UIs
    -   Detailed scenario documents for each UI (execution-grade)
2.  Astra will:
    -   Convert scenarios into Test Scripts (TS)
    -   Run Developer Integration Testing (DIT)
3.  Viji will:
    -   Perform UAT using BBP + Scenarios + DIT results

Explicit rejection of partial samples or generic plans.

------------------------------------------------------------------------

## User Request: Registry-first architecture

Problem: Agents waste time searching codebase for files when asked to
modify screens.

User intent: Create a **UI Registry Manifest** that becomes the first
lookup source for all file discovery and navigation, similar to how
`/start` maps to `.agent/workflows/start.md`.

Instruction: - Agents must always consult registry first before scanning
directories. - Registry must contain canonical keys, aliases, and
frontend/backend paths.

------------------------------------------------------------------------

## User Request: Unified Registry Creation + Registry-first Enforcement

User requested a consolidated SCCB that: - Forces Astra to build a full
UI registry manifest - Forces Astra to consult that registry before any
file search - Makes this behavior mandatory, not optional

------------------------------------------------------------------------

## User Instruction: Platform Tools Restructure

User requested that the following utilities from 01practicev2:

-   Database Configuration
-   Web Console
-   HTML Preview Tool
-   DataOps Studio
-   Wireframe Launchpad

Must be replicated under:

Olivine Platform → System Tools

And aligned consistently across: - Sidebar - MenuConfig / ERP menu - UI
Registry - Test Console

Also included previously added: - File Search Explorer - Backup &
Recovery - Visual Extractor

System Tools becomes the single canonical home for platform utilities.

------------------------------------------------------------------------

## User Instruction: Visual Extractor Screen

New screen to exist under: Platform → System Tools → Visual Extractor

Purpose: - Left panel: Image upload / preview - Right panel: Extracted
text in Markdown - Only Area C used (A=Header, B=Sidebar, D=Status Bar
remain untouched)

Astra proposed registry patch with path:
frontend/src/pages/system_tools/visual_extractor/VisualExtractorPage.tsx

User requested Mindra to issue SCCB governing this change.

------------------------------------------------------------------------

## User Closing Instruction

User explicitly stated: \> "I am starting a new session. Save all
today's prompts into mindra.prompts.25012026-0825pm.md"

This file fulfills that request.

------------------------------------------------------------------------

End of document.
