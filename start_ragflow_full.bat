@echo off
REM Script per avviare il backend RagFlow e il frontend-user minimale

echo Avvio backend RagFlow...
start cmd /k "cd /d %~dp0 && start_ragflow.bat"

timeout /t 10 /nobreak >nul

echo Avvio frontend-user RagFlow...
start cmd /k "cd /d %~dp0web-client && npm install && npm run dev"

echo Tutti i servizi sono stati avviati.
pause
