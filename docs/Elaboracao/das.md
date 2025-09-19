---
id: documento_de_arquitetura
title: Documento de Arquitetura
---

## Requisitos

# Introdução

## Proposta

<p align="justify"> O sistema tem como proposta **facilitar e modernizar a gestão das monitorias acadêmicas** dentro da instituição de ensino. Ele permitirá que estudantes, monitores e professores interajam de forma organizada, centralizando informações e automatizando processos que hoje são manuais ou dispersos. </p>
</p>

## Escopo

<p align = "justify">
O sistema tem o objetivo fornecer uma plataforma digital que **organize e gerencie as atividades de monitoria acadêmica**, permitindo o cadastro de alunos, monitores e disciplinas, além de facilitar o **agendamento de atendimentos, o acompanhamento de presença e a comunicação entre os envolvidos**. Com isso, busca-se **aumentar a eficiência, a transparência e a acessibilidade** do programa de monitorias dentro da instituição de ensino.
</p>

## Visão Geral

<p align = "justify">
O sistema será desenvolvido em **Django (Python)**. O banco de dados relacional, como PostgreSQL ou MySQL, será utilizado para persistência das informações. O sistema será acessível via navegador, com suporte para dispositivos móveis e desktops. Neste documento serão abordadas as seguintes visões da aplicação TCM:
</p>

- Caso de Uso;
- Lógica;
- Implantação;
- Implementação;
- Dados;

# Especificação de Requisitos – Sistema de Monitoria Acadêmica

## 1. Introdução

Este documento descreve os requisitos do sistema de gerenciamento de monitorias acadêmicas. O objetivo é facilitar a interação entre alunos e monitores, permitindo agendamento de horários, acompanhamento de atividades e gestão das disciplinas atendidas.

---

## 2. Visão Geral do Sistema

- O sistema permitirá que estudantes consultem monitorias disponíveis, reservem horários com monitores e recebam notificações sobre agendamentos.  
- Monitores poderão gerenciar suas disciplinas, disponibilizar horários e acompanhar reservas.  
- Administradores terão acesso para cadastrar disciplinas, gerenciar usuários e monitorias.  

---

## 3. Requisitos Funcionais

- **RF01 – Cadastro e Autenticação de Usuário**  
  O sistema deve permitir cadastro e login de alunos, monitores e administradores.  

- **RF02 – Gestão de Disciplinas**  
  O sistema deve permitir cadastrar, editar e excluir disciplinas oferecidas.  

- **RF03 – Perfil de Monitor**  
  O sistema deve permitir que monitores associem disciplinas que atendem e disponibilizem horários de atendimento.  

- **RF04 – Reserva de Monitoria**  
  O sistema deve permitir que alunos reservem horários de monitoria disponíveis com base na disciplina e no monitor escolhido.  

- **RF05 – Confirmação e Notificação**  
  O sistema deve enviar notificações (por e-mail ou no painel do usuário) confirmando reservas ou alterações.  

- **RF06 – Histórico de Atendimentos**  
  O sistema deve registrar e disponibilizar o histórico de monitorias de cada aluno e monitor.  

- **RF07 – Gestão de Usuários (Admin)**  
  O administrador deve poder cadastrar e gerenciar usuários (alunos, monitores, administradores).  

- **RF08 – Relatórios**  
  O sistema deve gerar relatórios de utilização de monitorias (quantidade de reservas por disciplina, por monitor, etc.).  

---

## 4. Requisitos Não Funcionais

- **RNF01 – Segurança**  
  Senhas devem ser armazenadas de forma criptografada.  

- **RNF02 – Disponibilidade**  
  O sistema deve estar disponível 99% do tempo, exceto em manutenções programadas.  

- **RNF03 – Usabilidade**  
  A interface deve ser simples, intuitiva e acessível tanto em desktop quanto em dispositivos móveis.  

- **RNF04 – Performance**  
  O carregamento das páginas principais (login, lista de disciplinas, reservas) deve ocorrer em até 3 segundos em conexões comuns.  

---

## 5. Regras de Negócio

- **RN01 – Reserva Limitada**  
  Um aluno só pode reservar um número limitado de sessões de monitoria por semana (definido pelo administrador).  

- **RN02 – Disponibilidade do Monitor**  
  Reservas só podem ser feitas em horários previamente disponibilizados pelo monitor.  

- **RN03 – Cancelamento de Reservas**  
  Alunos devem cancelar a reserva com pelo menos 24h de antecedência, caso contrário a ausência será registrada.  

- **RN04 – Relacionamento Monitor–Disciplina**  
  Um monitor pode atender mais de uma disciplina, mas cada disciplina pode ter vários monitores.  

---

## 6. Interfaces Externas

- Integração com sistema de autenticação do Django (Django Auth).  
- Possível integração com e-mail para envio de confirmações.  

---

## 7. Restrições

- O sistema deve ser implementado em Django (back-end).  
- O front-end deve seguir boas práticas de responsividade (HTML, CSS e JavaScript).  
- Deve estar em conformidade com a LGPD para proteção dos dados pessoais dos usuários.  

---

## 8. Critérios de Aceitação

- Usuário consegue se cadastrar, fazer login e reservar uma sessão de monitoria.  
- Monitor consegue cadastrar horários disponíveis.  
- Administrador consegue cadastrar disciplinas e associar monitores.  
- Sistema gera relatório de reservas por disciplina/monitor.  

---

## 9. Glossário

- **Aluno**: Usuário que busca auxílio em uma disciplina.  
- **Monitor**: Estudante selecionado para atender alunos em determinada disciplina.  
- **Administrador**: Responsável pela gestão do sistema, usuários e disciplinas.  
- **Reserva de Monitoria**: Agendamento de horário entre aluno e monitor.  


# Visão de Caso de Uso

<p align = "justify">
O primeiro caso de uso descreve a ação...
</p>

![Caso de uso 1](../assets/Casos_de_Uso/Exemplocaso_de_uso_1.png)

![Caso de uso 2](../assets/Casos_de_Uso/Exemplocaso_de_uso_1.png)

# Visão Lógica

# Visão de Implantação

# Visão de Implementação

## Visão Geral

![Diagrama de Componentes](../assets/Casos_de_Uso/Exemplocaso_de_uso_1.png)

# Visão de Dados

## Modelo Entidade Relacionamento (MER)

#### Entidades e Relacionamentos:

## Diagrama Entidade Relacionamento (DER)

# Tamanho e Desempenho

# Qualidade

</p>




