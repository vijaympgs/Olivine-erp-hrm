import re

file_path = "c:\\00mindra\\olivine-platform\\HRM\\frontend\\src\\pages\\EmployeeForm.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Identify Blocks
# Start of Fields: "  // Employee Identification Fields"
# End of Tabs: Just before "  const tabs = ["

start_marker = "  // Employee Identification Fields"
end_marker = "  const tabs = ["

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Could not find blocks")
    exit(1)

extracted_block = content[start_idx:end_idx]

# Remove indentation (2 spaces) from extracted block
lines = extracted_block.split('\n')
cleaned_lines = []
for line in lines:
    if line.startswith('  '):
        cleaned_lines.append(line[2:])
    else:
        cleaned_lines.append(line)
cleaned_block = '\n'.join(cleaned_lines)

# 2. Construct New Content
# Imports
imports_end_marker = "interface EmployeeFormData {"
imports_end_idx = content.find(imports_end_marker)

# We want to keep imports and interfaces
# But we want to REMOVE the local component definitions (PageContainer... Button)
# Local components start at line 6: "// PageContainer Component"
# And end before "interface EmployeeFormData"

local_comps_start = content.find("// PageContainer Component")
local_comps_end = imports_end_idx

header = content[:local_comps_start]
interfaces_and_form_start = content[local_comps_end:start_idx]
rest_of_form = content[end_idx:]

new_content = header + "\n" + interfaces_and_form_start + "\n" + cleaned_block + "\n" + rest_of_form

# 3. Write Back
with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Refactoring complete.")
