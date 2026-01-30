"""
Management command to seed menu items and role permissions
Based on the ROLE-USER separation model
"""
from django.core.management.base import BaseCommand
from core.auth_access.backend.user_management.models import Role, MenuItemType, RolePermission


# Menu items from frontend menuConfig - hierarchical structure
MENU_ITEMS = [
    # Top level
    {'menu_id': 'retail-now', 'menu_name': 'Retail Now', 'parent': None, 'order': 1},
    {'menu_id': 'security', 'menu_name': 'User & Permissions', 'parent': None, 'order': 2},
    {'menu_id': 'user-permissions', 'menu_name': 'Permission Matrix', 'parent': 'security', 'order': 1},
    
    # Retail Module
    {'menu_id': 'retail', 'menu_name': 'Retail', 'parent': None, 'order': 3},
    {'menu_id': 'retail-dashboard', 'menu_name': 'Retail Dashboard', 'parent': 'retail', 'order': 1},
    
    # Store Ops / POS
    {'menu_id': 'pos', 'menu_name': 'Store Ops', 'parent': 'retail', 'order': 2},
    {'menu_id': 'pos-checkout', 'menu_name': 'Checkout', 'parent': 'pos', 'order': 1},
    {'menu_id': 'pos-daily-ops', 'menu_name': 'Daily Operations', 'parent': 'pos', 'order': 2},
    {'menu_id': 'pos-day-open', 'menu_name': 'Day Open', 'parent': 'pos-daily-ops', 'order': 1},
    {'menu_id': 'pos-session-open', 'menu_name': 'Shift Start', 'parent': 'pos-daily-ops', 'order': 2},
    {'menu_id': 'pos-session-close', 'menu_name': 'Shift End', 'parent': 'pos-daily-ops', 'order': 3},
    {'menu_id': 'pos-day-close', 'menu_name': 'Day Close', 'parent': 'pos-daily-ops', 'order': 4},
    {'menu_id': 'pos-settlement', 'menu_name': 'Reconciliation', 'parent': 'pos-daily-ops', 'order': 5},
    {'menu_id': 'pos-terminal-configuration', 'menu_name': 'Registers', 'parent': 'pos', 'order': 3},
    
    # Sales
    {'menu_id': 'sales', 'menu_name': 'Sales', 'parent': 'retail', 'order': 3},
    {'menu_id': 'quotes', 'menu_name': 'Quotes & Estimates', 'parent': 'sales', 'order': 1},
    {'menu_id': 'orders', 'menu_name': 'Fulfillment', 'parent': 'sales', 'order': 2},
    {'menu_id': 'invoices', 'menu_name': 'Invoices', 'parent': 'sales', 'order': 3},
    {'menu_id': 'returns', 'menu_name': 'Returns & Refunds', 'parent': 'sales', 'order': 4},
    {'menu_id': 'sales-config', 'menu_name': 'Configuration', 'parent': 'sales', 'order': 5},
    
    # Merchandising
    {'menu_id': 'master-data', 'menu_name': 'Merchandising', 'parent': 'retail', 'order': 4},
    {'menu_id': 'item-master', 'menu_name': 'Catalog', 'parent': 'master-data', 'order': 1},
    {'menu_id': 'categories', 'menu_name': 'Hierarchy', 'parent': 'master-data', 'order': 2},
    {'menu_id': 'brands', 'menu_name': 'Brands', 'parent': 'master-data', 'order': 3},
    {'menu_id': 'attributes', 'menu_name': 'Variants', 'parent': 'master-data', 'order': 4},
    {'menu_id': 'attribute-values', 'menu_name': 'Attribute Values', 'parent': 'master-data', 'order': 5},
    {'menu_id': 'attribute-templates', 'menu_name': 'Attribute Templates', 'parent': 'master-data', 'order': 6},
    {'menu_id': 'pricing-master', 'menu_name': 'Pricing', 'parent': 'master-data', 'order': 7},
    {'menu_id': 'price-lists-master', 'menu_name': 'Price Lists', 'parent': 'master-data', 'order': 8},
    {'menu_id': 'uom', 'menu_name': 'UOM', 'parent': 'master-data', 'order': 9},
    
    # Inventory
    {'menu_id': 'inventory', 'menu_name': 'Inventory', 'parent': 'retail', 'order': 5},
    {'menu_id': 'stock-on-hand', 'menu_name': 'Stock on Hand', 'parent': 'inventory', 'order': 1},
    {'menu_id': 'stock-overview', 'menu_name': 'Overview', 'parent': 'stock-on-hand', 'order': 1},
    {'menu_id': 'stock-location', 'menu_name': 'By Location', 'parent': 'stock-on-hand', 'order': 2},
    {'menu_id': 'stock-low', 'menu_name': 'Low Stock', 'parent': 'stock-on-hand', 'order': 3},
    {'menu_id': 'logistics', 'menu_name': 'Logistics', 'parent': 'inventory', 'order': 2},
    {'menu_id': 'movements', 'menu_name': 'Stock Flow', 'parent': 'logistics', 'order': 1},
    {'menu_id': 'transfers', 'menu_name': 'Internal Transfers', 'parent': 'logistics', 'order': 2},
    {'menu_id': 'intercompany-transfers', 'menu_name': 'Intercompany', 'parent': 'logistics', 'order': 3},
    {'menu_id': 'reorder-policies', 'menu_name': 'Reorder Policies', 'parent': 'logistics', 'order': 4},
    {'menu_id': 'physical-inventory', 'menu_name': 'Physical Inventory', 'parent': 'inventory', 'order': 3},
    {'menu_id': 'cycle-count', 'menu_name': 'Stock Take', 'parent': 'physical-inventory', 'order': 1},
    {'menu_id': 'adjustments', 'menu_name': 'Adjustments', 'parent': 'physical-inventory', 'order': 2},
    
    # Procurement
    {'menu_id': 'procurement', 'menu_name': 'Procurement', 'parent': 'retail', 'order': 6},
    {'menu_id': 'suppliers', 'menu_name': 'Vendors', 'parent': 'procurement', 'order': 1},
    {'menu_id': 'requisitions', 'menu_name': 'Requisitions', 'parent': 'procurement', 'order': 2},
    {'menu_id': 'rfqs', 'menu_name': 'Requests for Quotation', 'parent': 'procurement', 'order': 3},
    {'menu_id': 'purchase-orders', 'menu_name': 'Purchase Orders', 'parent': 'procurement', 'order': 4},
    {'menu_id': 'asns', 'menu_name': 'ASNs', 'parent': 'procurement', 'order': 5},
    {'menu_id': 'receipts', 'menu_name': 'Goods Receipts', 'parent': 'procurement', 'order': 6},
    {'menu_id': 'bills', 'menu_name': 'Invoice Matching', 'parent': 'procurement', 'order': 7},
    {'menu_id': 'purchase-returns', 'menu_name': 'Purchase Returns', 'parent': 'procurement', 'order': 8},
    {'menu_id': 'payments', 'menu_name': 'Payments', 'parent': 'procurement', 'order': 9},
    {'menu_id': 'compliance', 'menu_name': 'Compliance', 'parent': 'procurement', 'order': 10},
    {'menu_id': 'procurement-config', 'menu_name': 'Configuration', 'parent': 'procurement', 'order': 11},
    
    # Customers
    {'menu_id': 'customers', 'menu_name': 'Customers', 'parent': 'retail', 'order': 7},
    {'menu_id': 'customer-list', 'menu_name': 'Directory', 'parent': 'customers', 'order': 1},
    {'menu_id': 'customer-groups', 'menu_name': 'Groups', 'parent': 'customers', 'order': 2},
    {'menu_id': 'loyalty', 'menu_name': 'Loyalty', 'parent': 'customers', 'order': 3},
    
    # Finance Module
    {'menu_id': 'finance', 'menu_name': 'Financial Management', 'parent': None, 'order': 4},
    {'menu_id': 'finance-dashboard', 'menu_name': 'Finance Dashboard', 'parent': 'finance', 'order': 1},
    {'menu_id': 'general-ledger', 'menu_name': 'General Ledger', 'parent': 'finance', 'order': 2},
    {'menu_id': 'accounts-receivable', 'menu_name': 'Accounts Receivable', 'parent': 'finance', 'order': 3},
    {'menu_id': 'accounts-payable', 'menu_name': 'Accounts Payable', 'parent': 'finance', 'order': 4},
    {'menu_id': 'cash-bank', 'menu_name': 'Cash & Bank', 'parent': 'finance', 'order': 5},
    {'menu_id': 'tax-management', 'menu_name': 'Tax Management', 'parent': 'finance', 'order': 6},
    {'menu_id': 'financial-reports', 'menu_name': 'Financial Reports', 'parent': 'finance', 'order': 7},
    {'menu_id': 'period-closing', 'menu_name': 'Period Closing', 'parent': 'finance', 'order': 8},
    
    # CRM Module
    {'menu_id': 'crm', 'menu_name': 'Customer Relationship Management', 'parent': None, 'order': 5},
    {'menu_id': 'crm-dashboard', 'menu_name': 'CRM Dashboard & Analytics', 'parent': 'crm', 'order': 1},
    {'menu_id': 'lead-management', 'menu_name': 'Lead Management', 'parent': 'crm', 'order': 2},
    {'menu_id': 'contact-management', 'menu_name': 'Contact Management', 'parent': 'crm', 'order': 3},
    {'menu_id': 'opportunity-management', 'menu_name': 'Opportunity Management', 'parent': 'crm', 'order': 4},
    
    # HR Module
    {'menu_id': 'hr', 'menu_name': 'Human Resources', 'parent': None, 'order': 6},
    {'menu_id': 'hr-dashboard', 'menu_name': 'HR Dashboard', 'parent': 'hr', 'order': 1},
    {'menu_id': 'employee-management', 'menu_name': 'Employee Management', 'parent': 'hr', 'order': 2},
]

