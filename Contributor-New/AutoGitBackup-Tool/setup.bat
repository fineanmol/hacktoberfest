@echo off
echo Auto Git Backup Tool - Setup Script
echo ===================================
echo.

echo Installing Python dependencies...
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Failed to install dependencies!
    echo Please make sure you have Python 3.10+ and pip installed.
    echo.
    pause
    exit /b 1
)

echo.
echo Dependencies installed successfully!
echo.
echo To run the tool:
echo   python main.py          (with configuration GUI)
echo   python main.py --service (as service without GUI)
echo.
echo The tool will create a system tray icon when running.
echo Right-click the icon to start/pause/exit the service.
echo.
pause
