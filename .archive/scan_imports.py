import os
import re

root_dirs = [
    r"c:\00mindra\olivine-erp-platform\frontend\src",
    r"c:\00mindra\olivine-erp-platform\apps",
    r"c:\00mindra\olivine-erp-platform\core"
]

patterns = [
    (r'from\s+["''](\.\./)+@', "Alias Misuse"),
    (r'from\s+["''](\.\./)+app', "Relative App Import"),
    (r'from\s+["''](\.\./)+services', "Relative Service Import"),
    (r'from\s+["''](\.\./)+ui', "Relative UI Import"),
    (r'from\s+["'']\.\./\.\./.+', "Deep Relative Import") 
]

results = []

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
                        for i, line in enumerate(lines):
                            for pat, issue_type in patterns:
                                if re.search(pat, line):
                                    # limit line length for readable output
                                    clean_line = line.strip()[:100]
                                    results.append(f"{filepath}|{i+1}|{clean_line}|{issue_type}")
                except Exception as e:
                    pass

print(f"{'FILE':<80} | {'LINE':<5} | {'CURRENT IMPORT':<60} | {'ISSUE TYPE'}")
print("-" * 160)
for r in results[:50]: # Show first 50 to avoid massive output, I can iterate
    parts = r.split("|")
    print(f"{parts[0][-80:]:<80} | {parts[1]:<5} | {parts[2]:<60} | {parts[3]}")




