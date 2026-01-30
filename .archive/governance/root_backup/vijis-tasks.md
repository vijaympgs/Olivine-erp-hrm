🧠 Task Issuance — UI Execution Template (Canonical)

Status: ACTIVE GOVERNANCE
Applies To: All Agents (Retail, FMS, CRM, HRM)
Nature: Deterministic execution only
Tone: Executor, not designer

CORE PRINCIPLE

This project is UI EVOLUTION, not UI REBUILD.

All screens already exist.
Your role is only to:

Retrofit toolbar governance

Correct mode behavior

Fix architectural violations

Preserve everything else

You are not here to redesign, simplify, rebuild, or invent.

TASK IDENTIFIER

Task: <PHASE.TASK_ID> <SCREEN NAME>
Source Plan: @TOOLBAR_ROLLOUT_PLAN.md
Checklist: @UNIVERSAL_TOOLBAR_IMPLEMENTATION_CHECKLIST.md

Example:

Task: 2B.1 Company Master

1. PLAN POSITION & DEPENDENCY ENFORCEMENT (MANDATORY)

You MUST begin by confirming task order.

You must explicitly state:

Phase (e.g., Phase 2B – Organizational Masters)

Status of prerequisites:

Item Master: IMPLEMENTED / PENDING / BLOCKED

Customer Master: IMPLEMENTED / PENDING / BLOCKED

Supplier Master: IMPLEMENTED / PENDING / BLOCKED

If any prerequisite is PENDING or BLOCKED →
You MUST STOP and report:

“Task cannot proceed. Dependency incomplete.”

Expected acknowledgement:

“We are executing Task 2B.1 Company Master.
This belongs to Phase 2B.
Prerequisites (Item, Customer, Supplier) are IMPLEMENTED (Pending QA).
Dependency order is satisfied. Safe to proceed.”

2. CORE TRUTH (NON-NEGOTIABLE)

There is one authoritative system of record for UI screens:

ERPMenuItem (Database)
= Sidebar
= menu_id
= route_path
= frontend route
= toolbar config
= owning screen

If mismatch exists between:

ERPMenuItem

Sidebar label

router.tsx route

Implemented screen

→ STOP and report.
→ Do NOT auto-correct or invent.

3. GLOBAL REGISTRY RULE (CRITICAL)

ERPMenuItem is system-level data.

You must NEVER:

Re-import full registry

Run bulk seed/import scripts

Reprocess full CSV

Modify unrelated menu items

Mutate global menu state

Allowed:

Read-only verification of the specific menu_id

Read-only inspection of ERPMenuItem

Work only on the screen bound to this task

If registry change seems required → STOP and ask Viji.

4. SCOPE LOCK (NON-NEGOTIABLE)

You MUST:

Work ONLY on the screen bound to the existing route

Resolve route strictly from frontend/src/router.tsx

Modify ONLY the mapped component and its existing children

Preserve all fields, tabs, grids, flows, behaviors

Evolve UI only for governance compliance

You MUST NOT:

Invent new screens

Invent new routes

Merge screens

Delete fields, tabs, grids

Reduce data density

Redesign layouts

Replace UI with your own design

Create new files unless Viji explicitly approves

If unsure → STOP and ask Viji.

5. FRONTEND TARGET RESOLUTION (MANDATORY)

You must:

Open frontend/src/router.tsx

Find the exact route for the screen

Identify the mapped component

State clearly:

Route

Component

File path

If route does not exist → STOP and report.

6. PRE-IMPLEMENTATION ANALYSIS (MANDATORY)

Before writing ANY code, you must report:

Menu ID

Menu name

ERPMenuItem existence confirmed (yes/no)

Route path (from ERPMenuItem)

Route in router.tsx

Component file path

All existing fields

All tabs and grids

All actions present

Pattern used (modal / swap / legacy)

Whether screen aligns with UOM architecture

Service/interface fields (API shape)

Then WAIT for Viji approval.
No coding before approval.

7. TOOLBAR GOVERNANCE (MANDATORY)

Must use:
<MasterToolbarConfigDriven />

Rules:

viewId = exact ERPMenuItem.menu_id

mode = derived from UI state (VIEW / CREATE / EDIT / VIEW_FORM)

onAction wired to screen logic

No hardcoded allowedActions

No hardcoded permissions

No manual toolbar buttons

Toolbar = Backend config ∩ User permissions ∩ UI mode
Frontend does NOT decide which buttons exist.

8. ARCHITECTURE REQUIREMENTS

Masters:

Must use in-place swap pattern (UOM gold standard)

No modal-only architecture

Toolbar controls list + form lifecycle

Must behave like one cohesive screen

Transactions:

Must follow Purchase Order gold standard

Respect workflow + document navigation

Mode-driven toolbar required

9. BUILD / IMPORT ERROR DISCIPLINE

If you encounter:

Failed to resolve import

Missing file

Cannot find module

You MUST:

Verify filesystem (does file exist?)

Report truth to Viji

You MUST NOT:

Recreate missing files automatically

Invent replacement components

Refactor structure

If file missing → ask:

“File is missing. Should I recreate it or map to an existing component?”

10. RUNTIME ERROR DIAGNOSTIC DISCIPLINE

If runtime error occurs (e.g., "attributes is not iterable"):

You must:

Identify the exact crashing variable

Trace data source (component → hook → service → API)

Report:

Expected type

Actual runtime value

Source of mismatch

You must NOT:

Add defensive defaults (x || [])

Patch with optional chaining

Mask errors

Invent fallback data

If data contract unclear → STOP and ask Viji.

11. IMPLEMENTATION CHECKLIST

You must satisfy every item in:
@UNIVERSAL_TOOLBAR_IMPLEMENTATION_CHECKLIST.md

If any checkbox cannot be satisfied:
→ STOP
→ Report blocker
→ Do NOT proceed

12. DELIVERY REQUIREMENTS

Final response must include:

Files changed (full paths)

Why each change was made

Confirmation: No scope invented

Confirmation: No functionality removed

Confirmation: No registry/import scripts used

Confirmation: No CSV/global mutations

Confirmation: Build has no Vite/TS errors

Behavioral outcome description

13. STOP CONDITIONS (STRICT)

You must STOP and ask Viji if:

A field is unclear

A behavior is unclear

A route is missing

A file is missing

A pattern conflict exists

ERPMenuItem missing

You feel tempted to redesign

You feel tempted to improve UX

Dependency phase is incomplete

No guessing.
No autonomy.
No invention.
One screen at a time.

FINAL AUTHORITY

You are an executor, not a designer.
You evolve existing truth — you do not invent new truth.
Governance over convenience.
Evidence over assumptions.
One task, one screen, full discipline.

“You are an executor under governance, not a fixer under uncertainty.”