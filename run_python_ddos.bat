@echo off
title Python DDoS Toolkit - Windows
color 0A
echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                🚀 PYTHON DDoS TOOLKIT 2025                ║
echo ║                  ⚡ ADVANCED CYBER FRAMEWORK                ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

echo 🐍 Checking Python installation...
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Python is not installed!
    echo 📦 Please install Python from https://python.org
    echo.
    pause
    exit /b 1
)

echo ✅ Python found!
echo.

echo 🚀 Starting Python DDoS Toolkit...
echo.

cd /d "%~dp0"
python test_ddos.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ❌ Error occurred while running the program!
    echo.
    pause
    exit /b 1
)

echo.
echo Program closed. Press any key to exit...
pause >nul