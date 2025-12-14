#!/bin/bash
# ==========================================
# AllePics - Script de Importação PostgreSQL
# Executar no SERVIDOR após deploy
# ==========================================

set -e

if [ -z "$1" ]; then
    echo "❌ Erro: Arquivo de backup não especificado!"
    echo "Uso: ./import_data.sh backup_20241214_120000.sql"
    exit 1
fi

BACKUP_FILE="$1"

if [ ! -f "$BACKUP_FILE" ]; then
    echo "❌ Erro: Arquivo $BACKUP_FILE não encontrado!"
    exit 1
fi

echo "🔍 Carregando variáveis de ambiente..."
source .env

echo "📥 Importando banco de dados PostgreSQL..."
echo "   Database: $POSTGRES_DB"
echo "   User: $POSTGRES_USER"
echo "   Arquivo: $BACKUP_FILE"
echo ""

# Verifica se o arquivo está compactado
if [[ "$BACKUP_FILE" == *.gz ]]; then
    echo "📦 Descompactando arquivo..."
    gunzip -k "$BACKUP_FILE"
    BACKUP_FILE="${BACKUP_FILE%.gz}"
fi

# Encontra o container do PostgreSQL
CONTAINER_ID=$(docker ps -qf "name=allepics_allepics_db")

if [ -z "$CONTAINER_ID" ]; then
    echo "❌ Erro: Container do PostgreSQL não encontrado!"
    echo "Certifique-se de que o stack foi deployado:"
    echo "   docker stack deploy -c docker-compose.prod.yml allepics"
    exit 1
fi

echo "🐳 Container encontrado: $CONTAINER_ID"
echo ""
echo "⏳ Aguardando PostgreSQL ficar pronto..."
sleep 5

echo "📥 Importando dados..."
docker exec -i "$CONTAINER_ID" psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" < "$BACKUP_FILE"

echo ""
echo "✅ Importação concluída com sucesso!"
echo ""
echo "🔍 Verificando dados importados..."
docker exec "$CONTAINER_ID" psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "\dt"
echo ""
echo "🎉 Pronto! Seu banco de dados está restaurado!"
echo ""