@echo off
echo ============================================
echo   QUICK DEV STARTUP (Unified Platform)
echo ============================================
echo.
echo This is a simplified version of START_UNIFIED.bat
echo for quick development without browser launch
echo.
echo Starting: Backend (8000) + Frontend (3001)
echo ============================================
echo.

REM Navigate to backend
cd backend
start "Backend" cmd /k "python manage.py runserver 8000"
cd ..

echo Waiting 5 seconds for backend...
timeout /t 5 /nobreak

REM Navigate to frontend
cd frontend
start "Frontend" cmd /k "npm run dev -- --port 3001"
cd ..

echo.
echo ============================================
echo   Servers Starting
echo ============================================
echo   Backend:  http://localhost:8000
echo   Frontend: http://localhost:3001
echo ============================================
echo.
echo Press any key to exit...
pause >nul
