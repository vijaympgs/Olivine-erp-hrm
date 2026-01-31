#!/usr/bin/env python
"""Verify ERPMenuItem admin configuration"""
import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.base')
django.setup()

from django.contrib import admin
from core.auth_access.backend.user_management.models import ERPMenuItem

def verify_admin():
    """Verify admin configuration"""
    
    print("Verifying ERPMenuItem Admin Configuration")
    print("=" * 60)
    print()
    
    # Get the admin class
    try:
        admin_site = admin.site
        model_admin = admin_site._registry[ERPMenuItem]
        
        print(f"Admin Class: {model_admin.__class__.__name__}")
        print(f"Model: {model_admin.model}")
        print()
        
        # Check list_display
        print(f"list_display ({len(model_admin.list_display)} columns):")
        for i, field in enumerate(model_admin.list_display, 1):
            print(f"  {i}. {field}")
        print()
        
        # Check list_per_page
        print(f"list_per_page: {model_admin.list_per_page}")
        print()
        
        # Check if table_name method exists
        if hasattr(model_admin, 'table_name'):
            print("✅ table_name method exists")
        else:
            print("❌ table_name method NOT found")
        print()
        
        # Check truncated methods
        for method in ['toolbar_list_truncated', 'toolbar_view_truncated', 'toolbar_edit_truncated', 'toolbar_create_truncated']:
            if hasattr(model_admin, method):
                print(f"✅ {method} method exists")
            else:
                print(f"❌ {method} method NOT found")
        print()
        
        # Check readonly_fields
        print(f"readonly_fields: {model_admin.readonly_fields}")
        print()
        
        print("=" * 60)
        print("NOTE: If the admin is not showing all columns, you may need to:")
        print("1. Restart the Django development server")
        print("2. Clear browser cache")
        print("3. Check if there are any JavaScript errors in the browser console")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    verify_admin()
