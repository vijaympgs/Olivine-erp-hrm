import os
import re
import json

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
                                match = re.search(pat, line)
                                if match:
                                    clean_line = line.strip()
                                    # Basic fix proposals (heuristics)
                                    proposal = "MANUAL FIX REQUIRED"
                                    if issue_type == "Alias Misuse":
                                        # Remove ../ prefix from alias
                                        proposal = clean_line.replace("../@", "@").replace("../../@", "@").replace("../../../@", "@")
                                    elif issue_type == "Relative App Import":
                                         if "menuConfig" in clean_line:
                                             proposal = 'import { menuConfig } from "@app/menuConfig";' # Canonical
                                         else:
                                             proposal = clean_line.replace("../app/", "@app/")
                                    elif issue_type == "Relative Service Import":
                                        # Replace relative part with src/services
                                        # import { x } from "../../services/x" -> import { x } from "src/services/x"
                                        # We need to extract the part after 'services/'
                                        m = re.search(r'["''](\.\./)+services/(.+?)["'']', clean_line)
                                        if m:
                                            service_path = m.group(2)
                                            proposal = f'import {{ ... }} from "src/services/{service_path}";' 
                                            # Note: exact import content hard to reconstruct in simple regex replacement without parsing
                                            # So we will just flag it.
                                    elif issue_type == "Relative UI Import":
                                        # ../../ui/components/X -> @ui/components/X
                                        # Need to handle various depths
                                        # Look for 'ui/'
                                        proposal = clean_line # Placeholder
                                        if "/ui/" in clean_line:
                                             # Try to replace everything before ui/ with @
                                             proposal = re.sub(r'["''](\.\./)+ui/', '"@ui/', clean_line)

                                    
                                    results.append({
                                        "file": filepath,
                                        "line": i+1,
                                        "current": clean_line,
                                        "type": issue_type,
                                        "proposal": proposal
                                    })
                                    break # count once per line
                except Exception as e:
                    pass

print(json.dumps(results, indent=2))




