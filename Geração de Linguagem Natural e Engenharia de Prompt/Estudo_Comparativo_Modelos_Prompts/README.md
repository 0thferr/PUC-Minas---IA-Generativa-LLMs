# Estudo Comparativo de Modelos e Prompts

## Pós-Graduação em IA Generativa e Aplicações com LLMs

**Disciplina:** Geração de Linguagem Natural e Engenharia de Prompt
**Trabalho:** Estudo Comparativo de Modelos e Prompts
**Professor:** Ricardo Brito Alves
**Instituição:** PUC Minas

---

## 1. Sobre o projeto

Este projeto tem como objetivo realizar um estudo comparativo entre diferentes modelos de linguagem em condições controladas, utilizando os mesmos dados de entrada, prompts, parâmetros e critérios de avaliação.

A proposta faz parte do desenvolvimento incremental de um **Copiloto Inteligente Corporativo**. O resultado deste experimento será utilizado como base para a seleção do modelo principal e de uma alternativa de contingência para as próximas etapas do projeto.

A atividade exige a comparação de, no mínimo, três modelos e a execução de quatro tarefas: resumo, reescrita, extração/classificação e geração orientada a um público específico.

---

## 2. Objetivo

Responder à seguinte pergunta de comparação:

> **Qual modelo e configuração atendem melhor ao projeto pretendido?**

Para isso, serão analisados:

* Correção e fidelidade das respostas;
* Relevância;
* Clareza;
* Completude;
* Aderência ao formato solicitado;
* Segurança e respeito aos limites;
* Latência;
* Quantidade de tokens, quando disponível;
* Custo estimado;
* Ocorrência de erros, recusas, alucinações ou respostas incompletas.

A recomendação final deverá indicar:

1. Um modelo principal;
2. Um modelo de contingência;
3. As condições em que cada modelo é mais adequado;
4. As limitações observadas durante o experimento.

---

## 3. Modelos avaliados

Os modelos devem ser identificados por nome, fornecedor, versão/data e forma de acesso.

| Código | Modelo       | Fornecedor     | Versão     | Acesso            |
| ------ | ------------ | -------------- | ---------- | ----------------- |
| A      | `[MODELO A]` | `[FORNECEDOR]` | `[VERSÃO]` | `[WEB/API/LOCAL]` |
| B      | `[MODELO B]` | `[FORNECEDOR]` | `[VERSÃO]` | `[WEB/API/LOCAL]` |
| C      | `[MODELO C]` | `[FORNECEDOR]` | `[VERSÃO]` | `[WEB/API/LOCAL]` |

### Configuração

Quando disponíveis, foram utilizadas configurações equivalentes entre os modelos:

* **Temperatura:** 0,2;
* **Top-p:** 1,0 ou valor padrão;
* **Limite de saída:** 600 tokens ou equivalente;
* **Sessão:** nova conversa para cada prompt;
* **Execução:** uma execução por combinação modelo × prompt.

Quando determinado parâmetro não estiver disponível na interface utilizada, ele deverá ser registrado como **"não disponível na interface"**, sem atribuição de valores não observados.

---

## 4. Organização do experimento

O experimento foi estruturado em seis áreas:

```text
01_planejamento/
├── modelos
├── parametros
└── rubrica

02_prompts/
├── P1_resumo.txt
├── P2_comunicado.txt
├── P3_extracao_json.txt
└── P4_faq.txt

03_entradas/
└── texto_base.txt

04_saidas_brutas/
├── modelo_A/
├── modelo_B/
└── modelo_C/

05_avaliacao/
├── notas
├── latencia
├── tokens
└── custos

06_relatorio/
├── README.md
└── apresentacao
```

As respostas brutas devem ser preservadas exatamente como recebidas, sem correções manuais.

---

## 5. Texto-base utilizado

O experimento utiliza como entrada controlada o caso fictício da **Aurora Tech**, relacionado a uma política-piloto de trabalho híbrido.

A política estabelece um período de teste entre **1º de setembro e 30 de novembro**, permitindo aos colaboradores elegíveis trabalhar remotamente até dois dias por semana, definidos com o gestor.

Também são estabelecidas regras relacionadas a presença presencial, elegibilidade, exceções, disponibilidade, autenticação multifator, utilização de dispositivos gerenciados, despesas, acompanhamento de resultados e comunicação de incidentes de segurança.

