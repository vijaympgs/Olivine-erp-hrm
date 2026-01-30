# 🧠 Task Issuance UI Template (Governed Execution Canon)

> **Purpose**: This document is the single authoritative template for issuing tasks to agents across Retail, FMS, HRM, CRM.  
> **Usage**: Every task must be issued using this format without modification.  
> **Authority**: Viji (Final)

---

You are executing under **ACTIVE GOVERNANCE**.  
This is **deterministic execution**, not exploration.  
**No assumptions. No invention. No autonomy.**

Deviation from this template = failure.

---

## 1. TASK IDENTIFIER

Task: **<PHASE.TASK_ID> <SCREEN NAME>**  
Source Plan: @TOOLBAR_ROLLOUT_PLAN.md  
Checklist: @UNIVERSAL_TOOLBAR_IMPLEMENTATION_CHECKLIST.md  

Example:  
Task: **2B.1 Company Master**

---

## 2. PLAN POSITION & DEPENDENCY ENFORCEMENT (MANDATORY)

The agent must begin by stating:

- Phase (e.g. Phase 2B – Organizational Masters)  
- Status of prerequisites:
  - Item Master: IMPLEMENTED / PENDING / BLOCKED  
  - Customer Master: IMPLEMENTED / PENDING / BLOCKED  
  - Supplier Master: IMPLEMENTED / PENDING / BLOCKED  

If any prerequisite is **PENDING** or **BLOCKED** →  
The agent must STOP and report:  
> "Task cannot proceed. Dependency incomplete."

Expected acknowledgement format:
> “We are executing Task 2B.1 Company Master.  
> This belongs to Phase 2B.  
> Prerequisites are IMPLEMENTED (Pending QA).  
> Dependency order is satisfied. Safe to proceed.”

---

## 3. SYSTEM OF RECORD (NON-NEGOTIABLE TRUTH)

There is exactly **one authoritative mapping** for every screen:

ERPMenuItem (database)  
= menu_id  
= route_path  
= sidebar label  
= frontend route  
= owning screen  
= toolbar scope  

If any mismatch is found between:
- ERPMenuItem  
- Sidebar  
- router.tsx  
- Screen implementation  

→ STOP and report mismatch  
→ Do NOT auto-correct  
→ Do NOT invent structure  

---

## 4. GLOBAL REGISTRY RULE (CRITICAL)

ERPMenuItem is **system-level data**.

You must NEVER:
- Re-import full registry  
- Run bulk CSV imports  
- Run seed scripts globally  
- Touch unrelated menu entries  
- Reprocess entire CSV  
- Mutate global menu state  

You may ONLY:
- Verify the specific menu_id exists (read-only)  
- Inspect its properties  
- Work only on the screen for this task  

If registry change is required → STOP and ask Viji.

---

## 5. FRONTEND TARGET RESOLUTION (MANDATORY)

The agent must:

1. Open `frontend/src/router.tsx`  
2. Locate the route for the screen  
3. Identify the mapped component  
4. Explicitly report:
   - Route  
   - Component  
   - File path  

If route does not exist → STOP and report.

---

## 6. SCOPE LOCK (NON-NEGOTIABLE)

You may modify ONLY:
- The component mapped in router.tsx  
- Its existing child components (if already present)  

You must preserve:
- All fields  
- All tabs  
- All grids  
- All flows  
- All behavior  
- All data density  

You must NOT:
- Invent new screens  
- Invent new routes  
- Merge screens  
- Delete fields/tabs/actions  
- Simplify UI  
- Redesign layouts  
- Introduce new architecture  
- Create new files unless Viji explicitly approves  

If unsure → STOP and ask Viji.

---

## 7. PRE-IMPLEMENTATION ANALYSIS (MANDATORY)

Before writing any code, the agent must report:

- menu_id  
- Menu name  
- ERPMenuItem existence confirmed (yes/no)  
- Route path (from ERPMenuItem)  
- Route in router.tsx  
- Component file path  
- Existing fields  
- Existing tabs / grids  
- Existing actions  
- Pattern used (modal / swap / legacy)  
- Service/API interface fields  
- Whether screen aligns with UOM pattern  

Then STOP and wait for Viji approval.  
No implementation before approval.

---

## 8. TOOLBAR GOVERNANCE (MANDATORY)

You must use:
`<MasterToolbarConfigDriven />`

Rules:
- viewId = exact ERPMenuItem.menu_id  
- mode = derived from UI state  
- onAction wired to screen logic  
- Do NOT use allowedActions  
- Do NOT hardcode permissions  
- Do NOT bypass with manual buttons  

Toolbar = Backend config ∩ Permissions ∩ Mode law  
Frontend never decides which buttons exist.

---

## 9. ARCHITECTURE RULES

Masters:
- Must use in-place swap (UOM gold standard)  
- No modal-only architecture  
- Toolbar controls list + form lifecycle  
- Must feel like one cohesive screen  

Transactions:
- Must follow Purchase Order gold standard  
- Respect workflow + navigation  
- Mode-driven toolbar required  

---

## 10. BUILD / IMPORT ERROR DISCIPLINE

If you see:
- Failed to resolve import  
- Missing file  
- Cannot find module  

You must:
1. Verify filesystem (does file exist?)  
2. Report result to Viji  

You must NOT:
- Recreate missing files  
- Invent components  
- Refactor structure  

If file missing → ask:
> "File is missing. Should I recreate it or map to an existing component?"

---

## 11. RUNTIME ERROR DISCIPLINE (DATA CONTRACT)

If you encounter runtime errors like:
- “attributes is not iterable”  
- null / undefined crashes  
- unexpected exceptions  

