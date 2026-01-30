import re

def add_table_name_mixin():
    """Add TableNameDisplayMixin to all admin classes in HRM admin.py"""
    
    file_path = 'HRM/backend/hrm/admin.py'
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Find all admin class definitions and add TableNameDisplayMixin to them
    # Pattern: class XAdmin(admin.ModelAdmin):
    # Replace with: class XAdmin(TableNameDisplayMixin, admin.ModelAdmin):
    
    pattern = r'class (\w+Admin)\(admin\.ModelAdmin\):'
    replacement = r'class \1(TableNameDisplayMixin, admin.ModelAdmin):'
    
    new_content = re.sub(pattern, replacement, content)
    
    with open(file_path, 'w') as f:
        f.write(new_content)
    
    print("Added TableNameDisplayMixin to all admin classes in HRM/admin.py")

if __name__ == "__main__":
    add_table_name_mixin()
