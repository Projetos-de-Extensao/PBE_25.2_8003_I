---
id: dt
title: Design Thinking
---

## **Design Thinking**

### **1. Capa**


Título do Projeto: Sistema de Monitoria Acadêmica 

Nome da Equipe: João Loss, Luis Cesar e Roberto Ramos 

Data: Agosto/2025 a Novembro/2025 

 

### 2. Introdução 

**Contexto do Projeto**: 
 Atualmente, muitas instituições de ensino realizam atividades de monitoria de forma manual, sem uma plataforma centralizada para organizar horários, agendamentos e relatórios. Isso gera problemas de comunicação entre monitores, professores e alunos, além de dificultar o acompanhamento dos atendimentos. 

**Objetivo**: 
 Desenvolver um sistema web em Django para gerenciar a monitoria acadêmica, permitindo: 

- Cadastro de disciplinas, monitores e horários de atendimento. 

- Agendamento online de monitoria por alunos. 

- Relatórios para professores e coordenação. 

**Público-Alvo**: 

- Alunos: que precisam de suporte em disciplinas. 

- Monitores: que oferecem atendimentos. 

- Professores: que supervisionam e avaliam a monitoria. 

- Administradores/Coordenação: que acompanham indicadores gerais. 

**Escopo**: 
 O sistema contempla cadastro de usuários, disciplinas, horários, agendamentos e relatórios básicos.  

 

### 3. Fases do Design Thinking 

#### 3.1. Empatia 

**Pesquisa**: 

- Observação dos métodos atuais (planilhas, grupos de WhatsApp, papel). 

Análise de sistemas semelhantes. 

Insights: 

- Alunos têm dificuldade em saber horários de monitoria atualizados. 

- Monitores precisam registrar atendimentos de forma simples. 

- Professores querem relatórios rápidos para avaliar impacto da monitoria. 

- A comunicação hoje é descentralizada (WhatsApp, e-mail, etc). 

#### 3.2. Definição 

**Problema Central**: 
 “Como podemos facilitar o agendamento, registro e acompanhamento das monitorias acadêmicas, de forma prática e acessível para alunos, monitores e professores? Além de obter resultados corretos sobre ela.” 

Pontos de Vista (POV): 

- Pessoa 1: Precisa de um sistema onde visualize facilmente horários e possa agendar monitorias sem burocracia. 

- Pessoa 2: Precisa de uma forma de registrar atendimentos e presenças sem perder tempo. 

- Pessoa 3: Precisa de relatórios confiáveis para avaliar a efetividade da monitoria. 

#### **3.3. Ideação**

 **Brainstorming**: Durante a sessão de brainstorm, a equipe levantou as seguintes ideias principais:

 - Criar uma plataforma exclusiva para alunos do Ibmec, com autenticação via e-mail institucional.

- Oferecer um canal centralizado de busca por monitores, evitando depender apenas de grupos informais como WhatsApp.

- Permitir que alunos se cadastrem como clientes (aprendizes) ou monitores (tutores), com fluxos de cadastro diferenciados.

- Implementar um sistema de verificação e aprovação de monitores, garantindo qualidade e credibilidade.

- Disponibilizar informações relevantes sobre os monitores, como foto, curso, semestre, CRA, matérias que domina e histórico acadêmico.

- Criar um sistema de reputação baseado em avaliações de alunos que já tiveram aulas.

- Possibilitar que o monitor defina preço, disponibilidade e metodologia de ensino.

- Disponibilizar um painel intuitivo de busca e agendamento de aulas.


 **Seleção de Ideias**:  Os critérios utilizados para selecionar as melhores ideias foram:

- Relevância para o problema de negócio: se a ideia realmente resolve as dores do aluno ou monitor.

- Viabilidade técnica: se é possível implementar a funcionalidade dentro do escopo do projeto.

- Valor agregado: se aumenta a confiança, qualidade ou usabilidade da plataforma.

- Escalabilidade: se a ideia pode ser expandida futuramente sem comprometer a estrutura inicial.


 **Ideias Selecionadas**: Com base nos critérios acima, as ideias escolhidas para prototipagem foram:

- Cadastro com e-mail institucional (@ibmec.aluno.br)

- Garante exclusividade e segurança para a comunidade acadêmica.

- Fluxos distintos para aluno e monitor

- Aluno: criação de conta rápida para buscar monitores.

- Monitor: cadastro com informações acadêmicas, matérias, mini-bio, foto e metodologia.

- Sistema de aprovação e selo de monitor verificado

- Admin revisa os perfis de monitores antes da publicação.

- Selo visual aumenta a confiança dos alunos.

- Perfil detalhado de monitor

- Foto, curso, semestre, matérias, nota ou experiência na disciplina, CRA (opcional).

- Busca e agendamento de aulas

- Painel com lista de monitores, filtros por matéria e disponibilidade.

- Opção de agendamento direto pela plataforma.

- Avaliação de monitores pelos alunos

- Sistema de reputação que permite feedback transparente e constrói confiança ao longo do tempo.

#### **3.4. Prototipagem**

- **Descrição do Protótipo**: O protótipo foi desenvolvido como um wireframe de baixa fidelidade, representando as principais telas do sistema de monitoria acadêmica. Foram criadas as seguintes telas: Login/Cadastro, Dashboard, Tela da Monitoria e Tela de Sessão. O protótipo apresenta campos de texto, botões, menus e cards de funcionalidades, permitindo visualizar a navegação e o fluxo de informações do sistema de forma simplificada, sem se preocupar com cores ou detalhes visuais avançados.

- **Materiais Utilizados**: O protótipo foi elaborado utilizando Python com a biblioteca Matplotlib para gerar uma imagem gráfica das telas. Foram utilizados retângulos, textos e layout em grade para representar os elementos de interface. Opcionalmente, o protótipo pode ser reproduzido em ferramentas digitais como Figma, caso seja necessário tornar o wireframe interativo ou mais visualmente detalhado.

- **Testes Realizados**: O protótipo foi revisado pela equipe para validar a organização das telas, fluxo de navegação e posicionamento dos elementos. Foram feitos ajustes na disposição dos menus e cards para garantir clareza visual e melhor entendimento das funcionalidades. O wireframe serviu como referência para futuras iterações e para orientar o desenvolvimento do sistema em Django.

#### **3.5. Teste**

- **Feedback dos Usuários**: O que os usuários acharam do protótipo.
- **Ajustes Realizados**: Mudanças feitas com base no feedback.
- **Resultados Finais**: Descrição da solução final.

---

### **4. Conclusão**

- **Resultados Obtidos**: O que foi alcançado com o projeto.
- **Próximos Passos**: O que ainda precisa ser feito ou implementado.
- **Aprendizados**: Lições aprendidas durante o processo.

---

### **5. Anexos**

- Fotos, gráficos, tabelas, transcrições de entrevistas, etc.

---

## **Dicas para Criar o Documento**

- Use uma linguagem clara e objetiva.
- Inclua visualizações, como mapas de empatia, jornadas do usuário ou esboços de ideias.
- Adapte o documento conforme o estágio do projeto (ex.: um documento inicial pode focar mais na pesquisa, enquanto um final pode detalhar a solução).

Esse modelo é flexível e pode ser ajustado conforme as necessidades do seu projeto ou da sua equipe. O importante é que o documento reflita o processo colaborativo e iterativo do Design Thinking.
