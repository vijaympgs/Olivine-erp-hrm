import re

file_path = "c:\\00mindra\\olivine-platform\\HRM\\frontend\\src\\pages\\EmployeeForm.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Identify Extracted Block (Fields + Tabs)
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

# 2. Identify Insertion Point (Before EmployeeForm)
component_marker = "export const EmployeeForm: React.FC<EmployeeFormProps> = ({"
component_idx = content.find(component_marker)

if component_idx == -1:
     print("Could not find component definition")
     exit(1)

# 3. Identify Interfaces Start (to keep them)
interfaces_start = content.find("interface EmployeeFormData {")
# Remove local components (Button, Input, etc) which are before interfaces
# Local comps start after imports.
first_import_end = content.find("import { User, Building") 
# Find end of imports section
header_end = content.find("\n\n", first_import_end) + 2

# Actually, let's just keep imports and interfaces.
# Remove everything between Imports End and Interfaces Start?
# Local components are usually between imports and interfaces.
local_comps_start_marker = "// PageContainer Component"
local_comps_start = content.find(local_comps_start_marker)

header = content[:local_comps_start] # Imports
interfaces = content[interfaces_start:component_idx] # Interfaces
form_start = content[component_idx:start_idx] # Component definition start + state
rest = content[end_idx:] # tabs definition + render + end

# 4. Assemble
# Imports -> Interfaces -> CLEANED BLOCK -> Component Start -> Rest
new_content = header + "\n" + interfaces + "\n" + cleaned_block + "\n" + form_start + "\n" + rest

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Refactoring complete (Corrected).")
