@echo off
echo ========================================
echo Moving HRM Development Files to hrm-dev-ref
echo ========================================

REM Create hrm-dev-ref directory if it doesn't exist
if not exist "hrm-dev-ref" (
    echo Creating hrm-dev-ref directory...
    mkdir "hrm-dev-ref"
)

REM Create subdirectories
if not exist "hrm-dev-ref\scripts" (
    echo Creating scripts directory...
    mkdir "hrm-dev-ref\scripts"
)

if not exist "hrm-dev-ref\docs" (
    echo Creating docs directory...
    mkdir "hrm-dev-ref\docs"
)

echo.
echo Moving Python script files...

REM Move Python scripts to scripts folder
echo Moving fix_core_imports.py...
move "fix_core_imports.py" "hrm-dev-ref\scripts\" 2>nul

echo Moving verify_menu_items.py...
move "verify_menu_items.py" "hrm-dev-ref\scripts\" 2>nul

echo Moving seed_hrm_menu_items.py...
move "seed_hrm_menu_items.py" "hrm-dev-ref\scripts\" 2>nul

echo Moving update_hrm_toolbar_configs.py...
move "update_hrm_toolbar_configs.py" "hrm-dev-ref\scripts\" 2>nul

echo Moving verify_hrm_configs.py...
move "verify_hrm_configs.py" "hrm-dev-ref\scripts\" 2>nul

echo Moving check_hrm_empty_configs.py...
move "check_hrm_empty_configs.py" "hrm-dev-ref\scripts\" 2>nul

echo Moving count_hrm_menu_items.py...
move "count_hrm_menu_items.py" "hrm-dev-ref\scripts\" 2>nul

echo Moving seed_all_hrm_menu_items.py...
move "seed_all_hrm_menu_items.py" "hrm-dev-ref\scripts\" 2>nul

echo Moving cleanup_non_hrm_items.py...
move "cleanup_non_hrm_items.py" "hrm-dev-ref\scripts\" 2>nul

echo Moving populate_applicable_toolbar_config.py...
move "populate_applicable_toolbar_config.py" "hrm-dev-ref\scripts\" 2>nul

echo.
echo Moving documentation files...

REM Move documentation files to docs folder
echo Moving ERP_Menu_Items_20260120_153213.csv...
move "ERP_Menu_Items_20260120_153213.csv" "hrm-dev-ref\docs\" 2>nul

echo.
echo Moving HRM backend files...

REM Move HRM backend files
if not exist "hrm-dev-ref\hrm-backend" (
    echo Creating hrm-backend directory...
    mkdir "hrm-dev-ref\hrm-backend"
)

echo Moving HRM backend views...
if exist "HRM\backend\hrm\views.py" (
    copy "HRM\backend\hrm\views.py" "hrm-dev-ref\hrm-backend\views.py" 2>nul
    echo Copied HRM views.py
)

echo.
echo Moving Django admin configuration...
if exist "backend\core\auth_access\backend\user_management\admin.py" (
    copy "backend\core\auth_access\backend\user_management\admin.py" "hrm-dev-ref\scripts\admin-config.py" 2>nul
    echo Copied admin configuration
)

echo.
echo Creating index file...
echo # HRM Development Reference Files > "hrm-dev-ref\README.md"
echo. >> "hrm-dev-ref\README.md"
echo This folder contains all the development reference files for HRM module. >> "hrm-dev-ref\README.md"
echo. >> "hrm-dev-ref\README.md"
echo ## Structure: >> "hrm-dev-ref\README.md"
echo - **scripts/**: Python utility scripts for HRM development >> "hrm-dev-ref\README.md"
echo - **docs/**: Documentation and CSV exports >> "hrm-dev-ref\README.md"
echo - **hrm-backend/**: HRM backend code references >> "hrm-dev-ref\README.md"
echo. >> "hrm-dev-ref\README.md"
echo ## Scripts: >> "hrm-dev-ref\README.md"
echo - fix_core_imports.py: Fix import issues >> "hrm-dev-ref\README.md"
echo - verify_menu_items.py: Verify menu items in database >> "hrm-dev-ref\README.md"
echo - seed_hrm_menu_items.py: Seed initial HRM menu items >> "hrm-dev-ref\README.md"
echo - update_hrm_toolbar_configs.py: Update toolbar configurations >> "hrm-dev-ref\README.md"
echo - verify_hrm_configs.py: Verify HRM configurations >> "hrm-dev-ref\README.md"
echo - check_hrm_empty_configs.py: Check for empty toolbar configs >> "hrm-dev-ref\README.md"
echo - count_hrm_menu_items.py: Count HRM menu items >> "hrm-dev-ref\README.md"
echo - seed_all_hrm_menu_items.py: Seed all 63 HRM menu items >> "hrm-dev-ref\README.md"
echo - cleanup_non_hrm_items.py: Remove non-HRM items >> "hrm-dev-ref\README.md"
echo - populate_applicable_toolbar_config.py: Populate applicable toolbar config >> "hrm-dev-ref\README.md"
echo - admin-config.py: Django admin configuration reference >> "hrm-dev-ref\README.md"
echo. >> "hrm-dev-ref\README.md"
echo ## Usage: >> "hrm-dev-ref\README.md"
echo Run scripts from the root directory: >> "hrm-dev-ref\README.md"
echo ```bash >> "hrm-dev-ref\README.md"
echo python hrm-dev-ref\scripts\verify_hrm_configs.py >> "hrm-dev-ref\README.md"
echo ``` >> "hrm-dev-ref\README.md"

echo.
echo ========================================
echo Cleanup Complete!
echo ========================================
echo.
echo All HRM development files have been moved to: hrm-dev-ref/
echo.
echo Structure:
echo hrm-dev-ref/
echo ├── scripts/          (Python utility scripts)
echo ├── docs/             (Documentation and exports)
echo ├── hrm-backend/      (Backend code references)
echo └── README.md         (This file)
echo.
echo Total files moved: 12
echo.
echo You can now safely delete the original files from the root directory.
echo.
pause
