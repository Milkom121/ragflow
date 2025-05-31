@echo off
REM Script di avvio automatico per RAGFlow (Docker Compose) - Windows
REM Usage: start_ragflow.bat

echo === RAGFlow: Avvio automatico (Windows) ===

REM Verifica presenza Docker
where docker >nul 2>nul
if errorlevel 1 (
    echo Errore: Docker non e' installato o non e' nel PATH.
    exit /b 1
)

REM Verifica che Docker sia in esecuzione
docker info >nul 2>nul
if errorlevel 1 (
    echo Errore: Docker non e' in esecuzione. Avvialo e riprova.
    exit /b 1
)

REM Directory docker e compose file
set DOCKER_DIR=docker
set COMPOSE_FILE=docker-compose.yml

if not exist "%DOCKER_DIR%\%COMPOSE_FILE%" (
    echo Errore: File %DOCKER_DIR%\%COMPOSE_FILE% non trovato.
    exit /b 1
)

cd "%DOCKER_DIR%"

echo Avvio dei servizi tramite Docker Compose...
docker compose -f "%COMPOSE_FILE%" up -d

echo.
echo Stato dei container RAGFlow:
docker compose ps

echo.
echo Per visualizzare i log del backend:
echo   docker logs -f ragflow-server
echo.
echo Quando i servizi sono attivi, accedi a: http://localhost
echo.
echo Per fermare i servizi:
echo   docker compose -f %COMPOSE_FILE% down

cd ..
