"""
Fix benchmark screens - UOM and Purchase Orders
"""
from django.core.management.base import BaseCommand
from core.auth_access.backend.user_management.models import ERPMenuItem

class Command(BaseCommand):
    help = 'Fix UOM and Purchase Order benchmark configurations'

    def handle(self, *args, **kwargs):
        self.stdout.write("\n" + "="*80)
        self.stdout.write("FIXING BENCHMARK SCREENS")
        self.stdout.write("="*80 + "\n")
        
        # Fix 1: UOM Setup
        self.stdout.write("\n1. Fixing UOM Setup...")
        self.stdout.write("-" * 80)
        
        try:
            uom = ERPMenuItem.objects.get(menu_id='inventory_uom_setup')
            self.stdout.write(f"   Found: {uom.menu_name}")
            self.stdout.write(f"   Current config: {uom.applicable_toolbar_config}")
            self.stdout.write(f"   Current view_type: {uom.view_type}")
            
            # Update to match frontend and correct type
            uom.menu_id = 'INVENTORY_UOM_SETUP'
            uom.view_type = 'MASTER'
            uom.applicable_toolbar_config = 'NESCKVDXRQF'
            uom.save()
            
            self.stdout.write(self.style.SUCCESS(f"   ✅ Updated UOM Setup:"))
            self.stdout.write(f"      menu_id: INVENTORY_UOM_SETUP")
            self.stdout.write(f"      view_type: MASTER")
            self.stdout.write(f"      config: NESCKVDXRQF")
        except ERPMenuItem.DoesNotExist:
            self.stdout.write(self.style.ERROR("   ❌ UOM entry not found!"))
        
        # Fix 2: Purchase Orders (verify it's correct)
        self.stdout.write("\n2. Verifying Purchase Orders (Transaction)...")
        self.stdout.write("-" * 80)
        
        try:
            po = ERPMenuItem.objects.get(menu_id='PURCHASE_ORDERS')
            self.stdout.write(f"   Found: {po.menu_name}")
            self.stdout.write(f"   Config: {po.applicable_toolbar_config}")
            self.stdout.write(f"   View Type: {po.view_type}")
            
            if po.applicable_toolbar_config == 'NESCKZTJAVPMRDX1234QF' and po.view_type == 'TRANSACTION':
                self.stdout.write(self.style.SUCCESS("   ✅ Purchase Orders config is correct!"))
            else:
                self.stdout.write(self.style.WARNING("   ⚠️ Purchase Orders config needs update"))
                po.applicable_toolbar_config = 'NESCKZTJAVPMRDX1234QF'
                po.view_type = 'TRANSACTION'
                po.save()
                self.stdout.write(self.style.SUCCESS("   ✅ Updated!"))
        except ERPMenuItem.DoesNotExist:
            self.stdout.write(self.style.ERROR("   ❌ Purchase Orders entry not found!"))
        
        # Fix 3: Create Purchase Orders List View entry if it doesn't exist
        self.stdout.write("\n3. Checking Purchase Orders List View...")
        self.stdout.write("-" * 80)
        
        list_view, created = ERPMenuItem.objects.get_or_create(
            menu_id='purchase-orders',
            defaults={
                'menu_name': 'Purchase Orders List',
                'view_type': 'LIST_VIEW',
                'applicable_toolbar_config': 'NRQFX',
                'route_path': '/procurement/purchase-orders',
                'module_name': 'RETAIL',
                'submodule_name': 'PROCUREMENT',
                'is_active': True
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS("   ✅ Created Purchase Orders List View entry"))
        else:
            self.stdout.write(f"   Found existing entry: {list_view.menu_name}")
            # Update if needed
            if list_view.applicable_toolbar_config != 'NRQFX' or list_view.view_type != 'LIST_VIEW':
                list_view.applicable_toolbar_config = 'NRQFX'
                list_view.view_type = 'LIST_VIEW'
                list_view.save()
                self.stdout.write(self.style.SUCCESS("   ✅ Updated List View config"))
            else:
                self.stdout.write(self.style.SUCCESS("   ✅ List View config is correct"))
        
        self.stdout.write("\n" + "="*80)
        self.stdout.write("BENCHMARK FIXES COMPLETE!")
        self.stdout.write("="*80 + "\n")
        
        # Summary
        self.stdout.write("\nSUMMARY:")
        self.stdout.write("-" * 80)
        
        uom_final = ERPMenuItem.objects.get(menu_id='INVENTORY_UOM_SETUP')
        po_final = ERPMenuItem.objects.get(menu_id='PURCHASE_ORDERS')
        po_list_final = ERPMenuItem.objects.get(menu_id='purchase-orders')
        
        self.stdout.write(f"\n✅ UOM Setup:")
        self.stdout.write(f"   menu_id: {uom_final.menu_id}")
        self.stdout.write(f"   view_type: {uom_final.view_type}")
        self.stdout.write(f"   config: {uom_final.applicable_toolbar_config}")
        
        self.stdout.write(f"\n✅ Purchase Orders (Transaction):")
        self.stdout.write(f"   menu_id: {po_final.menu_id}")
        self.stdout.write(f"   view_type: {po_final.view_type}")
        self.stdout.write(f"   config: {po_final.applicable_toolbar_config}")
        
        self.stdout.write(f"\n✅ Purchase Orders (List View):")
        self.stdout.write(f"   menu_id: {po_list_final.menu_id}")
        self.stdout.write(f"   view_type: {po_list_final.view_type}")
        self.stdout.write(f"   config: {po_list_final.applicable_toolbar_config}")
        
        self.stdout.write("\n" + "="*80 + "\n")




