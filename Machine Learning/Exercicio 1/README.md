# Atividade Prática – Unidade 1: EDA e Preparação de Dados

## Objetivo

Realizar uma **Análise Exploratória de Dados (EDA)** completa e preparar o dataset **Adult Census Income** para futuras aplicações de Machine Learning.

O foco da atividade é compreender a estrutura do conjunto de dados, identificar padrões, tratar inconsistências e preparar as variáveis para etapas posteriores de modelagem.

---

## Dataset

O projeto utiliza o conjunto de dados **Adult Census Income**, disponibilizado pelo **UCI Machine Learning Repository**.

**Fonte oficial:**

https://archive.ics.uci.edu/dataset/2/adult

O arquivo utilizado é:

- `adult.data.txt`

Também será utilizado o notebook base:

- `tarefa_1_eda.ipynb`

Para compreender o significado de cada atributo, recomenda-se consultar o arquivo `adult.names`, que descreve todas as colunas e seus respectivos valores categóricos.

---

## Etapas da Atividade

### 1. Importação e Visualização Inicial

Nesta etapa, o objetivo é conhecer a estrutura geral do dataset.

As atividades incluem:

- Importar o dataset utilizando a biblioteca **Pandas**;
- Definir os nomes das colunas conforme o arquivo `adult.names`;
- Visualizar as primeiras observações utilizando `head()`;
- Analisar o formato e os tipos de dados com `info()`;
- Obter estatísticas descritivas utilizando `describe()`.

---

### 2. Análise Exploratória de Dados (EDA)

Realizar uma análise detalhada do conjunto de dados, investigando seus principais aspectos.

#### Tipos de Variáveis

- Identificar variáveis numéricas e categóricas;
- Verificar a necessidade de conversão de tipos de dados.

#### Distribuição dos Dados

Analisar a distribuição de variáveis como:

- Idade;
- Horas trabalhadas por semana;
- Escolaridade;
- Ocupação;
- Outras variáveis relevantes.

Utilizar visualizações como:

- Histogramas;
- Boxplots;
- Gráficos de barras.

#### Valores Ausentes ou Inconsistentes

- Identificar valores nulos;
- Detectar marcadores de ausência, como `"?"`;
- Quantificar ocorrências utilizando funções como `isnull()` e `value_counts()`.

#### Relação com a Variável Alvo

Investigar quais características apresentam maior relação com a variável **income**.

Para isso, utilizar recursos como:

- `groupby()`;
- `crosstab()`;
- Gráficos comparativos;
- Estatísticas descritivas.

---

### 3. Preparação dos Dados

Após a análise exploratória, realizar o pré-processamento do dataset.

#### Tratamento de Valores Ausentes

Escolher uma estratégia adequada, como:

- Remoção de registros;
- Imputação de valores.

#### Normalização ou Padronização *(Opcional)*

Aplicar técnicas de escalonamento nas variáveis numéricas utilizando:

- `StandardScaler`;
- `MinMaxScaler`.

#### Engenharia de Atributos *(Opcional)*

Criar novas variáveis que possam melhorar futuras modelagens, por exemplo:

- Agrupamento por faixas etárias;
- Categorização das horas trabalhadas;
- Outras transformações relevantes.

---

## Entregáveis

Ao final da atividade, deverá ser entregue um notebook **`.ipynb`** contendo:

- Código comentado;
- Visualizações gráficas;
- Análises e interpretações dos resultados;
- Explicação das decisões tomadas durante o pré-processamento.

---

## Resumo Final

O notebook deverá apresentar uma conclusão contendo:

- Principais descobertas obtidas na análise exploratória;
- Estratégias utilizadas na preparação dos dados;
- Limitações identificadas;
- Sugestões para futuras etapas de modelagem em Machine Learning.

---

## Objetivo Final

Preparar o dataset **Adult Census Income** para aplicações de Machine Learning, garantindo que os dados estejam limpos, organizados e adequadamente transformados, além de proporcionar uma compreensão aprofundada das características do conjunto de dados antes da construção de modelos preditivos.s