O texto-base completo deve ser mantido em:

```text
03_entradas/texto_base.txt
```

O mesmo conteúdo deve ser utilizado em todos os modelos para garantir a comparabilidade dos resultados.

---

## 6. Prompts controlados

Foram definidos quatro prompts, aplicados de maneira idêntica aos três modelos.

### P1 — Resumo executivo

**Objetivo:** produzir um resumo executivo da política.

**Restrições principais:**

* Utilizar somente informações do texto fornecido;
* Produzir entre 100 e 130 palavras;
* Destacar objetivo, período, elegibilidade, regras, controles e avaliação;
* Não inventar justificativas, benefícios ou exceções;
* Utilizar um título e um único parágrafo.

---

### P2 — Comunicado

**Objetivo:** transformar a política em um comunicado destinado aos colaboradores.

**Restrições principais:**

* Utilizar linguagem clara, cordial e objetiva;
* Preservar datas, condições, exceções e responsabilidades;
* Organizar a resposta em assunto, abertura, regras principais e canal para dúvidas;
* Não adicionar regras ou promessas inexistentes no texto-base.

---

### P3 — Extração em JSON

**Objetivo:** extrair informações estruturadas da política.

A resposta deve utilizar JSON válido e exatamente as seguintes chaves:

```json
{
  "periodo_inicio": "AAAA-MM-DD ou null",
  "periodo_fim": "AAAA-MM-DD ou null",
  "dias_remotos_maximo": 0,
  "dia_presencial_comum": "",
  "horario_disponibilidade": "",
  "funcoes_nao_elegiveis": [],
  "controles_seguranca": [],
  "canal_duvidas": ""
}
```

Caso uma informação não esteja presente no texto-base, deve ser utilizado `null`.

---

### P4 — FAQ para gestores

**Objetivo:** criar uma FAQ destinada aos gestores.

Requisitos:

* Exatamente seis perguntas e respostas;
* Cobrir elegibilidade;
* Definição dos dias;
* Presença comum;
* Exceções;
* Acompanhamento;
* Segurança;
* Máximo de 45 palavras por resposta;
* Utilizar somente informações do texto-base;
* Quando não houver informação suficiente, orientar o gestor a consultar o canal RH Responde.

A especificação dos quatro prompts está definida no roteiro da atividade, entre as páginas 7 e 8 do documento.

---

## 7. Execuções

O experimento possui **12 combinações**:

| Execução | Modelo | Prompt | Saída      |
| -------- | ------ | ------ | ---------- |
| E01      | A      | P1     | `A_P1.txt` |
| E02      | A      | P2     | `A_P2.txt` |
| E03      | A      | P3     | `A_P3.txt` |
| E04      | A      | P4     | `A_P4.txt` |
| E05      | B      | P1     | `B_P1.txt` |
| E06      | B      | P2     | `B_P2.txt` |
| E07      | B      | P3     | `B_P3.txt` |
| E08      | B      | P4     | `B_P4.txt` |
| E09      | C      | P1     | `C_P1.txt` |
| E10      | C      | P2     | `C_P2.txt` |
| E11      | C      | P3     | `C_P3.txt` |
| E12      | C      | P4     | `C_P4.txt` |

Para cada execução devem ser registrados:

* Modelo;
* Prompt;
* Horário de início;
* Latência;
* Tokens;
* Arquivo da saída;
* Erros ou ocorrências;
* Observações.

O roteiro determina que as 12 saídas brutas sejam preservadas e identificadas individualmente.

---

## 8. Critérios de avaliação

Cada resposta é avaliada de **1 a 5** nos seguintes critérios:

| Critério             | Peso |
| -------------------- | ---: |
| Correção/Fidelidade  |  25% |
| Relevância           |  20% |
| Clareza              |  15% |
| Completude           |  15% |
| Aderência ao formato |  15% |
| Segurança/Limites    |  10% |

A nota ponderada é calculada por:

```text
Nota =
(correção × 0,25) +
(relevância × 0,20) +
(clareza × 0,15) +
(completude × 0,15) +
(formato × 0,15) +
(segurança × 0,10)
```

Para conversão da escala de 1–5 para 0–100:

```text
Nota final = Nota ponderada × 20
```

A rubrica oficial define os níveis 1, 3 e 5 para cada critério, sendo as notas 2 e 4 utilizadas para representar desempenhos intermediários.

