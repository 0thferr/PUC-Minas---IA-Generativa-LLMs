# Especificação do Copiloto e Baseline

Projeto desenvolvido para a disciplina **Geração de Linguagem Natural e Engenharia de Prompt**, do curso de pós-graduação **IA Generativa e Aplicações com LLMs — PUC Minas**.

O Trabalho 2 tem como objetivo transformar as decisões obtidas no Trabalho 1 em uma especificação clara de um **Copiloto Inteligente Corporativo**, definindo seu problema, público-alvo, tarefas, requisitos, limitações, critérios de sucesso e um primeiro prompt executável denominado **baseline v0.1**.

> **Observação:** o caso apresentado no documento da disciplina, envolvendo um Copiloto de RH da Aurora Tech, é um exemplo de laboratório. Os dados abaixo devem ser substituídos pelos dados reais do projeto desenvolvido pelo grupo.

## Objetivo

O projeto busca especificar uma primeira versão simples, reproduzível e mensurável de um copiloto corporativo.

A solução deve definir:

* problema atual e impactos;
* público principal;
* proposta de valor;
* tarefas prioritárias;
* entradas e saídas esperadas;
* requisitos funcionais e não funcionais;
* limites de atuação;
* critérios de recusa e encaminhamento;
* indicadores de sucesso;
* prompt baseline versão `v0.1`;
* testes representativos e casos-limite;
* análise das falhas encontradas.

O baseline deve funcionar como uma referência inicial para que as melhorias realizadas nos trabalhos seguintes possam ser comparadas de maneira objetiva.

## Continuidade do projeto

O Trabalho 2 faz parte de uma trajetória incremental composta por seis trabalhos:

| Trabalho | Entrega                                   | Resultado                                         |
| -------- | ----------------------------------------- | ------------------------------------------------- |
| 1        | Estudo Comparativo de Modelos e Prompts   | Modelo e estratégia inicial                       |
| 2        | Especificação do Copiloto e Baseline      | Escopo, requisitos, métricas e referência inicial |
| 3        | Biblioteca Versionada de Prompts          | Prompts reutilizáveis e rastreáveis               |
| 4        | Fluxo de Geração e Protótipo Textual      | Fluxo integrado e protótipo                       |
| 5        | Protótipo Multimodal e Plano de Avaliação | Nova modalidade, testes e rubrica                 |
| 6        | Copiloto Inteligente Corporativo          | Solução consolidada, demonstrada e avaliada       |

O caso de uso definido no Trabalho 2 poderá ser mantido até o Trabalho 6.

## 1. Problema e proposta de valor

### Problema

**[Descrever o problema corporativo escolhido pelo grupo.]**

O problema deve apresentar uma dificuldade real, seus impactos e as pessoas afetadas.

### Público-alvo

**[Definir o usuário principal do copiloto.]**

Descrever:

* perfil do usuário;
* conhecimento técnico necessário;
* necessidades;
* contexto de utilização;
* principais dificuldades enfrentadas.

### Proposta de valor

**[Descrever como o copiloto ajudará o usuário.]**

A proposta deve demonstrar ganho de produtividade, qualidade, padronização, redução de tempo ou outro benefício mensurável.

### Escopo

#### Dentro do escopo

* [Funcionalidade 1]
* [Funcionalidade 2]
* [Funcionalidade 3]

#### Fora do escopo

* [Limitação 1]
* [Limitação 2]
* [Limitação 3]

O documento da disciplina exige que as atividades dentro e fora do escopo estejam claramente separadas e que o copiloto não seja apresentado como substituto de decisões humanas.

### Principais riscos

* Geração de informações inexistentes;
* interpretação incorreta da base de conhecimento;
* respostas fora do escopo;
* utilização inadequada das respostas;
* exposição de informações pessoais ou sigilosas;
* tomada de decisões que deveriam permanecer sob responsabilidade humana.

## 2. Usuários, tarefas e jornada

O projeto deve possuir exatamente **três tarefas prioritárias**, cada uma com entrada, processamento esperado, saída e mecanismo de validação humana.

| Tarefa      | Entrada   | Processamento   | Saída   | Validação humana |
| ----------- | --------- | --------------- | ------- | ---------------- |
| T1 — [Nome] | [Entrada] | [Processamento] | [Saída] | [Validação]      |
| T2 — [Nome] | [Entrada] | [Processamento] | [Saída] | [Validação]      |
| T3 — [Nome] | [Entrada] | [Processamento] | [Saída] | [Validação]      |

