# 📸 AllePics - Rede Social de Fotos

Uma mini rede social de fotos moderna desenvolvida com Django, PostgreSQL, Redis e MinIO, utilizando arquitetura profissional com containers Docker e processamento assíncrono de imagens.

---

## 📌 Índice
- [📜 Descrição](#-descrição)
- [📸 Screenshots](#-screenshots)
- [🚀 Recursos](#-recursos)
- [🛠 Tecnologias](#-tecnologias)
- [✅ Pré-requisitos](#-pré-requisitos)
- [🔧 Instalação](#-instalação)
- [⚙️ Configuração](#️-configuração)
- [▶️ Uso](#️-uso)
- [🗂️ Arquitetura](#️-arquitetura)
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

## 📸 Screenshots do Sistema 
Abaixo estão algumas telas principais da aplicação, demonstrando o fluxo completo do usuário — desde o cadastro até a navegação pela galeria.

📝 **1. Tela de Cadastro**

<img src="https://github.com/allesantos/allesantos/blob/main/imagens/Django-Plataforma-AllePics/1-cadastro.png" width="700">

✅ **2. Tela de Confirmação de Cadastro**

<img src="https://github.com/allesantos/allesantos/blob/main/imagens/Django-Plataforma-AllePics/2-confirma%C3%A7%C3%A3o.png" width="700">

🔐 **3. Tela de Login**

<img src="https://github.com/allesantos/allesantos/blob/main/imagens/Django-Plataforma-AllePics/3-login.png" width="700">

📤 **4. Tela de Upload de Imagem**

<img src="https://github.com/allesantos/allesantos/blob/main/imagens/Django-Plataforma-AllePics/4-enviar_foto.png" width="700">

🖼️ **5. Galeria de Imagens**

<img src="https://github.com/allesantos/allesantos/blob/main/imagens/Django-Plataforma-AllePics/5-galeria.png" width="700">

📑 **6. Paginação da Galeria**

<img src="https://github.com/allesantos/allesantos/blob/main/imagens/Django-Plataforma-AllePics/6-pagina%C3%A7%C3%A3o.png" width="700">

🔍 **7. Detalhes de uma Imagem**

<img src="https://github.com/allesantos/allesantos/blob/main/imagens/Django-Plataforma-AllePics/7-detalhes.png" width="700">

👤 **8. Perfil do Usuário**

<img src="https://github.com/allesantos/allesantos/blob/main/imagens/Django-Plataforma-AllePics/8-ver_perfil.png" width="700">

---

## 🚀 Recursos

### Implementados ✅
- 👤 **Sistema de Autenticação Completo**
  - Cadastro de usuários com validação robusta
  - Login/Logout seguro
  - Perfil de usuário personalizado
  - Proteção de rotas com decorators

- 📸 **Sistema de Fotos Completo**
  - Upload de fotos com preview instantâneo
  - Validação de tipo (JPG, PNG) e tamanho (máx 5MB)
  - Galeria responsiva com grid 4 colunas
  - Paginação inteligente (12 fotos por página)
  - Página de detalhes com informações completas
  - Download de foto original
  - Deleção com modal de confirmação
  - Proteção: apenas dono acessa suas fotos
  - Armazenamento organizado por data (YYYY/MM/DD)

- 🎨 **Interface Moderna e Responsiva**
  - Design clean com Bootstrap 5
  - Ícones elegantes com Bootstrap Icons
  - Layout responsivo (mobile-first)
  - Mensagens de feedback contextualizadas
  - Hover effects nos cards
  - Dropdown menu na navbar
  - Breadcrumbs para navegação
  - Estados vazios (empty states) bonitos

- 🔐 **Segurança**
  - Senhas com hash bcrypt
  - Proteção CSRF
  - Validações de formulários server-side e client-side
  - Variáveis de ambiente para credenciais
  - Upload apenas para usuários autenticados
  - Validação de propriedade de fotos

- 🐳 **Infraestrutura com Docker**
  - PostgreSQL 16 (banco de dados)
  - Redis 7 (cache e message broker)
  - MinIO (object storage S3-compatible)
  - Health checks automáticos

### Em Desenvolvimento 🚧
- 🔍 Busca e filtros na galeria
- 🔄 Processamento assíncrono de imagens (thumbnails)
- 💾 Cache inteligente de consultas
- ☁️ Migração para MinIO (Object Storage)
- ⚡ Otimização de queries

### Próximas Features 📅
- ❤️ Sistema de curtidas
- 💬 Sistema de comentários
- 👥 Sistema de seguidores
- 🔔 Notificações
- 🔎 Busca avançada

---

## 🛠 Tecnologias

| Camada        | Tecnologias                                            |
| :------------ | :----------------------------------------------------- |
| **Backend**   | Python 3.14, Django 5.2.8                              |
| **Banco de Dados** | PostgreSQL 16                                     |
| **Cache/Broker** | Redis 7                                             |
| **Storage**   | MinIO (S3-compatible) - Preparado                      |
| **Task Queue** | Celery - Preparado                                    |
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
- Django==5.2.8
- python-decouple==3.8
- psycopg2-binary==2.9.9
- Pillow==10.1.0
- django-storages==1.14.2 (preparado)
- boto3==1.29.7 (preparado)
- celery==5.3.4 (preparado)
- redis==5.0.1 (preparado)
- django-redis==5.4.0 (preparado)

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

Adicione as seguintes configurações (exemplo seguro – personalize com seus próprios valores antes de usar):

```env
# PostgreSQL - Banco de Dados
POSTGRES_DB=allepics_db
POSTGRES_USER=allepics_user
POSTGRES_PASSWORD=allepics_senha_segura_123
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

# Redis - Cache e Broker
REDIS_HOST=localhost
REDIS_PORT=6379

# MinIO - Armazenamento de Objetos
MINIO_ROOT_USER=allepics_admin
MINIO_ROOT_PASSWORD=allepics_minio_senha_123
MINIO_HOST=localhost
MINIO_PORT=9000
MINIO_CONSOLE_PORT=9001

# Django
SECRET_KEY=django-insecure-desenvolvimento-local-123
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
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
# Criar todas as tabelas do projeto
python manage.py migrate

# Verificar migrations aplicadas
python manage.py showmigrations
```

### 4️⃣ Criar Superusuário (Admin)

```bash
python manage.py createsuperuser
```

Preencha as informações solicitadas:
- Username: `admin`
- Email: `admin@allepics.com`
- Password: `admin123` (ou outra senha forte)

### 5️⃣ Configurar MinIO (Object Storage) - Opcional

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

**Nota:** Atualmente o sistema usa armazenamento local (pasta `media/`). A integração com MinIO será implementada em breve.

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
- Links para upload e galeria (quando logado)

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
- Link para galeria
- Acesso rápido para sair

#### 📸 Sistema de Fotos

**Upload de Fotos:**
1. Clique em "Upload" no menu
2. Preencha o título (obrigatório)
3. Adicione descrição (opcional)
4. Selecione a foto (JPG ou PNG, máx 5MB)
5. Veja o preview da foto antes de enviar
6. Clique em "Enviar Foto"

**Galeria:**
- Visualize todas as suas fotos em grid responsivo
- 12 fotos por página com paginação
- Hover effect nos cards
- Botões de ação: Ver detalhes e Deletar

**Detalhes da Foto:**
- Visualize a foto em tamanho maior
- Veja todas as informações (título, descrição, data)
- Baixe a foto original
- Delete a foto (com confirmação)
- Breadcrumb para navegação fácil

**Deletar Foto:**
- Clique no ícone da lixeira
- Confirme no modal
- Foto e arquivo físico são removidos

#### 🔧 Django Admin

Acesse o painel administrativo em: **http://localhost:8000/admin/**

Funcionalidades:
- Gerenciar usuários
- Visualizar e gerenciar fotos
- Preview de imagens no admin
- Filtros e busca avançada
- Configurações avançadas

---

## 🗂️ Arquitetura

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
│  │  • photos (galeria) ✅          │  │
│  └─────────────────────────────────┘  │
└──┬───────┬──────────┬──────────────────┘
   │       │          │
   ▼       ▼          ▼
┌─────┐ ┌─────┐  ┌────────┐
│ PG  │ │Redis│  │ MinIO  │
│SQL  │ │     │  │ (prep) │
└─────┘ └─────┘  └────────┘
  DB     Cache    Storage
```

### Fluxo de Upload de Fotos

```
1. Usuário acessa /upload/
2. Preenche formulário (título, descrição, foto)
3. JavaScript mostra preview
4. Django valida:
   - Tipo de arquivo (JPG, PNG)
   - Tamanho (máx 5MB)
   - Campos obrigatórios
5. Salva em media/photos/YYYY/MM/DD/
6. Cria registro no PostgreSQL
7. Associa foto ao usuário
8. Redirect para /upload/ com mensagem
9. Usuário pode fazer novo upload
```

### Fluxo de Galeria

```
1. Usuário acessa /gallery/
2. Django busca fotos do usuário
3. Aplica ordenação (mais recentes primeiro)
4. Divide em páginas (12 fotos/página)
5. Renderiza grid responsivo
6. Cada card tem:
   - Preview da foto
   - Título e descrição
   - Data de upload
   - Botões: Ver detalhes, Deletar
7. Paginação no final
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
│   ├── users/                  # Sistema de usuários
│   │   ├── migrations/
│   │   │   └── 0001_initial.py
│   │   ├── templates/
│   │   │   └── users/
│   │   │       ├── register.html
│   │   │       ├── login.html
│   │   │       └── profile.html
│   │   ├── models.py           # User Model customizado
│   │   ├── forms.py            # Formulários
│   │   ├── views.py            # Lógica de negócio
│   │   ├── urls.py             # Rotas do app
│   │   └── admin.py            # Config do Django Admin
│   │
│   └── photos/                 # Sistema de fotos ✅
│       ├── migrations/
│       │   └── 0001_initial.py
│       ├── templates/
│       │   └── photos/
│       │       ├── upload.html     # Form de upload
│       │       ├── gallery.html    # Grid de fotos
│       │       └── detail.html     # Detalhes da foto
│       ├── models.py           # Photo Model
│       ├── forms.py            # PhotoUploadForm
│       ├── views.py            # upload, gallery, detail, delete
│       ├── urls.py             # Rotas do app
│       └── admin.py            # Admin com preview
│
├── static/                     # Arquivos estáticos (futuro)
│   ├── css/
│   ├── js/
│   └── images/
│
├── media/                      # Uploads de fotos ✅
│   └── photos/
│       └── YYYY/MM/DD/         # Organizados por data
│
└── venv/                       # Ambiente virtual Python
```

---

## 🐳 Docker Services

### PostgreSQL 16
**Porta:** 5432  
**Uso:** Banco de dados relacional principal

**Tabelas:**
- `users_user` - Usuários do sistema
- `photos_photo` - Fotos enviadas

**Comandos úteis:**
```bash
# Conectar ao PostgreSQL
docker exec -it allepics_postgres psql -U allepics_user -d allepics_db

# Ver todas as fotos
SELECT id, title, user_id, uploaded_at FROM photos_photo;

# Contar fotos por usuário
SELECT u.username, COUNT(p.id) as total_fotos
FROM users_user u
LEFT JOIN photos_photo p ON u.id = p.user_id
GROUP BY u.username;

# Ver logs
docker-compose logs postgres
```

---

### Redis 7
**Porta:** 6379  
**Uso:** Cache e message broker para Celery (preparado)

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
**Uso:** Object storage para fotos (preparado para migração)

**Acesso:**
- Console: http://localhost:9001
- API: http://localhost:9000

**Status:** Containers rodando e buckets criados. Integração será implementada em breve.

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

✅ **Validação de Upload**
- Apenas JPG e PNG permitidos
- Tamanho máximo: 5MB por foto
- Verificação de content_type
- Apenas usuários autenticados

✅ **Proteção de Dados**
- Usuários só veem suas próprias fotos
- `@login_required` em todas as views de fotos
- `get_object_or_404` com filtro de propriedade
- 404 automático para fotos de outros usuários

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
ALLOWED_HOSTS=seu-dominio.com,www.seu-dominio.com
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

5. **Upload funcionando?**
   - Acesse /upload/
   - Faça upload de uma foto
   - Deve mostrar preview e salvar

6. **Galeria funcionando?**
   - Acesse /gallery/
   - Deve mostrar suas fotos em grid
   - Teste paginação (se tiver mais de 12)

7. **Detalhes funcionando?**
   - Clique em "Ver detalhes" em uma foto
   - Deve abrir página com foto grande
   - Teste download da foto

8. **Deleção funcionando?**
   - Clique em "Deletar"
   - Confirme no modal
   - Foto deve ser removida

9. **Admin funcionando?**
   - Acesse /admin/
   - Faça login com superusuário
   - Visualize fotos com preview

---

## 📊 Status do Projeto

### Módulos Implementados ✅

| Módulo | Status | Descrição |
|--------|--------|-----------|
| Infraestrutura Docker | ✅ Completo | PostgreSQL, Redis, MinIO |
| Autenticação | ✅ Completo | Cadastro, Login, Logout |
| Perfil de Usuário | ✅ Completo | Visualização de dados e contador |
| Interface UI/UX | ✅ Completo | Bootstrap 5 responsivo |
| Django Admin | ✅ Completo | Painel administrativo |
| Upload de Fotos | ✅ Completo | Form, validações, preview |
| Galeria | ✅ Completo | Grid responsivo, paginação |
| Detalhes | ✅ Completo | Visualização e download |
| Deleção | ✅ Completo | Modal de confirmação |

### Próximas Funcionalidades 🚧

| Módulo | Status | Descrição |
|--------|--------|-----------|
| Busca e Filtros | 🔄 Próximo | Buscar por título, filtros |
| Otimização | 🔄 Próximo | Queries otimizadas |
| MinIO Integration | 📅 Planejado | Migrar para object storage |
| Celery Tasks | 📅 Planejado | Processamento assíncrono |
| Thumbnails | 📅 Planejado | Redimensionamento automático |
| Cache Redis | 📅 Planejado | Otimização de queries |
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

## 🛠 Troubleshooting

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

### ❌ Erro: "Cannot use ImageField"
**Solução:**
```bash
pip install Pillow
pip freeze > requirements.txt
```

### ❌ Erro: Foto não aparece (404)
**Solução:**
Verificar se MEDIA está configurado no `settings.py` e `urls.py`:
```python
# settings.py
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

# urls.py
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
```

### ❌ Erro: "TemplateDoesNotExist"
**Solução:**
Verificar estrutura de pastas:
```
apps/photos/templates/photos/gallery.html
                     └─── app_name/template.html
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

---

## 🎯 Roadmap

### Versão 1.0 (MVP) - Atual ✅
- [x] Sistema de autenticação
- [x] Perfil de usuário
- [x] Interface responsiva
- [x] Docker infrastructure
- [x] Upload de fotos
- [x] Galeria com paginação
- [x] Detalhes e deleção de fotos

### Versão 1.1 - Próximo 🚧
- [ ] Busca e filtros na galeria
- [ ] Otimização de queries
- [ ] Edição de fotos
- [ ] Tags/categorias

### Versão 1.2 - Planejado 📅
- [ ] Integração com MinIO
- [ ] Processamento assíncrono (Celery)
- [ ] Geração de thumbnails
- [ ] Cache inteligente (Redis)

### Versão 2.0 - Futuro 🚀
- [ ] Sistema de curtidas
- [ ] Sistema de comentários
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


**⭐ Se este projeto foi útil para você, deixe uma estrela no repositório!**

---

**Última atualização:** Novembro 2025 
**Versão:** 1.0