---

## 9. Resultados da avaliação

### Modelo A

| Prompt | Correção | Relevância | Clareza | Completude | Formato | Segurança |  Nota |
| ------ | -------: | ---------: | ------: | ---------: | ------: | --------: | ----: |
| P1     |    `[ ]` |      `[ ]` |   `[ ]` |      `[ ]` |   `[ ]` |     `[ ]` | `[ ]` |
| P2     |    `[ ]` |      `[ ]` |   `[ ]` |      `[ ]` |   `[ ]` |     `[ ]` | `[ ]` |
| P3     |    `[ ]` |      `[ ]` |   `[ ]` |      `[ ]` |   `[ ]` |     `[ ]` | `[ ]` |
| P4     |    `[ ]` |      `[ ]` |   `[ ]` |      `[ ]` |   `[ ]` |     `[ ]` | `[ ]` |

### Modelo B

| Prompt | Correção | Relevância | Clareza | Completude | Formato | Segurança |  Nota |
| ------ | -------: | ---------: | ------: | ---------: | ------: | --------: | ----: |
| P1     |    `[ ]` |      `[ ]` |   `[ ]` |      `[ ]` |   `[ ]` |     `[ ]` | `[ ]` |
| P2     |    `[ ]` |      `[ ]` |   `[ ]` |      `[ ]` |   `[ ]` |     `[ ]` | `[ ]` |
| P3     |    `[ ]` |      `[ ]` |   `[ ]` |      `[ ]` |   `[ ]` |     `[ ]` | `[ ]` |
| P4     |    `[ ]` |      `[ ]` |   `[ ]` |      `[ ]` |   `[ ]` |     `[ ]` | `[ ]` |

### Modelo C

| Prompt | Correção | Relevância | Clareza | Completude | Formato | Segurança |  Nota |
| ------ | -------: | ---------: | ------: | ---------: | ------: | --------: | ----: |
| P1     |    `[ ]` |      `[ ]` |   `[ ]` |      `[ ]` |   `[ ]` |     `[ ]` | `[ ]` |
| P2     |    `[ ]` |      `[ ]` |   `[ ]` |      `[ ]` |   `[ ]` |     `[ ]` | `[ ]` |
| P3     |    `[ ]` |      `[ ]` |   `[ ]` |      `[ ]` |   `[ ]` |     `[ ]` | `[ ]` |
| P4     |    `[ ]` |      `[ ]` |   `[ ]` |      `[ ]` |   `[ ]` |     `[ ]` | `[ ]` |

---

## 10. Latência e desempenho

| Modelo | Latência média | Tokens de entrada | Tokens de saída | Falhas/recusas |
| ------ | -------------: | ----------------: | --------------: | -------------: |
| A      |        `[ ] s` |             `[ ]` |           `[ ]` |          `[ ]` |
| B      |        `[ ] s` |             `[ ]` |           `[ ]` |          `[ ]` |
| C      |        `[ ] s` |             `[ ]` |           `[ ]` |          `[ ]` |

A latência deve ser registrada durante a execução de cada prompt. Caso a interface não disponibilize a quantidade de tokens, deve ser informado **"não disponível"**, podendo ser apresentada uma estimativa separadamente.

---

## 11. Custos

O custo estimado deve considerar tokens de entrada e saída:

```text
custo =
(tokens_entrada / 1.000.000 × preço_entrada) +
(tokens_saida / 1.000.000 × preço_saida)
```

| Modelo |  Custo total | Fonte do preço | Data da consulta |
| ------ | -----------: | -------------- | ---------------- |
| A      | `[R$ / US$]` | `[fonte]`      | `[data]`         |
| B      | `[R$ / US$]` | `[fonte]`      | `[data]`         |
| C      | `[R$ / US$]` | `[fonte]`      | `[data]`         |

A comparação deve considerar o custo real estimado das execuções, e não somente o preço anunciado por milhão de tokens.

---

## 12. Comparação geral

| Modelo | Qualidade média | Aderência ao formato | Latência média | Custo | Falhas/recusas |
| ------ | --------------: | -------------------: | -------------: | ----: | -------------: |
| A      |           `[ ]` |                `[ ]` |        `[ ] s` | `[ ]` |          `[ ]` |
| B      |           `[ ]` |                `[ ]` |        `[ ] s` | `[ ]` |          `[ ]` |
| C      |           `[ ]` |                `[ ]` |        `[ ] s` | `[ ]` |          `[ ]` |