### Jornada do usuário

```text
Usuário realiza uma solicitação
        ↓
Copiloto identifica a tarefa
        ↓
Consulta a base de conhecimento disponível
        ↓
Processa a solicitação
        ↓
Gera resposta no formato definido
        ↓
Usuário valida a resposta
        ↓
Confirma ou encaminha para responsável humano
```

A jornada deve deixar explícito em quais momentos existe participação ou validação humana.

## 3. Requisitos

### Requisitos funcionais

O copiloto deverá:

* [RF01] Executar a tarefa 1;
* [RF02] Executar a tarefa 2;
* [RF03] Executar a tarefa 3;
* [RF04] Utilizar o contexto necessário para responder;
* [RF05] Produzir respostas em formato padronizado;
* [RF06] Encaminhar situações que exigem decisão humana.

### Requisitos não funcionais

| Categoria       | Requisito                                      |
| --------------- | ---------------------------------------------- |
| Desempenho      | [Definir tempo máximo de resposta]             |
| Acessibilidade  | [Definir requisito]                            |
| Privacidade     | Não solicitar dados pessoais desnecessários    |
| Custo           | [Definir custo máximo por interação]           |
| Disponibilidade | [Definir disponibilidade esperada]             |
| Contexto        | [Definir informações que podem ser utilizadas] |

A especificação da disciplina considera tempo de resposta, acessibilidade, privacidade, custo e disponibilidade como aspectos relevantes dos requisitos não funcionais.

## 4. Limites e critérios de recusa

O copiloto não deve responder de maneira especulativa quando não possuir informações suficientes.

As principais situações de recusa ou encaminhamento são:

1. A informação solicitada não está presente na base de conhecimento.
2. O usuário solicita uma decisão, aprovação ou exceção que depende de um responsável humano.
3. A solicitação está fora do domínio definido ou exige dados pessoais desnecessários.

Uma mensagem de limite pode seguir o seguinte padrão:

> "Não consigo determinar isso com segurança usando a base de conhecimento disponível. Consulte o responsável para validação. Posso explicar as informações gerais disponíveis."

Esses critérios seguem a orientação apresentada no documento da disciplina.

## 5. Critérios de sucesso

O projeto deve utilizar pelo menos cinco indicadores mensuráveis. Os indicadores serão utilizados como referência para futuras comparações.

| Indicador                     | Como medir                             | Meta inicial |    Baseline |
| ----------------------------- | -------------------------------------- | -----------: | ----------: |
| Taxa de conclusão             | Casos respondidos adequadamente / 7    |        ≥ 70% | [Resultado] |
| Aderência ao formato          | Respostas no formato definido / 7      |        ≥ 85% | [Resultado] |
| Factualidade                  | Casos sem informação inventada / 7     |         100% | [Resultado] |
| Recusa/encaminhamento correto | Casos-limite tratados corretamente / 2 |         100% | [Resultado] |
| Latência média                | Soma das latências / 7                 |    [Definir] | [Resultado] |

As metas devem ser definidas **antes da execução dos testes** e não devem ser modificadas após a obtenção dos resultados.

## 6. Modelo e configuração

As decisões relacionadas ao modelo devem ser herdadas do Trabalho 1.

### Modelo principal

**[Nome do modelo]**

### Modelo de contingência

**[Nome do modelo alternativo]**

### Configuração

```text
Temperatura: [valor]
Max tokens: [valor]
Top-p: [valor]
Outros parâmetros: [valores]
```

### Justificativa

**[Descrever por que o modelo e a configuração foram selecionados, utilizando as evidências obtidas no Trabalho 1.]**

O documento estabelece que a justificativa do modelo e da configuração deve estar conectada às evidências do Trabalho 1.

## 7. Prompt Baseline v0.1

O baseline deve ser simples, reproduzível e suficientemente documentado para permitir comparações futuras.

Arquivo:

```text
baseline_v0.1.txt
```

Estrutura esperada:

