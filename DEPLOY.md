# 🚀 Guia de Deploy - AllePics

## 📋 Pré-requisitos

- ✅ Git configurado
- ✅ Docker instalado localmente (opcional - só pra testar)
- ✅ Acesso SSH ao servidor: `ssh root@alleartserv`
- ✅ Servidor com Docker Swarm ativo
- ✅ Traefik rodando na rede `aiautomate`

## 💻 Observação - Comandos Windows vs Linux

Este guia mostra comandos para **ambos os sistemas**:

- **Windows PowerShell:** Comandos com `New-Item`, `Copy-Item`, etc
- **Linux/Mac/Servidor:** Comandos com `cp`, `touch`, `chmod`, etc

No **servidor** (Linux), sempre use os comandos Linux! 🐧

---

## 🎯 Fase 1: Preparação Local

### 1.1 - Gerar SECRET_KEY para produção

```python
# No terminal Python local
python manage.py shell
>>> from django.core.management.utils import get_random_secret_key
>>> print(get_random_secret_key())
>>> exit()
```

### 1.2 - Criar arquivo `.env.production`

**No Windows PowerShell:**

```powershell
# Crie o arquivo .env.production
New-Item -Path .env.production -ItemType File

# Edite com VS Code ou Notepad
code .env.production
# OU
notepad .env.production
```

**No Linux/Mac:**

```bash
# Crie o arquivo
touch .env.production

# Edite com nano ou vim
nano .env.production
```

**📝 Cole este conteúdo dentro do arquivo:**

```bash
# ===================================
# ALLEPICS - VARIÁVEIS DE PRODUÇÃO
# ===================================

# Django
SECRET_KEY=COLE_A_SECRET_KEY_GERADA_NO_PASSO_1.1_AQUI
DEBUG=False
ALLOWED_HOSTS=allepics.alleart.com.br

# PostgreSQL (Produção)
POSTGRES_DB=allepics_db
POSTGRES_USER=allepics_user
POSTGRES_PASSWORD=CRIE_SENHA_FORTE_AQUI_MINIMO_20_CARACTERES
POSTGRES_HOST=allepics_db
POSTGRES_PORT=5432
```

**Preencha:**
- `SECRET_KEY=` (valor gerado no passo 1.1)
- `POSTGRES_PASSWORD=` (senha forte, mínimo 20 caracteres)

### 1.3 - Exportar dados do PostgreSQL local

**⚠️ IMPORTANTE:** Este script é para **Linux/Mac ou Git Bash no Windows**

**No Windows PowerShell, use:**

```powershell
# Certifique-se que o Docker está rodando
docker ps

# Exportar banco manualmente
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$backupFile = "backup_$timestamp.sql"

docker exec allepics_postgres pg_dump -U allepics_user allepics_db > $backupFile

Write-Host "✅ Backup criado: $backupFile"
```

**No Linux/Mac ou Git Bash:**

```bash
# Dê permissão de execução
chmod +x export_data.sh

# Execute o script
./export_data.sh
```

Será gerado: `backup_YYYYMMDD_HHMMSS.sql`

---

## 🐳 Fase 2: Preparar Repositório Git

### 2.1 - Criar branch de deploy

```bash
git checkout -b feat/docker-producao
```

### 2.2 - Adicionar arquivos novos

```bash
git add Dockerfile
git add entrypoint.sh
git add docker-compose.prod.yml
git add .dockerignore
git add requirements.txt
git add allepics/settings.py
git add .gitignore
git add export_data.sh
git add import_data.sh
git add DEPLOY.md
```

### 2.3 - Commit

```bash
git commit -m "feat: adicionar configuração Docker para produção

- Adicionar Dockerfile otimizado com Python 3.11
- Configurar docker-compose.prod.yml para Swarm
- Adicionar Gunicorn e Whitenoise
- Configurar entrypoint.sh com wait-for-postgres
- Adicionar scripts de backup/restore PostgreSQL
- Atualizar settings.py com configurações de produção
- Configurar labels Traefik para SSL automático
"
```

### 2.4 - Push para GitHub

```bash
git push origin feat/docker-producao
```

### 2.5 - Criar Pull Request no GitHub

1. Acesse: https://github.com/allesantos/Django-Plataforma-AllePics
2. Clique em "Compare & pull request"
3. Revise as mudanças
4. Crie o Pull Request
5. Faça o Merge para `main`

---

## 🖥️ Fase 3: Deploy no Servidor

### 3.1 - Conectar no servidor

```bash
ssh root@alleartserv
```

### 3.2 - Clonar repositório

```bash
cd /root
git clone https://github.com/allesantos/Django-Plataforma-AllePics.git allepics
cd allepics
```

### 3.3 - Criar arquivo `.env` no servidor

```bash
nano .env
```

**Cole o conteúdo do seu `.env.production` local** (com as senhas já preenchidas)

**⚠️ IMPORTANTE:** Nunca commite este arquivo no Git!

### 3.4 - Transferir backup do PostgreSQL

**Na sua máquina local:**

```bash
# Use o arquivo gerado pelo export_data.sh
scp backup_20241214_120000.sql root@alleartserv:/root/allepics/
```

### 3.5 - Transferir pasta media

**Na sua máquina local:**

```bash
scp -r media/ root@alleartserv:/root/allepics/
```

### 3.6 - Build da imagem Docker

**No servidor:**

```bash
docker build -t allepics-app:latest .
```

⏱️ **Tempo estimado:** 3-5 minutos

### 3.7 - Deploy da stack no Swarm

```bash
docker stack deploy -c docker-compose.prod.yml allepics
```

### 3.8 - Verificar serviços

