---
id: diagrama_de_casos de uso
title: Diagrama de Casos de Uso
---

## Casos de Uso

### Descrição:

-  Gestao de Contas
	- Cadastro (vinculado ao e-mail institucional)
    - Login (Autenticação)
    - Alteração de Senha
    - Recuperação de Senha
    - Visualização de dados cadastrais

- Perfis de Alunos e Monitores
	- Edição de perfil (cursos de interesse, matérias lecionadas, horários)
	- Pesquisa por Monitores (por matéria, nome ou disponibilidade)
	- Visualização de perfil (informações, avaliações)

- Agendamento de Monitorias	 	
	- Solicitação de agendamento por parte do Aluno
    - Aceite/Recusa de agendamento pelo Monitor
    - Cancelamento de monitoria
    - Visualização de agenda (monitorias passadas e futuras)

- Fórum de Dúvidas (por Matéria)
    - Criação de postagem (dúvida)
    - Resposta a uma dúvida (pelo Monitor ou outros Alunos)
    - Interação (marcar como útil)
    - Visualização de dúvidas por matéria

- Material de Apoio
    - Upload de arquivos pelo Monitor (listas de exercícios, resumos)
    - Download de arquivos pelos Alunos
    - Organização por matéria

- Avaliações e Feedback
	- Aluno avalia a monitoria após a sessão
	- Sistema compila a nota média do Monitor

### Criação de uma conta no sistema

* Atores:

	- Aluno/Monitor (Usuário)
	- Sistema

- Pré-Condições:
	- O usuário deve possuir um e-mail institucional válido do Ibmec (ex: @ibmec.edu.br).

* Fluxo Básico:
    1. Usuário acessa a página de cadastro e informa seu nome completo, e-mail institucional e senha.
    2. Sistema valida se o e-mail pertence ao domínio do Ibmec e se os dados do formulário são válidos.
	3. Sistema criptografa a senha do Usuário.
	4. Sistema persiste os dados do Usuário no banco de dados.
	5. Sistema gera um link de verificação com prazo de expiração.
	6. Sistema envia um e-mail de verificação para o e-mail institucional informado.
	7. Usuário clica no link de verificação antes que ele expire.
	8. Sistema ativa a conta do Usuário e exibe uma mensagem de sucesso.
	9. Sistema redireciona o Usuário para a página de Login.

- Fluxos Alternativos:
	- 2a. E-mail do Usuário não pertence ao domínio @ibmec.edu.br.
		- 2a1. Sistema exibe a mensagem: "Cadastro permitido apenas com e-mail institucional do Ibmec".
	- 2b. Senha do Usuário não cumpre os requisitos de segurança.
		- 2b1. Sistema exibe os requisitos de senha e solicita uma nova tentativa.
	- 7a. O link de verificação de e-mail está expirado.
		- 7a1. Sistema informa que o link expirou e oferece a opção de reenviar um novo e-mail de verificação.

### Entrada do usuário no sistema

- Atores:
	- Aluno/Monitor (Usuário)
	- Sistema

- Pré-Condições:
	- Usuário deve possuir uma conta ativa e verificada na plataforma.

- Fluxo Básico:
    - 1. Usuário informa seu e-mail institucional e senha na página de login.
	- 2. Sistema autentica as credenciais do Usuário.
	- 3. Sistema redireciona o Usuário para o seu Dashboard pessoal.

- Fluxos Alternativos:
	- 2a. E-mail ou senha inválidos.
		- 2a1. Sistema exibe a mensagem: "E-mail ou senha incorretos."
	- 3a. Primeiro acesso do Usuário após o cadastro.
		- 3a1. Sistema redireciona o Usuário para a página de edição de perfil, incentivando-o a completar suas informações (ex: selecionar matérias de interesse para o aluno, ou matérias que leciona e horários para o monitor).
