# Previsão de Demanda em Mobilidade Urbana com RNNs

## Contexto de Negócio

Uma empresa de mobilidade urbana opera um sistema de bicicletas compartilhadas em uma grande cidade e precisa prever a demanda de aluguel nas próximas horas para otimizar suas operações.

A previsão da demanda permite melhorar a eficiência operacional e a qualidade do serviço oferecido aos usuários.

As principais aplicações incluem:

- Reposicionamento de bicicletas entre estações;
- Planejamento das equipes de manutenção e redistribuição;
- Antecipação de horários de maior demanda;
- Melhoria da disponibilidade das bicicletas;
- Redução de estações vazias ou superlotadas;
- Apoio à tomada de decisões utilizando informações climáticas e temporais.

Neste projeto, serão desenvolvidos modelos de **Redes Neurais Recorrentes (RNNs)** para prever a demanda futura com base no histórico de utilização e em variáveis contextuais.

---

## Dataset Utilizado

O projeto utiliza o **Bike Sharing Dataset**, disponibilizado pelo **UCI Machine Learning Repository** e disponível no Kaggle.

**Dataset:**

https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset

O conjunto de dados contém registros horários de aluguel de bicicletas, incluindo informações como:

- Data e hora;
- Estação do ano;
- Ano;
- Mês;
- Hora do dia;
- Feriado;
- Dia da semana;
- Dia útil;
- Condições climáticas;
- Temperatura;
- Sensação térmica;
- Umidade;
- Velocidade do vento;
- Quantidade total de bicicletas alugadas.

---

## Objetivo Técnico

O objetivo é desenvolver e comparar três arquiteturas de Redes Neurais Recorrentes para previsão de séries temporais:

- **SimpleRNN**
- **LSTM (Long Short-Term Memory)**
- **GRU (Gated Recurrent Unit)**

Todos os modelos deverão resolver o mesmo problema:

> **Prever a quantidade total de bicicletas alugadas na próxima hora.**

---

## Problema de Regressão

**Entrada:** Sequências temporais contendo informações históricas da demanda e variáveis contextuais.

**Saída:** Quantidade prevista de bicicletas alugadas na próxima hora.

---

## Objetivos da Prática

Ao final desta atividade, espera-se ser capaz de:

- Explorar e visualizar uma série temporal;
- Preparar dados para modelos recorrentes;
- Construir janelas temporais (*time windows*);
- Treinar modelos **SimpleRNN**, **LSTM** e **GRU**;
- Comparar o desempenho entre diferentes arquiteturas recorrentes;
- Avaliar os modelos utilizando métricas de regressão;
- Analisar a capacidade de previsão dos modelos em dados reais.

---

## Entregáveis

Ao final do projeto, deverão ser apresentados os seguintes itens:

- Visualização inicial da série temporal;
- Explicação do pré-processamento dos dados;
- Construção das janelas temporais;
- Treinamento dos três modelos recorrentes;
- Comparação das métricas de desempenho;
- Gráfico comparando os valores **Reais × Previstos**.

---

## Objetivo Final

Desenvolver modelos de Deep Learning capazes de prever a demanda horária de bicicletas compartilhadas com alta precisão, fornecendo suporte à gestão operacional, ao planejamento logístico e à melhoria da disponibilidade do serviço.