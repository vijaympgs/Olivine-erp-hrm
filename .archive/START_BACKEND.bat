@echo off
echo ..............................
echo    Starting Backend Server
echo ..............................
echo.

cd backend

echo Starting server on port 8000...
echo.
echo .....................................................
echo   Backend running at: http://localhost:8000
echo .....................................................
echo.
echo Press Ctrl+C to stop the server
echo.

python manage.py runserver 8000