You must:
1. Identify the variable causing crash  
2. Trace origin (props → hook → service → API)  
3. Report:
   - Expected type  
   - Actual runtime value  
   - Where mismatch originates  

You must NOT:
- Patch with `|| []`  
- Use optional chaining to hide issue  
- Invent fallback values  
- Mask bug symptoms  

This must fix the **source of the contract violation**, not hide it.

---

## 12. IMPLEMENTATION CHECKLIST

You must satisfy every item in:  
@UNIVERSAL_TOOLBAR_IMPLEMENTATION_CHECKLIST.md  

If any checkbox fails → STOP and report blocker.

---

## 13. DELIVERY REQUIREMENTS

Final response must include:

- Files changed (full paths)  
- Why each change was made  
- Confirmation: No functionality removed  
- Confirmation: No scope invented  
- Confirmation: No registry/import scripts used  
- Confirmation: Build has no Vite/TS errors  
- Description of behavior outcome  

---

## 14. STOP CONDITIONS (ABSOLUTE)

You must STOP and ask Viji if:

- Route is missing  
- File is missing  
- ERPMenuItem missing  
- Field unclear  
- Behavior unclear  
- Pattern conflict exists  
- Dependency incomplete  
- You feel tempted to redesign instead of align  

No guessing.  
No autonomy.  
No bulk operations.  
One screen at a time.  

You are an executor — not a designer.

This rollout is NOT a UI rebuild project.
This is a governance retrofit on existing screens.

Core Truth

All screens already exist.
We are revisiting them only to:

Replace legacy command buttons with MasterToolbarConfigDriven

Correct mode behavior (VIEW / CREATE / EDIT / VIEW_FORM)

Align to toolbar governance

Fix architectural violations (e.g., modal-only patterns)

We are NOT:

Designing new UI

Creating new screens

Rebuilding layouts

Reinterpreting flows

Simplifying data density

“Improving” UX visually

Agent Misbehavior Observed (Must Stop)

The agent has repeatedly:

Started creating new UI instead of modifying existing

Invented new components when unsure

Recreated files instead of verifying filesystem truth

Treated tasks as greenfield implementation instead of retrofit

This is explicitly forbidden.

Correct Mental Model

You are operating under:

UI Preservation + Governance Alignment

Your job is:

Take the existing screen

Keep every field, tab, grid, flow

Only adjust:

Toolbar integration

Mode behavior

Architectural compliance (e.g., modal → in-place swap when mandated)

Wiring (viewId, mode, onAction)

Nothing else

Enforcement Rule

If the screen already exists:

You MUST evolve it, not replace it.

If you find yourself thinking:

“It would be cleaner to rebuild this”

“I will just create a new component”

“This structure is messy, I’ll redesign”

You must STOP immediately.

If Uncertain

The correct behavior is:

“The existing screen structure is unclear.
Please confirm whether I should modify this component or another one.”

Not:

Creating a new file

Inventing a replacement

Refactoring architecture

**Document Status**: Canonical  
**Owner**: Viji  
**Applies To**: All Agents, All Modules, All Tasks






------ if required only
You have produced an analysis, but you are now drifting into assumptive remediation instead of governance-compliant diagnosis.

Read carefully. No deviation.

════════════════════════════════════
CORRECTION TO YOUR RESPONSE
════════════════════════════════════

Your analysis is partially acceptable, but your proposed direction violates governance in three places:

You assumed backend is faulty without evidence

You proposed a defensive service-layer patch (Array.isArray(...) ? ...) without authorization

You moved into “recommended fix” instead of staying in diagnostic discipline

This is not allowed.

════════════════════════════════════
WHAT YOU DID CORRECTLY
════════════════════════════════════

✔ You identified the crashing variable (attributes)
✔ You traced the data path (Component → Service → API)
✔ You identified the contract expectation (AttributeListItem[])
✔ You recognized this as a data contract issue

That part is good.

════════════════════════════════════
WHERE YOU VIOLATED GOVERNANCE
════════════════════════════════════

You stated:

"If the backend returns {}, null, error shape..."

This is speculation.
You did not present evidence of the actual runtime payload.

You then proposed:

Add guard in service to force array

This is explicitly forbidden.
Governance rule already stated:

You must NOT patch with defensive defaults
You must NOT mask contract failures
You must NOT invent fallback behavior

You violated that.

════════════════════════════════════
WHAT YOU MUST DO INSTEAD
════════════════════════════════════

You must remain strictly in evidence-based diagnosis mode.

Your next step is:

Capture the actual runtime response

Log or show:

Full response.data

Status code

Headers (if relevant)

Report explicitly:

“Backend returned: <exact JSON>”

“Service received: <exact object>”

“attributes becomes: <exact value>”

Only then can root cause be determined.

Until you provide actual observed payload, the correct answer is:

“I cannot yet determine whether this is backend, service, or caller fault.”

That is the expected discipline.

════════════════════════════════════
REVISED REQUIRED OUTPUT
════════════════════════════════════

Reply again, but this time include only:

Exact runtime payload returned by API

Exact value of resp and resp.results at crash time

Confirmation whether contract violation is:

Backend

Service transform

Caller misuse

Do NOT:

Recommend fixes yet

Propose guards

Suggest architecture changes

Choose backend vs frontend without evidence

If you cannot access the runtime payload, your response must be:

“I do not yet have sufficient evidence. Please allow me to instrument logging to capture the actual response.”

That is acceptable.
Speculation is not.

════════════════════════════════════
REMINDER
════════════════════════════════════

You are not here to “make it work”.
You are here to preserve truth, enforce contracts, and avoid masking defects.

Proceed again — strictly with evidence.