# Role permission templates based on ROLE_MENU_VISIBILITY
# access, view, create, edit, delete
ROLE_PERMISSIONS = {
    'admin': {
        # Administrator has full access to everything
        '_default': (True, True, True, True, True),
    },
    'backofficemanager': {
        # Full back office access + approvals, no POS operations, no HR, no Security
        '_default': (True, True, True, True, False),  # No delete by default
        'security': (False, False, False, False, False),
        'user-permissions': (False, False, False, False, False),
        'pos': (False, False, False, False, False),
        'pos-checkout': (False, False, False, False, False),
        'pos-daily-ops': (False, False, False, False, False),
        'pos-day-open': (False, False, False, False, False),
        'pos-session-open': (False, False, False, False, False),
        'pos-session-close': (False, False, False, False, False),
        'pos-day-close': (False, False, False, False, False),
        'pos-settlement': (False, False, False, False, False),
        'pos-terminal-configuration': (False, False, False, False, False),
        'hr': (False, False, False, False, False),
        'hr-dashboard': (False, False, False, False, False),
        'employee-management': (False, False, False, False, False),
    },
    'backofficeuser': {
        # Back office read/write, no approvals, no finance, no CRM, no POS, no HR
        '_default': (True, True, True, True, False),
        'security': (False, False, False, False, False),
        'user-permissions': (False, False, False, False, False),
        'pos': (False, False, False, False, False),
        'pos-checkout': (False, False, False, False, False),
        'pos-daily-ops': (False, False, False, False, False),
        'pos-day-open': (False, False, False, False, False),
        'pos-session-open': (False, False, False, False, False),
        'pos-session-close': (False, False, False, False, False),
        'pos-day-close': (False, False, False, False, False),
        'pos-settlement': (False, False, False, False, False),
        'pos-terminal-configuration': (False, False, False, False, False),
        'finance': (False, False, False, False, False),
        'finance-dashboard': (False, False, False, False, False),
        'general-ledger': (False, False, False, False, False),
        'accounts-receivable': (False, False, False, False, False),
        'accounts-payable': (False, False, False, False, False),
        'cash-bank': (False, False, False, False, False),
        'tax-management': (False, False, False, False, False),
        'financial-reports': (False, False, False, False, False),
        'period-closing': (False, False, False, False, False),
        'crm': (False, False, False, False, False),
        'crm-dashboard': (False, False, False, False, False),
        'lead-management': (False, False, False, False, False),
        'contact-management': (False, False, False, False, False),
        'opportunity-management': (False, False, False, False, False),
        'hr': (False, False, False, False, False),
        'hr-dashboard': (False, False, False, False, False),
        'employee-management': (False, False, False, False, False),
    },
    'posmanager': {
        # POS + limited inventory, customers/loyalty, no back office, no finance
        '_default': (False, False, False, False, False),
        'retail-now': (True, True, False, False, False),
        'retail': (True, True, False, False, False),
        'retail-dashboard': (True, True, False, False, False),
        # Full POS access
        'pos': (True, True, True, True, False),
        'pos-checkout': (True, True, True, True, False),
        'pos-daily-ops': (True, True, True, True, False),
        'pos-day-open': (True, True, True, True, False),
        'pos-session-open': (True, True, True, True, False),
        'pos-session-close': (True, True, True, True, False),
        'pos-day-close': (True, True, True, True, False),
        'pos-settlement': (True, True, True, True, False),
        'pos-terminal-configuration': (True, True, True, True, False),
        # Limited inventory - view only
        'inventory': (True, True, False, False, False),
        'stock-on-hand': (True, True, False, False, False),
        'stock-overview': (True, True, False, False, False),
        'stock-location': (True, True, False, False, False),
        'stock-low': (True, True, False, False, False),
        # Customers for loyalty
        'customers': (True, True, True, False, False),
        'customer-list': (True, True, True, False, False),
        'customer-groups': (True, True, False, False, False),
        'loyalty': (True, True, True, False, False),
    },
    'posuser': {
        # Checkout only - very limited access
        '_default': (False, False, False, False, False),
        'retail': (True, True, False, False, False),
        'pos': (True, True, False, False, False),
        'pos-checkout': (True, True, True, False, False),  # Can create transactions
        'pos-session-open': (True, True, True, False, False),
        'pos-session-close': (True, True, True, False, False),
        # Minimal customer access for on-the-fly creation
        'customers': (True, True, True, False, False),
        'customer-list': (True, True, True, False, False),
    },
}


