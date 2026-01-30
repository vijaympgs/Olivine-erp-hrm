# Continue / GPT-4.1 Contribution Guidelines

- Keep code modular and typed.
- Follow the existing folder structure:
  - src/app for shell, router and layout
  - src/auth for auth context and services
  - src/modules for domain modules (stores, products, procurement, etc.)
  - src/ui for reusable UI components
- Reuse existing Button, Card, Input, PageHeader, DataTable where possible.
- Preserve Olivine UI design language:
  - Dark sidebar, white header, warm background
  - Colors from Tailwind theme (olivine.*)
- When adding a new module:
  - Create a folder under src/modules/<domain>
  - Add <domain>.types.ts, <domain>.service.ts, use<Domain>.ts, and <Domain>Page.tsx
