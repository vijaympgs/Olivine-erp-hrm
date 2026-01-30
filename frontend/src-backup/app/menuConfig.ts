export const menuConfig = [
  {
    id: 'dashboard',
    label: 'Dashboard',
    icon: 'LayoutDashboard',
    path: '/dashboard',
  },
  {
    id: 'core-setup',
    label: 'Core Setup',
    children: [
      {
        id: 'org-setup',
        label: '1. Organization Setup',
        children: [
          { id: 'company', label: 'Company', path: '/setup/company' },
          { id: 'locations', label: 'Locations / Outlets', path: '/setup/locations' },
          { id: 'warehouses', label: 'Warehouses' },
          { id: 'fiscal', label: 'Fiscal Period & Calendar' },
          { id: 'roles', label: 'Roles & Permissions' },
        ],
      },
      {
        id: 'merch-partners',
        label: 'Merchandise & Partners',
        children: [
          { id: 'attributes', label: 'Attributes & Values' },
          { id: 'uom', label: 'Units of Measure' },
          { id: 'item-master', label: 'Item Master / SKU' },
          { id: 'customers', label: 'Customers' },
          { id: 'suppliers', label: 'Suppliers' },
        ],
      },
    ],
  },
  { id: 'operations', label: 'Operations', children: [{ id: 'procurement', label: '4. Procurement', path: '/procurement' }] },
  { id: 'inventory', label: '5. Inventory Management', path: '/inventory' },
  { id: 'pos', label: '7. Sales & POS Operations', path: '/pos' },
  { id: 'commercial', label: 'Commercial' },
  { id: 'pricing', label: '6. Pricing & Promotion', path: '/pricing' },
  { id: 'loyalty', label: '9. Loyalty & CRM' },
  { id: 'finance', label: '8. Payments & Finance', path: '/finance' },
  { id: 'store-ops', label: '10. Store Operations' },
  { id: 'reporting', label: '11. Reporting & Analytics', path: '/analytics' },
  { id: 'platform', label: 'Platform & Integrations' },
  { id: 'sysadmin', label: '12. System Administration', path: '/admin' },
  { id: 'integration', label: '13. Integration Framework' },
  { id: 'extensibility', label: '14. Extensibility Layer' },
];

