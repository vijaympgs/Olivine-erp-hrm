# High-Level Implementation Plan: Dynamic Toolbar Configuration

## Objective
Implement a backend-driven, string-based configuration system for Toolbars, allowing hierarchical control from Module level down to specific Menu Items and User Permissions.

## 1. Backend Architecture (Django)

### A. Create `ERPToolbarControl` Model
Create a new model to define the "Master Control String" for each module.
*   **Fields**:
    *   `module_name` (e.g., RETAIL, FMS, HRM, CRM) - Unique/PK.
    *   `master_toolbar_string` (e.g., "NESCAVPRDXYZ...") - Represents ALL possible actions for this module.
    *   `description`

### B. Update `ERPMenuItem` Model
Refactor `ERPMenuItem` (and alias `MenuItemType`) to store derived configurations.
*   **New Fields**:
    *   `original_toolbar_string`: The full superset derived from `ERPToolbarControl` (Read-only reference).
    *   `applicable_toolbar_config`: The specific subset of actions relevant for THIS menu item (e.g., UOM might only have "NEX", while PO has "NESCA").
*   **Logic**:
    *   On save, if `applicable_toolbar_config` is empty, it might default to a safe subset or the full master string.

### C. Update Permission Models
Ensure `RolePermission` and `UserPermission` can override or restrict this string.
*   **Update**:
    *   `toolbar_override` field should now store the "String Format" (e.g., "NE") instead of the old position-based '1,0,1...' format.

### D. API Layer (`user_management`)
*   Update the `ui-config` endpoint (`toolbar_views.py`) to resolve the final effective string:
    *   Logic: `UserOverride` ?? `RoleOverride` ?? `MenuItem.applicable_toolbar_config` ?? `Default`.
    *   Return the config as a string of characters (e.g., "NESC") to the frontend.

## 2. Frontend Architecture (React)

### A. Update `useToolbarConfig` Hook
*   **Parsing Logic**: deprecate existing bitmask/boolean-array logic.
*   **New Logic**:
    *   Receive string (e.g., "NESC").
    *   Map characters to keys:
        *   `N` -> new
        *   `E` -> edit
        *   `S` -> save
        *   `C` -> cancel
        *   `X` -> exit
        *   `A` -> amend
        *   `Z` -> authorize
        *   `R` -> refresh
        *   `D` -> delete
        *   `P` -> print
        *   `V` -> view
        *   (Define full character map).
    *   Return a boolean map based on presence of character in string.

### B. Update `MasterToolbarConfigDriven`
*   Ensure it consumes the new boolean map correctly.
*   (Already largely compatible if hook returns the `ToolbarPermissions` object).

### C. List Page Standardization
*   **Requirement**: "All list pages should have the toolbar, with only + (New) and X (Exit) enabled by default".
*   **Implementation**:
    *   List pages usually start in **VIEW** mode.
    *   We need to ensure the standard "List View" string for `ERPMenuItem` is configured as "NX" (or N+Refresh+Search+Exit).
    *   When an item is selected, the page logic might locally enable 'Open' or 'Edit' if logic permits, OR the toolbar config string needs to include 'E' but the Component locally disables it until selection.
    *   *Clarification*: The backend sends *Permission* (what CAN be done). The Frontend State determines what is *Currently Available* (e.g., Delete is permitted but requires selection).

## 3. Data Migration & Seeding
*   **Seed Data**:
    *   Create valid `ERPToolbarControl` entries for all modules.
    *   Update all existing `ERPMenuItem` rows to have valid `applicable_toolbar_config` strings.
    *   Set UOM-like masters to "NESC...X" but ensure specific workflow items (PO) have "NESCAZ...".

## 4. Execution Steps
1.  [x] [Backend] Create Models & Migrations. (Done - Migration 0004)
2.  [x] [Backend] Seed Toolbar Control Strings. (Done - Seeded RETAIL/FMS/HRM/CRM)
3.  [x] [Backend] Update API Logic. (Done - toolbar_views.py parses new strings)
4.  [x] [Frontend] Refactor Hook & Toolbar Component. (Done - MasterToolbarConfigDriven updated)
5.  [x] [Frontend] Verify List Page behavior. (Done - Defaults set to NRQFX)

## Status: COMPLETE
The backend-driven toolbar configuration is now active. All ERPMenuItems have been updated with default configuration strings.

