#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de Testes de Autenticação por Token
Sistema Casa (Monitoria)
"""

import requests
import json
from datetime import datetime

BASE_URL = "http://127.0.0.1:8000"
TEST_USER = "apitestuser"
TEST_PASSWORD = "apipass123"

passed = 0
failed = 0
valid_token = None
old_token = None

def print_header():
    print("\n" + "="*70)
    print("  TESTES DE AUTENTICAÇÃO POR TOKEN - SISTEMA CASA (MONITORIA)")
    print(f"  Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("="*70 + "\n")

def print_section(title):
    print("\n" + "-"*70)
    print(f"  {title}")
    print("-"*70)

def test_result(passed_test, message):
    global passed, failed
    if passed_test:
        print(f"✅ PASSOU: {message}")
        passed += 1
    else:
        print(f"❌ FALHOU: {message}")
        failed += 1

# ========================= TESTE 1 =========================
print_header()
print_section("TESTE 1: Login com Credenciais Válidas")

try:
    response = requests.post(
        f"{BASE_URL}/api-token-auth-rotate/",
        data={"username": TEST_USER, "password": TEST_PASSWORD}
    )
    
    if response.status_code == 200:
        data = response.json()
        if "token" in data and len(data["token"]) == 40:
            print(f"Token gerado: {data['token']}")
            valid_token = data["token"]
            test_result(True, "Token gerado com sucesso - 40 caracteres")
        else:
            test_result(False, "Token com tamanho incorreto")
    else:
        test_result(False, f"Erro HTTP {response.status_code}")
except Exception as e:
    test_result(False, f"Erro: {str(e)}")

# ========================= TESTE 2 =========================
print_section("TESTE 2: Login com Credenciais Inválidas")

try:
    response = requests.post(
        f"{BASE_URL}/api-token-auth-rotate/",
        data={"username": TEST_USER, "password": "senhaErrada"}
    )
    
    if response.status_code == 400:
        data = response.json()
        print(f"Mensagem: {data.get('detail', 'Sem detalhes')}")
        test_result(True, "Retornou erro 400 - Credenciais inválidas")
    else:
        test_result(False, f"Código de erro inesperado: {response.status_code}")
except Exception as e:
    test_result(False, f"Erro: {str(e)}")

# ========================= TESTE 3 =========================
print_section("TESTE 3: Falta de Credenciais")

try:
    response = requests.post(
        f"{BASE_URL}/api-token-auth-rotate/",
        data={}
    )
    
    if response.status_code == 400:
        test_result(True, "Retornou erro 400 - Mensagem de erro apropriada")
    else:
        test_result(False, f"Código de erro inesperado: {response.status_code}")
except Exception as e:
    test_result(False, f"Erro: {str(e)}")

# ========================= TESTE 4 =========================
print_section("TESTE 4: Requisição SEM Token (Deve Falhar)")

try:
    response = requests.get(f"{BASE_URL}/api/usuarios/")
    
    if response.status_code == 401:
        test_result(True, "Retornou erro 401 - Proteção ativa")
    else:
        test_result(False, f"Código de erro inesperado: {response.status_code}")
except Exception as e:
    test_result(False, f"Erro: {str(e)}")

# ========================= TESTE 5 =========================
print_section("TESTE 5: Requisição COM Token Válido")

if valid_token:
    try:
        response = requests.get(
            f"{BASE_URL}/api/usuarios/",
            headers={"Authorization": f"Token {valid_token}"}
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"Usuários encontrados: {len(data)}")
            test_result(True, "Requisição autenticada bem-sucedida")
        else:
            test_result(False, f"Código de erro: {response.status_code}")
    except Exception as e:
        test_result(False, f"Erro: {str(e)}")
else:
    test_result(False, "Token válido não disponível")

# ========================= TESTE 6 =========================
print_section("TESTE 6: Token Inválido (Deve Falhar)")

try:
    response = requests.get(
        f"{BASE_URL}/api/usuarios/",
        headers={"Authorization": "Token tokenInvalido123xyz"}
    )
    
    if response.status_code == 401:
        test_result(True, "Token inválido rejeitado - Erro 401")
    else:
        test_result(False, f"Código de erro inesperado: {response.status_code}")
except Exception as e:
    test_result(False, f"Erro: {str(e)}")

# ========================= TESTE 7 =========================
print_section("TESTE 7: Rotacao de Tokens (Novo Login = Novo Token)")

try:
    response1 = requests.post(
        f"{BASE_URL}/api-token-auth-rotate/",
        data={"username": TEST_USER, "password": TEST_PASSWORD}
    )
    token1 = response1.json()["token"]
    
    response2 = requests.post(
        f"{BASE_URL}/api-token-auth-rotate/",
        data={"username": TEST_USER, "password": TEST_PASSWORD}
    )
    token2 = response2.json()["token"]
    
    if token1 != token2:
        print(f"Token 1: {token1[:20]}...")
        print(f"Token 2: {token2[:20]}...")
        test_result(True, "Tokens sao diferentes - Rotacao funcionando")
        old_token = token1
    else:
        test_result(False, "Tokens sao iguais - Rotacao nao funcionou")
except Exception as e:
    test_result(False, f"Erro: {str(e)}")

# ========================= TESTE 8 =========================
print_section("TESTE 8: Token Antigo Apos Rotacao (Deve ser Invalido)")

if old_token:
    try:
        response = requests.get(
            f"{BASE_URL}/api/usuarios/",
            headers={"Authorization": f"Token {old_token}"}
        )
        
        if response.status_code == 401:
            test_result(True, "Token antigo foi invalidado apos rotacao")
        else:
            test_result(False, f"Token antigo deveria ter sido invalidado")
    except Exception as e:
        test_result(False, f"Erro: {str(e)}")
else:
    test_result(False, "Token antigo nao disponivel")

# ========================= RESUMO =========================
print("\n" + "="*70)
print("  RESUMO DOS TESTES")
print("="*70)
print(f"  Testes PASSOU: {passed}")
print(f"  Testes FALHOU: {failed}")
print(f"  Total: {passed + failed}")

if failed == 0:
    print("\n  🎉 TODOS OS TESTES PASSARAM! AUTENTICACAO FUNCIONAL! 🎉")
else:
    print(f"\n  ⚠️  {failed} teste(s) falharam. Verifique acima.")

print("="*70)
print(f"Relatorio gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
