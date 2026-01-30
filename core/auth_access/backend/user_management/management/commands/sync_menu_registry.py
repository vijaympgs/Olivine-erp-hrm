import os
import json
import re
from django.core.management.base import BaseCommand
from Core.auth_access.backend.user_management.models import ERPMenuItem

class Command(BaseCommand):
    help = 'Synchronize and verify ERP Menu Items against the frontend menuConfig.ts'

    def add_arguments(self, parser):
        parser.add_argument('--check', action='store_true', help='Compare DB with menuConfig.ts')
        parser.add_argument('--backup', action='store_true', help='Backup DB menu items to registry JSON')
        parser.add_argument('--restore', type=str, help='Restore/Update DB from a JSON backup file')
        parser.add_argument('--output', type=str, default='menu_registry_backup.json', help='Output file name for backup')

    def handle(self, *args, **options):
        if options['backup']:
            self.handle_backup(options['output'])
        elif options['restore']:
            self.handle_restore(options['restore'])
        elif options['check']:
            self.handle_check()
        else:
            self.print_help('manage.py', 'sync_menu_registry')

    def handle_backup(self, output_file):
        self.stdout.write(f"Backing up ERPMenuItem table to {output_file}...")
        items = ERPMenuItem.objects.all().order_by('module_name', 'menu_order')
        data = []
        for item in items:
            data.append({
                'menu_id': item.menu_id,
                'menu_name': item.menu_name,
                'parent_menu_id': item.parent_menu.menu_id if item.parent_menu else None,
                'module_name': item.module_name,
                'submodule': item.submodule,
                'view_type': item.view_type,
                'applicable_toolbar_config': item.applicable_toolbar_config,
                'original_toolbar_string': item.original_toolbar_string,
                'route_path': item.route_path,
                'menu_order': item.menu_order,
                'is_active': item.is_active
            })
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        
        self.stdout.write(self.style.SUCCESS(f"Successfully backed up {len(data)} items."))

    def handle_check(self):
        self.stdout.write("Comparing DB with frontend menuConfig.ts...")
        # Path to menuConfig.ts
        config_path = os.path.join(os.getcwd(), '..', 'frontend', 'src', 'app', 'menuConfig.tsx')
        if not os.path.exists(config_path):
             config_path = os.path.join(os.getcwd(), '..', 'frontend', 'src', 'app', 'menuConfig.ts')
        
        if not os.path.exists(config_path):
            self.stdout.write(self.style.ERROR(f"Could not find menuConfig.ts at {config_path}"))
            return

        with open(config_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Simple regex to find IDs from the TS file
        intent_ids = re.findall(r"id:\s*'([^']*)'", content)
        intent_ids = [i for i in intent_ids if not i.startswith('divider')]

        db_items = ERPMenuItem.objects.all()
        db_ids = set(db_items.values_list('menu_id', flat=True))
        
        missing_in_db = [i for i in intent_ids if i not in db_ids]
        orphans_in_db = [i for i in db_ids if i not in intent_ids and i not in ['retail', 'finance', 'crm', 'hr']] # Roots might be different

        self.stdout.write(f"\n--- SYNC REPORT ---")
        self.stdout.write(f"Total entries in menuConfig.ts: {len(intent_ids)}")
        self.stdout.write(f"Total entries in DB: {len(db_ids)}")
        
        if missing_in_db:
            self.stdout.write(self.style.WARNING(f"⚠️ MISSING IN DATABASE ({len(missing_in_db)}):"))
            for mid in missing_in_db[:10]:
                self.stdout.write(f"  - {mid}")
            if len(missing_in_db) > 10: self.stdout.write(f"  ... and {len(missing_in_db)-10} more")
        else:
            self.stdout.write(self.style.SUCCESS("✅ All frontend IDs are present in Database."))

        # Check for empty toolbars
        empty_toolbars = db_items.filter(applicable_toolbar_config__isnull=True) | db_items.filter(applicable_toolbar_config='')
        if empty_toolbars.exists():
            self.stdout.write(self.style.WARNING(f"⚠️ EMPTY TOOLBARS ({empty_toolbars.count()}):"))
            for item in empty_toolbars[:5]:
                self.stdout.write(f"  - {item.menu_id} ({item.menu_name})")
        else:
            self.stdout.write(self.style.SUCCESS("✅ All DB items have a toolbar configuration."))

        # Check for submodule coverage
        missing_sub = db_items.filter(submodule__isnull=True) | db_items.filter(submodule='')
        retail_missing_sub = missing_sub.filter(module_name='RETAIL')
        if retail_missing_sub.exists():
            self.stdout.write(self.style.WARNING(f"⚠️ RETAIL ITEMS MISSING SUBMODULE ({retail_missing_sub.count()}):"))
            for item in retail_missing_sub[:5]:
                self.stdout.write(f"  - {item.menu_id}")

    def handle_restore(self, file_path):
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
            return

        self.stdout.write(f"Restoring/Updating Menu Registry from {file_path}...")
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        count = 0
        for item_data in data:
            parent = None
            if item_data['parent_menu_id']:
                parent = ERPMenuItem.objects.filter(menu_id=item_data['parent_menu_id']).first()
            
            ERPMenuItem.objects.update_or_create(
                menu_id=item_data['menu_id'],
                defaults={
                    'menu_name': item_data['menu_name'],
                    'parent_menu': parent,
                    'module_name': item_data['module_name'],
                    'submodule': item_data.get('submodule'),
                    'view_type': item_data.get('view_type', 'TRANSACTION'),
                    'applicable_toolbar_config': item_data.get('applicable_toolbar_config'),
                    'original_toolbar_string': item_data.get('original_toolbar_string'),
                    'route_path': item_data.get('route_path'),
                    'menu_order': item_data.get('menu_order', 0),
                    'is_active': item_data.get('is_active', True)
                }
            )
            count += 1
        
        self.stdout.write(self.style.SUCCESS(f"Successfully processed {count} items from backup."))
