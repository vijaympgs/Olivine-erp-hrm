#!/usr/bin/env python
"""Check ERPMenuItem admin configuration from file"""
import re

def check_admin_file():
    """Check admin configuration from file"""
    
    print("Checking ERPMenuItem Admin Configuration from File")
    print("=" * 60)
    print()
    
    try:
        with open('backend/core/auth_access/backend/user_management/admin.py', 'r') as f:
            content = f.read()
        
        # Find list_display
        list_display_match = re.search(r'list_display\s*=\s*\[(.*?)\]', content, re.DOTALL)
        if list_display_match:
            list_display_str = list_display_match.group(1)
            # Extract field names
            fields = [f.strip().strip("'").strip('"') for f in list_display_str.split(',') if f.strip()]
            
            print(f"list_display ({len(fields)} columns):")
            for i, field in enumerate(fields, 1):
                print(f"  {i}. {field}")
            print()
        else:
            print("❌ Could not find list_display")
            print()
        
        # Check for table_name method
        if 'def table_name(self, obj):' in content:
            print("✅ table_name method exists in admin.py")
        else:
            print("❌ table_name method NOT found in admin.py")
        print()
        
        # Check for truncated methods
        for method in ['toolbar_list_truncated', 'toolbar_view_truncated', 'toolbar_edit_truncated', 'toolbar_create_truncated']:
            if f'def {method}(self, obj):' in content:
                print(f"✅ {method} method exists in admin.py")
            else:
                print(f"❌ {method} method NOT found in admin.py")
        print()
        
        # Check for list_per_page
        list_per_page_match = re.search(r'list_per_page\s*=\s*(\d+)', content)
        if list_per_page_match:
            print(f"list_per_page: {list_per_page_match.group(1)}")
        else:
            print("list_per_page: Not set (default: 100)")
        print()
        
        # Check for TableNameDisplayMixin
        if 'TableNameDisplayMixin' in content:
            print("⚠️  TableNameDisplayMixin is still imported (may cause conflicts)")
        else:
            print("✅ TableNameDisplayMixin not imported (good)")
        print()
        
        print("=" * 60)
        print("Configuration Summary:")
        print(f"  - Total columns in list_display: {len(fields) if list_display_match else 0}")
        print(f"  - Expected columns: 28")
        print()
        print("If the admin is not showing all columns in the browser:")
        print("1. Restart the Django development server:")
        print("   - Stop the server (Ctrl+C)")
        print("   - Run: python backend/manage.py runserver")
        print()
        print("2. Clear browser cache:")
        print("   - Press Ctrl+Shift+R (hard refresh)")
        print("   - Or clear cache in browser settings")
        print()
        print("3. Check browser console for JavaScript errors")
        print("   - Press F12 to open DevTools")
        print("   - Look for red error messages in Console tab")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    check_admin_file()
