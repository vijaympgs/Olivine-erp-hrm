# Standardized UI Prompt Template (Layout V2)

**Purpose**: Use this prompt template when requesting the creation of new UI forms or modules. It incorporates strict layout constraints to ensure components fit perfectly within the application's **"Section C: Primary Workspace"** without alignment issues, overlapping, or visibility cutoffs.

---

## Prompt Template

```markdown
Build [MODULE_NAME] as per BBP [SECTION_REF].

────────────────────────────────────────
1. BACKEND REQUIREMENTS
────────────────────────────────────────
Models:
- [Model Name] (Fields: ...)

API Endpoints:
- [List endpoints]

────────────────────────────────────────
2. FRONTEND LAYOUT SPECIFICATIONS (CRITICAL)
────────────────────────────────────────
Target Zone: Section C (Primary Workspace)
The UI must strictly adhere to the following position constraints to avoid scrollbar issues and layout overlap:

Layout Strategy:
- Position: Fixed (Overlay/Modal Mode)
- Constraints (Use explicit Style prop, NOT calc):
  - Top: '64px' (Starts exactly below Application Header)
  - Left: '256px' (Starts exactly after Sidebar)
  - Bottom: '0' (Stretches to viewport bottom - No height calc)
  - Right: '0' (Stretches to viewport right - No width calc)
- Layering:
  - Modal Container: z-50
  - Backdrop: z-40 (Must utilize same Top/Left/Bottom/Right constraints as modal - do NOT use inset-0)

Visual Density & Spacing:
- Workspace Padding: Compact (`p-3` to `p-4`)
- Section Spacing: Tight (`space-y-4`)
- Internal Section Padding: `p-3` (Reduce white space after fields)
- Footer: Fixed at bottom of container, ensuring buttons are always 100% visible (no cutoffs).

Styling Patterns:
- Sections: Distinct background colors (e.g., `bg-gray-50`, `bg-blue-50`, `bg-green-50`) with `rounded-lg`.
- Headers: Clear section titles with minimal bottom margin (`mb-4`).

────────────────────────────────────────
3. COMPONENT STRUCTURE
────────────────────────────────────────
Components:
- [Module]Form.tsx (The main container implementing the layout above)
- [Module]List.tsx

State Management:
- Loading States: Must handle API loading states gracefully (disable inputs, show spinners).
- Error Handling: Display inline error messages for failed API fetches (e.g., dropdown data).

────────────────────────────────────────
4. DELIVERABLES
────────────────────────────────────────
☐ React Component (tsx) meeting Layout V2 standards
☐ Integration with existing Sidebar/Header
☐ API Service Hooks
```

---

## Example Usage (Terminal Form)

```markdown
"Refactor the Terminal Form to match Layout V2 standards.
Ensure the form container uses `style={{ top: '64px', left: '256px', right: '0', bottom: '0' }}` to fit Section C.
Use strict z-indexing (z-50 for form, z-40 for backdrop).
Reduce internal padding to `p-3` to minimize white space."
```
