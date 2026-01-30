@echo off
echo ========================================
echo 🚀 Starting File Search Explorer
echo ========================================
echo.
echo This will start:
echo 1. Backend API Server (Python)
echo 2. Frontend Web Interface
echo.
echo Base Directory: d:\olvine-erp
echo Server Port: 8888
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python is not installed or not in PATH
    echo Please install Python and try again
    pause
    exit /b 1
)

REM Start the backend server
echo 📡 Starting backend API server...
cd /d "%~dp0"
start "File Search API Server" cmd /k "python file-search-api.py"

REM Wait a moment for server to start
timeout /t 3 /nobreak >nul

REM Open the frontend in browser
echo 🌐 Opening web interface...
start http://localhost:8888/

echo.
echo ✅ File Search Explorer started successfully!
echo.
echo 📝 Usage:
echo    - Search for files using the web interface
echo    - Select file types to search (.md, .py, .js/.ts, .tsx/.jsx, .json, .bat/.sh)
echo    - Click on files to preview content
echo    - Use "Open in Editor" to open files in your default editor
echo.
echo 🛑 To stop: Close the API server window
echo.
pause
