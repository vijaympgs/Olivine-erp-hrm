@echo off
echo ========================================
echo Restarting File Search API Server
echo ========================================
echo.

REM Kill any existing Python processes running file-search-api.py
taskkill /F /IM python.exe /FI "WINDOWTITLE eq file-search-api*" 2>nul

echo Waiting 2 seconds...
timeout /t 2 /nobreak >nul

echo Starting File Search API Server...
echo.
start "File Search API Server" python file-search-api.py

echo.
echo ========================================
echo Server restarted!
echo ========================================
echo.
echo The server is now running in a new window.
echo Close this window or press any key to exit.
pause >nul
