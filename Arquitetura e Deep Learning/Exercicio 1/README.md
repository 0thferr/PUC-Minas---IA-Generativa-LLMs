# Predição de Churn com Redes Neurais (MLP)

## Contexto do Problema

Uma empresa de telecomunicações deseja reduzir o cancelamento de clientes (*churn*). Para isso, a equipe de Ciência de Dados foi encarregada de desenvolver um modelo capaz de identificar clientes com maior probabilidade de cancelar seus serviços.

Nesta atividade, será treinada uma Rede Neural Multicamadas (**MLP - Multilayer Perceptron**) para prever se um cliente permanecerá ou cancelará seu contrato.

---

## Dataset Utilizado

O projeto utiliza o conjunto de dados público **IBM Telco Customer Churn**, disponível em:

**Dataset:**
https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv

O dataset contém informações sobre os clientes, incluindo:

- Perfil do cliente;
- Tipo de contrato;
- Serviços contratados;
- Valores pagos;
- Tempo de relacionamento com a empresa;
- Status de churn (cancelamento).

---

## Objetivos da Prática

Ao final desta atividade, espera-se que seja possível:

- Carregar e explorar um conjunto de dados de negócio;
- Preparar atributos categóricos e numéricos para utilização em Redes Neurais;
- Treinar uma Rede Neural MLP para classificação binária;
- Avaliar o desempenho do modelo utilizando métricas apropriadas;
- Identificar possíveis sinais de **overfitting** e **underfitting** durante o treinamento.

---

## Problema de Classificação

**Entrada:** Informações cadastrais e contratuais dos clientes.

**Saída:**

- **0** → Cliente permanece na empresa.
- **1** → Cliente cancela o serviço (*Churn*).

---

## Objetivo Final

Desenvolver um modelo de Deep Learning capaz de prever, com boa precisão, quais clientes apresentam maior probabilidade de cancelar seus serviços, permitindo que a empresa adote estratégias preventivas de retenção.