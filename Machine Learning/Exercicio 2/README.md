# Tarefa: Prevendo Custos Médicos com Regressão

## Objetivo

Desenvolver modelos de **Aprendizado Supervisionado** para estimar o valor do seguro de saúde (**`charges`**) utilizando informações dos clientes, como idade, índice de massa corporal (IMC), número de filhos, tabagismo, sexo e região.

O projeto utiliza o dataset **`custo_medico.csv`**, disponibilizado no Portal do Aluno.

---

## Dataset

O conjunto de dados contém informações demográficas e de saúde dos clientes, sendo utilizado para prever o custo individual do seguro médico.

As principais variáveis são:

- **age** — Idade do cliente;
- **sex** — Sexo;
- **bmi** — Índice de Massa Corporal (IMC);
- **children** — Número de filhos/dependentes;
- **smoker** — Indica se o cliente é fumante;
- **region** — Região de residência;
- **charges** — Valor do seguro de saúde *(variável alvo)*.

---

## Etapas da Atividade

### 1. Exploração Inicial

Realizar a importação e inspeção do conjunto de dados utilizando a biblioteca **Pandas**.

Nesta etapa deverão ser executadas as seguintes atividades:

- Carregar o dataset;
- Visualizar as primeiras linhas utilizando `head()`;
- Obter informações gerais com `info()`;
- Gerar estatísticas descritivas com `describe()`.

Responder às seguintes questões:

- Quais variáveis são numéricas?
- Quais variáveis são categóricas?
- Qual será a variável dependente (**y**)?

---

### 2. Análise Exploratória de Dados (EDA)

Investigar a relação entre as variáveis explicativas e o custo do seguro.

As análises devem incluir:

- Gráfico de dispersão entre **idade (age)** e **charges**;
- Gráfico de dispersão entre **IMC (bmi)** e **charges**;
- Boxplots comparando os custos entre fumantes e não fumantes.

Responder às seguintes questões:

- O tabagismo parece influenciar os custos médicos?
- Existe uma relação clara entre idade e valor do seguro?

---

### 3. Pré-processamento

Preparar os dados para treinamento dos modelos.

As etapas incluem:

- Transformar as variáveis categóricas (`sex`, `smoker` e `region`) em variáveis numéricas utilizando:
  - `OneHotEncoder`; ou
  - `pd.get_dummies()`.
- Dividir os dados em:
  - **80%** para treinamento;
  - **20%** para teste.

---

### 4. Modelagem

Desenvolver e comparar diferentes algoritmos de regressão.

Os modelos sugeridos são:

- Regressão Linear;
- Ridge Regression ou Lasso Regression;
- Random Forest Regressor;
- XGBoost Regressor.

---

### 5. Avaliação dos Modelos

Avaliar o desempenho dos modelos utilizando as seguintes métricas:

- **MAE (Mean Absolute Error)** — Erro Absoluto Médio;
- **RMSE (Root Mean Squared Error)** — Raiz do Erro Quadrático Médio;
- **R² (Coeficiente de Determinação)**.

Também deverá ser realizada uma comparação entre os modelos desenvolvidos.

---

### 6. Reflexão

Ao final do projeto, responder às seguintes questões:

- Qual modelo apresentou o melhor desempenho?
- O tabagismo foi realmente um fator determinante para os custos médicos?
- Quais limitações podem ser identificadas na solução desenvolvida?

---

## Entregáveis

O notebook **`.ipynb`** deverá conter:

- Importação e descrição do dataset;
- Análise exploratória com gráficos;
- Pré-processamento dos dados;
- Implementação dos modelos de regressão;
- Avaliação utilizando métricas de desempenho;
- Comparação entre os modelos;
- Respostas às questões propostas;
- Discussão dos resultados e limitações.

---

## Objetivo Final

Construir modelos de regressão capazes de prever os custos médicos de clientes com base em características demográficas e de saúde, avaliando diferentes algoritmos de Machine Learning e identificando os fatores que mais influenciam o valor do seguro.