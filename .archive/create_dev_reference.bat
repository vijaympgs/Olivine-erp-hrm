ld@echo off
echo ========================================
echo Creating Development Reference Folder
echo ========================================

REM Create dev-reference directory if it doesn't exist
if not exist "dev-reference" (
    echo Creating dev-reference directory...
    mkdir "dev-reference"
)

REM Create subdirectories
if not exist "dev-reference\bootstrap" (
    echo Creating bootstrap directory...
    mkdir "dev-reference\bootstrap"
)

if not exist "dev-reference\steering" (
    echo Creating steering directory...
    mkdir "dev-reference\steering"
)

if not exist "dev-reference\docs" (
    echo Creating docs directory...
    mkdir "dev-reference\docs"
)

if not exist "dev-reference\hrm" (
    echo Creating hrm directory...
    mkdir "dev-reference\hrm"
)

echo.
echo Copying Bootstrap Documents...

REM Copy bootstrap documents
echo Copying bootstrap files...
if exist "bootstrap\*.md" (
    copy "bootstrap\*.md" "dev-reference\bootstrap\" 2>nul
    echo Copied bootstrap markdown files
)

if exist "sessions-bootstrap\*.md" (
    copy "sessions-bootstrap\*.md" "dev-reference\bootstrap\" 2>nul
    echo Copied sessions-bootstrap markdown files
)

echo.
echo Copying Steering Documents...

REM Copy steering documents
if exist "Steering\*.md" (
    copy "Steering\*.md" "dev-reference\steering\" 2>nul
    echo Copied steering markdown files
)

echo.
echo Copying Unified Shell Scripts...

REM Copy unified shell scripts
if exist "unified-shell\*.sh" (
    copy "unified-shell\*.sh" "dev-reference\docs\" 2>nul
    echo Copied unified shell scripts
)

if exist "unified-shell\*.bat" (
    copy "unified-shell\*.bat" "dev-reference\docs\" 2>nul
    echo Copied unified shell batch files
)

echo.
echo Copying Toolbar Documentation...

REM Find and copy all toolbar*.md files
echo Searching for toolbar documentation files...
for /r . %%f in (toolbar*.md) do (
    echo Copying %%f to dev-reference\docs\
    copy "%%f" "dev-reference\docs\" 2>nul
)

echo.
echo Copying HRM Development Files...

REM Copy HRM development files from hrm-dev-ref if it exists
if exist "hrm-dev-ref\scripts\*.py" (
    copy "hrm-dev-ref\scripts\*.py" "dev-reference\hrm\" 2>nul
    echo Copied HRM scripts
)

if exist "hrm-dev-ref\docs\*" (
    copy "hrm-dev-ref\docs\*" "dev-reference\hrm\" 2>nul
    echo Copied HRM documentation
)

if exist "hrm-dev-ref\hrm-backend\*" (
    copy "hrm-dev-ref\hrm-backend\*" "dev-reference\hrm\" 2>nul
    echo Copied HRM backend files
)

echo.
echo Copying Key Configuration Files...

REM Copy important configuration files
if exist "README.md" (
    copy "README.md" "dev-reference\" 2>nul
    echo Copied main README
)

if exist "QUICK_START.md" (
    copy "QUICK_START.md" "dev-reference\" 2>nul
    echo Copied QUICK_START
)

if exist "ARCHITECTURE.md" (
    copy "ARCHITECTURE.md" "dev-reference\" 2>nul
    echo Copied ARCHITECTURE
)

echo.
echo Creating Master Index...

REM Create master index file
echo # Development Reference Center > "dev-reference\README.md"
echo. >> "dev-reference\README.md"
echo This folder contains all essential development reference documents and scripts. >> "dev-reference\README.md"
echo. >> "dev-reference\README.md"
echo ## Quick Access >> "dev-reference\README.md"
echo - **Bootstrap/**: Bootstrap and setup documentation >> "dev-reference\README.md"
echo - **Steering/**: Project steering and governance documents >> "dev-reference\README.md"
echo - **docs/**: Technical documentation and shell scripts >> "dev-reference\README.md"
echo - **hrm/**: HRM module development files and scripts >> "dev-reference\README.md"
echo. >> "dev-reference\README.md"
echo ## Bootstrap Documents >> "dev-reference\README.md"
echo - Bootstrap guides and setup instructions >> "dev-reference\README.md"
echo - Session bootstrap files for different modules >> "dev-reference\README.md"
echo. >> "dev-reference\README.md"
echo ## Steering Documents >> "dev-reference\README.md"
echo - Project governance and steering committee documents >> "dev-reference\README.md"
echo - Technical decisions and architectural guidelines >> "dev-reference\README.md"
echo. >> "dev-reference\README.md"
echo ## Technical Documentation >> "dev-reference\README.md"
echo - Shell scripts for unified operations >> "dev-reference\README.md"
echo - Toolbar documentation and guides >> "dev-reference\README.md"
echo - API documentation and technical specs >> "dev-reference\README.md"
echo. >> "dev-reference\README.md"
echo ## HRM Development >> "dev-reference\README.md"
echo - HRM module development scripts and utilities >> "dev-reference\README.md"
echo - Configuration files and references >> "dev-reference\README.md"
echo - Backend code examples and templates >> "dev-reference\README.md"
echo. >> "dev-reference\README.md"
echo ## Usage >> "dev-reference\README.md"
echo This folder serves as your single reference point for all development activities. >> "dev-reference\README.md"
echo. >> "dev-reference\README.md"
echo ### Quick Start: >> "dev-reference\README.md"
echo 1. Read: dev-reference\README.md >> "dev-reference\README.md"
echo 2. Bootstrap: dev-reference\bootstrap\ >> "dev-reference\README.md"
echo 3. Configure: dev-reference\docs\ >> "dev-reference\README.md"
echo 4. Develop: dev-reference\hrm\ >> "dev-reference\README.md"
echo.5. Govern: dev-reference\steering\ >> "dev-reference\README.md"

echo.
echo ========================================
echo Development Reference Created!
echo ========================================
echo.
echo All reference files have been copied to: dev-reference/
echo.
echo Structure:
echo dev-reference/
echo ├── bootstrap/         (Bootstrap and setup docs)
echo ├── steering/          (Steering and governance)
echo ├── docs/              (Technical docs and scripts)
echo ├── hrm/               (HRM development files)
echo └── README.md          (Master index)
echo.
echo This is now your single reference folder for all development work.
echo You can clean up other folders manually as needed.
echo.
pause
