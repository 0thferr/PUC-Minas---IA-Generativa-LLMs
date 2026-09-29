# Assistente Acadêmico Inteligente — RNNs, Transformers, RAG e GenAI

Projeto final da disciplina de **Redes Neurais Recorrentes e Transformadores**, desenvolvido durante a pós-graduação em **IA Generativa e Aplicações com LLMs — PUC Minas**.

O projeto apresenta uma evolução prática dos principais conceitos estudados na disciplina, partindo do processamento básico de textos e redes neurais sequenciais até uma proposta de aplicação de **GenAI para atendimento acadêmico**, combinando classificação, recuperação de contexto com RAG, geração de respostas estruturadas, guardrails e human-in-the-loop.

> O notebook foi desenvolvido com foco didático, utilizando dados sintéticos e implementações simplificadas para demonstrar os conceitos.

## Objetivo

Construir um trabalho integrador capaz de demonstrar, de forma progressiva, como diferentes arquiteturas e técnicas podem ser utilizadas no processamento de linguagem natural.

O projeto percorre o seguinte caminho:

```text
Texto
  ↓
Tokenização
  ↓
Bag of Words
  ↓
RNN
  ↓
LSTM / GRU
  ↓
Attention
  ↓
Self-Attention
  ↓
Transformers
  ↓
LLMs
  ↓
RAG
  ↓
GenAI
  ↓
Assistente Acadêmico Inteligente
```

O objetivo não é apenas implementar os modelos, mas compreender suas características, limitações e possibilidades de aplicação em sistemas reais.

## Conteúdo do projeto

O notebook está dividido em cinco grandes etapas.

### 1. Redes Neurais Recorrentes

A primeira etapa apresenta o processamento de textos como sequências e implementa uma abordagem progressiva:

* Normalização de textos;
* Tokenização;
* Construção de vocabulário;
* `<PAD>` e `<UNK>`;
* Conversão de textos para sequências numéricas;
* Tensores com PyTorch;
* Bag of Words;
* Rede neural simples;
* Embeddings;
* RNN;
* LSTM;
* GRU;
* Treinamento e validação;
* Análise de limitações das RNNs;
* Vanishing gradients;
* Exploding gradients.

Também são realizadas comparações entre abordagens que ignoram a ordem das palavras e modelos capazes de trabalhar com sequências.

## 2. Attention e Self-Attention

A segunda etapa introduz o mecanismo de atenção, utilizado para permitir que o modelo atribua diferentes níveis de importância aos elementos de uma sequência.

São explorados conceitos como:

* Attention;
* Query;
* Key;
* Value;
* Pesos de atenção;
* Self-Attention;
* Matriz de atenção;
* Visualização da atenção;
* Relação entre atenção e processamento de sequências.

Essa etapa prepara a transição conceitual das arquiteturas recorrentes para os Transformers.

## 3. Transformers e LLMs

A terceira etapa apresenta a arquitetura Transformer e sua importância para os modelos modernos de linguagem.

São abordados:

* Arquitetura Transformer;
* Encoder;
* Decoder;
* Encoder-Decoder;
* Self-Attention;
* Processamento paralelo;
* Modelos de linguagem;
* LLMs;
* Pré-treinamento;
* Fine-tuning;
* Relação entre Transformers e aplicações modernas de IA generativa.

A proposta é compreender a evolução arquitetural que levou dos modelos sequenciais tradicionais aos grandes modelos de linguagem.

## 4. Retrieval-Augmented Generation — RAG

A quarta etapa apresenta uma implementação didática de RAG.

O fluxo utilizado é:

```text
Pergunta do usuário
        ↓
Divisão dos documentos em chunks
        ↓
Vetorização
        ↓
Recuperação por similaridade
        ↓
Seleção dos documentos relevantes
        ↓
Construção do contexto
        ↓
Prompt
        ↓
Resposta
```

São explorados conceitos como:

* Chunking;
* Sobreposição entre chunks;
* TF-IDF;
* Similaridade por cosseno;
* `top_k`;
* Recuperação de contexto;
* Construção de prompts;
* Fontes utilizadas na resposta;
* Fallback quando não existe informação suficiente.

A implementação é propositalmente simplificada para demonstrar o funcionamento interno do conceito de RAG.

## 5. Aplicação de GenAI

Na etapa final, os conceitos anteriores são combinados na proposta de um **Assistente Acadêmico Inteligente**.

O sistema recebe uma mensagem de um aluno e executa um fluxo semelhante a:

```text
Mensagem do aluno
       ↓
Classificação
       ↓
Identificação da urgência
       ↓
Recuperação de contexto com RAG
       ↓
Construção do prompt
       ↓
Resposta estruturada
       ↓
Guardrails
       ↓
Decisão operacional
       ↓
Resposta automática ou encaminhamento humano
```

A aplicação contempla:

* Classificação de categoria;
* Classificação de urgência;
* Extração de informações;
* Recuperação de conhecimento;
* Construção de prompts;
* Saída estruturada em JSON;
* Guardrails;
* Fallback;
* Human-in-the-loop;
* Avaliação de respostas;
* Definição de ações operacionais.

Como não é utilizada uma API externa de LLM no notebook, algumas etapas são simuladas por funções baseadas em regras. Em uma aplicação de produção, essas funções poderiam ser substituídas por chamadas a modelos de linguagem.

## Arquitetura conceitual

```text
                 ┌─────────────────────┐
                 │    Mensagem aluno   │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │ Classificação       │
                 │ categoria / urgência│
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │       RAG           │
                 │ recuperação contexto│
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │      Prompt         │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │ Resposta estruturada│
                 │       JSON          │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │     Guardrails      │
                 └──────────┬──────────┘
                            ↓
                  ┌─────────┴─────────┐
                  ↓                   ↓
           Resposta automática   Atendimento humano
```

