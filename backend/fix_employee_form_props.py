import re

file_path = "c:\\00mindra\\olivine-platform\\HRM\\frontend\\src\\pages\\EmployeeForm.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Pattern 1: Add hideButtons to Interface/Type in Props
# Look for: "errors?: Record<string, string> }>"
# Replace with: "errors?: Record<string, string>; hideButtons?: boolean }>"

content_v2 = re.sub(
    r"errors\?: Record<string, string>\s*}\>",
    r"errors?: Record<string, string>; hideButtons?: boolean }>",
    content
)

# Pattern 2: Add hideButtons to Destructuring
# Look for: "({ data, onChange, onCancel, loading, errors })"
# Replace with: "({ data, onChange, onCancel, loading, errors, hideButtons })"

content_v3 = re.sub(
    r"\({ data, onChange, onCancel, loading, errors }\)",
    r"({ data, onChange, onCancel, loading, errors, hideButtons })",
    content_v2
)

# Verify change happened
if content == content_v3:
    print("No changes made! Regex didn't match.")
    
    # Debug: Print sample
    match = re.search(r"\({ data.*errors }\)", content)
    if match:
        print("Found destructuring:", match.group(0))
    else:
        print("Destructuring pattern not found")
        
    match_type = re.search(r"errors\?: Record<string, string>\s*}\>", content)
    if match_type:
        print("Found type def:", match_type.group(0))
    else:
        print("Type def pattern not found")

else:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content_v3)
    print("Fixed hideButtons in Tab Components.")
