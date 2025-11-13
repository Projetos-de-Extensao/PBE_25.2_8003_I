# Sistema de Autenticação por Token - Casa (Monitoria)

## 📋 Resumo

O sistema de autenticação da API utiliza **Token Authentication** do Django REST Framework. Cada usuário recebe um token único ao fazer login, que deve ser incluído em todas as requisições para acessar os endpoints protegidos.

**Características principais:**
- ✅ Autenticação por token (40 caracteres hexadecimais)
- ✅ Rotação de tokens a cada login (invalida tokens antigos)
- ✅ Mensagens de erro em português
- ✅ Proteção de endpoints (requer autenticação)
- ✅ Permissão padrão: `IsAuthenticated`

---

## 🚀 Como Funciona

### 1️⃣ **Fluxo de Autenticação**

```
┌─────────────────────────────────────────────────┐
│ 1. Cliente envia username + password             │
│    POST /api-token-auth-rotate/                 │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│ 2. Servidor valida credenciais                  │
│    - Se inválidas: erro 400                     │
│    - Se válidas: continua                       │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│ 3. Servidor apaga tokens antigos do usuário     │
│    (rotação de token)                           │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│ 4. Servidor cria novo token                     │
│    e retorna: {"token": "abc123..."}            │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│ 5. Cliente armazena o token                     │
│    e o usa em próximas requisições              │
└─────────────────────────────────────────────────┘
```

---

## 🔐 Endpoints de Autenticação

### **Obter Token (Login)**

**URL:** `POST http://127.0.0.1:8000/api-token-auth-rotate/`

**Método:** `POST`

**Parâmetros (form-encoded):**
```
username=seu_usuario
password=sua_senha
```

**Resposta (sucesso - 200):**
```json
{
  "token": "a3808d3165daac2e72f4382fa2a744d3608a763f"
}
```

**Resposta (erro - 400):**
```json
{
  "detail": "Credenciais inválidas."
}
```

ou

```json
{
  "detail": "Nome de usuário e senha são obrigatórios."
}
```

---

## 📡 Como Usar o Token

Após obter o token, inclua-o em **todas** as requisições protegidas:

### **Header Obrigatório:**
```
Authorization: Token abc123def456...
```

### **Exemplo de Requisição Autenticada:**

**Listar Usuários:**
```
GET http://127.0.0.1:8000/api/usuarios/
Header: Authorization: Token a3808d3165daac2e72f4382fa2a744d3608a763f
```

**Resposta (200 OK):**
```json
[
  {
    "id": 1,
    "username": "coord_mat",
    "email": "coordenador@ibmec.br",
    "first_name": "Maria",
    "last_name": "Coordenação",
    "tipo": "professor",
    "is_active": true,
    "is_staff": false
  },
  ...
]
```

---

## 🧪 Testando a Autenticação

### **Teste 1: Login com Credenciais Válidas**

```powershell
$response = Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/api-token-auth-rotate/ `
  -Body @{username='apitestuser'; password='apipass123'}

