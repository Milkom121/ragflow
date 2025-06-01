@echo off
echo === RAGFlow: Riavvio veloce (soft restart, solo servizi) ===
docker compose -f docker/docker-compose.yml restart
echo Tutti i servizi RAGFlow sono stati riavviati rapidamente.
