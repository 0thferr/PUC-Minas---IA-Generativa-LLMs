# Central Inteligente de Atendimento com LLMs e LoRA

## Contexto de Negócio

Uma empresa recebe diariamente centenas de reclamações de clientes por diferentes canais de atendimento, como formulários online, e-mails, chats, redes sociais e central telefônica.

Para otimizar o processo de triagem e reduzir o tempo de resposta, a empresa pretende utilizar Inteligência Artificial Generativa baseada em **Large Language Models (LLMs)**.

A solução deverá auxiliar a equipe de atendimento nas seguintes tarefas:

- Classificar automaticamente o tipo da reclamação;
- Identificar o produto ou serviço mencionado;
- Estimar o nível de urgência da solicitação;
- Extrair o principal problema relatado pelo cliente;
- Gerar uma resposta inicial para o atendimento;
- Adaptar o comportamento do modelo por meio de **LoRA (Low-Rank Adaptation)**.

---

## Dataset Utilizado

O projeto utiliza uma base pública de reclamações de consumidores disponível no **Hugging Face**, derivada das reclamações do **Consumer Financial Protection Bureau (CFPB)**.

**Dataset:**

https://huggingface.co/datasets/claritystorm/cfpb-consumer-complaints

O conjunto de dados contém relatos reais de consumidores sobre produtos e serviços financeiros, sendo adequado para tarefas de Processamento de Linguagem Natural (PLN) e ajuste fino de modelos de linguagem.

---

## Modelo Utilizado

O modelo recomendado para o projeto é:

- **Qwen2.5-0.5B-Instruct**

Esse modelo será utilizado tanto para inferência quanto para o processo de **fine-tuning** utilizando a técnica **LoRA**, permitindo adaptar o modelo à tarefa com menor custo computacional.

---

## Objetivo Técnico

Desenvolver uma solução baseada em **Large Language Models (LLMs)** capaz de:

- Ler uma reclamação textual real;
- Classificar automaticamente sua categoria principal;
- Extrair informações relevantes do texto;
- Gerar uma resposta inicial ao cliente;
- Construir um dataset no formato instrucional;
- Realizar o fine-tuning generativo utilizando **LoRA**;
- Comparar o desempenho do modelo antes e depois do ajuste fino.

---

## Fluxo da Solução

1. Recebimento da reclamação do cliente;
2. Pré-processamento do texto;
3. Classificação da categoria da reclamação;
4. Extração das principais informações;
5. Geração automática de uma resposta inicial;
6. Fine-tuning do modelo utilizando LoRA;
7. Comparação entre o modelo original e o modelo ajustado.

---

## Objetivos da Prática

Ao final desta atividade, espera-se ser capaz de:

- Trabalhar com um dataset textual real;
- Preparar dados para modelos de linguagem;
- Criar instruções (*instruction tuning*) para treinamento;
- Utilizar um LLM para tarefas de classificação e geração de texto;
- Aplicar **LoRA** para realizar fine-tuning eficiente;
- Comparar qualitativamente e quantitativamente os resultados antes e depois do ajuste fino.

---

## Tecnologias Utilizadas

- Python
- Hugging Face Datasets
- Transformers
- PEFT (Parameter-Efficient Fine-Tuning)
- LoRA (Low-Rank Adaptation)
- PyTorch
- Qwen2.5-0.5B-Instruct

---

## Objetivo Final

Desenvolver uma solução inteligente de atendimento capaz de automatizar a triagem inicial de reclamações, extrair informações relevantes e gerar respostas contextualizadas, utilizando um Large Language Model adaptado por meio da técnica **LoRA**, reduzindo custos computacionais e aumentando a eficiência do atendimento ao cliente.