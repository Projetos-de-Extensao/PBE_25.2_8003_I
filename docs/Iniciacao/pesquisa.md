---
id: pesquisa
title: Pesquisa
---

# Pesquisa  sobre o Sistema de Monitoria da Ibmec.

---

# Apresentação do Projeto

A presente pesquisa documenta a concepção e a estruturação do projeto de backend para um Sistema de Monitoria próprio. A iniciativa visa fortalecer o suporte pedagógico na instituição ao formalizar e otimizar os processos de monitoria através de uma plataforma digital robusta, segura e escalável, desenvolvida com o framework **Django**.

O sistema foi projetado para atender às necessidades dos três principais perfis de usuário — alunos, monitores e professores —, facilitando atividades cruciais como agendamentos, compartilhamento de materiais e geração de relatórios. Nas páginas seguintes, exploraremos em detalhe cada uma das funcionalidades que nortearão o desenvolvimento do projeto.

Além disso, o projeto estará alinhado juntamente as outras materias ministradas no semestre por outros professores. Como, Programação Orientada a Objetos, Projetos e Padrões de Software e Engenharia de Dados.

---

# Principais Funcionalidades do Sistema de Monitoria

Um sistema de monitoria eficaz deve atender às necessidades de três tipos de usuários: Alunos, Monitores e Professores/Coordenadores. As funcionalidades podem ser divididas da seguinte forma:


## 1. Gestão de Usuários e Autenticação

- **Cadastro e Login:** Perfis distintos para alunos, monitores e professores. A autenticação pode ser feita via e-mail e senha ou integrada ao sistema acadêmico da instituição.
- **Gerenciamento de Perfis:** Usuários podem visualizar e editar suas informações básicas.
- **Controle de Permissões:** Cada tipo de usuário terá acesso a funcionalidades específicas. O sistema de permissões do Django é ideal para isso.

---

## 2. Agendamento e Gerenciamento de Atendimentos

- **Disponibilidade de Monitores:** Monitores devem poder cadastrar seus horários disponíveis para atendimento.
- **Agendamento de Monitorias:** Alunos podem visualizar os horários disponíveis e agendar um horário com o monitor da disciplina desejada.
- **Cancelamento e Remarcação:** Tanto alunos quanto monitores devem poder cancelar ou solicitar a remarcação de um atendimento, com regras de antecedência.
- **Notificações:** Envio de e-mails ou notificações no sistema para lembrar sobre agendamentos, cancelamentos e outras atualizações importantes.

---

## 3. Gestão de Disciplinas e Conteúdo

- **Cadastro de Disciplinas:** Professores ou coordenadores podem cadastrar as disciplinas que terão monitoria.
- **Associação de Monitores:** Vincular monitores às suas respectivas disciplinas.
- **Repositório de Materiais:** Monitores e professores podem fazer upload de materiais de apoio (listas de exercícios, resumos, slides etc.), organizados por disciplina.
- **Fórum de Dúvidas:** Um espaço para que os alunos postem dúvidas, que podem ser respondidas pelos monitores ou outros alunos, criando uma base de conhecimento.

---

## 4. Comunicação

- **Chat em Tempo Real (opcional, mas recomendado):** Um chat para comunicação rápida entre aluno e monitor durante o horário de atendimento.
- **Sistema de Mensagens Internas:** Para comunicação assíncrona entre os usuários.


---

## 5. Relatórios e Acompanhamento

- **Registro de Atendimentos:** O sistema deve registrar todos os atendimentos realizados, incluindo data, hora, aluno e monitor.
- **Feedback e Avaliação:** Alunos podem avaliar o atendimento do monitor ao final de cada sessão.
- **Dashboards para Professores/Coordenadores:** Visualização de dados como número de atendimentos por disciplina, principais dúvidas, avaliações dos monitores etc. Isso ajuda a identificar dificuldades dos alunos e a eficácia do programa de monitoria.

---

# Comparação Sistema de Monitoria - Sistema de Agendamento (Clínicas/Salas)


| Critério                | Sistema de Monitoria Acadêmica                                                                 | Sistema de Agendamento (Clínicas/Salas)                                  |
|-------------------------|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| Objetivo Principal      | Fortalecer o aprendizado e o suporte pedagógico.                                              | Otimizar a agenda de um profissional/recurso e gerenciar o fluxo de clientes/pacientes. |
| Perfis de Usuário       | Aluno (solicitante), Monitor (provedor), Professor (gestor).                                  | Paciente/Cliente (solicitante), Profissional (provedor), Recepcionista (gestor).        |
| "Recurso" Agendado      | O tempo e o conhecimento de um Monitor sobre uma disciplina específica.                       | O tempo de um Profissional de saúde/serviço e, opcionalmente, uma sala/equipamento.     |
| Entidades Associadas    | Disciplinas, Materiais de Apoio, Fóruns de Dúvidas, Avaliações de Desempenho.                 | Prontuários de Pacientes, Convênios, Procedimentos, Salas, Faturamento.                 |
| Natureza do Serviço     | Educacional e colaborativa. O sucesso é o aprendizado do aluno.                               | Prestação de serviço (muitas vezes comercial). O sucesso é a eficiência e a satisfação do cliente. |
| Funcionalidades Específicas | - Upload/Download de materiais<br>- Fórum de Dúvidas<br>- Relatórios de temas com mais dificuldade | - Gestão de prontuários/histórico<br>- Integração com convênios e faturamento<br>- Gestão de salas e equipamentos |
| Métricas de Sucesso     | - Nº de atendimentos<br>- Melhora nas notas dos alunos<br>- Feedback positivo sobre os monitores | - Taxa de ocupação da agenda<br>- Redução do "no-show" (faltas)<br>- Faturamento