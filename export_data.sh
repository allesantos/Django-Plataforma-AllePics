#!/bin/bash
# ==========================================
# AllePics - Script de Exportação PostgreSQL
# ==========================================

set -e

echo "🔍 Carregando variáveis de ambiente..."
source .env

BACKUP_FILE="backup_$(date +%Y%m%d_%H%M%S).sql"

echo "📦 Exportando banco de dados PostgreSQL..."
echo "   Database: $POSTGRES_DB"
echo "   User: $POSTGRES_USER"
echo "   Host: $POSTGRES_HOST"
echo "   Port: $POSTGRES_PORT"
echo ""

# Exporta via Docker (se estiver usando docker-compose local)
if docker ps | grep -q "allepics_postgres"; then
    echo "🐳 Detectado PostgreSQL rodando no Docker..."
    docker exec allepics_postgres pg_dump -U "$POSTGRES_USER" "$POSTGRES_DB" > "$BACKUP_FILE"
else
    echo "💻 Exportando via pg_dump local..."
    PGPASSWORD="$POSTGRES_PASSWORD" pg_dump -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -p "$POSTGRES_PORT" "$POSTGRES_DB" > "$BACKUP_FILE"
fi

echo ""
echo "✅ Backup criado com sucesso!"
echo "📄 Arquivo: $BACKUP_FILE"
echo "📊 Tamanho: $(du -h "$BACKUP_FILE" | cut -f1)"
echo ""
echo "🔐 Criando versão compactada..."
gzip -k "$BACKUP_FILE"
echo "📦 Arquivo compactado: ${BACKUP_FILE}.gz"
echo "📊 Tamanho compactado: $(du -h "${BACKUP_FILE}.gz" | cut -f1)"
echo ""
echo "🎉 Pronto! Agora você pode transferir para o servidor:"
echo "   scp $BACKUP_FILE root@alleartserv:/root/allepics/"
echo ""