class Command(BaseCommand):
    help = 'Seeds menu items and role permissions for all system roles'

    def handle(self, *args, **options):
        self.stdout.write('Seeding menu items and role permissions...')
        
        # Step 1: Create menu items
        self.stdout.write('\n--- Creating Menu Items ---')
        menu_items_map = {}
        created_menus = 0
        updated_menus = 0
        
        for item in MENU_ITEMS:
            parent = None
            if item['parent']:
                parent = menu_items_map.get(item['parent'])
            
            menu_item, created = MenuItemType.objects.update_or_create(
                menu_id=item['menu_id'],
                defaults={
                    'menu_name': item['menu_name'],
                    'parent_menu': parent,
                    'menu_order': item['order'],
                    'is_active': True,
                }
            )
            menu_items_map[item['menu_id']] = menu_item
            
            if created:
                created_menus += 1
            else:
                updated_menus += 1
        
        self.stdout.write(self.style.SUCCESS(
            f'Menu items: Created {created_menus}, Updated {updated_menus}'
        ))
        
        # Step 2: Create role permissions
        self.stdout.write('\n--- Creating Role Permissions ---')
        
        for role_key, permissions in ROLE_PERMISSIONS.items():
            try:
                role = Role.objects.get(role_key=role_key)
            except Role.DoesNotExist:
                self.stdout.write(self.style.WARNING(
                    f'Role {role_key} not found - skipping'
                ))
                continue
            
            default_perms = permissions.get('_default', (False, False, False, False, False))
            created_perms = 0
            updated_perms = 0
            
            for menu_item in MenuItemType.objects.all():
                # Get specific permission or use default
                perms = permissions.get(menu_item.menu_id, default_perms)
                
                _, created = RolePermission.objects.update_or_create(
                    role=role,
                    menu_item=menu_item,
                    defaults={
                        'can_access': perms[0],
                        'can_view': perms[1],
                        'can_create': perms[2],
                        'can_edit': perms[3],
                        'can_delete': perms[4],
                    }
                )
                
                if created:
                    created_perms += 1
                else:
                    updated_perms += 1
            
            self.stdout.write(self.style.SUCCESS(
                f'{role.role_name}: Created {created_perms}, Updated {updated_perms} permissions'
            ))
        
        # Step 3: Summary
        total_menus = MenuItemType.objects.count()
        total_permissions = RolePermission.objects.count()
        
        self.stdout.write(self.style.SUCCESS(
            f'\n✅ Seeding complete!'
        ))
        self.stdout.write(f'Total menu items: {total_menus}')
        self.stdout.write(f'Total role permissions: {total_permissions}')
        
        # Show permission summary per role
        self.stdout.write('\n--- Permission Summary ---')
        for role in Role.objects.filter(is_system_role=True):
            access_count = RolePermission.objects.filter(
                role=role, can_access=True
            ).count()
            self.stdout.write(f'{role.role_name}: {access_count}/{total_menus} menus accessible')