```text
VERSÃO: baseline_v0.1

PAPEL:
[Definição do papel do copiloto]

OBJETIVO:
[Objetivo principal]

CONTEXTO:
[Contexto necessário para a execução]

BASE DE CONHECIMENTO:
[Informações utilizadas pelo copiloto]

REGRAS:
1. Não inventar informações.
2. Utilizar somente informações disponíveis na base.
3. Encaminhar situações que exigem decisão humana.
4. Não solicitar dados pessoais desnecessários.
5. Respeitar os limites definidos para o projeto.

FORMATO OBRIGATÓRIO:
[Definir formato esperado da resposta]

PERGUNTA DO USUÁRIO:
[Entrada do teste]
```

O prompt não deve ser alterado durante a execução dos sete testes. As falhas encontradas devem permanecer registradas para servir como referência para os próximos trabalhos.

## 8. Testes

O baseline deve ser executado em **sete situações**, sendo:

* cinco casos representativos;
* dois casos-limite.

Cada teste deve utilizar uma nova sessão, mantendo prompt, base e parâmetros iguais. Apenas a pergunta do usuário deve ser alterada.

| ID | Tipo           | Pergunta   | Resultado esperado   |
| -- | -------------- | ---------- | -------------------- |
| R1 | Representativo | [Pergunta] | [Resultado esperado] |
| R2 | Representativo | [Pergunta] | [Resultado esperado] |
| R3 | Representativo | [Pergunta] | [Resultado esperado] |
| R4 | Representativo | [Pergunta] | [Resultado esperado] |
| R5 | Representativo | [Pergunta] | [Resultado esperado] |
| L1 | Caso-limite    | [Pergunta] | [Resultado esperado] |
| L2 | Caso-limite    | [Pergunta] | [Resultado esperado] |

### Registro dos resultados

| ID | Conclusão | Formato | Factual | Encaminhamento | Latência | Falha observada |
| -- | --------- | ------- | ------- | -------------- | -------: | --------------- |
| R1 | S/N       | S/N     | S/N     | S/N/NA         |     [ms] | [Descrição]     |
| R2 | S/N       | S/N     | S/N     | S/N/NA         |     [ms] | [Descrição]     |
| R3 | S/N       | S/N     | S/N     | S/N/NA         |     [ms] | [Descrição]     |
| R4 | S/N       | S/N     | S/N     | S/N/NA         |     [ms] | [Descrição]     |
| R5 | S/N       | S/N     | S/N     | S/N/NA         |     [ms] | [Descrição]     |
| L1 | S/N       | S/N     | S/N     | S/N/NA         |     [ms] | [Descrição]     |
| L2 | S/N       | S/N     | S/N     | S/N/NA         |     [ms] | [Descrição]     |

Se ocorrer um erro técnico, ele deve ser registrado e a execução pode ser repetida uma única vez. A primeira tentativa deve permanecer como evidência.

## 9. Análise das falhas

As falhas observadas devem ser utilizadas para determinar as limitações do baseline.

| Falha | Evidência/Teste | Causa provável | Melhoria futura | Prioridade       |
| ----- | --------------- | -------------- | --------------- | ---------------- |
| 1     | [Teste]         | [Causa]        | [Melhoria]      | Alta/Média/Baixa |
| 2     | [Teste]         | [Causa]        | [Melhoria]      | Alta/Média/Baixa |
| 3     | [Teste]         | [Causa]        | [Melhoria]      | Alta/Média/Baixa |

A análise deve responder:

* Quais metas foram atingidas?
* Quais metas falharam?
* A falha foi causada pelo modelo, prompt, base de conhecimento ou requisito?
* Alguma limitação identificada no Trabalho 1 reapareceu?
* O modelo de contingência seria útil?
* Quais três melhorias serão priorizadas no Trabalho 3?

O baseline deve ser tratado como **referência**, e não como versão final. As correções identificadas serão implementadas posteriormente na Biblioteca Versionada de Prompts do Trabalho 3.

## 10. Estrutura do projeto

Uma estrutura sugerida para o repositório é:

```text
trabalho-02-copiloto-baseline/
│
├── README.md
│
├── docs/
│   ├── especificacao.md
│   ├── requisitos.md
│   ├── criterios-sucesso.md
│   └── analise-falhas.md
│
├── prompts/
│   └── baseline_v0.1.txt
│
├── knowledge/
│   └── base_conhecimento/
│
├── tests/
│   ├── testes_representativos.md
│   └── casos_limite.md
│
├── results/
│   ├── respostas_brutas/
│   └── metricas.csv
│
├── evidence/
│   └── screenshots/
│
└── src/
    └── [implementação opcional]
```

