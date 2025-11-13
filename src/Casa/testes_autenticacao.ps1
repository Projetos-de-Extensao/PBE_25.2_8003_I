#!/usr/bin/env pwsh

Write-Host "╔════════════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  TESTES DE AUTENTICAÇÃO POR TOKEN - SISTEMA CASA (MONITORIA)      ║" -ForegroundColor Cyan
Write-Host "║  Data: $(Get-Date -Format 'dd/MM/yyyy HH:mm:ss')                      ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

$baseUrl = "http://127.0.0.1:8000"
$testUser = "apitestuser"
$testPassword = "apipass123"
$passCount = 0
$failCount = 0

function Test-Section {
    param([string]$title)
    Write-Host ""
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Yellow
    Write-Host "  $title" -ForegroundColor Yellow
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Yellow
}

function Test-Result {
    param([bool]$passed, [string]$message)
    if ($passed) {
        Write-Host "✅ PASSOU: $message" -ForegroundColor Green
        $script:passCount++
    } else {
        Write-Host "❌ FALHOU: $message" -ForegroundColor Red
        $script:failCount++
    }
}

# ========================= TESTE 1 =========================
Test-Section "TESTE 1: Login com Credenciais Válidas"
try {
    $response = Invoke-RestMethod -Method Post -Uri "$baseUrl/api-token-auth-rotate/" `
        -Body @{username=$testUser; password=$testPassword}
    
    if ($response.token -and $response.token.Length -eq 40) {
        Write-Host "Token gerado: $($response.token)" -ForegroundColor Cyan
        $script:validToken = $response.token
        Test-Result $true "Token gerado com sucesso - 40 caracteres"
    } else {
        Test-Result $false "Token com tamanho incorreto"
    }
} catch {
    Test-Result $false "Erro ao fazer login: $($_.Exception.Response.StatusCode)"
}

# ========================= TESTE 2 =========================
Test-Section "TESTE 2: Login com Credenciais Inválidas"
try {
    $response = Invoke-RestMethod -Method Post -Uri "$baseUrl/api-token-auth-rotate/" `
        -Body @{username=$testUser; password="senhaErrada"} -ErrorAction Stop
    Test-Result $false "Deveria ter retornado erro 400"
} catch {
    if ($_.Exception.Response.StatusCode -eq 400) {
        Test-Result $true "Retornou erro 400 (Bad Request) - Credenciais inválidas"
    } else {
        Test-Result $false "Código de erro inesperado: $($_.Exception.Response.StatusCode)"
    }
}

# ========================= TESTE 3 =========================
Test-Section "TESTE 3: Falta de Credenciais"
try {
    $response = Invoke-RestMethod -Method Post -Uri "$baseUrl/api-token-auth-rotate/" `
        -Body @{} -ErrorAction Stop
    Test-Result $false "Deveria ter retornado erro 400"
} catch {
    if ($_.Exception.Response.StatusCode -eq 400) {
        Test-Result $true "Retornou erro 400 - Mensagem de erro apropriada"
    } else {
        Test-Result $false "Código de erro inesperado: $($_.Exception.Response.StatusCode)"
    }
}

# ========================= TESTE 4 =========================
Test-Section "TESTE 4: Requisição SEM Token (Deve Falhar)"
try {
    $response = Invoke-RestMethod -Uri "$baseUrl/api/usuarios/" -ErrorAction Stop
    Test-Result $false "Deveria ter retornado erro 401"
} catch {
    if ($_.Exception.Response.StatusCode -eq 401) {
        Test-Result $true "Retornou erro 401 (Unauthorized) - Proteção ativa"
    } else {
        Test-Result $false "Código de erro inesperado: $($_.Exception.Response.StatusCode)"
    }
}

# ========================= TESTE 5 =========================
Test-Section "TESTE 5: Requisição COM Token Válido"
if ($script:validToken) {
    try {
        $response = Invoke-RestMethod -Uri "$baseUrl/api/usuarios/" `
            -Headers @{Authorization="Token $($script:validToken)"}
        
        if ($response -and $response.Count -gt 0) {
            Write-Host "Usuários encontrados: $($response.Count)" -ForegroundColor Cyan
            Test-Result $true "Requisição autenticada bem-sucedida"
        } else {
            Test-Result $false "Resposta vazia ou inválida"
        }
    } catch {
        Test-Result $false "Erro ao fazer requisição autenticada: $($_.Exception.Response.StatusCode)"
    }
} else {
    Test-Result $false "Token válido não disponível de teste anterior"
}

