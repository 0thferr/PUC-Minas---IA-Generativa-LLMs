# Tarefa 5 – Otimização de Hiperparâmetros com Grid Search CV

## Objetivo

Aprimorar o desempenho dos modelos de classificação desenvolvidos na **Tarefa 4** por meio da otimização de hiperparâmetros utilizando a técnica de **Grid Search com Validação Cruzada (GridSearchCV)**.

O objetivo é identificar a melhor combinação de hiperparâmetros para maximizar o desempenho do algoritmo escolhido, utilizando validação cruzada para obter resultados mais confiáveis e reduzir o risco de sobreajuste (*overfitting*).

---

## Dataset

Utilize a mesma base de dados empregada na **Tarefa 4**, mantendo o mesmo notebook como ponto de partida.

As bases disponíveis são:

| Base de Dados | Descrição |
|---------------|-----------|
| **Bank Marketing** | Dados de campanhas de marketing realizadas por uma instituição bancária. |
| **dados_risco_credito.csv** | Base simulada contendo informações relacionadas ao risco de crédito de clientes. |

---

## Etapas da Atividade

### 1. Revisão do Modelo

Nesta etapa, deverá ser reutilizado o modelo desenvolvido na atividade anterior.

As atividades incluem:

- Carregar o notebook da **Tarefa 4**;
- Selecionar um dos algoritmos previamente treinados;
- Definir qual modelo será submetido ao processo de otimização.

---

### 2. Definição dos Hiperparâmetros

Criar um dicionário contendo os hiperparâmetros que serão avaliados durante a busca.

Exemplos de parâmetros para cada algoritmo:

#### Regressão Logística

- `C`
- `penalty`
- `solver`

#### Gaussian Naive Bayes

- `var_smoothing`

#### Redes Neurais (MLPClassifier)

- `hidden_layer_sizes`
- `activation`
- `solver`
- `alpha`

Os valores escolhidos deverão representar diferentes configurações para comparação.

---

### 3. Aplicação do GridSearchCV

Utilizar a classe **GridSearchCV**, disponível no módulo `sklearn.model_selection`.

Configurar os seguintes elementos:

- Modelo base;
- Dicionário de hiperparâmetros;
- Métrica de avaliação (por exemplo, `accuracy` ou `f1`);
- Número de partições da validação cruzada (ex.: `cv = 5`).

Após a execução da busca, registrar:

- Melhor combinação de hiperparâmetros;
- Melhor desempenho obtido durante a validação cruzada.

---

### 4. Avaliação do Modelo Otimizado

Treinar novamente o modelo utilizando os melhores hiperparâmetros encontrados.

Avaliar o desempenho utilizando as seguintes métricas:

- **Acurácia (Accuracy)**
- **Precisão (Precision)**
- **Recall**
- **F1-Score**
- **Matriz de Confusão**

Em seguida, comparar esses resultados com aqueles obtidos na **Tarefa 4**, verificando se houve melhoria no desempenho.

---

### 5. Conclusão

Realizar uma análise crítica sobre os resultados obtidos.

A discussão deverá abordar:

- Ganhos de desempenho após a otimização;
- Influência dos hiperparâmetros no comportamento do modelo;
- Vantagens e limitações da utilização do **GridSearchCV**;
- Considerações sobre possíveis otimizações futuras.

---

## Entregáveis

O aluno deverá entregar um notebook **`.ipynb`** contendo:

- Nome completo no início do notebook;
- Código comentado;
- Implementação do **GridSearchCV**;
- Tabela com os melhores hiperparâmetros encontrados;
- Comparação entre o modelo original e o modelo otimizado;
- Gráficos e visualizações dos resultados;
- Análise escrita e interpretação dos resultados.

---

## Estrutura Recomendada do Notebook

1. Identificação do aluno;
2. Revisão do modelo desenvolvido na Tarefa 4;
3. Definição dos hiperparâmetros;
4. Configuração do GridSearchCV;
5. Treinamento e otimização;
6. Avaliação do modelo otimizado;
7. Comparação entre os resultados;
8. Conclusão e sugestões de melhorias.

---

## Objetivo Final

Otimizar um modelo de classificação supervisionada utilizando **Grid Search com Validação Cruzada**, identificando a melhor combinação de hiperparâmetros para aumentar sua capacidade preditiva e comparando seu desempenho com o modelo originalmente desenvolvido.