### Análise

O **Modelo [X]** apresentou o melhor desempenho geral, principalmente nas tarefas `[P1/P2/P3/P4]`.

O **Modelo [Y]** apresentou maior consistência na aderência aos formatos solicitados, especialmente em `[tarefa]`.

Durante os testes foram observados `[alucinações/omissões/JSON inválido/extrapolações/recusas]`, principalmente no modelo `[X]`.

A diferença de qualidade entre os modelos `[X]` e `[Y]` `[justifica/não justifica]` o aumento observado de custo ou latência devido a `[justificativa baseada nos resultados]`.

---

## 13. Recomendação

### Modelo principal

**[MODELO PRINCIPAL]**

**Justificativa:**

[Descrever a escolha com base nos resultados obtidos, considerando qualidade, aderência ao formato, latência, custo, segurança e adequação ao futuro Copiloto Inteligente Corporativo.]

### Modelo de contingência

**[MODELO DE CONTINGÊNCIA]**

**Justificativa:**

[Explicar por que o modelo pode ser utilizado como alternativa, indicando seus pontos fortes e limitações.]

### Modelo não recomendado

**[MODELO, SE APLICÁVEL]**

**Justificativa:**

[Descrever os resultados que justificam a decisão.]

A escolha não deve ser baseada somente na maior média. O documento orienta considerar o projeto futuro, qualidade, consistência, custo, latência, falhas e limitações do experimento.

---

## 14. Limitações

As principais limitações do experimento são:

* Número limitado de modelos avaliados;
* Apenas quatro tarefas utilizadas;
* Quantidade limitada de execuções;
* Diferenças entre as interfaces e parâmetros disponibilizados pelos fornecedores;
* Tokens podem não estar disponíveis em algumas interfaces;
* Latência pode variar de acordo com infraestrutura e condições de rede;
* Os resultados representam o comportamento dos modelos nas condições específicas deste experimento;
* A conclusão não deve ser generalizada para todos os casos de uso.

---

## 15. Estrutura dos arquivos

```text
.
├── 01_planejamento/
├── 02_prompts/
├── 03_entradas/
├── 04_saidas_brutas/
├── 05_avaliacao/
├── 06_relatorio/
└── README.md
```

As saídas devem permanecer identificadas conforme o padrão:

```text
A_P1.txt
A_P2.txt
A_P3.txt
A_P4.txt

B_P1.txt
B_P2.txt
B_P3.txt
B_P4.txt

C_P1.txt
C_P2.txt
C_P3.txt
C_P4.txt
```

---

## 16. Checklist final

* [ ] Três modelos identificados por versão/data.
* [ ] Forma de acesso registrada.
* [ ] Parâmetros registrados.
* [ ] Texto-base único utilizado.
* [ ] Quatro prompts idênticos aplicados aos modelos.
* [ ] Doze execuções realizadas.
* [ ] Doze saídas brutas preservadas.
* [ ] Latências registradas.
* [ ] Tokens registrados quando disponíveis.
* [ ] Custos calculados.
* [ ] Fonte dos preços registrada.
* [ ] Todas as respostas avaliadas nos seis critérios.
* [ ] Notas extremas justificadas.
* [ ] Falhas, recusas e limitações documentadas.
* [ ] Modelo principal definido.
* [ ] Modelo de contingência definido.
* [ ] Recomendação baseada em evidências.
* [ ] Prompts e entradas anexados.
* [ ] Resultados brutos anexados.
* [ ] Nenhum dado pessoal ou sigiloso utilizado.
* [ ] Links e arquivos da entrega verificados.

---

## 17. Conclusão

O experimento foi estruturado para permitir uma comparação controlada entre modelos de linguagem, reduzindo a influência de preferências pessoais na escolha da tecnologia.

A partir das quatro tarefas propostas, das 12 execuções, da rubrica de avaliação e dos registros de latência e custo, será possível selecionar o modelo mais adequado para servir como base do **Copiloto Inteligente Corporativo**.

Os resultados deste trabalho deverão ser reutilizados nas próximas etapas do projeto, especialmente na definição do modelo e na criação do prompt baseline do Copiloto.