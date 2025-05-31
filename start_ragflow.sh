#!/bin/bash
# Script di avvio automatico per RAGFlow (Docker Compose)
# Usage: bash start_ragflow.sh

set -e

echo "=== RAGFlow: Avvio automatico ==="

# Verifica presenza Docker
if ! command -v docker &> /dev/null; then
  echo "Errore: Docker non è installato o non è nel PATH."
  exit 1
fi

# Verifica che Docker sia in esecuzione
if ! docker info &> /dev/null; then
  echo "Errore: Docker non è in esecuzione. Avvialo e riprova."
  exit 1
fi

# Directory docker
DOCKER_DIR="docker"
COMPOSE_FILE="docker-compose.yml"

if [ ! -d "$DOCKER_DIR" ] || [ ! -f "$DOCKER_DIR/$COMPOSE_FILE" ]; then
  echo "Errore: File $DOCKER_DIR/$COMPOSE_FILE non trovato."
  exit 1
fi

cd "$DOCKER_DIR"

echo "Avvio dei servizi tramite Docker Compose..."
docker compose -f "$COMPOSE_FILE" up -d

echo ""
echo "Stato dei container RAGFlow:"
docker compose ps

echo ""
echo "Per visualizzare i log del backend:"
echo "  docker logs -f ragflow-server"
echo ""
echo "Quando i servizi sono attivi, accedi a: http://localhost"
echo ""
echo "Per fermare i servizi:"
echo "  docker compose -f $COMPOSE_FILE down"
