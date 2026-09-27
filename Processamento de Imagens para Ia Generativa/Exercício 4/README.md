# Classificação de Flores com CNNs e Vision Transformers

**Disciplina:** Processamento de Imagem para IA Generativa

## Contexto do problema

Uma empresa de floricultura e comércio eletrônico deseja automatizar parte do processo de **catalogação de espécies de flores** recebidas de diferentes fornecedores.

Atualmente, a identificação das espécies depende de inspeção humana, o que pode gerar inconsistências, retrabalho e dificuldades de escalabilidade à medida que o volume de imagens aumenta.

Nesta atividade, serão comparadas duas estratégias de classificação de imagens:

1. Uma arquitetura **CNN pré-treinada**;
2. Uma arquitetura **Vision Transformer pré-treinada**.

O objetivo é avaliar qual abordagem apresenta o melhor equilíbrio entre desempenho, capacidade de generalização, custo computacional, complexidade do modelo e tempo necessário para o fine-tuning.

---

## Dataset utilizado

Será utilizado o dataset público **Oxford Flowers 102**, disponível por meio do `torchvision`.

A base contém imagens de **102 categorias de flores**, apresentando variações reais relacionadas a:

* Iluminação;
* Escala;
* Enquadramento;
* Fundo;
* Posição;
* Aparência visual.

O problema será tratado como uma tarefa de **classificação multiclasse de imagens**.

---

## Objetivos da prática

Ao final da atividade, espera-se que seja possível:

* Carregar e explorar um dataset real de imagens;
* Preparar imagens para arquiteturas pré-treinadas;
* Aplicar Transfer Learning em uma CNN;
* Aplicar Transfer Learning em um Vision Transformer;
* Compreender o papel dos patches e do mecanismo de atenção no ViT;
* Avaliar os modelos utilizando Accuracy e F1-score;
* Analisar sinais de overfitting e underfitting;
* Comparar o desempenho e o custo computacional dos modelos;
* Recomendar a arquitetura mais adequada para o problema.

---

## Arquiteturas utilizadas

### CNN pré-treinada

A primeira abordagem utiliza uma **Convolutional Neural Network (CNN)** pré-treinada.

As CNNs são especialmente eficientes para o processamento de imagens, pois utilizam convoluções para identificar características visuais, como:

* Bordas;
* Texturas;
* Formas;
* Padrões;
* Estruturas mais complexas.

Será utilizada uma arquitetura pré-treinada com pesos aprendidos anteriormente no ImageNet e adaptada para a classificação das 102 espécies de flores.

### Vision Transformer

A segunda abordagem utiliza um **Vision Transformer (ViT)** pré-treinado.

Diferentemente das CNNs, o ViT divide a imagem em pequenos blocos chamados **patches**. Cada patch é transformado em uma representação vetorial, que é processada pelo mecanismo de **self-attention**.

Esse mecanismo permite que o modelo aprenda relações entre diferentes regiões da imagem, inclusive regiões distantes entre si.

---

## Fluxo da atividade

O fluxo geral do projeto será:

```text
Dataset Oxford Flowers 102
          ↓
Exploração e visualização das imagens
          ↓
Pré-processamento e Data Augmentation
          ↓
Transfer Learning com CNN
          ↓
Treinamento e avaliação da CNN
          ↓
Transfer Learning com Vision Transformer
          ↓
Treinamento e avaliação do ViT
          ↓
Comparação dos resultados
          ↓
Análise de desempenho e generalização
          ↓
Recomendação da melhor arquitetura
```

---

## Métricas de avaliação

Os modelos serão avaliados utilizando principalmente:

### Accuracy

A Accuracy representa a proporção de previsões realizadas corretamente pelo modelo.

```text
Accuracy = número de previsões corretas / número total de previsões
```

### F1-score Macro

O F1-score combina Precision e Recall em uma única métrica.

O F1-score Macro calcula o F1-score para cada classe e realiza uma média entre elas, atribuindo a mesma importância para todas as 102 categorias.

Essa métrica é útil para avaliar o desempenho geral do modelo em um problema multiclasse.

---

## Análise de overfitting e underfitting

Durante o treinamento, serão analisadas as curvas de:

* Loss de treino;
* Loss de validação;
* Accuracy de treino;
* Accuracy de validação;
* F1-score de treino;
* F1-score de validação.

### Overfitting

Pode ocorrer quando o modelo aprende muito bem os dados de treinamento, mas apresenta pior desempenho em dados que não foram vistos anteriormente.

Um possível sinal é:

```text
Accuracy de treino alta
        ↓
Accuracy de validação significativamente menor
```

### Underfitting

Pode ocorrer quando o modelo não consegue aprender adequadamente os padrões presentes nos dados.

Um possível sinal é:

```text
Accuracy de treino baixa
        ↓
Accuracy de validação também baixa
```

---

## Comparação entre os modelos

A comparação final considerará os seguintes critérios:

| Critério             | CNN                                           | Vision Transformer                            |
| -------------------- | --------------------------------------------- | --------------------------------------------- |
| Accuracy             | Avaliada no conjunto de teste                 | Avaliada no conjunto de teste                 |
| F1-score Macro       | Avaliado no conjunto de teste                 | Avaliado no conjunto de teste                 |
| Generalização        | Analisada pelas curvas de treino e validação  | Analisada pelas curvas de treino e validação  |
| Tempo de treinamento | Medido durante o fine-tuning                  | Medido durante o fine-tuning                  |
| Complexidade         | Baseada na arquitetura e número de parâmetros | Baseada na arquitetura e número de parâmetros |
| Custo computacional  | Comparado durante a execução                  | Comparado durante a execução                  |

---

## Tecnologias utilizadas

O projeto utiliza as seguintes bibliotecas:

* Python;
* PyTorch;
* Torchvision;
* NumPy;
* Pandas;
* Matplotlib;
* Seaborn;
* Scikit-learn;
* TQDM.

---

## Estrutura esperada do notebook

```text
1. Introdução
2. Importação das bibliotecas
3. Configuração do ambiente
4. Carregamento do Oxford Flowers 102
5. Exploração visual do dataset
6. Pré-processamento das imagens
7. Criação dos DataLoaders
8. CNN pré-treinada
9. Treinamento da CNN
10. Avaliação da CNN
11. Curvas de treinamento
12. Vision Transformer pré-treinado
13. Explicação sobre patches e atenção
14. Treinamento do ViT
15. Avaliação do ViT
16. Matrizes de confusão
17. Comparação entre os modelos
18. Análise de overfitting e underfitting
19. Conclusão
20. Recomendação da arquitetura
```

---

## Resultado esperado

Ao final da prática, será possível identificar qual das duas arquiteturas apresentou o melhor resultado para a classificação das espécies de flores.

A recomendação final deverá considerar não apenas a métrica de desempenho, mas também aspectos práticos, como:

* Capacidade de generalização;
* Tempo de treinamento;
* Número de parâmetros;
* Custo computacional;
* Complexidade de manutenção;
* Viabilidade de utilização em um ambiente real de comércio eletrônico.

A arquitetura escolhida deverá representar o melhor equilíbrio entre **qualidade da classificação e custo operacional**.
