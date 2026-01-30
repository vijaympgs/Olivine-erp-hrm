# Quick script to find and report all Location imports from legacy location
import os
import re

# Search for Location imports from legacy paths
patterns = [
    r'from core\.org_structure\.backend\.company\.models import.*Location',
    r'from core\.org_structure\.backend\.location',
]

root_dir = r'c:\00mindra\olivine-erp-platform'
problem_files = []

for root, dirs, files in os.walk(root_dir):
    # Skip certain directories
    if any(skip in root for skip in ['.venv', '__pycache__', 'node_modules', '.git']):
        continue
    
    for file in files:
        if file.endswith('.py'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    for pattern in patterns:
                        if re.search(pattern, content):
                            problem_files.append(filepath)
                            break
            except:
                pass

print(f"Found {len(problem_files)} files with legacy Location imports:")
for f in problem_files:
    print(f"  - {f}")




