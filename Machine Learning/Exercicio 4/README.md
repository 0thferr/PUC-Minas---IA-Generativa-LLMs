# Tarefa Individual – Modelagem Preditiva com Algoritmos Supervisionados

## Objetivo

Desenvolver um projeto de **Classificação Supervisionada** utilizando uma das bases de dados disponibilizadas no Portal do Aluno.

O projeto deverá contemplar todas as etapas de um fluxo de Machine Learning, desde a definição do problema até a avaliação do modelo, utilizando **um ou dois algoritmos supervisionados** dentre os seguintes:

- Regressão Logística;
- Naive Bayes;
- Redes Neurais.

O foco é construir modelos preditivos, avaliar seu desempenho e interpretar os resultados com base nas características do conjunto de dados.

---

## Bases de Dados Disponíveis

O aluno deverá selecionar **uma** das seguintes bases:

| Base de Dados | Descrição |
|---------------|-----------|
| **Bank Marketing** | Dados de campanhas de marketing realizadas por uma instituição bancária. |
| **dados_risco_credito.csv** | Base simulada contendo informações relacionadas ao risco de crédito de clientes. |

As bases encontram-se disponíveis no **Portal do Aluno**.

A base **Bank Marketing** também pode ser obtida no repositório oficial da UCI Machine Learning Repository:

https://archive.ics.uci.edu/ml/datasets/bank+marketing

---

## Etapas da Atividade

### 1. Definição do Problema

Nesta etapa, deverão ser definidos os objetivos do projeto.

As atividades incluem:

- Identificar o problema como uma tarefa de classificação;
- Definir a variável alvo;
- Estabelecer métricas de sucesso;
- Definir objetivos claros e mensuráveis.

---

### 2. Coleta e Preparação dos Dados

Realizar a inspeção inicial do conjunto de dados.

As atividades incluem:

- Carregar o dataset;
- Verificar a qualidade dos dados;
- Identificar valores ausentes;
- Detectar registros duplicados;
- Avaliar a integridade das informações disponíveis.

---

### 3. Análise Exploratória de Dados (EDA)

Explorar o comportamento das variáveis presentes no dataset.

As análises devem incluir:

- Estatísticas descritivas;
- Distribuição das variáveis;
- Visualizações gráficas;
- Identificação de padrões;
- Detecção de possíveis outliers.

---

### 4. Pré-processamento dos Dados

Preparar o conjunto de dados para a etapa de modelagem.

As principais etapas incluem:

- Tratamento de valores faltantes por imputação ou remoção;
- Normalização ou padronização das variáveis, quando necessário;
- Conversão de variáveis categóricas para representação numérica;
- Separação dos dados em conjuntos de treino e teste.

---

### 5. Seleção e Treinamento do Modelo

Escolher **um ou dois algoritmos supervisionados** entre os seguintes:

- Regressão Logística;
- Naive Bayes;
- Redes Neurais.

Após a escolha:

- Treinar os modelos;
- Ajustar hiperparâmetros, quando necessário;
- Comparar o desempenho obtido.

---

### 6. Avaliação do Modelo

Avaliar os modelos utilizando métricas apropriadas para classificação.

As análises devem contemplar:

- Aplicação de métricas de desempenho;
- Avaliação em dados de teste;
- Comparação entre os modelos (quando houver mais de um);
- Identificação dos principais erros de classificação;
- Discussão sobre a capacidade de generalização do modelo.

---

## Entregáveis

O aluno deverá entregar um notebook **`.ipynb`** contendo:

- Nome completo no início do notebook;
- Código organizado e comentado;
- Visualizações e gráficos;
- Análises escritas;
- Interpretação dos resultados obtidos.

---

## Estrutura Recomendada do Notebook

1. Identificação do aluno;
2. Definição do problema;
3. Descrição do dataset;
4. Análise exploratória dos dados (EDA);
5. Pré-processamento;
6. Implementação dos modelos;
7. Ajuste de hiperparâmetros (quando aplicável);
8. Avaliação dos resultados;
9. Comparação entre os modelos;
10. Conclusão e sugestões de melhorias.

---

## Objetivo Final

Desenvolver uma solução de classificação supervisionada capaz de realizar previsões confiáveis a partir de dados reais, aplicando técnicas de preparação, treinamento e avaliação de modelos de Machine Learning, além de interpretar criticamente os resultados obtidos.