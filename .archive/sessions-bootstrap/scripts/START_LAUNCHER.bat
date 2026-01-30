@echo off
echo ============================================
echo   QA LAUNCHER CONSOLE STARTUP
echo ============================================
echo.
echo This script starts the QA Launcher Console:
echo - Backend Controller (Port 3000)
echo - Frontend UI (Port 5174)
echo.
echo Use this to orchestrate and monitor all modules
echo ============================================
echo.

REM Check if we're in the right directory
if not exist "Common\qa-launcher-console" (
    echo ERROR: Please run this script from the olivine-platform root directory
    echo Current directory: %CD%
    pause
    exit /b 1
)

echo [CLEANUP] Clearing ports 3000 and 5174 if in use...
echo.

REM Kill any Node processes on port 3000 (Launcher Backend)
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :3000 ^| findstr LISTENING') do (
    echo Clearing port 3000...
    taskkill /F /PID %%a 2>nul
)

REM Kill any Node processes on port 5174 (Launcher Frontend)
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :5174 ^| findstr LISTENING') do (
    echo Clearing port 5174...
    taskkill /F /PID %%a 2>nul
)

echo Ports cleared.
timeout /t 2 /nobreak >nul

echo.
echo ============================================
echo   STARTING LAUNCHER BACKEND (Port 3000)
echo ============================================
echo.

cd Common\qa-launcher-console\backend

REM Check if node_modules exists
if not exist "node_modules" (
    echo Installing backend dependencies...
    call npm install
)

start "QA Launcher Backend" cmd /k "npm start"

cd ..\..\..

echo Waiting 5 seconds for backend to initialize...
timeout /t 5 /nobreak

echo.
echo ============================================
echo   STARTING LAUNCHER FRONTEND (Port 5174)
echo ============================================
echo.

cd Common\qa-launcher-console\frontend

REM Check if node_modules exists
if not exist "node_modules" (
    echo Installing frontend dependencies...
    call npm install
)

start "QA Launcher Frontend" cmd /k "npm run dev"

cd ..\..\..

echo Waiting 3 seconds for frontend to initialize...
timeout /t 3 /nobreak

echo.
echo ============================================
echo   QA LAUNCHER CONSOLE STARTED
echo ============================================
echo.
echo   Backend Controller:  http://localhost:3000
echo   Frontend Console:    http://localhost:5174
echo.
echo   From the console, you can start:
echo   - ERP Core (Retail, HRM, CRM, FMS)
echo   - Individual modules
echo   - Monitor logs in real-time
echo.
echo ============================================
echo.

echo Opening browser in 3 seconds...
timeout /t 3 /nobreak

start chrome http://localhost:5174

echo.
echo QA Launcher is running. Check the separate windows for logs.
echo Press any key to exit this launcher window...
pause >nul
