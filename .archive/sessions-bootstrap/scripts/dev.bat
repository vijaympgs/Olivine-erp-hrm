@echo off
echo ============================================
echo   STARTING DEVELOPMENT SERVERS
echo ============================================

echo Starting backend server...
start "Backend Server" cmd /k "cd backend && .venv\Scripts\activate && python manage.py runserver"

timeout /t 3 /nobreak > nul

echo Starting frontend server...
start "Frontend Server" cmd /k "cd frontend && npm run dev"

echo.
echo Development servers are starting...
echo Backend: http://localhost:8000
echo Frontend: http://localhost:5173 (or 3000)
echo API Docs: http://localhost:8000/api/docs/
echo.
echo Press any key to exit...
pause > nul