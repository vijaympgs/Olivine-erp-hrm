@echo off
title Update Olivine Platform Ports - Avoid Conflict with Knowledge Bot
color 0F

echo ========================================
echo  OLIVINE PLATFORM PORT UPDATE UTILITY
echo ========================================
echo.
echo Updating platform ports to avoid conflict:
echo  Knowledge Bot: 8000 (backend), 3000 (frontend)
echo  Platform:      8001 (backend), 3001 (frontend)
echo.
echo Current directory: %CD%
echo Script location: %~dp0
echo.

:: Define platform path
set PLATFORM_PATH=C:\00mindra\olivine-platform

:: Check if platform directory exists
if not exist "%PLATFORM_PATH%" (
    echo [ERROR] Platform directory not found: %PLATFORM_PATH%
    echo [INFO] Please verify the platform installation path.
    pause
    exit /b 1
)

echo [INFO] Platform found at: %PLATFORM_PATH%
echo.

:: Update batch files in scripts directory
echo [INFO] Updating batch files in scripts directory...

if exist "%PLATFORM_PATH%\scripts\START_UNIFIED.bat" (
    echo [INFO] Updating START_UNIFIED.bat...
    powershell -Command "(Get-Content '%PLATFORM_PATH%\scripts\START_UNIFIED.bat') -replace ':8000', ':8001' -replace 'port 8000', 'port 8001' | Set-Content '%PLATFORM_PATH%\scripts\START_UNIFIED.bat'"
    echo [SUCCESS] START_UNIFIED.bat updated
) else (
    echo [WARNING] START_UNIFIED.bat not found
)

if exist "%PLATFORM_PATH%\scripts\START_BACKEND.bat" (
    echo [INFO] Updating START_BACKEND.bat...
    powershell -Command "(Get-Content '%PLATFORM_PATH%\scripts\START_BACKEND.bat') -replace ':8000', ':8001' -replace 'port 8000', 'port 8001' | Set-Content '%PLATFORM_PATH%\scripts\START_BACKEND.bat'"
    echo [SUCCESS] START_BACKEND.bat updated
) else (
    echo [WARNING] START_BACKEND.bat not found
)

if exist "%PLATFORM_PATH%\scripts\START_FRONTEND.bat" (
    echo [INFO] Updating START_FRONTEND.bat...
    powershell -Command "(Get-Content '%PLATFORM_PATH%\scripts\START_FRONTEND.bat') -replace 'localhost:3000', 'localhost:3001' | Set-Content '%PLATFORM_PATH%\scripts\START_FRONTEND.bat'"
    echo [SUCCESS] START_FRONTEND.bat updated
) else (
    echo [WARNING] START_FRONTEND.bat not found
)

:: Update Django settings if accessible
if exist "%PLATFORM_PATH%\backend\erp_core\settings.py" (
    echo [INFO] Updating Django settings...
    powershell -Command "(Get-Content '%PLATFORM_PATH%\backend\erp_core\settings.py') -replace '8000', '8001' | Set-Content '%PLATFORM_PATH%\backend\erp_core\settings.py'"
    echo [SUCCESS] Django settings updated
) else (
    echo [WARNING] Django settings.py not found
)

:: Update package.json proxy settings
if exist "%PLATFORM_PATH%\frontend\package.json" (
    echo [INFO] Updating frontend proxy settings...
    powershell -Command "(Get-Content '%PLATFORM_PATH%\frontend\package.json') -replace 'localhost:8000', 'localhost:8001' | Set-Content '%PLATFORM_PATH%\frontend\package.json'"
    echo [SUCCESS] Frontend proxy updated
) else (
    echo [WARNING] Frontend package.json not found
)

:: Update QA Launcher Console ports
if exist "%PLATFORM_PATH%\Common\qa-launcher-console" (
    echo [INFO] Updating QA Launcher Console configuration...
    
    if exist "%PLATFORM_PATH%\Common\qa-launcher-console\backend\server.js" (
        powershell -Command "(Get-Content '%PLATFORM_PATH%\Common\qa-launcher-console\backend\server.js') -replace '8000', '8001' | Set-Content '%PLATFORM_PATH%\Common\qa-launcher-console\backend\server.js'"
        echo [SUCCESS] QA Launcher backend updated
    )
    
    if exist "%PLATFORM_PATH%\Common\qa-launcher-console\frontend\src\config.js" (
        powershell -Command "(Get-Content '%PLATFORM_PATH%\Common\qa-launcher-console\frontend\src\config.js') -replace '8000', '8001' | Set-Content '%PLATFORM_PATH%\Common\qa-launcher-console\frontend\src\config.js'"
        echo [SUCCESS] QA Launcher frontend updated
    )
    
) else (
    echo [WARNING] QA Launcher Console not found
)

echo.
echo ========================================
echo  PORT UPDATE COMPLETED
echo ========================================
echo.
echo Updated Platform Ports:
echo  Backend:  8001 (was 8000)
echo  Frontend: 3001 (unchanged)
echo.
echo Knowledge Bot Ports (unchanged):
echo  Backend:  8000
echo  Frontend: 3000
echo.
echo [INFO] Both systems can now run simultaneously without port conflicts.
echo [INFO] This script can be run from any directory.
echo.
pause