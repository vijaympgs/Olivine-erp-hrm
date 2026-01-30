"""
Test script for toolbar permission system
Tests the backend API and permission resolution
"""
import os
import sys
import django

# Setup Django
sys.path.insert(0, 'c:/00mindra/olivine-erp-platform/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.dev')
django.setup()

from django.contrib.auth import get_user_model
from core.auth_access.backend.user_management.models import ERPMenuItem, RolePermission, Role
from core.auth_access.backend.user_management.services.toolbar_permission_service import resolve_toolbar_permissions

User = get_user_model()

print("=" * 80)
print("TOOLBAR PERMISSION SYSTEM - TEST SUITE")
print("=" * 80)

# Test 1: Check if ERPMenuItem exists
print("\n[TEST 1] Checking ERPMenuItem for UOM Setup...")
try:
    uom_item = ERPMenuItem.objects.get(menu_id='INVENTORY_UOM_SETUP')
    print(f"✅ Found: {uom_item.menu_name}")
    print(f"   Toolbar Config: {uom_item.applicable_toolbar_config}")
except ERPMenuItem.DoesNotExist:
    print("❌ ERPMenuItem 'INVENTORY_UOM_SETUP' not found")
    print("   Available menu items:")
    for item in ERPMenuItem.objects.filter(menu_id__icontains='UOM')[:5]:
        print(f"   - {item.menu_id}: {item.menu_name}")

# Test 2: Check if admin user exists
print("\n[TEST 2] Checking admin user...")
try:
    admin_user = User.objects.get(username='admin')
    print(f"✅ Found admin user: {admin_user.username} (ID: {admin_user.id})")
    print(f"   Is superuser: {admin_user.is_superuser}")
except User.DoesNotExist:
    print("❌ Admin user not found")
    print("   Creating admin user...")
    admin_user = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print(f"✅ Created admin user (ID: {admin_user.id})")

# Test 3: Test permission resolution for admin
print("\n[TEST 3] Testing permission resolution for admin user...")
try:
    result = resolve_toolbar_permissions(admin_user.id, 'INVENTORY_UOM_SETUP', 'VIEW')
    print(f"✅ Permission resolution successful!")
    print(f"   Menu ID: {result['menu_id']}")
    print(f"   Mode: {result['mode']}")
    print(f"   Toolbar String: {result['toolbar_string']}")
    print(f"   Permission Mask: {result['permission_mask']}")
    print(f"   Allowed Characters: {result['allowed_characters']}")
    print(f"   Allowed Actions: {result['allowed_actions']}")
    
    if 'error' in result:
        print(f"❌ Error: {result['error']}")
except Exception as e:
    print(f"❌ Error during resolution: {str(e)}")
    import traceback
    traceback.print_exc()

# Test 4: Test permission resolution for NEW mode
print("\n[TEST 4] Testing permission resolution for NEW mode...")
try:
    result = resolve_toolbar_permissions(admin_user.id, 'INVENTORY_UOM_SETUP', 'NEW')
    print(f"✅ Permission resolution successful!")
    print(f"   Mode: {result['mode']}")
    print(f"   Allowed Characters: {result['allowed_characters']}")
    print(f"   Allowed Actions: {result['allowed_actions']}")
    
    # Verify Mode Law: NEW should only show S, C, K, X, B, G, ?
    expected_chars = ['S', 'C', 'K', 'X']
    actual_chars = result['allowed_characters']
    mode_law_passed = all(c in expected_chars + ['B', 'G', '?'] for c in actual_chars)
    
    if mode_law_passed:
        print(f"✅ Mode Law PASSED: Only S,C,K,X,B,G,? shown in NEW mode")
    else:
        print(f"❌ Mode Law FAILED: Unexpected characters in NEW mode")
        print(f"   Expected: S,C,K,X (+ optional B,G,?)")
        print(f"   Got: {actual_chars}")
except Exception as e:
    print(f"❌ Error: {str(e)}")

# Test 5: Check RolePermission model fields
print("\n[TEST 5] Checking RolePermission model fields...")
try:
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute("PRAGMA table_info(role_permissions)")
        columns = cursor.fetchall()
        
    field_names = [col[1] for col in columns]
    
    if 'toolbar_string' in field_names:
        print("✅ Field 'toolbar_string' exists")
    else:
        print("❌ Field 'toolbar_string' NOT found")
    
    if 'toolbar_permissions' in field_names:
        print("✅ Field 'toolbar_permissions' exists")
    else:
        print("❌ Field 'toolbar_permissions' NOT found")
    
    print(f"\n   All fields: {', '.join(field_names)}")
except Exception as e:
    print(f"❌ Error checking fields: {str(e)}")

print("\n" + "=" * 80)
print("TEST SUITE COMPLETE")
print("=" * 80)