```bash
docker service ls | grep allepics
```

**Deve mostrar:**
```
allepics_allepics         1/1
allepics_allepics_db      1/1
```

### 3.9 - Aguardar PostgreSQL ficar pronto

```bash
docker service logs allepics_allepics_db --tail 20
```

**Aguarde:** `database system is ready to accept connections`

### 3.10 - Importar dados no PostgreSQL

```bash
# Dê permissão de execução
chmod +x import_data.sh

# Execute o script
./import_data.sh backup_20241214_120000.sql
```

### 3.11 - Verificar logs da aplicação

```bash
docker service logs allepics_allepics --tail 50
```

**Logs esperados:**
```
✅ PostgreSQL está pronto!
🔄 Executando migrações do banco de dados...
📦 Coletando arquivos estáticos...
🚀 Iniciando Gunicorn...
```

---

## 🌐 Fase 4: Configurar DNS

### 4.1 - Adicionar registro DNS

No seu provedor de domínio (ex: Registro.br):

```
Tipo: A
Nome: allepics
Valor: <IP_DO_SERVIDOR>
TTL: 3600
```

### 4.2 - Aguardar propagação

```bash
# Testar propagação DNS
nslookup allepics.alleart.com.br
```

⏱️ **Tempo:** 5-30 minutos

---

## ✅ Fase 5: Verificação Final

### 5.1 - Testar acesso HTTPS

```bash
curl -I https://allepics.alleart.com.br
```

**Resposta esperada:** `HTTP/2 200`

### 5.2 - Verificar no navegador

Acesse: https://allepics.alleart.com.br

**Checklist:**
- [ ] Página inicial carrega
- [ ] Login funciona
- [ ] Fotos antigas aparecem
- [ ] Upload de nova foto funciona
- [ ] Profile pictures aparecem
- [ ] CSS carrega corretamente
- [ ] Certificado SSL válido (cadeado verde)

### 5.3 - Verificar logs de erro

```bash
docker service logs allepics_allepics | grep -i error
```

---

## 🔄 Atualizações Futuras

### Workflow obrigatório:

```
Local → Branch → Commit → Push → Pull Request → Merge → Servidor → Pull → Build → Deploy
```

### Comandos:

**1. Na máquina local:**

```bash
# Criar branch
git checkout -b feat/nova-feature

# Fazer alterações no código
# ...

# Commit e push
git add .
git commit -m "feat: descrição da mudança"
git push origin feat/nova-feature
```

**2. No GitHub:**
- Criar Pull Request
- Revisar mudanças
- Fazer Merge

**3. No servidor:**

```bash
cd /root/allepics

# Atualizar código
git pull origin main

# Rebuild imagem
docker build -t allepics-app:latest .

# Atualizar serviço (zero-downtime)
docker service update --image allepics-app:latest allepics_allepics

# Verificar logs
docker service logs allepics_allepics --tail 30
```

---

## 🛠️ Comandos Úteis

### Ver logs em tempo real

```bash
docker service logs -f allepics_allepics
```

### Executar comandos Django

```bash
# Encontrar container
CONTAINER_ID=$(docker ps -qf name=allepics_allepics)

# Shell Django
docker exec -it $CONTAINER_ID python manage.py shell

# Criar superuser
docker exec -it $CONTAINER_ID python manage.py createsuperuser
```

### Backup do PostgreSQL (no servidor)

```bash
# Encontrar container do banco
DB_CONTAINER=$(docker ps -qf name=allepics_allepics_db)

# Fazer backup
docker exec $DB_CONTAINER pg_dump -U allepics_user allepics_db > backup_$(date +%Y%m%d).sql

# Backup compactado
docker exec $DB_CONTAINER pg_dump -U allepics_user allepics_db | gzip > backup_$(date +%Y%m%d).sql.gz
```

### Reiniciar serviço

```bash
docker service update --force allepics_allepics
```

### Ver recursos consumidos

```bash
docker stats $(docker ps -qf name=allepics)
```

---

## 🚨 Troubleshooting

### Problema: PostgreSQL não inicia

```bash
# Ver logs
docker service logs allepics_allepics_db

# Verificar senha no .env
cat .env | grep POSTGRES_PASSWORD
```

### Problema: Fotos não aparecem

```bash
# Verificar volume
docker volume inspect allepics_media

# Verificar permissões dentro do container
CONTAINER_ID=$(docker ps -qf name=allepics_allepics)
docker exec $CONTAINER_ID ls -la /app/media
```

### Problema: SSL não funciona

```bash
# Ver logs do Traefik
docker service logs traefik_traefik | grep allepics

# Verificar labels
docker service inspect allepics_allepics --format='{{json .Spec.TaskTemplate.ContainerSpec.Labels}}' | jq
```

### Problema: Static files não carregam

```bash
# Re-coletar static files
CONTAINER_ID=$(docker ps -qf name=allepics_allepics)
docker exec $CONTAINER_ID python manage.py collectstatic --noinput
```

---

## 📊 Recursos Estimados

### Espaço em Disco:
- Imagem Django: ~300MB
- Imagem PostgreSQL: ~140MB
- Banco PostgreSQL: ~10MB
- Media files: ~30MB
- Static files: ~5MB
- **Total:** ~485MB

### CPU e RAM:
- **Django:** 0.5-1.0 core | 512MB-1GB
- **PostgreSQL:** 0.25 core | 256MB-512MB
- **Total:** ~0.75-1.25 cores | 768MB-1.5GB

---

## 🎉 Pronto!

Seu AllePics está no ar! 🚀

**URL:** https://allepics.alleart.com.br

Para dúvidas, consulte o arquivo `plano_deploy_allepics.md` completo.