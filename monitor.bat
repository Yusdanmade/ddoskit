@echo off
title DDoS Monitor - Real Time
color 0A
:loop
cls
echo ================================
echo    DDoS ATTACK MONITOR
echo    %time%
echo ================================
echo.
if exist attack_log.json (
    type attack_log.json
    echo.
) else (
    Waiting for attack data...
)
echo ================================
timeout /t 1 >nul
goto loop
