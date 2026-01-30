"""
Add POS Business Rules to ERPMenuItem model.
Run: python manage.py runscript add_business_rules_menu
Or execute directly via shell
"""
import os
import sys
import django

# Setup Django
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings')
django.setup()

from Core.auth_access.backend.user_management.models import ERPMenuItem

def run():
    # Get POS parent
    pos = ERPMenuItem.objects.get(menu_id='pos')
    print(f"Found POS parent: ID={pos.id}")
    
    # Create Settings & Rules group if not exists
    settings_group, created = ERPMenuItem.objects.update_or_create(
        menu_id='pos-settings-group',
        defaults={
            'menu_name': 'Settings & Rules',
            'parent_menu': pos,
            'module_name': 'RETAIL',
            'submodule': 'POS',
            'view_type': 'CONFIGURATION',
            'applicable_toolbar_config': 'ESCKXR',
            'route_path': None,
            'menu_order': 3,
            'is_active': True,
            'is_system_menu': True
        }
    )
    status = "CREATED" if created else "UPDATED"
    print(f"Settings group: {status} (ID: {settings_group.id})")
    
    # Create Business Rules entry
    biz_rules, created = ERPMenuItem.objects.update_or_create(
        menu_id='pos-business-rules',
        defaults={
            'menu_name': 'Business Rules',
            'parent_menu': settings_group,
            'module_name': 'RETAIL',
            'submodule': 'POS',
            'view_type': 'CONFIGURATION',
            'applicable_toolbar_config': 'ESCKXR',
            'route_path': '/pos/business-rules',
            'component_name': 'POSBusinessRulesPage',
            'description': 'Vertical-specific business rules and feature flags configuration',
            'menu_order': 2,
            'is_active': True,
            'is_system_menu': True
        }
    )
    status = "CREATED" if created else "UPDATED"
    print(f"Business Rules: {status} (ID: {biz_rules.id})")
    
    # Update Registers to be under Settings group
    registers = ERPMenuItem.objects.filter(menu_id='pos-terminal-configuration').first()
    if registers:
        registers.parent_menu = settings_group
        registers.menu_order = 1
        registers.save()
        print("Registers moved under Settings group")
    
    print("\n✅ Done! POS Business Rules menu item added.")
    
    # Show hierarchy
    print("\n📋 Updated POS Menu Structure:")
    print(f"  └── {pos.menu_name} (ID: {pos.id})")
    for child in ERPMenuItem.objects.filter(parent_menu=pos).order_by('menu_order'):
        print(f"      ├── {child.menu_name} (ID: {child.id})")
        for subchild in ERPMenuItem.objects.filter(parent_menu=child).order_by('menu_order'):
            print(f"      │   ├── {subchild.menu_name} (ID: {subchild.id})")

if __name__ == '__main__':
    run()
