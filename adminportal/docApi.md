# Documentação da API Django REST Framework

Esta documentação detalha como interagir com a API do seu projeto Django, incluindo a criação de tokens de autenticação e a utilização de todos os endpoints disponíveis.

## 1. Autenticação na API: Criação e Uso de Tokens

Sua API está configurada para exigir autenticação para a maioria dos endpoints (`IsAuthenticated`). A forma mais comum de autenticação para clientes de API (como frontends JavaScript, n8n, Postman, etc.) é via Token Authentication.

### 1.1. Criação de um Token de API no Painel de Administração

Para obter um token de API para um usuário, você pode criá-lo diretamente no painel de administração do Django:

1. Acesse o Painel de Administração: Navegue até `http://localhost:8000/admin/` (ou a URL do seu site, por exemplo, `https://7lxwl92c-8000.brs.devtunnels.ms/admin/`).
2. Faça Login: Utilize as credenciais de um usuário administrador (superusuário) do Django.
3. Navegue até Tokens: No painel de administração, localize a seção "AUTHTOKEN" e clique em "Tokens".
4. Adicionar Token: Clique em "Adicionar Token" (ou "Add Token").
5. Selecione o Usuário: Na página de criação do token, selecione o usuário para o qual você deseja gerar o token (por exemplo, seu usuário admin).
6. Salvar: Clique em "Salvar".
7. Copie a Chave do Token: Após salvar, você será redirecionado para a página de detalhes do token. A "Chave" (Key) é o seu token de API. Copie este valor.

### 1.2. Como Usar o Token em Requisições da API

Para usar o token em suas requisições, você deve incluí-lo no cabeçalho `Authorization` de cada requisição HTTP para endpoints protegidos.

**Formato do Cabeçalho:**

`Authorization: Token <sua_chave_do_token>`

**Exemplo com curl:**

```
curl -X GET \
  https://7lxwl92c-8000.brs.devtunnels.ms/api/planos/ \
  -H 'Authorization: Token sua_chave_do_token_aqui' \
  -H 'Accept: application/json'

```

## 2. Endpoints da API do Projeto

Todos os endpoints da API estão localizados sob o prefixo `/api/` (para viewsets e `api-auth/`) ou na raiz do projeto (para suas páginas HTML e o endpoint `/transcribe/`). A estrutura geral das URLs para os viewsets é `https://<seu_dominio_ou_ip>/api/<nome_do_recurso>/`.

Cada endpoint listado abaixo suporta operações CRUD (Create, Retrieve, Update, Delete) através de diferentes métodos HTTP, graças ao uso de `viewsets.ModelViewSet` e `rest_framework.routers.DefaultRouter`, **exceto o endpoint de Transcrição, que é customizado.**

**URL Base da API:** `https://<seu_dominio_ou_ip>/api/`

### **2.0. Transcrição de Áudio** (Endpoint Customizado)

Este endpoint é utilizado para submeter arquivos de áudio ou URLs de áudio para transcrição. Ele usa o MinIO para armazenar arquivos e a AssemblyAI para realizar a transcrição.

**URL Base:** `/transcribe/` (acessível diretamente na raiz do domínio, ex: `http://localhost:8000/transcribe/`)

| Método HTTP | URL Completa             | Propósito                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Headers Necessários                                                  | Corpo da Requisição (Exemplo)
