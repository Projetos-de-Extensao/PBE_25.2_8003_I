---
id: documento_de_visao
title: Documento de Visão
---
## Introdução

<p align = "justify">
O propósito deste documento é fornecer uma visão geral sobre o projeto que será desenvolvido na disciplina de Projeto Back-End. Este documento descreve de maneira resumida as principais funcionalidades, a usabilidade, o problema a ser abordado e os objetivos da equipe. O sistema proposto será uma aplicação web para gerenciamento de monitorias acadêmicas, construída utilizando o framework Django.
</p>

## Descrição do Problema 

<p align = "justify">
Atualmente, muitas instituições de ensino enfrentam dificuldades no gerenciamento de monitorias, seja pelo uso de processos manuais, como planilhas e formulários em papel, ou pela ausência de um sistema centralizado que facilite a comunicação entre alunos, monitores e professores. Esse cenário pode gerar desorganização, falta de controle de horários, dificuldades no acompanhamento do desempenho dos monitores e insatisfação dos alunos.
</p>

### Problema

Dificuldade em gerenciar e organizar as atividades de monitoria acadêmica, incluindo agendamentos, acompanhamento de alunos e controle de relatórios.


### Impactados

- **Alunos**: têm dificuldade em encontrar horários disponíveis de monitoria.  
- **Monitores**: precisam de uma forma prática de organizar atendimentos e registrar atividades.  
- **Professores/Coordenação**: necessitam de relatórios claros para acompanhar o desempenho da monitoria.  

### Consequência

- Perda de tempo com processos manuais.  
- Falta de dados centralizados sobre a utilização da monitoria.  
- Dificuldade em avaliar a eficiência do programa de monitoria.  

### Solução

Desenvolver uma aplicação web que centralize e organize as atividades de monitoria, permitindo o cadastro de usuários (alunos, monitores e professores), agendamento de atendimentos, controle de relatórios e geração de dados para acompanhamento da coordenação.

## Objetivos

<p align = "justify">
O objetivo da equipe de desenvolvimento é fornecer um sistema web responsivo e intuitivo que facilite a gestão das monitorias acadêmicas, proporcionando maior organização, eficiência e transparência no processo. A solução deverá beneficiar tanto os alunos, que terão acesso simplificado aos horários e vagas, quanto os monitores e professores, que terão recursos para organizar, acompanhar e avaliar a monitoria.
</p>

## Descrição do Usuário 

<p align="justify">
Os usuários do sistema serão divididos em três perfis principais:  
</p>

- **Aluno**: poderá visualizar as disciplinas com monitoria disponível, agendar atendimentos e avaliar o suporte recebido.  
- **Monitor**: poderá cadastrar horários de atendimento, confirmar presença dos alunos, registrar relatórios e acompanhar sua carga horária.  
- **Professor/Coordenação**: terá acesso a relatórios consolidados, poderá validar monitorias realizadas e acompanhar o desempenho do monitor.  



## Recursos do produto

### Conta
<p align="justify">
Usuários poderão realizar cadastro e login no sistema, com perfis diferenciados (aluno, monitor, professor/coordenação).
</p>

### Agendamento

<p align = "justify">
Os alunos poderão visualizar horários disponíveis e agendar atendimentos de forma prática e rápida.
</p>

### Monitoria

<p align = "justify">
O sistema permitirá o cadastro de monitorias vinculadas a disciplinas específicas, com horários e monitores responsáveis.
</p>

### Relatórios

<p align = "justify">
Os monitores poderão registrar relatórios de cada sessão de monitoria, permitindo acompanhamento detalhado das atividades.
</p>

## Gestão de Usuários

<p align = "justify">
Professores e coordenação poderão acompanhar o desempenho de monitores, validar registros e gerar relatórios gerais.
</p>


## Restrições

<p align="justify">
- O sistema será desenvolvido utilizando o framework Django.  
- A aplicação dependerá de conexão com a internet.  
- A autenticação de usuários será realizada apenas por cadastro interno (sem integração com sistemas externos na versão inicial).  
</p>

## Versionamento
| Data | Versão | Descrição | Autor(es) |
| -- | -- | -- | -- |
| DD/MM/YYYY | 1.0 | Criação do documento | XXX XXXX e ZZZ ZZZZ | 