## Dataset

O trabalho utiliza um **dataset sintético**, criado dentro do próprio notebook.

As mensagens simulam situações relacionadas a atendimento acadêmico, como:

* problemas de acesso;
* dúvidas sobre provas;
* questões financeiras;
* solicitações acadêmicas;
* mensagens urgentes;
* mensagens ambíguas;
* perguntas que não possuem informação correspondente na base.

A utilização de dados sintéticos permite demonstrar os conceitos sem depender de uma base externa.

## Tecnologias utilizadas

### Linguagem

* Python

### Machine Learning / Deep Learning

* PyTorch
* NumPy
* Pandas

### Processamento de texto

* `re`
* `unicodedata`
* Tokenização
* Vocabulário
* Embeddings

### NLP / IA Generativa

* RNN
* LSTM
* GRU
* Attention
* Self-Attention
* Transformers
* LLMs
* RAG
* TF-IDF

## Principais funções implementadas

Entre as funções utilizadas no notebook estão componentes para:

* normalização e tokenização;
* construção do vocabulário;
* conversão de textos em sequências;
* treinamento e avaliação;
* mecanismos de atenção;
* recuperação de documentos;
* classificação de mensagens;
* extração de informações;
* construção de prompts;
* geração de respostas estruturadas;
* aplicação de guardrails;
* avaliação das respostas;
* definição de ações operacionais.

## Estrutura do projeto

```text
Assistente Acadêmico Inteligente/
│
├── Assistente Acadêmico Inteligente.ipynb
└── README.md
```

O arquivo principal contém toda a implementação, explicações teóricas, exercícios, testes e análises.

## Resultados e aprendizados

O desenvolvimento do projeto permitiu observar a evolução dos modelos de processamento de linguagem:

**Bag of Words**

Representa o texto considerando principalmente a presença das palavras, mas não preserva adequadamente a ordem da sequência.

**RNN**

Introduz o processamento sequencial e uma forma de memória do conteúdo processado anteriormente.

**LSTM e GRU**

Buscam lidar melhor com dependências mais longas através de mecanismos de controle de memória.

**Attention**

Permite atribuir diferentes pesos aos elementos da sequência.

**Transformers**

Utilizam mecanismos de atenção para processar informações de maneira mais eficiente e formam a base de grande parte dos modelos modernos de linguagem.

**RAG**

Permite complementar a geração com informações recuperadas de uma base de conhecimento.

**GenAI aplicada**

Mostra que uma aplicação real precisa considerar não apenas o modelo, mas também contexto, estrutura de saída, segurança, avaliação e participação humana.

## Limitações

O projeto possui algumas limitações importantes:

* Dataset pequeno e sintético;
* Modelos utilizados para fins didáticos;
* RAG implementado de forma simplificada;
* Recuperação baseada em TF-IDF;
* Ausência de embeddings semânticos;
* Ausência de uma API real de LLM;
* Ausência de banco vetorial em produção;
* Avaliação simplificada das respostas;
* Não representa um sistema acadêmico pronto para produção.

Essas limitações são importantes porque os resultados obtidos no notebook não devem ser interpretados como uma avaliação de um sistema real de atendimento.

## Possíveis evoluções

O projeto pode ser expandido para uma arquitetura mais próxima de uma aplicação real utilizando:

* Embeddings modernos;
* ChromaDB ou FAISS;
* LLMs via API;
* Hugging Face;
* LangChain;
* FastAPI;
* Interface web com React;
* Banco de dados;
* Autenticação;
* Observabilidade;
* Logging;
* Avaliação automática de respostas;
* Métricas de recuperação;
* Métricas de geração;
* Sistema de feedback humano;
* Monitoramento de qualidade;
* Pipeline de deploy com Docker.

## Proposta de aplicação

A aplicação proposta no trabalho é um **Assistente Acadêmico Inteligente**.

Seu objetivo é automatizar o primeiro nível de atendimento aos alunos, permitindo:

1. Receber uma solicitação em linguagem natural;
2. Identificar a categoria;
3. Identificar a urgência;
4. Recuperar informações relevantes;
5. Gerar uma resposta baseada no contexto;
6. Indicar as fontes utilizadas;
7. Aplicar regras de segurança;
8. Encaminhar situações que exigem intervenção humana.

O sistema segue o princípio de **human-in-the-loop**, evitando que decisões sensíveis sejam tomadas exclusivamente pelo sistema automatizado.

## Conclusão

Este trabalho demonstra uma evolução conceitual e prática que começa no processamento básico de texto e chega à construção de uma aplicação de GenAI.

A principal linha de evolução apresentada é:

```text
RNN
 ↓
LSTM / GRU
 ↓
Attention
 ↓
Self-Attention
 ↓
Transformers
 ↓
LLMs
 ↓
RAG
 ↓
GenAI aplicada
```

O projeto evidencia que construir uma aplicação baseada em IA generativa envolve mais do que utilizar um modelo de linguagem. É necessário considerar **dados, contexto, recuperação de informação, prompts, estrutura de saída, guardrails, avaliação e participação humana**.

---

## Autora

**Thaís da Silva Ferreira**

Engenharia da Computação — UNISAL
Pós-graduação em IA Generativa e Aplicações com LLMs — PUC Minas

**Áreas de interesse:**

* Inteligência Artificial
* IA Generativa
* Large Language Models
* RAG
* Machine Learning
* Deep Learning
* NLP
* Desenvolvimento Full Stack
* Engenharia de Software

---

## Tecnologias

`Python` `PyTorch` `NumPy` `Pandas` `NLP` `RNN` `LSTM` `GRU` `Attention` `Transformers` `LLM` `RAG` `TF-IDF` `GenAI`
