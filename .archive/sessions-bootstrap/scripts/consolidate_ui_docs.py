
import os

SOURCE_DIR = r"c:\00mindra\retail-erp-platform\uidocs"

# Define Groups
GROUPS = {
    "CONSOLIDATED_GOVERNANCE_RULES.md": [
        "agent.olivine_ruleset.md",
        "olivine_ai_governance_agent_rules.md",
        "system-rules.md",
        "06prompt-ui-governance.md"
    ],
    "CONSOLIDATED_DESIGN_SYSTEM.md": [
        "UI_LAYOUT_TERMINOLOGY.md",
        "MENU_TREE_STRUCTURE.md",
        "COMPONENT_LIBRARY.md",
        "STATE_PATTERNS.md",
        "typography.md"
    ],
    "CONSOLIDATED_IMPLEMENTATION_SPECS.md": [
        "OLIVINE_SIDEBAR_ENHANCEMENT_PROMPT.md",
        "SIDEBAR_ENHANCEMENT_SUMMARY.md",
        "PHASE_3_SIDEBAR_IMPLEMENTATION.md",
        "FINAL_UI_STEPS.md",
        "LAYOUT_SETTINGS_REFINEMENT.md",
        "LAYOUT_REORGANIZATION_PLAN.md"
    ]
}

def consolidate_files():
    print(f"Processing files in {SOURCE_DIR}...")
    
    for out_filename, file_list in GROUPS.items():
        out_path = os.path.join(SOURCE_DIR, out_filename)
        print(f"Creating {out_filename}...")
        
        with open(out_path, 'w', encoding='utf-8') as outfile:
            outfile.write(f"# {out_filename.replace('.md', '').replace('_', ' ')}\n")
            outfile.write(f"Generated consolidation of {len(file_list)} files.\n\n")
            
            for fname in file_list:
                fpath = os.path.join(SOURCE_DIR, fname)
                if os.path.exists(fpath):
                    try:
                        with open(fpath, 'r', encoding='utf-8') as infile:
                            content = infile.read()
                            
                        outfile.write(f"\n\n{'='*80}\n")
                        outfile.write(f"FILE START: {fname}\n")
                        outfile.write(f"{'='*80}\n\n")
                        outfile.write(content)
                        outfile.write(f"\n\n{'='*80}\n")
                        outfile.write(f"FILE END: {fname}\n")
                        outfile.write(f"{'='*80}\n\n")
                        print(f"  + Added {fname}")
                    except Exception as e:
                        print(f"  ! Error reading {fname}: {e}")
                else:
                    print(f"  ! Skipped (Not Found): {fname}")
        
    print("Consolidation complete.")

if __name__ == "__main__":
    consolidate_files()



