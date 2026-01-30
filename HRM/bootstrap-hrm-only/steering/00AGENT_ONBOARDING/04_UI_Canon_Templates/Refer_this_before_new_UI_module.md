# Refer This Before Creating Any New UI Module
Olivine Retail ERP – UI + Backend Alignment Playbook

This document is the mandatory reference before creating or modifying any new UI module in the Olivine Retail ERP platform. It ensures consistent UI–API alignment, domain-driven backend structure, enterprise-grade scalability, and safe collaboration with AI agents.

CORE PRINCIPLE
Every UI module MUST map to a backend domain module.
No orphan UI. No shared APIs. No cross-module shortcuts.
UI follows DOMAIN — not the other way around.

BACKEND – DOMAIN MODULE STRUCTURE (MANDATORY)

Every module must exist under:
backend/domain/<module_name>/

Required files (all are mandatory):
models.py        → Domain entities & persistence
serializers.py   → API contracts (read/write)
views.py         → Use-case orchestration (thin only)
urls.py          → Module API routes
admin.py         → Admin visibility & audit
apps.py          → Django app registration
__init__.py

If any of these files are missing, the module is NOT COMPLETE.

BACKEND – CROSS-CUTTING CHANGES (ALWAYS REQUIRED)

Register the app
File: backend/config/settings/base.py
Add:
INSTALLED_APPS += ["domain.<module_name>"]

Register URLs
File: backend/domain/erp_core/urls.py (or project-level urls.py)
Add:
path("api/<module_name>/", include("domain.<module_name>.urls"))

Database migration
Run:
python manage.py makemigrations <module_name>
python manage.py migrate

BACKEND – BUSINESS LOGIC SEPARATION (VERY IMPORTANT)

Do NOT overload models.py.

As complexity grows, introduce:
services.py      → Business rules (reserve, adjust, validate)
selectors.py     → Read-only queries (availability, KPIs)
constants.py     → Statuses, enums, movement types
permissions.py   → Role-based access

Golden rule:
models.py → structure only
services.py → business logic
views.py → request/response wiring only

FRONTEND – UI MODULE STRUCTURE (MANDATORY)

Each backend domain must have a matching UI module:
spa/src/modules/<module_name>/

pages/           → Screens (List, Detail, Dashboard)
components/      → Reusable UI blocks
services/        → API calls
hooks/           → Data hooks
index.ts

No shared component shortcuts across domains without approval.

FRONTEND – ROUTING & NAVIGATION (ALWAYS TOUCHED)

App routing
File: spa/src/routes/app.routes.tsx
Add:
path: "/<module_name>"
element: <<ModuleName>Dashboard />

Sidebar / Menu registration
File: spa/src/config/menu.config.ts
Add label, icon, route, permission (if applicable).
Navigation consistency is mandatory.

FRONTEND – API MAPPING RULE (CRITICAL)

Every UI module MUST have its own API service file:
spa/src/services/<module_name>.api.ts

This maps 1:1 to:
backend/domain/<module_name>/urls.py

Never mix APIs across modules.

DOCUMENTATION & GOVERNANCE (MANDATORY)

Every new UI module requires updates to:
- **[RETAIL_IMPLEMENTATION_TRACKER.md](../../RETAIL_IMPLEMENTATION_TRACKER.md)** → Implementation progress
- **[UI_LAYOUT_TERMINOLOGY.md](../standards/UI_LAYOUT_TERMINOLOGY.md)** → Naming consistency
- **[MENU_TREE_STRUCTURE.md](./MENU_TREE_STRUCTURE.md)** → Navigation structure

This prevents context loss, agent drift, and architecture erosion.

ESSENTIAL REFERENCE DOCUMENTS

Before starting any UI work, consult:
- **[Sidebar Quick Reference](./SIDEBAR_QUICK_REFERENCE.md)** - Navigation patterns
- **[Section C Migration Guide](./SECTION_C_MIGRATION_GUIDE.md)** - Workspace positioning
- **[Layout Configuration System](./LAYOUT_CONFIGURATION_SYSTEM.md)** - Centralized config
- **[POS Implementation Guide](./POS_IMPLEMENTATION_GUIDE.md)** - POS module specifics
- **[Accordion Implementation Guide](./ACCORDION_IMPLEMENTATION_GUIDE.md)** - Component usage

For standards and best practices:
- **[UI Layout Terminology](../standards/UI_LAYOUT_TERMINOLOGY.md)** - Naming conventions
- **[Olivine Sidebar Enhancement Prompt](../standards/OLIVINE_SIDEBAR_ENHANCEMENT_PROMPT.md)** - Sidebar patterns
- **[Final UI Steps](../standards/FINAL_UI_STEPS.md)** - UI completion checklist

MINIMAL COMPLETION CHECKLIST

Backend:
models.py
serializers.py
views.py
urls.py
admin.py
apps.py
settings/base.py updated
project URLs registered
migrations applied

Frontend:
UI module folder created
routes updated
sidebar/menu updated
API service file created

FINAL RULE

Consistency beats speed.
Structure beats shortcuts.
Every UI module must look like it belongs.

This document must be followed by humans, AI agents, and future contributors.
Any deviation requires explicit architectural approval.

— End of Reference
