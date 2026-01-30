#!/usr/bin/env python3
"""
Add Font Family Support to Menu Typography
Updates all necessary files to support font family selection
"""

import os
import platform

# Detect OS
current_os = platform.system()  # 'Windows', 'Linux', or 'Darwin' (macOS)

# OS-specific font lists
WINDOWS_FONTS = [
    'Segoe UI',
    'Arial',
    'Calibri',
    'Consolas',
    'Courier New',
    'Georgia',
    'Tahoma',
    'Times New Roman',
    'Trebuchet MS',
    'Verdana',
]

LINUX_FONTS = [
    'Ubuntu',
    'DejaVu Sans',
    'Liberation Sans',
    'Noto Sans',
    'Roboto',
    'Droid Sans',
    'FreeSans',
    'Cantarell',
    'Oxygen',
]

# Universal web-safe fonts
UNIVERSAL_FONTS = [
    'Inter',
    'system-ui',
    '-apple-system',
    'sans-serif',
    'monospace',
]

# Default font family
DEFAULT_FONT = 'Segoe UI' if current_os == 'Windows' else 'Ubuntu' if current_os == 'Linux' else 'Inter'

print(f"Detected OS: {current_os}")
print(f"Default Font: {DEFAULT_FONT}")
print(f"Font List: {WINDOWS_FONTS if current_os == 'Windows' else LINUX_FONTS}")

# File paths
LAYOUT_SETTINGS_PAGE = r'c:\00mindra\olivine-platform\frontend\src\pages\admin\LayoutSettingsPage.tsx'
LAYOUT_CONFIG = r'c:\00mindra\olivine-platform\frontend\src\config\layoutConfig.ts'

def add_default_font_families():
    """Add default fontFamily values to LayoutSettingsPage.tsx"""
    print("\n=== Updating LayoutSettingsPage.tsx ===")
    
    with open(LAYOUT_SETTINGS_PAGE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and replace the menuText default values
    old_pattern = """            level0FontSize: '11px',
            level1Color: '#8B8FAF',"""
    
    new_pattern = f"""            level0FontSize: '11px',
            level0FontFamily: '{DEFAULT_FONT}',
            level1Color: '#8B8FAF',"""
    
    if old_pattern in content:
        content = content.replace(old_pattern, new_pattern)
        print("✅ Added level0FontFamily default")
    
    # Add other levels
    replacements = [
        ("""            level1FontSize: '12px',
            level2Color: '#8B8FAF',""",
         f"""            level1FontSize: '12px',
            level1FontFamily: '{DEFAULT_FONT}',
            level2Color: '#8B8FAF',"""),
        
        ("""            level2FontSize: '12px',
            level3Color: '#8B8FAF',""",
         f"""            level2FontSize: '12px',
            level2FontFamily: '{DEFAULT_FONT}',
            level3Color: '#8B8FAF',"""),
        
        ("""            level3FontSize: '11px',
            hoverColor: '#E7E9F1',""",
         f"""            level3FontSize: '11px',
            level3FontFamily: '{DEFAULT_FONT}',
            hoverColor: '#E7E9F1',"""),
    ]
    
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
    
    # Also update the fallback in useEffect
    fallback_old = """                        level0FontSize: config.sidebar.menuText.level0FontSize || '11px',
                        level1FontSize: config.sidebar.menuText.level1FontSize || '12px',"""
    
    fallback_new = f"""                        level0FontSize: config.sidebar.menuText.level0FontSize || '11px',
                        level0FontFamily: config.sidebar.menuText.level0FontFamily || '{DEFAULT_FONT}',
                        level1FontSize: config.sidebar.menuText.level1FontSize || '12px',
                        level1FontFamily: config.sidebar.menuText.level1FontFamily || '{DEFAULT_FONT}',"""
    
    if fallback_old in content:
        content = content.replace(fallback_old, fallback_new)
    
    # Add remaining fallbacks
    content = content.replace(
        "level2FontSize: config.sidebar.menuText.level2FontSize || '12px',",
        f"level2FontSize: config.sidebar.menuText.level2FontSize || '12px',\n                        level2FontFamily: config.sidebar.menuText.level2FontFamily || '{DEFAULT_FONT}',"
    )
    
    content = content.replace(
        "level3FontSize: config.sidebar.menuText.level3FontSize || '11px',",
        f"level3FontSize: config.sidebar.menuText.level3FontSize || '11px',\n                        level3FontFamily: config.sidebar.menuText.level3FontFamily || '{DEFAULT_FONT}',"
    )
    
    with open(LAYOUT_SETTINGS_PAGE, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Updated all fontFamily defaults in LayoutSettingsPage.tsx")

def update_layout_config():
    """Update layoutConfig.ts with fontFamily properties"""
    print("\n=== Updating layoutConfig.ts ===")
    
    with open(LAYOUT_CONFIG, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update interface
    interface_replacements = [
        ("level0FontSize: string;",
         "level0FontSize: string;\n            level0FontFamily: string;"),
        ("level1FontSize: string;",
         "level1FontSize: string;\n            level1FontFamily: string;"),
        ("level2FontSize: string;",
         "level2FontSize: string;\n            level2FontFamily: string;"),
        ("level3FontSize: string;",
         "level3FontSize: string;\n            level3FontFamily: string;"),
    ]
    
    for old, new in interface_replacements:
        content = content.replace(old, new, 1)
    
    # Update default config
    default_replacements = [
        ("level0FontSize: '11px',",
         f"level0FontSize: '11px',\n            level0FontFamily: '{DEFAULT_FONT}',"),
        ("level1FontSize: '12px',",
         f"level1FontSize: '12px',\n            level1FontFamily: '{DEFAULT_FONT}',"),
        ("level2FontSize: '12px',",
         f"level2FontSize: '12px',\n            level2FontFamily: '{DEFAULT_FONT}',"),
        ("level3FontSize: '11px',",
         f"level3FontSize: '11px',\n            level3FontFamily: '{DEFAULT_FONT}',"),
    ]
    
    for old, new in default_replacements:
        content = content.replace(old, new, 1)
    
    with open(LAYOUT_CONFIG, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Updated layoutConfig.ts with fontFamily properties")

def main():
    print("=" * 70)
    print("FONT FAMILY SUPPORT - MENU TYPOGRAPHY")
    print("=" * 70)
    
    add_default_font_families()
    update_layout_config()
    
    print("\n" + "=" * 70)
    print("✅ FONT FAMILY SUPPORT ADDED SUCCESSFULLY")
    print("=" * 70)
    print(f"\nDefault Font: {DEFAULT_FONT}")
    print("\nNext: Add UI controls for font selection in LayoutSettingsPage.tsx")

if __name__ == '__main__':
    main()
