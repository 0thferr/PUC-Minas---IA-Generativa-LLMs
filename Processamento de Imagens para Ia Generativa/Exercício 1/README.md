# Classificação de Dígitos Manuscritos com Redes Neurais MLP

## 📌 Sobre o Projeto

Este projeto apresenta uma aplicação prática de **Machine Learning / Deep Learning** utilizando uma rede neural **MLP (Multi-Layer Perceptron)** para realizar a classificação automática de dígitos manuscritos.

O objetivo é desenvolver um modelo capaz de identificar números de **0 a 9** a partir de imagens em escala de cinza, utilizando o dataset **MNIST** disponibilizado pela biblioteca **TensorFlow/Keras**.

A atividade permite compreender como imagens são convertidas em dados numéricos e como uma rede neural aprende padrões visuais por meio do treinamento supervisionado.

---

## 📂 Dataset Utilizado

O projeto utiliza o dataset público **MNIST (Modified National Institute of Standards and Technology database)**.

A base contém imagens de dígitos manuscritos com as seguintes características:

- **Quantidade de classes:** 10 (dígitos de 0 a 9);
- **Formato das imagens:** 28 × 28 pixels;
- **Tipo de imagem:** escala de cinza;
- **Representação:** matriz numérica contendo valores de intensidade dos pixels;
- **Dados disponíveis:**
  - 60.000 imagens para treinamento;
  - 10.000 imagens para teste.

Cada imagem é representada por uma matriz de pixels, onde os valores variam entre 0 e 255, indicando a intensidade da cor em escala de cinza.

---

## 🎯 Objetivos

Ao desenvolver este projeto, os seguintes conceitos serão aplicados:

- Carregamento e exploração de um dataset de imagens;
- Visualização e interpretação de imagens como matrizes numéricas;
- Pré-processamento dos dados;
- Normalização dos valores dos pixels;
- Construção de uma rede neural MLP;
- Classificação multiclasse utilizando redes neurais;
- Treinamento utilizando:
  - Forward Propagation;
  - Função de perda;
  - Backpropagation;
  - Algoritmos de otimização;
- Avaliação do modelo utilizando dados não vistos;
- Análise de erros e previsões incorretas;
- Identificação de problemas como:
  - Overfitting;
  - Underfitting;
- Discussão das limitações de redes MLP em tarefas envolvendo imagens.

---

## 🧠 Modelo Utilizado

A arquitetura utilizada é uma **Multi-Layer Perceptron (MLP)**.

Como a MLP trabalha com dados vetoriais, as imagens de entrada precisam ser transformadas:
