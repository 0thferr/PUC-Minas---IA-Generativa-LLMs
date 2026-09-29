# Inspeção Visual de Defeitos em Peças Industriais com CNNs e Transfer Learning

## 📖 Contexto do Problema

Uma indústria de componentes metálicos deseja automatizar parte do processo de inspeção de qualidade realizado ao final da linha de produção. 

Atualmente, operadores verificam visualmente as peças para identificar possíveis defeitos de fabricação. Esse processo manual apresenta alguns desafios para o negócio:
* Pode ser muito demorado;
* Apresenta variação de critérios entre diferentes avaliadores;
* Torna-se difícil de escalar com o aumento do volume de produção.

Para solucionar essas dores, este projeto visa desenvolver um modelo de **Visão Computacional** capaz de classificar automaticamente imagens de peças em duas categorias:
* 🔴 **Peça com defeito**
* 🟢 **Peça sem defeito**

Para encontrar a melhor abordagem técnica, serão implementadas e comparadas três estratégias de modelagem:
1. Uma **CNN** (Rede Neural Convolucional) desenhada e treinada do zero.
2. **Feature Extraction** utilizando um modelo de Deep Learning pré-treinado.
3. **Fine-tuning** de um modelo pré-treinado.

---

## 📊 Dataset Utilizado

Será utilizado o dataset público **Casting Product Image Data for Quality Inspection**, disponibilizado no Kaggle. 

O conjunto contém imagens reais de componentes produzidos por fundição e foi criado com o propósito de apoiar a automação da inspeção de qualidade industrial. As imagens estão organizadas em duas categorias:

* `def_front`: Peças com defeito detectado na parte frontal.
* `ok_front`: Peças consideradas adequadas (sem defeito).

O dataset já disponibiliza os conjuntos separados em diretórios de treinamento e teste.

🔗 **Fonte:** [Kaggle — ravirajsinh45/real-life-industrial-dataset-of-casting-product](https://www.kaggle.com/datasets/ravirajsinh45/real-life-industrial-dataset-of-casting-product)

---

## 🎯 Objetivos da Prática

Ao final desta atividade, o projeto deve demonstrar a capacidade de:

- [x] Carregar e explorar um dataset de imagens associado a um problema real de negócio.
- [x] Preparar imagens para o treinamento de redes neurais.
- [x] Aplicar técnicas de normalização e *Data Augmentation*.
- [x] Construir uma CNN para classificação binária.
- [x] Interpretar convolução, *pooling* e extração hierárquica de características.
- [x] Avaliar o modelo através de métricas adequadas: *Accuracy, Precision, Recall, F1-score* e Matriz de Confusão.
- [x] Analisar criticamente o impacto prático de **falsos positivos** e **falsos negativos** no contexto de qualidade industrial.
- [x] Aplicar *Transfer Learning* utilizando um modelo pré-treinado.
- [x] Diferenciar, na prática, as estratégias de *Feature Extraction* e *Fine-tuning*.
- [x] Comparar os resultados das três estratégias e recomendar a solução mais viável e segura para o problema de negócio.

---

## 🛠️ Tecnologias e Técnicas Abordadas

* **Deep Learning & Visão Computacional:** Redes Neurais Convolucionais (CNNs)
* **Otimização:** Transfer Learning (Feature Extraction e Fine-Tuning)
* **Pré-processamento:** Escalonamento/Normalização de imagens e Data Augmentation
* **Métricas de Avaliação:** Matriz de Confusão, Acurácia, Precisão, Revocação (Recall) e F1-Score