@echo off
echo ============================================
echo   RETAIL ERP PLATFORM - INITIAL SETUP
echo ============================================

echo.
echo Setting up backend...
cd backend

echo Creating virtual environment...
python -m venv .venv

echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo Installing Python dependencies...
pip install -r requirements.txt

echo Running database migrations...
python manage.py migrate

echo.
echo Backend setup complete!
echo.
echo Setting up frontend...
cd ..\frontend

echo Installing Node.js dependencies...
npm install

echo.
echo ============================================
echo   SETUP COMPLETE!
echo ============================================
echo.
echo To start development:
echo 1. Backend: cd backend && .venv\Scripts\activate && python manage.py runserver
echo 2. Frontend: cd frontend && npm run dev
echo.
echo Don't forget to:
echo - Copy .env.example to .env in both backend and frontend
echo - Create a superuser: python manage.py createsuperuser
echo.

pause