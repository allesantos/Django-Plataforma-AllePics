# 📸 AllePics - Rede Social de Fotos

Uma mini rede social de fotos moderna desenvolvida com Django, PostgreSQL, Redis e MinIO, utilizando arquitetura profissional com containers Docker e processamento assíncrono de imagens.

---

## 📌 Índice
- [📜 Descrição](#-descrição)
- [🚀 Recursos](#-recursos)
- [🛠 Tecnologias](#-tecnologias)
- [✅ Pré-requisitos](#-pré-requisitos)
- [🔧 Instalação](#-instalação)
- [⚙️ Configuração](#️-configuração)
- [▶️ Uso](#️-uso)
- [🏗️ Arquitetura](#️-arquitetura)
- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
- [🐳 Docker Services](#-docker-services)
- [🔒 Segurança](#-segurança)
- [🤝 Contribuição](#-contribuição)
- [📄 Licença](#-licença)

---

## 📜 Descrição  
**AllePics** é uma plataforma web para compartilhamento de fotos, inspirada em redes sociais modernas. O projeto demonstra boas práticas de desenvolvimento web, incluindo autenticação robusta, armazenamento em nuvem (S3-compatible), cache inteligente e processamento assíncrono de imagens.

O sistema foi projetado para ser escalável e seguir padrões da indústria, utilizando containers Docker para serviços de infraestrutura e Python/Django para a aplicação web.

### 🎯 Objetivo do Projeto
Demonstrar conhecimentos em:
- Desenvolvimento web full-stack com Django
- Arquitetura de microsserviços com Docker
- Object Storage (S3-compatible com MinIO)
- Processamento assíncrono com Celery
- Cache e otimização de performance com Redis
- Banco de dados relacional com PostgreSQL
- Autenticação e autorização seguras
- UI/UX responsivo com Bootstrap 5

---

## 🚀 Recursos

### Implementados ✅
- 👤 **Sistema de Autenticação Completo**
  - Cadastro de usuários com validação robusta
  - Login/Logout seguro
  - Perfil de usuário personalizado
  - Proteção de rotas com decorators

- 🎨 **Interface Moderna e Responsiva**
  - Design clean com Bootstrap 5
  - Ícones elegantes com Bootstrap Icons
  - Layout responsivo (mobile-first)
  - Mensagens de feedback contextualizadas

- 🔐 **Segurança**
  - Senhas com hash bcrypt
  - Proteção CSRF
  - Validações de formulários server-side e client-side
  - Variáveis de ambiente para credenciais

- 🐳 **Infraestrutura com Docker**
  - PostgreSQL 16 (banco de dados)
  - Redis 7 (cache e message broker)
  - MinIO (object storage S3-compatible)
  - Health checks automáticos

### Em Desenvolvimento 🚧
- 📤 Upload de fotos com preview
- 🖼️ Galeria de fotos com paginação
- 🔄 Processamento assíncrono de imagens (thumbnails)
- 💾 Cache inteligente de consultas
- ❤️ Sistema de curtidas e comentários
- 👥 Sistema de seguidores

---

## 🛠 Tecnologias

| Camada        | Tecnologias                                            |
| :------------ | :----------------------------------------------------- |
| **Backend**   | Python 3.10+, Django 4.2+                              |
| **Banco de Dados** | PostgreSQL 16                                     |
| **Cache/Broker** | Redis 7                                             |
| **Storage**   | MinIO (S3-compatible)                                  |
| **Task Queue** | Celery (planejado)                                    |
| **Frontend**  | HTML5, CSS3, JavaScript, Bootstrap 5                   |
| **Containers** | Docker, Docker Compose                                |
| **Processamento** | Pillow (Python Imaging Library)                    |
| **Segurança** | python-decouple, django-environ                        |

---

## ✅ Pré-requisitos
Antes de iniciar, certifique-se de ter:

- **Python 3.10 ou superior** instalado
- **Docker Desktop** instalado e rodando
- **Git** para clonar o repositório
- **VS Code** (recomendado) ou outro editor de código
- Sistema operacional: Windows 10/11, Linux ou macOS

---

## 🔧 Instalação

### 1️⃣ Clone o Repositório

```bash
git clone https://github.com/seu-usuario/allepics.git
cd allepics
```

### 2️⃣ Crie o Ambiente Virtual

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate
```

### 3️⃣ Instale as Dependências

```bash
pip install -r requirements.txt
```

**Dependências principais:**
- Django==4.2.7
- python-decouple==3.8
- psycopg2-binary==2.9.9
- django-storages==1.14.2
- boto3==1.29.7
- celery==5.3.4
- redis==5.0.1
- django-redis==5.4.0
- Pillow==10.1.0

---

## ⚙️ Configuração

### 1️⃣ Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```bash
# Windows:
type nul > .env

# Linux/Mac:
touch .env
```

Adicione as seguintes configurações (exemplo seguro — personalize com seus próprios valores antes de usar):

```env
# PostgreSQL - Banco de Dados
POSTGRES_DB=seu_banco
POSTGRES_USER=seu_usuario
POSTGRES_PASSWORD=sua_senha
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

# Redis - Cache e Broker
REDIS_HOST=localhost
REDIS_PORT=6379

# MinIO - Armazenamento de Objetos
MINIO_ROOT_USER=seu_usuario_minio
MINIO_ROOT_PASSWORD=sua_senha_minio
MINIO_HOST=localhost
MINIO_PORT=9000
MINIO_CONSOLE_PORT=9001

# Django
SECRET_KEY=sua_chave_django
DEBUG=True
```

### 2️⃣ Iniciar Serviços Docker

```bash
# Subir todos os containers
docker-compose up -d

# Verificar status dos containers
docker-compose ps
```

**Containers iniciados:**
- `allepics_postgres` → PostgreSQL (porta 5432)
- `allepics_redis` → Redis (porta 6379)
- `allepics_minio` → MinIO (portas 9000, 9001)

### 3️⃣ Aplicar Migrations

```bash
# Criar tabelas do Django
python manage.py migrate

# Criar migrations do app users
python manage.py makemigrations users

# Aplicar migrations do users
python manage.py migrate
```

### 4️⃣ Criar Superusuário (Admin)

```bash
python manage.py createsuperuser
```

Preencha as informações solicitadas:
- Username: `admin`
- Email: `admin@allepics.com`
- Password: `admin123` (ou outra senha forte)

### 5️⃣ Configurar MinIO (Object Storage)

1. Acesse a interface do MinIO:
   ```
   http://localhost:9001
   ```

2. Faça login:
   - **Username:** `allepics_admin`
   - **Password:** `allepics_minio_senha_123`

3. Crie os buckets necessários:
   - `allepics-photos` (para fotos originais)
   - `allepics-thumbnails` (para miniaturas)

---

## ▶️ Uso

### 🚀 Iniciar o Servidor de Desenvolvimento

```bash
# Ativar ambiente virtual (se não estiver ativo)
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Iniciar servidor Django
python manage.py runserver
```

Acesse a aplicação em: **http://localhost:8000/**

---

### 📱 Funcionalidades Disponíveis

#### 🏠 Página Inicial
- Hero section com apresentação
- Cards explicativos dos recursos
- Botões de cadastro e login

#### 👤 Sistema de Usuários

**Cadastro:**
1. Clique em "Cadastrar"
2. Preencha: usuário, email e senha
3. Confirme a senha
4. Clique em "Criar Conta"

**Login:**
1. Clique em "Entrar"
2. Digite usuário e senha
3. Clique em "Entrar"

**Perfil:**
- Visualize suas informações
- Veja estatísticas (fotos, curtidas, seguidores)
- Acesso rápido para sair

#### 🔧 Django Admin

Acesse o painel administrativo em: **http://localhost:8000/admin/**

Funcionalidades:
- Gerenciar usuários
- Visualizar dados do sistema
- Configurações avançadas

---

## 🏗️ Arquitetura

### Diagrama de Componentes

```
┌─────────────────────────────────────────┐
│         CLIENTE (Navegador)             │
│  HTML + Bootstrap 5 + JavaScript        │
└──────────────┬──────────────────────────┘
               │ HTTP/HTTPS
               ▼
┌─────────────────────────────────────────┐
│      DJANGO APPLICATION (Python)        │
│                                         │
│  ┌─────────────────────────────────┐  │
│  │  Apps Django                    │  │
│  │  • core (home)                  │  │
│  │  • users (autenticação)         │  │
│  │  • photos (galeria) [futuro]    │  │
│  └─────────────────────────────────┘  │
└──┬───────┬──────────┬──────────────────┘
   │       │          │
   ▼       ▼          ▼
┌─────┐ ┌─────┐  ┌────────┐
│ PG  │ │Redis│  │ MinIO  │
│SQL  │ │     │  │        │
└─────┘ └─────┘  └────────┘
  DB     Cache    Storage
```

### Fluxo de Autenticação

```
1. Usuário acessa /cadastro/
2. Preenche formulário
3. Django valida dados
4. Hash de senha (bcrypt)
5. Salva no PostgreSQL
6. Login automático
7. Sessão criada no Redis
8. Redirect para home
```

---

## 📁 Estrutura do Projeto

```
allepics/
│
├── .env                        # Variáveis de ambiente (não versionado)
├── .gitignore                  # Arquivos ignorados pelo Git
├── docker-compose.yml          # Configuração dos containers
├── requirements.txt            # Dependências Python
├── manage.py                   # CLI do Django
│
├── allepics/                   # Configurações do projeto Django
│   ├── __init__.py
│   ├── settings.py             # Configurações principais
│   ├── urls.py                 # URLs principais
│   ├── wsgi.py
│   └── asgi.py
│
├── apps/                       # Aplicações Django
│   ├── __init__.py
│   │
│   ├── core/                   # App principal (home)
│   │   ├── templates/
│   │   │   └── core/
│   │   │       └── home.html
│   │   ├── views.py
│   │   └── urls.py
│   │
│   └── users/                  # Sistema de usuários
│       ├── migrations/
│       │   └── 0001_initial.py
│       ├── templates/
│       │   └── users/
│       │       ├── register.html
│       │       ├── login.html
│       │       └── profile.html
│       ├── models.py           # User Model customizado
│       ├── forms.py            # Formulários
│       ├── views.py            # Lógica de negócio
│       ├── urls.py             # Rotas do app
│       └── admin.py            # Config do Django Admin
│
├── static/                     # Arquivos estáticos (futuro)
│   ├── css/
│   ├── js/
│   └── images/
│
├── media/                      # Uploads temporários (dev)
│
└── venv/                       # Ambiente virtual Python
```

---

## 🐳 Docker Services

### PostgreSQL 16
**Porta:** 5432  
**Uso:** Banco de dados relacional principal

**Comando úteis:**
```bash
# Conectar ao PostgreSQL
docker exec -it allepics_postgres psql -U allepics_user -d allepics_db

# Ver logs
docker-compose logs postgres
```

---

### Redis 7
**Porta:** 6379  
**Uso:** Cache e message broker para Celery

**Comandos úteis:**
```bash
# Conectar ao Redis CLI
docker exec -it allepics_redis redis-cli

# Ver logs
docker-compose logs redis

# Comandos Redis úteis:
# KEYS *           → Ver todas as chaves
# GET key          → Ver valor de uma chave
# FLUSHALL         → Limpar todo o cache
```

---

### MinIO
**Portas:** 9000 (API), 9001 (Console)  
**Uso:** Object storage para fotos (S3-compatible)

**Acesso:**
- Console: http://localhost:9001
- API: http://localhost:9000

**Comandos úteis:**
```bash
# Ver logs
docker-compose logs minio

# Listar buckets via CLI
docker exec -it allepics_minio mc ls local/
```

---

### Gerenciar Containers

```bash
# Iniciar todos os serviços
docker-compose up -d

# Parar todos os serviços
docker-compose stop

# Ver status
docker-compose ps

# Ver logs em tempo real
docker-compose logs -f

# Parar e remover containers (mantém volumes)
docker-compose down

# Parar e remover containers + volumes (⚠️ apaga dados!)
docker-compose down -v

# Reiniciar um serviço específico
docker-compose restart postgres
```

---

## 🔒 Segurança

### Boas Práticas Implementadas

✅ **Senhas com Hash Bcrypt**
- Django usa bcrypt automaticamente
- Senhas nunca são armazenadas em texto plano

✅ **Proteção CSRF**
- Token CSRF em todos os formulários
- Proteção contra Cross-Site Request Forgery

✅ **Validações de Formulários**
- Server-side: validações Django robustas
- Client-side: validações HTML5 e JavaScript

✅ **Variáveis de Ambiente**
- Credenciais no `.env` (não versionado)
- `python-decouple` para gerenciar configs

✅ **Senhas Fortes**
- Mínimo 8 caracteres
- Validação de senhas comuns
- Não similar ao username/email
- Não apenas números

✅ **Proteção de Rotas**
- Decorator `@login_required` para rotas protegidas
- Redirecionamento automático para login

---

### ⚠️ IMPORTANTE - Segurança em Produção

Para ambientes de produção, altere:

```env
# .env PRODUÇÃO
DEBUG=False
SECRET_KEY=gere-uma-chave-forte-aleatoria-aqui
POSTGRES_PASSWORD=senha-muito-mais-forte-aqui
MINIO_ROOT_PASSWORD=outra-senha-forte-aqui
```

**Gerar SECRET_KEY segura:**
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

---

## 🧪 Testando o Sistema

### Teste Manual

1. **Containers rodando?**
   ```bash
   docker-compose ps
   # Todos devem estar "Up" e "healthy"
   ```

2. **Banco conectado?**
   ```bash
   python manage.py check --database default
   # Deve retornar: System check identified no issues
   ```

3. **Servidor rodando?**
   ```bash
   python manage.py runserver
   # Acesse http://localhost:8000
   ```

4. **Cadastro funcionando?**
   - Acesse /cadastro/
   - Cadastre um usuário
   - Deve fazer login automático

5. **Admin funcionando?**
   - Acesse /admin/
   - Faça login com superusuário
   - Visualize usuários cadastrados

---

## 📊 Status do Projeto

### Módulos Implementados ✅

| Módulo | Status | Descrição |
|--------|--------|-----------|
| Infraestrutura Docker | ✅ Completo | PostgreSQL, Redis, MinIO |
| Autenticação | ✅ Completo | Cadastro, Login, Logout |
| Perfil de Usuário | ✅ Completo | Visualização de dados |
| Interface UI/UX | ✅ Completo | Bootstrap 5 responsivo |
| Django Admin | ✅ Completo | Painel administrativo |

### Próximas Funcionalidades 🚧

| Módulo | Status | Descrição |
|--------|--------|-----------|
| Upload de Fotos | 🔄 Em breve | Form e validações |
| Galeria | 🔄 Em breve | Grid responsivo |
| Celery Tasks | 🔄 Em breve | Processamento assíncrono |
| Thumbnails | 🔄 Em breve | Redimensionamento automático |
| Cache Redis | 🔄 Em breve | Otimização de queries |
| Curtidas | 📅 Planejado | Sistema de likes |
| Comentários | 📅 Planejado | Interação social |
| Seguidores | 📅 Planejado | Rede social completa |

---

## 🤝 Contribuição

Contribuições são bem-vindas! Siga estas etapas:

1. **Fork o projeto**

2. **Clone seu fork**
   ```bash
   git clone https://github.com/seu-usuario/allepics.git
   cd allepics
   ```

3. **Crie uma branch para sua feature**
   ```bash
   git checkout -b feature/minha-feature
   ```

4. **Faça suas alterações e commit**
   ```bash
   git add .
   git commit -m "feat: adiciona minha feature"
   ```

5. **Push para o GitHub**
   ```bash
   git push origin feature/minha-feature
   ```

6. **Abra um Pull Request**

### Padrão de Commits

Seguimos o padrão [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` Nova funcionalidade
- `fix:` Correção de bug
- `docs:` Documentação
- `style:` Formatação
- `refactor:` Refatoração de código
- `test:` Testes
- `chore:` Tarefas gerais

---

## 🐛 Troubleshooting

### ❌ Erro: "No module named 'decouple'"
**Solução:**
```bash
pip install python-decouple
pip freeze > requirements.txt
```

### ❌ Erro: "connection refused" PostgreSQL
**Solução:**
```bash
# Verificar containers
docker-compose ps

# Reiniciar serviços
docker-compose restart postgres

# Ver logs
docker-compose logs postgres
```

### ❌ Erro: "Destination directory does not exist"
**Solução:**
```bash
# Criar pasta antes do startapp
mkdir apps\nome_do_app
python manage.py startapp nome_do_app apps/nome_do_app
```

### ❌ Erro: "Dependency on app with no migrations"
**Solução:**
```bash
# Criar migrations primeiro
python manage.py makemigrations nome_do_app
python manage.py migrate
```

### ❌ Mensagens em inglês
**Solução:** Altere no `settings.py`:
```python
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
```

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License**.

Você é livre para:
- ✅ Usar comercialmente
- ✅ Modificar
- ✅ Distribuir
- ✅ Uso privado

---

## 📞 Contato

Desenvolvido com ❤️ por **Alexandre Santos**

- 📧 Email: alledesenvolvimento@gmail.com
- 💼 LinkedIn: [linkedin.com/in/alle-carlos-alexandre](https://www.linkedin.com/in/alle-carlos-alexandre)
- 🐙 GitHub: [github.com/allesantos](https://github.com/allesantos)
- 🌐 Portfolio: [em breve]

---

## 🎯 Roadmap

### Versão 1.0 (MVP) - Atual ✅
- [x] Sistema de autenticação
- [x] Perfil de usuário
- [x] Interface responsiva
- [x] Docker infrastructure

### Versão 1.1 - Em Desenvolvimento 🚧
- [ ] Upload de fotos
- [ ] Galeria com paginação
- [ ] Processamento assíncrono (Celery)
- [ ] Geração de thumbnails

### Versão 1.2 - Planejado 📅
- [ ] Cache inteligente (Redis)
- [ ] Sistema de curtidas
- [ ] Sistema de comentários
- [ ] Busca de fotos

### Versão 2.0 - Futuro 🚀
- [ ] Sistema de seguidores
- [ ] Feed personalizado
- [ ] Notificações em tempo real
- [ ] API REST com Django REST Framework
- [ ] App mobile (React Native)

---

## 🌟 Agradecimentos

- [Django](https://www.djangoproject.com/) - Framework web
- [Bootstrap](https://getbootstrap.com/) - Framework CSS
- [Docker](https://www.docker.com/) - Containerização
- [PostgreSQL](https://www.postgresql.org/) - Banco de dados
- [Redis](https://redis.io/) - Cache e message broker
- [MinIO](https://min.io/) - Object storage

---

## 📸 Screenshots

> 📝 **Nota:** Screenshots serão adicionados em breve com as principais telas do sistema.

---

**⭐ Se este projeto foi útil para você, deixe uma estrela no repositório!**

---

**Última atualização:** Novembro 2024  
**Versão:** 1.0.0-alpha