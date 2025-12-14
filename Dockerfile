# ==========================================
# AllePics - Dockerfile para Produção
# Python 3.11 + Django 5.2 + PostgreSQL
# ==========================================

FROM python:3.11-slim

# Evita prompts interativos
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Instala dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Cria diretório de trabalho
WORKDIR /app

# Copia requirements e instala dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia código do projeto
COPY . .

# Cria diretórios necessários
RUN mkdir -p /app/staticfiles /app/media /app/logs

# Cria usuário não-root (segurança)
RUN useradd -m -u 1000 django && \
    chown -R django:django /app

# Dá permissão de execução ao entrypoint
RUN chmod +x /app/entrypoint.sh

# Muda para usuário não-root
USER django

# Expõe porta 8000
EXPOSE 8000

# Entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]