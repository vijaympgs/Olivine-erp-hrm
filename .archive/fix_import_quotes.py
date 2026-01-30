import os
import re

root_dirs = [
    r"c:\00mindra\olivine-erp-platform\frontend\src",
    r"c:\00mindra\olivine-erp-platform\apps",
    r"c:\00mindra\olivine-erp-platform\core"
]

def fix_line(line):
    # Fix 1: Normalize src/services to @services
    if 'from "src/services/' in line or "from 'src/services/" in line:
        line = line.replace('src/services/', '@services/')
    
    # Fix 2: Check for mismatched quotes in imports
    # Regex for import ... from "path' or 'path"
    match = re.search(r'(import\s+.*?from\s+)(["\'])(.*?)(["\'])(;?)', line)
    if match:
        prefix, q1, path, q2, suffix = match.groups()
        if q1 != '"' or q2 != '"':
            # Normalize to double quotes
            return f'{prefix}"{path}"{suffix}\n'
    
    # Fallback: simple replace for the specific breakage pattern if regex missed complex cases
    # Broken pattern: from "path'
    if 'from "' in line and line.strip().endswith("'") or line.strip().endswith("';"):
        line = line.replace("';", '";').replace("'", '"')

    return line

for root_dir in root_dirs:
    for root, dirs, files in os.walk(root_dir):
        if "node_modules" in root:
            continue
        for file in files:
            if file.endswith((".tsx", ".ts")):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                    
                    new_lines = []
                    changed = False
                    for line in lines:
                        new_line = fix_line(line)
                        if new_line != line:
                            changed = True
                            new_lines.append(new_line)
                        else:
                            new_lines.append(line)
                    
                    if changed:
                        with open(filepath, "w", encoding="utf-8") as f:
                            f.writelines(new_lines)
                        print(f"Fixed quotes/paths in {file}")
                except Exception as e:
                    print(f"Error processing {file}: {e}")




