"""
Management command to seed all menu items from a central JSON manifest.
This ensures a single source of truth for the ERP Menu Registry.
"""
import os
import json
from django.core.management.base import BaseCommand
from core.auth_access.backend.user_management.models import MenuItemType

class Command(BaseCommand):
    help = 'Seeds all menu items from the registry/menu_manifest.json file.'

    def handle(self, *args, **options):
        # Path to the manifest file
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        manifest_path = os.path.join(base_dir, 'registry', 'menu_manifest.json')

        if not os.path.exists(manifest_path):
            self.stdout.write(self.style.ERROR(f"Manifest file not found at {manifest_path}"))
            return

        self.stdout.write(f'Seeding menu items from manifest: {manifest_path}')

        with open(manifest_path, 'r', encoding='utf-8') as f:
            menu_items = json.load(f)

        created_count = 0
        updated_count = 0

        # Step 1: Pre-fetch all IDs to avoid redundant DB queries
        all_ids = {item['menu_id'] for item in menu_items}
        
        # Step 2: Iterate and update
        for item_data in menu_items:
            parent_menu_obj = None
            if item_data.get('parent_menu_id'):
                try:
                    parent_menu_obj = MenuItemType.objects.get(menu_id=item_data['parent_menu_id'])
                except MenuItemType.DoesNotExist:
                    # Parent might be created later in the loop if not ordered hierarchically
                    # but our backup is sorted.
                    pass

            menu_item, created = MenuItemType.objects.update_or_create(
                menu_id=item_data['menu_id'],
                defaults={
                    'menu_name': item_data['menu_name'],
                    'parent_menu': parent_menu_obj,
                    'module_name': item_data['module_name'],
                    'submodule': item_data.get('submodule'),
                    'view_type': item_data.get('view_type', 'TRANSACTION'),
                    'menu_order': item_data.get('menu_order', 0),
                    'is_active': item_data.get('is_active', True),
                    'original_toolbar_string': item_data.get('original_toolbar_string'),
                    'applicable_toolbar_config': item_data.get('applicable_toolbar_config'),
                    'route_path': item_data.get('route_path')
                }
            )

            if created:
                created_count += 1
            else:
                updated_count += 1

        self.stdout.write(self.style.SUCCESS(
            f'\n✅ Seeding complete! Total: {len(menu_items)}, Created: {created_count}, Updated: {updated_count}'
        ))
