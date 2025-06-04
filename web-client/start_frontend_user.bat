@echo off
REM Script per installare dipendenze e avviare il frontend-user minimale di RagFlow

cd /d %~dp0

echo Installazione dipendenze...
npm install

echo Avvio del frontend-user RagFlow...
start cmd /k "npm run dev"
