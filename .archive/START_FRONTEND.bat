@echo off
echo ..............................
echo    Starting Frontend Server
echo ..............................
echo.

cd frontend

echo Starting frontend server on port 3000...
echo.
echo ...................................................
echo   Frontend running at: http://localhost:3000
echo   Backend at: http://localhost:8000
echo ...................................................
echo.
echo Press Ctrl+C to stop the server
echo.

npx vite --port 3000
