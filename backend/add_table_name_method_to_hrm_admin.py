#!/usr/bin/env python
"""Add table_name method to all HRM admin classes"""
import re

def add_table_name_method():
    """Add table_name method to all DefaultAdmin classes"""
    
    file_path = 'HRM/backend/hrm/admin.py'
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Split by class definitions
    lines = content.split('\n')
    result = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        result.append(line)
        
        # Check if this is a DefaultAdmin class
        if 'class' in line and 'DefaultAdmin(TableNameDisplayMixin, admin.ModelAdmin):' in line:
            # Look for search_fields
            j = i + 1
            while j < len(lines) and 'search_fields' not in lines[j]:
                result.append(lines[j])
                j += 1
            
            if j < len(lines) and 'search_fields' in lines[j]:
                # Found search_fields line
                result.append(lines[j])
                
                # Check if table_name method already exists
                k = j + 1
                has_table_name_method = False
                while k < len(lines) and k < j + 10:  # Check next 10 lines
                    if 'def table_name(self, obj):' in lines[k]:
                        has_table_name_method = True
                        break
                    k += 1
                
                if not has_table_name_method:
                    # Add table_name method after search_fields
                    result.append('')
                    result.append('    def table_name(self, obj):')
                    result.append('        """Display the database table name"""')
                    result.append('        return obj._meta.db_table')
                    result.append('    table_name.short_description = \'Table Name\'')
                    result.append('    table_name.admin_order_field = \'id\'')
                    print(f"[OK] Added table_name method to {lines[i].split('class')[1].split('DefaultAdmin')[0].strip()}")
                else:
                    print(f"[SKIP] table_name method already in {lines[i].split('class')[1].split('DefaultAdmin')[0].strip()}")
                
                i = j
            else:
                print(f"[WARN] No search_fields found for {lines[i].split('class')[1].split('DefaultAdmin')[0].strip()}")
        
        i += 1
    
    # Write back
    with open(file_path, 'w') as f:
        f.write('\n'.join(result))
    
    print("\n[OK] Done! Restart Django server to see changes.")

if __name__ == "__main__":
    add_table_name_method()
