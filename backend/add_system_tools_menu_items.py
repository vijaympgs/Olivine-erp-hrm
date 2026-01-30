#!/usr/bin/env python
"""
Add missing System Tools menu items to the database
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_core.settings.base')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
django.setup()

from django.db import connection

def add_system_tools_menu_items():
    """Add missing System Tools menu items"""
    
    print("ADDING SYSTEM TOOLS MENU ITEMS TO DATABASE")
    print("=" * 80)
    
    # Check existing menu items
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT menu_id, menu_name, module_name, is_active 
            FROM erp_menu_items 
            WHERE module_name = 'SYSTEM_TOOLS' OR menu_id LIKE '%FILE_SEARCH%' OR menu_id LIKE '%VISUAL%' OR menu_id LIKE '%DATAOPS%'
            ORDER BY menu_id
        """)
        existing_items = cursor.fetchall()
        
        if existing_items:
            print(f"Found {len(existing_items)} existing System Tools menu items:")
            for item in existing_items:
                status = "ACTIVE" if item[3] else "INACTIVE"
                print(f"  {item[0]} - {item[1]} ({item[2]}) - {status}")
        else:
            print("No existing System Tools menu items found")
    
    # System Tools menu items to add
    system_tools_items = [
        {
            'menu_id': 'FILE_SEARCH_EXPLORER',
            'menu_name': 'File Search Explorer',
            'module_name': 'SYSTEM_TOOLS',
            'submodule': 'DEVELOPER_TOOLS',
            'toolbar_config': 'NESCKVDXRQF',  # Standard toolbar config
            'route_path': '/admin/file-search',
            'component_name': 'FileSearchExplorerPage',
            'description': 'Search and explore files in the codebase',
            'menu_order': 1,
            'display_order': 1,
            'is_active': True,
            'is_system_menu': True,
            'view_type': 'MASTER',
            'applicable_toolbar_config': 'NESCKVDXRQF'
        },
        {
            'menu_id': 'VISUAL_EXTRACTOR',
            'menu_name': 'Visual Extractor',
            'module_name': 'SYSTEM_TOOLS',
            'submodule': 'DEVELOPER_TOOLS',
            'toolbar_config': 'NESCKVDXRQF',  # Standard toolbar config
            'route_path': '/system-tools/visual-extractor',
            'component_name': 'VisualExtractorPage',
            'description': 'OCR tool for extracting text from images',
            'menu_order': 2,
            'display_order': 2,
            'is_active': True,
            'is_system_menu': True,
            'view_type': 'MASTER',
            'applicable_toolbar_config': 'NESCKVDXRQF'
        },
        {
            'menu_id': 'DATAOPS_STUDIO',
            'menu_name': 'DataOps Studio',
            'module_name': 'SYSTEM_TOOLS',
            'submodule': 'DEVELOPER_TOOLS',
            'toolbar_config': 'NESCKVDXRQF',  # Standard toolbar config
            'route_path': '/system-tools/dataops-studio',
            'component_name': 'DataOpsStudioPage',
            'description': 'Database exploration and operations tool',
            'menu_order': 3,
            'display_order': 3,
            'is_active': True,
            'is_system_menu': True,
            'view_type': 'MASTER',
            'applicable_toolbar_config': 'NESCKVDXRQF'
        }
    ]
    
    print(f"\nAdding {len(system_tools_items)} System Tools menu items...")
    
    added_count = 0
    with connection.cursor() as cursor:
        for item in system_tools_items:
            # Check if item already exists
            cursor.execute("""
                SELECT id FROM erp_menu_items WHERE menu_id = %s
            """, [item['menu_id']])
            
            if cursor.fetchone():
                print(f"[WARNING] {item['menu_id']} already exists - skipping")
                continue
            
            # Insert new menu item
            cursor.execute("""
                INSERT INTO erp_menu_items (
                    menu_id, menu_name, module_name, submodule, toolbar_config,
                    route_path, component_name, description, menu_order, display_order,
                    is_active, is_system_menu, created_at, updated_at,
                    applicable_toolbar_config, original_toolbar_string, view_type
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    datetime('now'), datetime('now'), %s, %s, %s
                )
            """, [
                item['menu_id'], item['menu_name'], item['module_name'], 
                item['submodule'], item['toolbar_config'], item['route_path'],
                item['component_name'], item['description'], item['menu_order'],
                item['display_order'], item['is_active'], item['is_system_menu'],
                item['applicable_toolbar_config'], item['toolbar_config'], item['view_type']
            ])
            
            print(f"[ADDED] {item['menu_id']} - {item['menu_name']}")
            added_count += 1
    
    print(f"\nSummary: Added {added_count} new System Tools menu items")
    
    # Verify the additions
    print("\nAll System Tools menu items after update:")
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT menu_id, menu_name, module_name, is_active 
            FROM erp_menu_items 
            WHERE module_name = 'SYSTEM_TOOLS'
            ORDER BY display_order
        """)
        all_items = cursor.fetchall()
        
        for item in all_items:
            status = "ACTIVE" if item[3] else "INACTIVE"
            print(f"  [{status}] {item[0]} - {item[1]} ({item[2]})")
    
    print("\nSystem Tools menu items setup completed!")

if __name__ == "__main__":
    add_system_tools_menu_items()
