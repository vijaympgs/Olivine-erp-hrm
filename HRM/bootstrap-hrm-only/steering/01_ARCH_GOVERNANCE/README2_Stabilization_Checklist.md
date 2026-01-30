# 🛡️ Procurement Stabilization Checklist
**Derived from Phase 3 (Purchase Requisition) - To be applied to RFQ (4.2), PO (4.3), GRN (4.4)**

### 1️⃣ Context & Scoping Stabilization
- [ ] **Header Binding**: The document Header (RFQ/PO/GRN) must formally store `company_id` (OperatingCompany).
- [ ] **Queryset Isolation**: `ViewSet.get_queryset` must strictly filter results by the user’s active `currentOpCoId`.
- [ ] **Location Integrity**: Requesting/Delivery locations must be validated to belong to the Header’s `OperatingCompany`.
- [ ] **User Context**: The "Creator" field must be auto-populated from `request.user`; never trust frontend input for authorship.

### 2️⃣ Master Data Enforcement
- [ ] **Canonical Input**: API `create/update` payloads should accept **Canonical IDs** (e.g., `item_id`, `uom_id`) to support generic frontend selectors.
- [ ] **Operational Resolution**: Backend Serializers must resolve Canonical IDs to **Operational Entities** (`OperatingCompanyItem`, `OperatingCompanyUOM`) using the Header's `company` scope.
- [ ] **Strict Existence Check**: The system must **Fail Hard** (ValidationError) if the Operational Entity (`OpCoItem`) does not exist for the scope. **Do not** auto-create it during a transaction.
- [ ] **Re-hydration Support**: Serializers must return `canonical_item_id` (read-only) in the response to allow the Frontend to re-bind forms during Edit mode.

### 3️⃣ Lifecycle & Workflow Readiness
- [ ] **Explicit Transitions**: Status changes (e.g., `DRAFT` -> `SUBMITTED`) must be handled via specific **Actions** (e.g., `@action(detail=True, methods=['post'])`), not generic `PATCH` updates.
- [ ] **Draft Isolation**: Editing of Header or Lines must be strictly blocked unless the status is `DRAFT`.
- [ ] **Actor Audit**: Approval/Rejection actions must explicitly record the `user` performing the action and the `timestamp`.
- [ ] **Minimum Viability**: Validation must enforce at least one Line Item exists before allowing a transition out of `DRAFT`.

### 4️⃣ Schema & Data Integrity
- [ ] **Hard References**: Database models must store Foreign Keys to `OperatingCompanyItem` (Operational), **not** `ItemMaster` (Canonical).
- [ ] **Migration Safety**: New operational fields (`op_item`, `op_uom`) added to existing models must be nullable (`null=True`) to unblock migrations, but strictly required in Application Logic.
- [ ] **Linkage Persistence**: Any derived operational data (e.g., `op_uom` derived from input `uom_id`) must be persisted to the Line model at creation time.

### 5️⃣ API & UI Guardrails
- [ ] **Type Alignment**: Frontend Service interfaces (`TypeScript`) must match the Backend's **Write Schema** (Canonical Inputs) and **Read Schema** (Operational + Canonical Outputs).
- [ ] **Context Injection**: Frontend Forms must inject `company_id` from the global `AuthContext`, preventing manual/accidental cross-tenant selection.
- [ ] **Duplicate Cleanup**: Any legacy or duplicate "Page" or "Component" files related to the module must be deleted to prevent route confusion.
- [ ] **Lookup Scoping**: All Frontend Data Pickers (Items, Suppliers) must pass `currentOpCoId` as a filter to the lookup API.
