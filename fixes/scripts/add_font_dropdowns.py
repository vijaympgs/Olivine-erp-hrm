#!/usr/bin/env python3
"""
Add Font Family Dropdowns to Menu Typography UI
Inserts font family select dropdowns for each menu level
"""

import re

LAYOUT_SETTINGS_PAGE = r'c:\00mindra\olivine-platform\frontend\src\pages\admin\LayoutSettingsPage.tsx'

def add_font_dropdowns():
    """Add font family dropdown after each font weight dropdown"""
    
    with open(LAYOUT_SETTINGS_PAGE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # For each level (0-3), add a font family dropdown after the font weight dropdown
    levels = [
        ('Level 0 (Module Headers)', 'level0'),
        ('Level 1 (Main Menu Items)', 'level1'),
        ('Level 2 (Submenu Items)', 'level2'),
        ('Level 3 (Nested Submenu)', 'level3'),
    ]
    
    for label, level in levels:
        # Find the pattern: closing </select> and </div> for font weight
        pattern = rf'({level}FontWeight.*?</select>\s*</div>\s*</div>)'
        
        # Replacement: add font family dropdown
        replacement = rf'''\1
                                    <div>
                                        <label className="block text-xs font-medium text-gray-500 mb-1">Font Family</label>
                                        <select
                                            value={{settings.sidebarStyling.menuText.{level}FontFamily}}
                                            onChange={{(e) => handleChange('sidebarStyling', {{ ...settings.sidebarStyling, menuText: {{ ...settings.sidebarStyling.menuText, {level}FontFamily: e.target.value }} }})}}
                                            className="w-full px-2 py-1 border rounded text-sm"
                                        >
                                            {{systemFonts.map(font => (
                                                <option key={{font}} value={{font}}>{{font}}</option>
                                            ))}}
                                        </select>
                                    </div>'''
        
        content = re.sub(pattern, replacement, content, count=1, flags=re.DOTALL)
    
    with open(LAYOUT_SETTINGS_PAGE, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Added font family dropdowns for all 4 levels")

def main():
    print("=" * 70)
    print("ADDING FONT FAMILY DROPDOWNS TO MENU TYPOGRAPHY")
    print("=" * 70)
    
    add_font_dropdowns()
    
    print("\n" + "=" * 70)
    print("✅ FONT FAMILY DROPDOWNS ADDED SUCCESSFULLY")
    print("=" * 70)

if __name__ == '__main__':
    main()
