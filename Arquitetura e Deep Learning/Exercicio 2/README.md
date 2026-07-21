# Classificação de Imagens Territoriais com CNNs

## Contexto de Negócio

Uma empresa especializada em monitoramento territorial, logística, infraestrutura e planejamento urbano recebe diariamente imagens capturadas por drones, satélites e câmeras em campo.

O objetivo é automatizar a classificação dessas imagens para agilizar a análise e apoiar a tomada de decisões em diferentes áreas de atuação.

Entre as principais aplicações estão:

- Identificação de áreas urbanizadas;
- Mapeamento de regiões naturais;
- Apoio ao planejamento de rotas;
- Classificação de imagens para relatórios ambientais;
- Priorização de inspeções em regiões específicas.

Neste projeto, será desenvolvida uma **Rede Neural Convolucional (CNN)** para classificar imagens em diferentes categorias geográficas.

---

## Dataset Utilizado

O projeto utiliza o conjunto de dados **Intel Image Classification**, disponível no Kaggle.

**Dataset:**

https://www.kaggle.com/datasets/puneet6060/intel-image-classification

O dataset é composto pelas seguintes classes:

- Buildings
- Forest
- Glacier
- Mountain
- Sea
- Street

Cada imagem pertence exclusivamente a uma dessas seis categorias, caracterizando um problema de **classificação multiclasse**.

---

## Objetivo Técnico

O principal objetivo é desenvolver e comparar o desempenho de dois modelos de Redes Neurais Convolucionais:

### CNN Simples

Modelo base contendo apenas camadas convolucionais, funções de ativação e camadas de pooling, sem técnicas explícitas de regularização.

### CNN Regularizada

Modelo aprimorado utilizando técnicas para melhorar a capacidade de generalização da rede:

- Batch Normalization;
- Dropout.

---

## Problema de Classificação

**Entrada:** Imagens de ambientes terrestres.

**Saída:** Uma das seguintes classes:

- Buildings
- Forest
- Glacier
- Mountain
- Sea
- Street

---

## Objetivos da Prática

Ao final desta atividade, espera-se ser capaz de:

- Carregar e preparar um dataset de imagens para Deep Learning;
- Construir uma CNN para classificação multiclasse;
- Aplicar técnicas de regularização utilizando **Batch Normalization** e **Dropout**;
- Comparar o desempenho entre uma CNN simples e uma CNN regularizada;
- Avaliar os modelos utilizando métricas de classificação e curvas de treinamento;
- Identificar sinais de **overfitting** e **underfitting**.

---

## Objetivo Final

Desenvolver um modelo de Deep Learning capaz de classificar automaticamente imagens territoriais com alta precisão, auxiliando processos de monitoramento ambiental, planejamento urbano, logística e infraestrutura.