import os
import re

def fix_all_imports():
    root_dir = r'c:\00mindra\olivine-platform\Retail\backend'
    
    # 1. Patterns for imports
    target_pattern = re.compile(r"from Core\.org_structure\.backend\.company\.models import \((.*?)\)", re.DOTALL)
    single_line_pattern = re.compile(r"from Core\.org_structure\.backend\.company\.models import (.*)")

    # 2. Map of models to their new locations
    model_map = {
        'Company': 'core.licensing.backend.business_entities.models',
        'Location': 'Retail.backend.domain.models',
        'ItemMaster': 'common.domain.models',
        'ItemVariant': 'common.domain.models',
        'UnitOfMeasure': 'common.domain.models',
        'Customer': 'common.domain.models',
        'Supplier': 'common.domain.models',
        'OperationalCustomer': 'common.domain.models',
        'OperationalSupplier': 'common.domain.models'
    }

    def get_replacement_imports(models_str):
        # Clean up the models string
        models = [m.strip().split(' as ')[0] for m in models_str.replace('(', '').replace(')', '').split(',')]
        models = [m for m in models if m]
        
        new_imports = []
        # Group by new location
        new_locs = {}
        for m in models:
            # Handle aliases
            alias_part = ""
            orig_m = m
            if ' as ' in m:
                # This should have been handled by split, but just in case
                pass
            
            # Since we cleaned aliases above, we might lose them.
            # Let's re-parse more carefully.
        
        # Actually, simpler: just iterate through each word and if it's in model_map, use it.
        # But some files have "from ... import Company, Location"
        
        # Let's try another approach for replacement
        return None # Fallback to manual for complex cases or refinement

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py') and 'tests' in root:
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if it has the legacy import
                if "core.org_structure.backend.company.models" in content:
                    print(f"Fixing imports in {path}")
                    # Remove it and add new ones
                    lines = content.split('\n')
                    new_lines = []
                    in_block = False
                    block_models = []
                    for line in lines:
                        if "from core.org_structure.backend.company.models import (" in line:
                            in_block = True
                            continue
                        if in_block:
                            if ")" in line:
                                in_block = False
                                block_models.extend([m.strip() for m in line.replace(')', '').split(',') if m.strip()])
                                # Process block_models
                                added = set()
                                for m_raw in block_models:
                                    m_name = m_raw.split(' as ')[0]
                                    loc = model_map.get(m_name, 'core.org_structure.backend.company.models')
                                    new_lines.append(f"from {loc} import {m_raw}")
                                block_models = []
                                continue
                            else:
                                block_models.extend([m.strip() for m in line.split(',') if m.strip()])
                                continue
                        
                        if "from core.org_structure.backend.company.models import " in line:
                            # Single line import
                            m_raw_list = line.split('import ')[1].split(',')
                            for m_raw in m_raw_list:
                                m_raw = m_raw.strip()
                                m_name = m_raw.split(' as ')[0]
                                loc = model_map.get(m_name, 'core.org_structure.backend.company.models')
                                new_lines.append(f"from {loc} import {m_raw}")
                            continue

                        new_lines.append(line)
                    
                    new_content = '\n'.join(new_lines)
                    if new_content != content:
                        with open(path, 'w', encoding='utf-8') as f:
                            f.write(new_content)

if __name__ == "__main__":
    fix_all_imports()