Write-Host "Token: $($response.token)"
```

**Resultado esperado:**
```
Token: a3808d3165daac2e72f4382fa2a744d3608a763f
```

---

### **Teste 2: Login com Credenciais Inválidas**

```powershell
try {
  $response = Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/api-token-auth-rotate/ `
    -Body @{username='apitestuser'; password='senhaErrada'}
} catch {
  Write-Host "Erro: $($_.Exception.Response.StatusCode)"
  Write-Host "Mensagem: Credenciais inválidas."
}
```

**Resultado esperado:**
```
Erro: BadRequest
Mensagem: Credenciais inválidas.
```

---

### **Teste 3: Requisição Autenticada (com Token)**

```powershell
$token = "a3808d3165daac2e72f4382fa2a744d3608a763f"
$response = Invoke-RestMethod -Uri http://127.0.0.1:8000/api/usuarios/ `
  -Headers @{Authorization="Token $token"}

Write-Host "Usuários listados: $($response.Count)"
```

**Resultado esperado:**
```
Usuários listados: 7
```

---

### **Teste 4: Requisição SEM Token (Deve Falhar)**

```powershell
try {
  $response = Invoke-RestMethod -Uri http://127.0.0.1:8000/api/usuarios/
} catch {
  Write-Host "Erro: $($_.Exception.Response.StatusCode)"
  Write-Host "Motivo: Não autenticado"
}
```

**Resultado esperado:**
```
Erro: Unauthorized
Motivo: Não autenticado
```

---

### **Teste 5: Token Inválido (Deve Falhar)**

```powershell
try {
  $response = Invoke-RestMethod -Uri http://127.0.0.1:8000/api/usuarios/ `
    -Headers @{Authorization="Token tokenInvalido123"}
} catch {
  Write-Host "Erro: $($_.Exception.Response.StatusCode)"
  Write-Host "Motivo: Token rejeitado"
}
```

**Resultado esperado:**
```
Erro: Unauthorized
Motivo: Token rejeitado
```

---

### **Teste 6: Rotação de Tokens (Novo Login = Novo Token)**

```powershell
# Primeiro login
$response1 = Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/api-token-auth-rotate/ `
  -Body @{username='apitestuser'; password='apipass123'}
$token1 = $response1.token

# Segundo login (mesmo usuário)
$response2 = Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/api-token-auth-rotate/ `
  -Body @{username='apitestuser'; password='apipass123'}
$token2 = $response2.token

Write-Host "Token 1: $token1"
Write-Host "Token 2: $token2"
Write-Host "São diferentes? $($token1 -ne $token2)"
```

**Resultado esperado:**
```
Token 1: a3808d3165daac2e72f4382fa2a744d3608a763f
Token 2: 6869216f57c749f99ae6...
São diferentes? True
```

**Teste com token antigo:**
```powershell
try {
  $response = Invoke-RestMethod -Uri http://127.0.0.1:8000/api/usuarios/ `
    -Headers @{Authorization="Token a3808d3165daac2e72f4382fa2a744d3608a763f"}
} catch {
  Write-Host "✅ Token antigo foi invalidado!"
  Write-Host "Erro: $($_.Exception.Response.StatusCode)"
}
```

**Resultado esperado:**
```
✅ Token antigo foi invalidado!
Erro: Unauthorized
```

---

## 📁 Arquivos Modificados

### **`monitoria/settings.py`**
- Adicionado `'rest_framework.authtoken'` em `INSTALLED_APPS`
- Configurado `REST_FRAMEWORK` com:
  - `TokenAuthentication` como autenticação padrão
  - `IsAuthenticated` como permissão padrão
- Idioma mudado para `pt-br` (português brasileiro)

### **`monitoria/views.py`**
- Criada classe `ObtainAuthTokenRotate(APIView)`:
  - Recebe `username` e `password`
  - Valida credenciais
  - Apaga tokens antigos (rotação)
  - Cria novo token
  - Retorna token em JSON

### **`monitoria/urls.py`**
- Adicionada rota: `path('api-token-auth-rotate/', ObtainAuthTokenRotate.as_view())`

### **Banco de Dados**
- Executadas migrações do `authtoken`:
  - Criada tabela `authtoken_token` para armazenar tokens

---

## 🔑 Usuários Padrão para Teste

| Username | Senha | Tipo |
|----------|-------|------|
| `apitestuser` | `apipass123` | Teste |
| `coord_mat` | **(solicitar ao admin)** | Professor |

---

## ⚠️ Mensagens de Erro (em Português)

| Erro | HTTP | Mensagem |
|------|------|----------|
| Credenciais inválidas | 400 | "Credenciais inválidas." |
| Falta de dados | 400 | "Nome de usuário e senha são obrigatórios." |
| Sem token | 401 | "Não foi fornecida informação de autenticação." |
| Token inválido | 401 | "Token inválido." |

---

## 🎯 Segurança

✅ **Implementado:**
- Token por usuário (40 caracteres hexadecimais)
- Rotação de tokens a cada login
- Invalidação de tokens antigos
- Permissão `IsAuthenticated` padrão
- Proteção de endpoints
- CSRF middleware ativo

⚠️ **Recomendações para Produção:**
- Usar HTTPS (não HTTP)
- Gerar nova `SECRET_KEY` segura
- Desabilitar `DEBUG = False`
- Configurar `ALLOWED_HOSTS`
- Usar token com expiração (adicionar JWT)
- Implementar rate limiting

---

## 📞 Suporte

**Para verificar o status do servidor:**
```powershell
python manage.py check
```

**Para rodar o servidor:**
```powershell
cd src/Casa
python manage.py runserver
```

**Para acessar o admin:**
```
URL: http://127.0.0.1:8000/admin/
```

---

## ✅ Checklist de Funcionalidades

- ✅ Endpoint de login (`/api-token-auth-rotate/`)
- ✅ Geração de token
- ✅ Rotação de tokens
- ✅ Validação de credenciais
- ✅ Proteção de endpoints
- ✅ Mensagens em português
- ✅ Tratamento de erros
- ✅ Testes bem-sucedidos

---

**Data:** 12 de Novembro de 2025  
**Status:** ✅ FUNCIONAL E TESTADO  
**Ambiente:** Desenvolvimento (localhost:8000)
