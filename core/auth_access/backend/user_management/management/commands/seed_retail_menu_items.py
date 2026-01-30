"""
Management command to seed retail menu items from menuConfig.ts
"""
from django.core.management.base import BaseCommand
from core.auth_access.backend.user_management.models import MenuItemType


class Command(BaseCommand):
    help = 'Seeds retail menu items from the frontend menuConfig.ts structure'

    def handle(self, *args, **options):
        self.stdout.write('Seeding retail menu items...')

        # Define retail menu structure based on menuConfig.ts
        retail_menu_items = [
            # User & Permissions Section
            {
                'menu_id': 'security',
                'menu_name': 'User & Permissions',
                'parent_menu': None,
                'module_name': 'retail',
                'menu_order': 1
            },
            {
                'menu_id': 'user-permissions',
                'menu_name': 'Permission Matrix',
                'parent_menu': 'security',
                'module_name': 'retail',
                'menu_order': 1
            },
            {
                'menu_id': 'pos-terminal-configuration',
                'menu_name': 'Registers',
                'parent_menu': 'security',
                'module_name': 'retail',
                'menu_order': 2
            },

            # Merchandising Section (Master Data Management)
            {
                'menu_id': 'master-data',
                'menu_name': 'Merchandising',
                'parent_menu': None,
                'module_name': 'retail',
                'menu_order': 2
            },
            {
                'menu_id': 'attributes',
                'menu_name': 'Variants',
                'parent_menu': 'master-data',
                'module_name': 'retail',
                'menu_order': 1
            },
            {
                'menu_id': 'item-master',
                'menu_name': 'Catalog',
                'parent_menu': 'master-data',
                'module_name': 'retail',
                'menu_order': 2
            },
            {
                'menu_id': 'uom',
                'menu_name': 'UOM',
                'parent_menu': 'master-data',
                'module_name': 'retail',
                'menu_order': 3
            },
            {
                'menu_id': 'customer-list',
                'menu_name': 'Directory',
                'parent_menu': 'master-data',
                'module_name': 'retail',
                'menu_order': 4
            },
            {
                'menu_id': 'suppliers',
                'menu_name': 'Vendors',
                'parent_menu': 'master-data',
                'module_name': 'retail',
                'menu_order': 5
            },
            {
                'menu_id': 'categories',
                'menu_name': 'Hierarchy',
                'parent_menu': 'master-data',
                'module_name': 'retail',
                'menu_order': 6
            },
            {
                'menu_id': 'brands',
                'menu_name': 'Brands',
                'parent_menu': 'master-data',
                'module_name': 'retail',
                'menu_order': 7
            },
            {
                'menu_id': 'pricing-master',
                'menu_name': 'Pricing',
                'parent_menu': 'master-data',
                'module_name': 'retail',
                'menu_order': 8
            },
            {
                'menu_id': 'price-lists-master',
                'menu_name': 'Price Lists',
                'parent_menu': 'master-data',
                'module_name': 'retail',
                'menu_order': 9
            },

            # Organization Setup Section
            {
                'menu_id': 'organization-setup',
                'menu_name': 'Organization Setup',
                'parent_menu': None,
                'module_name': 'retail',
                'menu_order': 3
            },
            {
                'menu_id': 'organization-center',
                'menu_name': 'Organization Center',
                'parent_menu': 'organization-setup',
                'module_name': 'retail',
                'menu_order': 1
            },
            {
                'menu_id': 'company-setup',
                'menu_name': 'Company Setup',
                'parent_menu': 'organization-setup',
                'module_name': 'retail',
                'menu_order': 2
            },

            # Store Ops & Sales & Inventory Section
            {
                'menu_id': 'retail',
                'menu_name': 'Store Ops & Sales & Inventory',
                'parent_menu': None,
                'module_name': 'retail',
                'menu_order': 4
            },
            {
                'menu_id': 'pos',
                'menu_name': 'Store Ops',
                'parent_menu': 'retail',
                'module_name': 'retail',
                'menu_order': 1
            },
            {
                'menu_id': 'sales',
                'menu_name': 'Sales',
                'parent_menu': 'retail',
                'module_name': 'retail',
                'menu_order': 2
            },
            {
                'menu_id': 'inventory',
                'menu_name': 'Inventory',
                'parent_menu': 'retail',
                'module_name': 'retail',
                'menu_order': 3
            },

            # Procurement Section
            {
                'menu_id': 'procurement',
                'menu_name': 'Procurement',
                'parent_menu': None,
                'module_name': 'retail',
                'menu_order': 5
            },
            {
                'menu_id': 'procurement-system-ready',
                'menu_name': 'System ready',
                'parent_menu': 'procurement',
                'module_name': 'retail',
                'menu_order': 1
            },
        ]

        # Create menu items
        created_count = 0
        updated_count = 0

        for item_data in retail_menu_items:
            parent_menu_obj = None
            if item_data['parent_menu']:
                try:
                    parent_menu_obj = MenuItemType.objects.get(menu_id=item_data['parent_menu'])
                except MenuItemType.DoesNotExist:
                    self.stdout.write(
                        self.style.WARNING(
                            f"Parent menu '{item_data['parent_menu']}' not found for '{item_data['menu_id']}'"
                        )
                    )
                    continue

            menu_item, created = MenuItemType.objects.update_or_create(
                menu_id=item_data['menu_id'],
                defaults={
                    'menu_name': item_data['menu_name'],
                    'parent_menu': parent_menu_obj,
                    'module_name': item_data['module_name'],
                    'menu_order': item_data['menu_order'],
                    'is_active': True
                }
            )

            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f"Created menu item: {menu_item.menu_name}")
                )
            else:
                updated_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f"Updated menu item: {menu_item.menu_name}")
                )

        self.stdout.write(
            self.style.SUCCESS(
                f'\nSeeding complete! Created: {created_count}, Updated: {updated_count}'
            )
        )




