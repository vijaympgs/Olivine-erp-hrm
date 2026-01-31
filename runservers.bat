@echo off
echo ============================================
echo   OLIVINE HRM PLATFORM STARTUP
echo ============================================
echo.
echo This script starts the HRM platform:
echo - Backend (Port 8000) - Django API
echo - Frontend (Port 3000) - React App
echo.
echo Module: Human Resources Management (HRM)
echo ============================================
echo.

REM Check if we're in the right directory
if not exist "backend\manage.py" (
    echo ERROR: Please run this script from the olvine-erp root directory
    echo Current directory: %CD%
    pause
    exit /b 1
)

echo [CLEANUP] Clearing ports 8000 and 3000 if in use...
echo.

REM Kill any Python processes on port 8000 (Django)
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8000 ^| findstr LISTENING') do (
    echo Clearing port 8000...
    taskkill /F /PID %%a 2>nul
)

REM Kill any Node processes on port 3000 (Vite)
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :3000 ^| findstr LISTENING') do (
    echo Clearing port 3000...
    taskkill /F /PID %%a 2>nul
)

echo Ports cleared.
timeout /t 2 /nobreak >nul
echo.

echo ============================================
echo   STARTING BACKEND (Port 8000)
echo ============================================
echo.

start "Olivine HRM Backend" cmd /k "cd backend && python manage.py runserver 8000"

echo Waiting 8 seconds for backend to initialize...
timeout /t 8 /nobreak
echo.

echo ============================================
echo   STARTING FRONTEND (Port 3000)
echo ============================================
echo.

start "Olivine HRM Frontend" cmd /k "cd frontend && npx vite --port 3000"

echo Waiting 5 seconds for frontend to initialize...
timeout /t 5 /nobreak
echo.

echo ============================================
echo   HRM PLATFORM STARTED SUCCESSFULLY
echo ============================================
echo.
echo   Backend API:     http://localhost:8000
echo   Django Platform: http://localhost:8000/platform/
echo   Frontend App:    http://localhost:3000
echo.
echo   Credentials:
echo   - Admin:         admin / admin123
echo.
echo ============================================
echo.

echo Opening browser in 3 seconds...
timeout /t 3 /nobreak
start chrome http://localhost:8000/platform/
timeout /t 1 /nobreak
start chrome http://localhost:3000

echo.
echo Platform is running. Check the separate windows for logs.
echo Press any key to exit this launcher window...
pause >nul
