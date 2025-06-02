@echo off
echo === Pulizia e ricostruzione frontend RAGFlow (compatibile PowerShell) ===
if exist web\.umi rmdir /s /q web\.umi
if exist web\.mfsu rmdir /s /q web\.mfsu
if exist web\dist rmdir /s /q web\dist
if exist web\node_modules rmdir /s /q web\node_modules
if exist web\package-lock.json del /f /q web\package-lock.json
cd web
echo Installazione dipendenze...
npm install
echo Avvio server di sviluppo...
npm run dev
echo.
echo Apri l'app nel browser: http://localhost:9223