# ========================= TESTE 6 =========================
Test-Section "TESTE 6: Token Inválido (Deve Falhar)"
try {
    $response = Invoke-RestMethod -Uri "$baseUrl/api/usuarios/" `
        -Headers @{Authorization="Token tokenInvalido123xyz"} -ErrorAction Stop
    Test-Result $false "Deveria ter retornado erro 401"
} catch {
    if ($_.Exception.Response.StatusCode -eq 401) {
        Test-Result $true "Token inválido rejeitado (401)"
    } else {
        Test-Result $false "Código de erro inesperado: $($_.Exception.Response.StatusCode)"
    }
}

# ========================= TESTE 7 =========================
Test-Section "TESTE 7: Rotação de Tokens (Novo Login = Novo Token)"
try {
    $response1 = Invoke-RestMethod -Method Post -Uri "$baseUrl/api-token-auth-rotate/" `
        -Body @{username=$testUser; password=$testPassword}
    $token1 = $response1.token
    
    Start-Sleep -Milliseconds 100
    
    $response2 = Invoke-RestMethod -Method Post -Uri "$baseUrl/api-token-auth-rotate/" `
        -Body @{username=$testUser; password=$testPassword}
    $token2 = $response2.token
    
    if ($token1 -ne $token2) {
        Write-Host "Token 1: $($token1.Substring(0, 20))..." -ForegroundColor Cyan
        Write-Host "Token 2: $($token2.Substring(0, 20))..." -ForegroundColor Cyan
        Test-Result $true "Tokens são diferentes (rotação funcionando)"
        $script:oldToken = $token1
    } else {
        Test-Result $false "Tokens são iguais (rotação não funcionou)"
    }
} catch {
    Test-Result $false "Erro ao testar rotação: $($_.Exception.Response.StatusCode)"
}

# ========================= TESTE 8 =========================
Test-Section "TESTE 8: Token Antigo Após Rotação (Deve ser Inválido)"
if ($script:oldToken) {
    try {
        $response = Invoke-RestMethod -Uri "$baseUrl/api/usuarios/" `
            -Headers @{Authorization="Token $($script:oldToken)"} -ErrorAction Stop
        Test-Result $false "Token antigo deveria ter sido invalidado"
    } catch {
        if ($_.Exception.Response.StatusCode -eq 401) {
            Test-Result $true "Token antigo foi invalidado após rotação"
        } else {
            Test-Result $false "Código de erro inesperado: $($_.Exception.Response.StatusCode)"
        }
    }
} else {
    Test-Result $false "Token antigo não disponível"
}

# ========================= RESUMO =========================
Write-Host ""
Write-Host "╔════════════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  RESUMO DOS TESTES                                                 ║" -ForegroundColor Cyan
Write-Host "╠════════════════════════════════════════════════════════════════════╣" -ForegroundColor Cyan
Write-Host "║  ✅ Testes PASSOU: $($script:passCount)                                              ║" -ForegroundColor Green
Write-Host "║  ❌ Testes FALHOU: $($script:failCount)                                              ║" -ForegroundColor Red
Write-Host "║  Total: $($script:passCount + $script:failCount)                                                     ║" -ForegroundColor Cyan

if ($script:failCount -eq 0) {
    Write-Host "║                                                                    ║" -ForegroundColor Cyan
    Write-Host "║  🎉 TODOS OS TESTES PASSARAM! AUTENTICAÇÃO FUNCIONAL! 🎉         ║" -ForegroundColor Green
    Write-Host "╚════════════════════════════════════════════════════════════════════╝" -ForegroundColor Green
} else {
    Write-Host "║                                                                    ║" -ForegroundColor Cyan
    Write-Host "║  ⚠️  Alguns testes falharam. Verifique a saída acima.             ║" -ForegroundColor Yellow
    Write-Host "╚════════════════════════════════════════════════════════════════════╝" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Relatório gerado em: $(Get-Date -Format 'dd/MM/yyyy HH:mm:ss')" -ForegroundColor Gray
