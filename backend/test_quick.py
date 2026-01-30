"""
Quick test of toolbar permission resolution
"""
from django.contrib.auth import get_user_model
from core.auth_access.backend.user_management.models import ERPMenuItem
from core.auth_access.backend.user_management.services.toolbar_permission_service import resolve_toolbar_permissions

User = get_user_model()

print("=" * 80)
print("TOOLBAR PERMISSION SYSTEM - QUICK TEST")
print("=" * 80)

# Get or create admin user
admin, created = User.objects.get_or_create(
    username='admin',
    defaults={'is_superuser': True, 'is_staff': True}
)
if created:
    admin.set_password('admin123')
    admin.save()
    print(f"✅ Created admin user")
else:
    print(f"✅ Found admin user (ID: {admin.id})")

# Check UOM menu item
try:
    uom = ERPMenuItem.objects.get(menu_id='INVENTORY_UOM_SETUP')
    print(f"✅ Found UOM Setup: {uom.applicable_toolbar_config}")
except ERPMenuItem.DoesNotExist:
    print("❌ UOM Setup not found, trying alternatives...")
    items = ERPMenuItem.objects.filter(menu_id__icontains='UOM')[:3]
    for item in items:
        print(f"   - {item.menu_id}")

# Test permission resolution
print("\n[TEST] Resolving permissions for admin in VIEW mode...")
result = resolve_toolbar_permissions(admin.id, 'INVENTORY_UOM_SETUP', 'VIEW')

if 'error' in result:
    print(f"❌ Error: {result['error']}")
else:
    print(f"✅ Success!")
    print(f"   Toolbar: {result['toolbar_string']}")
    print(f"   Mask: {result['permission_mask']}")
    print(f"   Allowed: {result['allowed_actions']}")

print("\n[TEST] Resolving permissions for admin in NEW mode...")
result = resolve_toolbar_permissions(admin.id, 'INVENTORY_UOM_SETUP', 'NEW')

if 'error' in result:
    print(f"❌ Error: {result['error']}")
else:
    print(f"✅ Success!")
    print(f"   Allowed: {result['allowed_actions']}")
    
    # Check Mode Law
    if set(result['allowed_actions']) <= {'save', 'cancel', 'clear', 'exit', 'notes', 'attach', 'help'}:
        print(f"✅ Mode Law PASSED: Only S,C,K,X,B,G,? in NEW mode")
    else:
        print(f"❌ Mode Law FAILED: {result['allowed_actions']}")

print("=" * 80)




