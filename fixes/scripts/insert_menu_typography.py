#!/usr/bin/env python3
"""
Menu Typography Insertion Script
Inserts menu typography controls into LayoutSettingsPage.tsx and layoutConfig.ts
Idempotent, creates backups, and logs all changes.
"""

import os
import shutil
from datetime import datetime

# File paths
LAYOUT_SETTINGS_PAGE = r'c:\00mindra\olivine-platform\frontend\src\pages\admin\LayoutSettingsPage.tsx'
LAYOUT_CONFIG = r'c:\00mindra\olivine-platform\frontend\src\config\layoutConfig.ts'
SNIPPET_FILE = r'c:\00mindra\olivine-platform\.agent\menu_typography_snippet.tsx'

# Anchors for insertion
LAYOUT_PAGE_ANCHOR = '                        {/* Feature Toggles */}'
CONFIG_ANCHOR = "        root.style.setProperty('--sidebar-panel-active-color', this.config.sidebar.panel.activeItemColor);"

# Check markers (for idempotency)
LAYOUT_PAGE_MARKER = '{/* Menu Typography */}'
CONFIG_MARKER = "// Menu Text Typography"

def backup_file(filepath):
    """Create a timestamped backup of the file"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = f"{filepath}.{timestamp}.bak"
    shutil.copy2(filepath, backup_path)
    print(f"✅ Backup created: {backup_path}")
    return backup_path

def read_file(filepath):
    """Read file content"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    """Write content to file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def insert_layout_page_section():
    """Insert Menu Typography section into LayoutSettingsPage.tsx"""
    print("\n=== Processing LayoutSettingsPage.tsx ===")
    
    # Check if file exists
    if not os.path.exists(LAYOUT_SETTINGS_PAGE):
        print(f"❌ ERROR: File not found: {LAYOUT_SETTINGS_PAGE}")
        return False
    
    # Read current content
    content = read_file(LAYOUT_SETTINGS_PAGE)
    
    # Check if already inserted (idempotency)
    if LAYOUT_PAGE_MARKER in content:
        print(f"⚠️  Menu Typography section already exists. Skipping insertion.")
        return True
    
    # Check if anchor exists
    if LAYOUT_PAGE_ANCHOR not in content:
        print(f"❌ ERROR: Anchor not found: {LAYOUT_PAGE_ANCHOR}")
        print("   Cannot safely insert. File structure may have changed.")
        return False
    
    # Read snippet
    if not os.path.exists(SNIPPET_FILE):
        print(f"❌ ERROR: Snippet file not found: {SNIPPET_FILE}")
        return False
    
    snippet = read_file(SNIPPET_FILE)
    
    # Create backup
    backup_file(LAYOUT_SETTINGS_PAGE)
    
    # Insert snippet before the anchor
    new_content = content.replace(
        LAYOUT_PAGE_ANCHOR,
        snippet + '\n\n' + LAYOUT_PAGE_ANCHOR
    )
    
    # Verify insertion happened
    if new_content == content:
        print("❌ ERROR: Insertion failed. Content unchanged.")
        return False
    
    # Write new content
    write_file(LAYOUT_SETTINGS_PAGE, new_content)
    print(f"✅ Menu Typography section inserted successfully")
    print(f"   Location: Before '{LAYOUT_PAGE_ANCHOR}'")
    
    return True

def insert_config_css_variables():
    """Insert CSS variable setters into layoutConfig.ts"""
    print("\n=== Processing layoutConfig.ts ===")
    
    # Check if file exists
    if not os.path.exists(LAYOUT_CONFIG):
        print(f"❌ ERROR: File not found: {LAYOUT_CONFIG}")
        return False
    
    # Read current content
    content = read_file(LAYOUT_CONFIG)
    
    # Check if already inserted (idempotency)
    if CONFIG_MARKER in content:
        print(f"⚠️  CSS variables already exist. Skipping insertion.")
        return True
    
    # Check if anchor exists
    if CONFIG_ANCHOR not in content:
        print(f"❌ ERROR: Anchor not found: {CONFIG_ANCHOR}")
        print("   Cannot safely insert. File structure may have changed.")
        return False
    
    # CSS variables to insert
    css_variables = """
        // Menu Text Typography
        root.style.setProperty('--menu-level0-font-size', this.config.sidebar.menuText.level0FontSize);
        root.style.setProperty('--menu-level0-font-weight', String(this.config.sidebar.menuText.level0FontWeight));
        root.style.setProperty('--menu-level1-font-size', this.config.sidebar.menuText.level1FontSize);
        root.style.setProperty('--menu-level1-font-weight', String(this.config.sidebar.menuText.level1FontWeight));
        root.style.setProperty('--menu-level2-font-size', this.config.sidebar.menuText.level2FontSize);
        root.style.setProperty('--menu-level2-font-weight', String(this.config.sidebar.menuText.level2FontWeight));
        root.style.setProperty('--menu-level3-font-size', this.config.sidebar.menuText.level3FontSize);
        root.style.setProperty('--menu-level3-font-weight', String(this.config.sidebar.menuText.level3FontWeight));
"""
    
    # Create backup
    backup_file(LAYOUT_CONFIG)
    
    # Insert after the anchor
    new_content = content.replace(
        CONFIG_ANCHOR,
        CONFIG_ANCHOR + css_variables
    )
    
    # Verify insertion happened
    if new_content == content:
        print("❌ ERROR: Insertion failed. Content unchanged.")
        return False
    
    # Write new content
    write_file(LAYOUT_CONFIG, new_content)
    print(f"✅ CSS variables inserted successfully")
    print(f"   Location: After '{CONFIG_ANCHOR[:50]}...'")
    
    return True

def main():
    """Main execution"""
    print("=" * 70)
    print("MENU TYPOGRAPHY INSERTION SCRIPT")
    print("=" * 70)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Track success
    success = True
    
    # Insert into LayoutSettingsPage.tsx
    if not insert_layout_page_section():
        success = False
    
    # Insert into layoutConfig.ts
    if not insert_config_css_variables():
        success = False
    
    # Summary
    print("\n" + "=" * 70)
    if success:
        print("✅ ALL INSERTIONS COMPLETED SUCCESSFULLY")
    else:
        print("❌ SOME INSERTIONS FAILED - CHECK ERRORS ABOVE")
    print("=" * 70)
    
    return 0 if success else 1

if __name__ == '__main__':
    exit(main())
