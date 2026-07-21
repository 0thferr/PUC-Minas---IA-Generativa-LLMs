# Atividade Prática – Unidade 3: Modelagem e Avaliação de Classificadores

## Objetivo

Aplicar algoritmos de **Classificação Supervisionada** para prever a renda dos indivíduos utilizando o dataset **Adult Census Income**.

O objetivo é treinar diferentes modelos de classificação, comparar seus desempenhos por meio de métricas de avaliação e justificar tecnicamente a escolha do modelo mais adequado para o problema.

---

## Dataset

O projeto utiliza o conjunto de dados **Adult Census Income**, previamente tratado na **Tarefa 1 – EDA e Preparação de Dados**.

**Fonte oficial:**

https://archive.ics.uci.edu/dataset/2/adult

**Arquivos utilizados:**

- Dataset: `adult.data.txt`
- Notebook base: `tarefa_1_eda.ipynb`

> **Importante:** Utilize a versão do dataset já limpa e preparada na atividade anterior, revisando o notebook de EDA caso seja necessário.

---

## Etapas da Atividade

### 1. Preparação do Ambiente

Inicialmente, deverão ser importadas as bibliotecas necessárias para manipulação dos dados, visualização e construção dos modelos.

Bibliotecas recomendadas:

- Pandas;
- NumPy;
- Matplotlib;
- Seaborn;
- Scikit-learn.

Em seguida:

- Carregar o dataset previamente tratado;
- Verificar se todas as variáveis estão prontas para modelagem.

---

### 2. Separação dos Dados

Preparar os dados para treinamento dos modelos.

As etapas incluem:

- Separar as variáveis preditoras (**X**);
- Definir a variável alvo (**y**), correspondente à renda (`income`);
- Dividir os dados em:
  - **70%** para treinamento;
  - **30%** para teste.

---

### 3. Aplicação dos Algoritmos de Classificação

Selecionar entre **2 e 3 algoritmos** estudados durante a disciplina.

Modelos sugeridos:

- **K-Nearest Neighbors (KNN)**
- **Support Vector Machine (SVM)**
- **Decision Tree (Árvore de Decisão)**

Para cada algoritmo, realizar as seguintes etapas:

- Treinar o modelo utilizando o conjunto de treinamento;
- Realizar previsões no conjunto de teste;
- Avaliar o desempenho utilizando métricas de classificação.

---

## Avaliação dos Modelos

Cada classificador deverá ser avaliado utilizando as seguintes métricas:

- **Acurácia (Accuracy)**
- **Precisão (Precision)**
- **Recall (Sensibilidade)**
- **F1-Score**
- **Curva ROC**
- **AUC (Área sob a Curva ROC)**

Ferramentas recomendadas do **Scikit-learn**:

- `classification_report`
- `confusion_matrix`
- `roc_curve`
- `auc`

---

## Comparação e Discussão

Após o treinamento dos modelos, realizar uma análise comparativa considerando:

- Desempenho obtido em cada métrica;
- Vantagens e limitações de cada algoritmo;
- Capacidade de generalização;
- Facilidade de interpretação dos resultados.

Ao final, justificar tecnicamente qual modelo apresentou o melhor desempenho para o problema proposto.

---

## Entregáveis

O notebook **`.ipynb`** deverá conter:

- Código organizado e comentado;
- Preparação dos dados;
- Implementação dos modelos de classificação;
- Avaliação utilizando métricas apropriadas;
- Matrizes de confusão;
- Curvas ROC;
- Gráficos comparativos;
- Tabelas com os resultados obtidos;
- Discussão dos resultados.

---

## Resumo Final

O trabalho deverá apresentar uma conclusão contendo:

- Justificativa para a escolha dos algoritmos utilizados;
- Interpretação das métricas de avaliação;
- Comparação entre os modelos;
- Identificação do classificador com melhor desempenho;
- Considerações sobre possíveis melhorias e trabalhos futuros.

---

## Objetivo Final

Desenvolver e comparar modelos de classificação supervisionada capazes de prever a renda dos indivíduos utilizando o dataset **Adult Census Income**, analisando seu desempenho por meio de métricas estatísticas e identificando a abordagem mais adequada para o problema de classificação.