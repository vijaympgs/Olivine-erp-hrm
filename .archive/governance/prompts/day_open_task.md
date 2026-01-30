# Task Prompt: Build "Day Open" (POS Session Start)

**Instruction**: Use this prompt to Generate the code for the Day Open module.

---

Build the **Day Open / Start Session** module for the POS system.

────────────────────────────────────────
1. BACKEND REQUIREMENTS
────────────────────────────────────────
**Models**:
- `PosSession`:
  - `user` (ForeignKey to User)
  - `terminal` (ForeignKey to Terminal)
  - `opening_balance` (Decimal, 2 places)
  - `opening_time` (DateTime, auto_now_add)
  - `status` (Enum: 'OPEN', 'CLOSED', 'RECONCILIATION')
  - `shift_reference` (String, optional)

**API Endpoints**:
- `POST /api/pos/sessions/start/`:
  - Input: `{ opening_balance: number, terminal_id: number }`
  - Logic: Check if user already has open session. If not, create new `PosSession`. return active session.

**Validations**:
- One active session per terminal/user pair.
- Opening balance non-negative.

────────────────────────────────────────
2. FRONTEND LAYOUT SPECIFICATIONS (CRITICAL)
────────────────────────────────────────
**Target Zone**: Section C (Primary Workspace)
**Component**: `DayOpenForm.tsx`

The UI **MUST** strictly adhere to the standardized **Layout V2** pattern:

**Positioning Constraints** (Apply via `style={{ ... }}`):
- `top: '64px'` (Starts exactly below Application Header)
- `left: '256px'` (Starts exactly after Sidebar)
- `bottom: '0'` (Stretches to viewport bottom)
- `right: '0'` (Stretches to viewport right)
- **Prohibited**: Do NOT use `calc(100vh)` or `calc(100vw)`.

**Layering**:
- Form Container: `z-50`
- Backdrop: `z-40` (Must use same Top/Left/Bottom/Right constraints - do not use `inset-0`)
- **Outcome**: Header and Sidebar must remain visible and untouched.

**Visual Density**:
- **Padding**: `p-4` or `p-3` (Compact).
- **Spacing**: `space-y-4` between sections.
- **Footer**: Fixed at bottom of container, `border-t`, buttons right-aligned.

**Styling**:
- **Sections**: Use distinct backgrounds (e.g., `bg-gray-50` for Info, `bg-blue-50` for Money Counting).
- **Titles**: Clear `h4` with `mb-2`.

────────────────────────────────────────
3. COMPONENT STRUCTURE
────────────────────────────────────────
- `DayOpenForm.tsx`: The main modal form.
- `MoneyCounter.tsx`: (Optional) Component to input denominations if opening float is counted.

**State**:
- `openingAmount`: State for input.
- `isSubmitting`: Loading state.
- `error`: To display API errors (e.g., "Terminal already open").

────────────────────────────────────────
4. DELIVERABLES
────────────────────────────────────────
☐ Django Model (`PosSession`) & Migration
☐ DRF Serializer & ViewSet (Start Action)
☐ React Component (`DayOpenForm`) implementing Layout V2
☐ Integration into POS Dashboard (Button to trigger modal)
