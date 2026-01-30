"""
Django management command to update toolbar configurations
Usage: python backend/manage.py update_toolbar_configs
"""

from django.core.management.base import BaseCommand
from core.auth_access.backend.menu_registry.models import ERPMenuItem


class Command(BaseCommand):
    help = 'Update toolbar configurations for 4 menu items'

    def handle(self, *args, **options):
        updates = [
            {
                'menu_id': 'MOVEMENT_TYPES',
                'new_config': 'NRQFX',
                'description': 'Movement Types (List view)'
            },
            {
                'menu_id': 'VALUATION_METHODS',
                'new_config': 'VRX',
                'description': 'Valuation Methods (View only)'
            },
            {
                'menu_id': 'INV_PARAMETERS',
                'new_config': 'ESCKXR',
                'description': 'Inventory Parameters (Edit-focused)'
            },
            {
                'menu_id': 'APPROVAL_RULES',
                'new_config': 'NRQFX',
                'description': 'Approval Rules (List view)'
            }
        ]

        self.stdout.write("=" * 80)
        self.stdout.write(self.style.SUCCESS("TOOLBAR CONFIGURATION UPDATE"))
        self.stdout.write("=" * 80)
        self.stdout.write("")

        for update in updates:
            try:
                menu_item = ERPMenuItem.objects.get(menu_id=update['menu_id'])
                old_config = menu_item.applicable_toolbar_config or 'None'
                
                self.stdout.write(f"📋 {update['description']}")
                self.stdout.write(f"   Menu ID: {update['menu_id']}")
                self.stdout.write(f"   Current: {old_config}")
                self.stdout.write(f"   New: {update['new_config']}")
                
                menu_item.applicable_toolbar_config = update['new_config']
                menu_item.save()
                
                self.stdout.write(self.style.SUCCESS(f"   ✅ Updated successfully"))
                self.stdout.write("")
                
            except ERPMenuItem.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"❌ Menu item not found: {update['menu_id']}"))
                self.stdout.write("")
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"❌ Error updating {update['menu_id']}: {e}"))
                self.stdout.write("")

        self.stdout.write("=" * 80)
        self.stdout.write(self.style.SUCCESS("UPDATE COMPLETE"))
        self.stdout.write("=" * 80)
        self.stdout.write("")

        # Verify updates
        self.stdout.write("VERIFICATION:")
        self.stdout.write("-" * 80)
        for update in updates:
            try:
                menu_item = ERPMenuItem.objects.get(menu_id=update['menu_id'])
                if menu_item.applicable_toolbar_config == update['new_config']:
                    self.stdout.write(self.style.SUCCESS(f"✅ {update['menu_id']}: {menu_item.applicable_toolbar_config}"))
                else:
                    self.stdout.write(self.style.ERROR(f"❌ {update['menu_id']}: {menu_item.applicable_toolbar_config} (expected {update['new_config']})"))
            except ERPMenuItem.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"❌ {update['menu_id']}: NOT FOUND"))




