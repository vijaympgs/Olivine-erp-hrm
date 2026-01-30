import re

file_path = "c:\\00mindra\\olivine-platform\\HRM\\frontend\\src\\pages\\EmployeeForm.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Markers
# Note: Indentation might be 0 or 2 spaces depending on previous runs.
# We'll regex find the start.

# Start: "// Employee Identification Fields"
# End: "const tabs = ["

# Regex to find start
start_match = re.search(r"^\s*// Employee Identification Fields", content, re.MULTILINE)
end_match = re.search(r"^\s*const tabs = \[", content, re.MULTILINE)

if not start_match or not end_match:
    print("Could not find blocks via regex")
    # Debug print around likely area
    print("Content snippet around 'Employee Identification Fields':")
    idx = content.find("Employee Identification Fields")
    print(content[idx-50:idx+50])
    exit(1)

start_idx = start_match.start()
end_idx = end_match.start()

extracted_block = content[start_idx:end_idx]

# Clean indentation (if any left)
lines = extracted_block.split('\n')
cleaned_lines = []
for line in lines:
    cleaned_lines.append(line.lstrip()) # Remove leading whitespace
cleaned_block = '\n'.join(cleaned_lines)

# Identify Component Start
comp_match = re.search(r"^export const EmployeeForm", content, re.MULTILINE)
if not comp_match:
    print("Could not find EmployeeForm definition")
    exit(1)
comp_idx = comp_match.start()

# We need to act carefully.
# The block is CURRENTLY inside the component (after comp_idx).
# We want to move it to BEFORE comp_idx.

# Split content into parts
part1 = content[:comp_idx] # Header + Imports + Interfaces
# part2 is from comp start to block start (This contains EmployeeForm start + state hooks)
part2 = content[comp_idx:start_idx]
# part3 is the rest (tabs definition + render + end)
# REMEMBER: extracted_block was between start_idx and end_idx.
part3 = content[end_idx:]

# New Order: Part1 + CLEANED_BLOCK + Part2 + Part3
new_content = part1 + "\n" + cleaned_block + "\n" + part2 + "\n" + part3

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Refactoring v3 complete.")