A organização deve permitir rastrear prompts, bases, configurações e resultados ao longo dos Trabalhos 3 a 6.

## 11. Implementação opcional

O trabalho pode ser encapsulado em uma aplicação Python simples, utilizando, por exemplo:

* Streamlit; ou
* FastAPI integrado a um frontend web.

A implementação opcional deve priorizar rastreabilidade, e não complexidade.

A aplicação pode centralizar:

* base de conhecimento;
* prompt baseline `v0.1`;
* configuração do modelo;
* perguntas dos testes;
* respostas brutas;
* modelo utilizado;
* versão;
* parâmetros;
* data da execução;
* latência;
* resultados dos testes.

### Exemplo de fluxo

```text
Interface
    ↓
Entrada do usuário
    ↓
Prompt Baseline v0.1
    ↓
Modelo LLM
    ↓
Resposta
    ↓
Registro de métricas
    ↓
Evidência / Resultado
```

## 12. Privacidade e segurança

O projeto não deve armazenar:

* credenciais;
* tokens de API;
* senhas;
* dados pessoais desnecessários;
* informações sigilosas.

Credenciais devem permanecer fora do repositório quando forem necessárias para a execução da aplicação.

Exemplo de arquivo `.gitignore`:

```gitignore
.env
*.key
*.pem
secrets/
credentials/
__pycache__/
.venv/
```

## 13. Entregáveis

A entrega final deve conter:

1. Especificação do caso de uso e mapa de escopo.
2. Tabela de tarefas, entradas e saídas.
3. Requisitos, restrições e critérios de sucesso.
4. Prompt baseline versionado como `v0.1`.
5. Resultados dos sete testes.
6. Análise das falhas.
7. Cinco indicadores e respectivas métricas.
8. Três melhorias priorizadas para o Trabalho 3.

Essa estrutura corresponde aos entregáveis definidos no documento da disciplina.

## 14. Checklist

* [ ] Modelo e configuração justificados pelo Trabalho 1.
* [ ] Problema corporativo claramente definido.
* [ ] Público-alvo identificado.
* [ ] Proposta de valor definida.
* [ ] Escopo e fora de escopo definidos.
* [ ] Três tarefas prioritárias especificadas.
* [ ] Entradas e saídas documentadas.
* [ ] Validação humana definida.
* [ ] Requisitos funcionais documentados.
* [ ] Requisitos não funcionais documentados.
* [ ] Limites e critérios de recusa definidos.
* [ ] Cinco indicadores definidos.
* [ ] Metas estabelecidas antes dos testes.
* [ ] Prompt `baseline_v0.1` salvo.
* [ ] Cinco testes representativos executados.
* [ ] Dois casos-limite executados.
* [ ] Sete respostas brutas armazenadas.
* [ ] Latências registradas.
* [ ] Falhas documentadas.
* [ ] Três melhorias priorizadas para o Trabalho 3.
* [ ] Nenhuma credencial armazenada no repositório.
* [ ] Nenhum dado pessoal ou sigiloso armazenado.

O checklist final do documento reforça que as sete saídas brutas e suas latências devem ser anexadas e que as falhas encontradas não devem ser ocultadas, pois servirão de entrada para o Trabalho 3.

## 15. Conexão com o Trabalho 3

O resultado deste trabalho servirá diretamente como entrada para a próxima etapa do projeto.

Os seguintes artefatos deverão ser reaproveitados:

```text
Especificação
      +
Baseline v0.1
      +
7 testes
      +
Resultados
      +
Falhas identificadas
      +
3 melhorias priorizadas
      ↓
Trabalho 3
Biblioteca Versionada de Prompts
```

A especificação, o baseline `v0.1`, os sete testes e as três melhorias priorizadas são definidos como entrada obrigatória para a construção da Biblioteca Versionada de Prompts no Trabalho 3.

## Referência

**PUC Minas — Diretoria de Educação Continuada (IEC).**

Disciplina: **Geração de Linguagem Natural e Engenharia de Prompt**
Curso: **IA Generativa e Aplicações com LLMs**
Trabalho: **Especificação do Copiloto e Baseline**
Professor: **Ricardo Brito Alves**.
