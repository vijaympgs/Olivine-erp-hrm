#!/usr/bin/env python
"""Add table_name to all HRM admin classes"""
import re

def add_table_name_to_admin():
    """Add table_name to all DefaultAdmin classes"""
    
    file_path = 'HRM/backend/hrm/admin.py'
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Find all DefaultAdmin classes and add table_name to their list_display
    # Pattern: class XDefaultAdmin(TableNameDisplayMixin, admin.ModelAdmin):\n    list_display = [...]
    
    # Split by class definitions
    lines = content.split('\n')
    result = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        result.append(line)
        
        # Check if this is a DefaultAdmin class
        if 'class' in line and 'DefaultAdmin(TableNameDisplayMixin, admin.ModelAdmin):' in line:
            # Look for list_display in the next few lines
            j = i + 1
            while j < len(lines) and 'list_display' not in lines[j]:
                result.append(lines[j])
                j += 1
            
            if j < len(lines) and 'list_display' in lines[j]:
                # Found list_display line
                list_display_line = lines[j]
                result.append(list_display_line)
                
                # Check if table_name is already in list_display
                if "'table_name'" not in list_display_line:
                    # Add table_name at the beginning
                    # Pattern: list_display = ['id', ...] or list_display = (...)
                    if '[' in list_display_line:
                        # List format
                        list_display_line = list_display_line.replace("list_display = [", "list_display = ['table_name', ")
                    elif '(' in list_display_line:
                        # Tuple format
                        list_display_line = list_display_line.replace("list_display = (", "list_display = ('table_name', ")
                    
                    result[-1] = list_display_line  # Replace the last added line
                    print(f"[OK] Added table_name to {lines[i].split('class')[1].split('DefaultAdmin')[0].strip()}")
                else:
                    print(f"[SKIP] table_name already in {lines[i].split('class')[1].split('DefaultAdmin')[0].strip()}")
                
                i = j
            else:
                print(f"[WARN] No list_display found for {lines[i].split('class')[1].split('DefaultAdmin')[0].strip()}")
        
        i += 1
    
    # Write back
    with open(file_path, 'w') as f:
        f.write('\n'.join(result))
    
    print("\n[OK] Done! Restart Django server to see changes.")

if __name__ == "__main__":
    add_table_name_to_admin()
