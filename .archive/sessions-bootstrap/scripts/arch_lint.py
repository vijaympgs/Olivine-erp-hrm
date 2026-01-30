import ast
import os
import sys

# Configuration
# (Module Path -> Set of Forbidden Class Names)
# If Set is None, the entire module is forbidden.
FORBIDDEN_IMPORTS = {
    "domain.company.models": {"Company", "Customer", "Supplier"},
    "domain.user_management.models": {"Employee"},
    "domain.master.customer.models.models": {"Customer"},
    "domain.master.customer.models": {"Customer"},
}

# Directories/Files to exclude from checking (Technical Debt / Self-Definition)
EXCLUDES = [
    "backend\\domain\\company", # Defines the models
    "backend\\domain\\user_management", # Defines the models
    "backend\\domain\\master", # Defines the models
    "backend\\common\\legacy_bridge.py", # The Bridge
    "migrations", # Django Migrations
    "tests", # Tests
    "backend\\domain\\pos", # POS is not yet migrated (Known Debt)
    "backend\\domain\\finance", # Finance is not yet migrated (Known Debt)
]


def is_excluded(file_path):
    for exc in EXCLUDES:
        if exc in file_path:
            return True
    return False

class ImportVisitor(ast.NodeVisitor):
    def __init__(self, filename):
        self.filename = filename
        self.errors = []

    def visit_ImportFrom(self, node):
        module = node.module
        if not module:
            return

        # Check full module ban
        if module in FORBIDDEN_IMPORTS and FORBIDDEN_IMPORTS[module] is None:
             self.errors.append(f"Line {node.lineno}: Forbidden import module '{module}'")
             return

        # Check specific class ban
        if module in FORBIDDEN_IMPORTS:
            forbidden_names = FORBIDDEN_IMPORTS[module]
            for alias in node.names:
                if alias.name in forbidden_names:
                    self.errors.append(f"Line {node.lineno}: Forbidden import class '{alias.name}' from '{module}'. Use Canonical (business_entities/hr) instead.")

    def visit_Import(self, node):
        for alias in node.names:
            name = alias.name
            if name in FORBIDDEN_IMPORTS and FORBIDDEN_IMPORTS[name] is None:
                self.errors.append(f"Line {node.lineno}: Forbidden import module '{name}'")

def check_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read(), filename=file_path)
        visitor = ImportVisitor(file_path)
        visitor.visit(tree)
        return visitor.errors
    except Exception as e:
        return [f"Could not parse file: {e}"]

def main():
    root_dir = os.path.join(os.getcwd(), "backend")
    violations = []
    
    print(f"Starting Architecture Lint in {root_dir}...")
    
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, os.getcwd())
                
                if is_excluded(rel_path):
                    continue
                
                errors = check_file(full_path)
                for err in errors:
                    violations.append(f"{rel_path}: {err}")

    if violations:
        print("\nARCHITECTURE VIOLATIONS FOUND:")
        for v in violations:
            print(f"  [x] {v}")
        print(f"\nTotal Violations: {len(violations)}")
        sys.exit(1)
    else:
        print("\n✅ Architecture Integrity Verified. No forbidden legacy usage found.")
        sys.exit(0)

if __name__ == "__main__":
    main()



