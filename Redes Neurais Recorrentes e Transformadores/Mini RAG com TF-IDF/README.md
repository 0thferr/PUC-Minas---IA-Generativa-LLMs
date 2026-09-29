# Mini RAG — Retrieval-Augmented Generation com TF-IDF

Implementação didática de um pipeline de **Retrieval-Augmented Generation (RAG)** desenvolvido em Python, explorando as principais etapas necessárias para construir um sistema capaz de recuperar informações relevantes de uma base de conhecimento antes de gerar uma resposta.

O projeto foi desenvolvido como parte da disciplina **Redes Neurais Recorrentes e Transformadores**, da pós-graduação em **IA Generativa e Aplicações com LLMs — PUC Minas**.

O objetivo principal é compreender o funcionamento interno de um sistema RAG sem depender inicialmente de APIs externas, LLMs pagos ou frameworks de alto nível como LangChain e LlamaIndex.

---

## Sobre o projeto

LLMs podem produzir respostas fluentes mesmo quando não possuem informações suficientes para responder corretamente a uma pergunta. Esse comportamento pode resultar em **alucinações**, especialmente quando a pergunta envolve documentos ou informações específicas.

O RAG busca reduzir esse problema adicionando uma etapa de recuperação de informação ao processo.

O fluxo implementado neste projeto é:

```text
Documentos
    ↓
Limpeza
    ↓
Chunking
    ↓
TF-IDF
    ↓
Representação vetorial
    ↓
Similaridade do cosseno
    ↓
Recuperação dos chunks relevantes
    ↓
Construção do contexto
    ↓
Construção do prompt
    ↓
Resposta baseada no contexto
```

O notebook implementa esse fluxo de forma progressiva, permitindo observar cada etapa individualmente.

---

## Objetivos

O projeto busca demonstrar, na prática:

* O problema das alucinações em LLMs;
* O conceito de Retrieval-Augmented Generation;
* A divisão de documentos em chunks;
* A importância da sobreposição entre chunks;
* A transformação de textos em representações vetoriais;
* O uso de TF-IDF como representação vetorial didática;
* A utilização de similaridade do cosseno;
* A recuperação dos documentos mais relevantes;
* O funcionamento do parâmetro `top_k`;
* O uso de limiares de similaridade;
* A avaliação da qualidade do retrieval;
* A construção de um armazenamento vetorial simplificado;
* A montagem de prompts utilizando contexto recuperado.

---

## Tecnologias utilizadas

* Python
* NumPy
* Pandas
* Scikit-learn
* TF-IDF
* Similaridade do Cosseno
* Jupyter Notebook / Google Colab

Principais bibliotecas utilizadas:

```python
import re
import textwrap
import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
```

O notebook utiliza `pandas` para manipulação dos documentos e `scikit-learn` para a representação TF-IDF e cálculo da similaridade.

---

## Arquitetura do mini RAG

### 1. Base de conhecimento

O primeiro passo consiste na criação de uma pequena base de documentos relacionados a LLMs e RAG.

A base contém informações sobre:

* Limitações dos LLMs;
* RAG;
* Embeddings e bancos vetoriais;
* Pipeline RAG;
* Avaliação de sistemas RAG.

Cada documento possui:

```text
ID
Título
Texto
```

A estrutura foi criada para simular uma pequena base de conhecimento que, em um sistema real, poderia ser composta por PDFs, documentos internos, artigos, contratos, relatórios ou páginas de uma wiki.

---

## 2. Chunking

Documentos grandes normalmente não devem ser enviados integralmente para o modelo.

Por isso, o projeto implementa uma função para dividir os textos em pequenos blocos chamados **chunks**.

```python
def criar_chunks_por_palavras(
    texto,
    tamanho_chunk=40,
    sobreposicao=10
):
    ...
```

A função permite controlar:

* `tamanho_chunk`: quantidade máxima de palavras;
* `sobreposicao`: quantidade de palavras compartilhadas entre chunks consecutivos.

Exemplo utilizado no projeto:

```python
tamanho_chunk = 35
sobreposicao = 8
```

A sobreposição ajuda a preservar informações que poderiam ficar divididas entre dois chunks.

---

## 3. Representação vetorial com TF-IDF

Em sistemas RAG modernos, normalmente são utilizados modelos de embeddings neurais.

Neste projeto, foi utilizada uma abordagem mais simples e didática baseada em **TF-IDF**.

```python
vectorizer = TfidfVectorizer()

matriz_chunks = vectorizer.fit_transform(
    textos_chunks
)
```

Cada chunk é transformado em uma representação numérica que permite compará-lo com uma pergunta.

O TF-IDF não possui a mesma capacidade semântica de embeddings produzidos por modelos neurais, mas é suficiente para demonstrar o princípio de recuperação utilizado em um pipeline RAG.

---

## 4. Recuperação por similaridade

Depois que os chunks são transformados em vetores, a pergunta do usuário também é convertida para o mesmo espaço vetorial.

A similaridade é calculada utilizando **similaridade do cosseno**:

```python
similaridades = cosine_similarity(
    vetor_pergunta,
    matriz_chunks
)[0]
```

Os chunks são então ordenados de acordo com sua similaridade com a pergunta.

O sistema retorna os `top_k` resultados mais relevantes.

```python
recuperar_chunks(
    pergunta,
    top_k=3
)
```

Cada resultado contém:

```text
chunk_id
título
texto
score
```

Essa etapa representa o componente de **retrieval** do RAG.

---

## 5. Construção do contexto

Depois da recuperação, os chunks selecionados são reunidos em um contexto estruturado.

O projeto utiliza uma função específica:

```python
montar_contexto(df_resultados)
```

Cada trecho recuperado mantém sua origem:

```text
Fonte
Chunk
Texto
```

Essa informação é importante para rastreabilidade e permite identificar quais partes da base foram utilizadas para construir o contexto.

---

## 6. Construção do prompt

Após recuperar as informações relevantes, o projeto monta um prompt no formato:

```text
Instrução
    +
Contexto recuperado
    +
Pergunta do usuário
    +
Regra de resposta
```

A instrução utilizada determina que a resposta deve utilizar apenas as informações presentes no contexto.

Quando o contexto não possui informação suficiente, o sistema deve informar:

```text
Não encontrei informação suficiente no contexto.
```

Esse mecanismo ajuda a estabelecer uma separação entre o conhecimento recuperado e informações que não estão presentes na base.

---

## 7. Simulação da geração

Para manter o exercício independente de APIs externas, o projeto não utiliza um LLM real para gerar a resposta final.

Em vez disso, foi implementada uma função que simula essa etapa:

```python
responder_com_rag_simples(
    pergunta,
    top_k=3
)
```

O processo é:

```text
Pergunta
   ↓
Retrieval
   ↓
Chunks relevantes
   ↓
Contexto
   ↓
Resposta simulada
```

Em uma aplicação real, a etapa final poderia utilizar modelos como GPT, Llama, Qwen, Mistral ou outros LLMs.

---

## 8. Influência do `top_k`

O parâmetro `top_k` determina quantos chunks serão recuperados.

Foram propostos testes utilizando:

```python
top_k = 1
top_k = 2
top_k = 3
top_k = 4
```

O experimento demonstra um dos principais desafios de sistemas RAG:

```text
top_k muito baixo
        ↓
pouco contexto
        ↓
possível perda de informação
```

Enquanto:

```text
top_k muito alto
        ↓
mais contexto
        ↓
possível entrada de informações irrelevantes
```

Portanto, aumentar o número de documentos recuperados não significa necessariamente melhorar a qualidade da resposta.

---

## 9. Avaliação do Retrieval

O projeto também implementa uma avaliação simples do sistema de recuperação.

Foram definidas perguntas de teste e seus respectivos documentos esperados:

```text
"O que é alucinação em LLMs?"
→ Limitações dos LLMs

"O que significa RAG?"
→ O que é RAG

"Para que servem embeddings?"
→ Embeddings e bancos vetoriais

"Quais são as etapas do pipeline RAG?"
→ Pipeline RAG

"Como avaliar um sistema RAG?"
→ Avaliação de RAG
```

A avaliação verifica se o documento esperado aparece entre os `top_k` resultados recuperados.

A métrica utilizada é uma **acurácia de recuperação@k**:

```python
acuracia = df_avaliacao["acertou"].mean()
```

O experimento também compara diferentes valores de `top_k` para observar como a quantidade de resultados recuperados influencia o retrieval.

---

## 10. Mini Vector Store

Para aproximar o exercício de uma arquitetura real, foi criada a classe:

```python
MiniVectorStore
```

Ela encapsula:

* Vetorização;
* Armazenamento da matriz;
* Dados dos chunks;
* Busca por similaridade.

Uso:

```python
store = MiniVectorStore()

store.fit(df_chunks)

store.search(
    "O que é banco vetorial?",
    top_k=3
)
```

A classe representa, de forma simplificada, o funcionamento conceitual de um banco vetorial.

Em aplicações reais, essa responsabilidade poderia ser assumida por tecnologias como:

* FAISS;
* Chroma;
* Pinecone;
* Weaviate;
* Milvus.

O próprio material utilizado no notebook apresenta essas alternativas como exemplos de bancos vetoriais.

---

## 11. Perguntas fora da base

Um dos experimentos mais importantes testa perguntas que não possuem resposta na base de conhecimento.

Exemplo:

```text
Qual foi a arquitetura exata do modelo GPT-4?
```

O problema identificado é que um sistema baseado apenas em similaridade pode sempre retornar algum resultado, mesmo quando a pergunta não possui relação suficiente com os documentos.

Para lidar com esse cenário, foi implementado um **limiar mínimo de similaridade**.

```python
def responder_com_limiar(
    pergunta,
    top_k=3,
    limiar=0.15
):
    ...
```

Se o melhor resultado possuir um score abaixo do limiar, o sistema retorna:

```text
Não encontrei informação suficiente no contexto.
```

Essa estratégia demonstra um mecanismo simples para evitar que qualquer resultado seja tratado como informação relevante.

---

## 12. Experimento com diferentes limiares

Foram propostos testes com diferentes valores:

```text
0.05
0.10
0.15
0.25
0.40
```

O objetivo é observar o equilíbrio entre:

* aceitar informações relevantes;
* rejeitar informações insuficientemente relacionadas;
* evitar falsos positivos;
* evitar rejeitar informações que poderiam ser úteis.

Esse experimento evidencia que o threshold de recuperação é um parâmetro importante para o comportamento de um sistema RAG.

---

## 13. Documento maior

Na etapa final, o projeto simula um cenário mais próximo de um documento real.

É criado um material maior sobre a própria Aula 4, contendo informações sobre:

* Alucinações;
* Conhecimento congelado;
* Janela de contexto;
* RAG;
* Indexação;
* Chunking;
* Embeddings;
* Bancos vetoriais;
* Recuperação;
* Avaliação;
* Limitações do RAG.

Esse material é dividido em chunks maiores:

```python
tamanho_chunk = 70
sobreposicao = 15
```

Em seguida, os chunks são indexados em um novo `MiniVectorStore` para realização das consultas.

---

## Fluxo completo

O projeto pode ser resumido pela seguinte arquitetura:

```text
                 ┌──────────────────┐
                 │    Documentos    │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │     Chunking     │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │      TF-IDF      │
                 │    Vetorização   │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │  Vector Store    │
                 └────────┬─────────┘
                          │
                          │
Pergunta ───────► Vetorização
                          │
                          ▼
                 ┌──────────────────┐
                 │   Similaridade   │
                 │    do Cosseno   │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │     Top-K        │
                 │     Chunks       │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │    Contexto      │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │      Prompt      │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │  Resposta RAG    │
                 └──────────────────┘
```

---

## Principais conceitos demonstrados

### Retrieval-Augmented Generation

Arquitetura que combina recuperação de informação com geração de texto.

### Chunking

Divisão dos documentos em partes menores para permitir recuperação granular.

### Embeddings

Representações numéricas utilizadas para comparar textos.

Neste projeto, o conceito é demonstrado utilizando TF-IDF.

### Vector Store

Estrutura responsável por armazenar as representações vetoriais e permitir buscas por similaridade.

### Similaridade do Cosseno

Métrica utilizada para medir a proximidade entre a pergunta e os chunks.

### Top-K

Quantidade de resultados recuperados pelo sistema.

### Threshold

Valor mínimo de similaridade necessário para considerar que existe informação relevante.

### Retrieval Evaluation

Processo de avaliação para verificar se os documentos relevantes estão sendo recuperados.

---

## Limitações do projeto

Este projeto possui caráter didático e utiliza algumas simplificações.

A principal delas é a utilização de **TF-IDF em vez de embeddings neurais**.

TF-IDF trabalha principalmente com a ocorrência e importância estatística das palavras. Portanto, não possui a mesma capacidade de compreender relações semânticas que modelos modernos de embeddings.

Além disso, o projeto não utiliza um LLM real para a etapa final de geração.

Em um sistema de produção, seria possível substituir os componentes didáticos por:

```text
TF-IDF
   ↓
Sentence Transformers / BGE / E5
```

e:

```text
MiniVectorStore
   ↓
Chroma / FAISS / Pinecone / Weaviate / Milvus
```

e:

```text
Resposta simulada
   ↓
LLM
```

O próprio notebook destaca que a qualidade do RAG depende não apenas do modelo gerador, mas também da qualidade dos documentos, chunks, embeddings e recuperação.

---

## Possíveis evoluções

Este projeto pode ser expandido para uma implementação mais próxima de um sistema RAG de produção.

### Embeddings neurais

Substituir TF-IDF por modelos como:

* Sentence Transformers;
* BGE;
* E5;
* embeddings da OpenAI.

### Banco vetorial

Substituir o `MiniVectorStore` por:

* ChromaDB;
* FAISS;
* Pinecone;
* Weaviate;
* Milvus.

### LLM

Adicionar um modelo generativo para produzir respostas utilizando o contexto recuperado.

### RAG completo

Evoluir o projeto para:

```text
PDF / DOCX / Web
       ↓
Document Loader
       ↓
Chunking
       ↓
Embeddings
       ↓
Vector Database
       ↓
Retriever
       ↓
Context
       ↓
LLM
       ↓
Resposta com fontes
```

Essa arquitetura permitiria transformar o exercício em uma aplicação de perguntas e respostas sobre documentos.

---

## Como executar

Clone o repositório:

```bash
git clone https://github.com/0thferr/PUC-Minas---IA-Generativa-LLMs.git
```

Entre na pasta:

```bash
cd "PUC-Minas---IA-Generativa-LLMs/Redes Neurais Recorrentes e Transformadores/Exercicio 4"
```

Instale as dependências:

```bash
pip install numpy pandas scikit-learn jupyter
```

Execute o notebook:

```bash
jupyter notebook "Exercício_4.ipynb"
```

Também é possível executar o notebook utilizando Google Colab.

---

## Estrutura do projeto

```text
Mini RAG com TF-IDF/
│
├── Mini RAG com TF-IDF.ipynb
└── README.md
```

### `Mini RAG com TF-IDF.ipynb`

Notebook contendo toda a implementação do mini pipeline RAG, incluindo:

* Base de conhecimento;
* Chunking;
* TF-IDF;
* Recuperação;
* Similaridade;
* Construção de contexto;
* Prompt;
* `top_k`;
* Avaliação;
* `MiniVectorStore`;
* Threshold;
* Testes com perguntas fora da base;
* Simulação de documento maior.

---

## Contexto acadêmico

**Curso:** Pós-graduação em IA Generativa e Aplicações com LLMs
**Instituição:** PUC Minas
**Disciplina:** Redes Neurais Recorrentes e Transformadores
**Atividade:** Exercício 4

---

## Autora

**Thaís Ferreira**

Desenvolvedora de Software | IA Generativa | Machine Learning

GitHub: [@0thferr](https://github.com/0thferr)

---

## Referências

* Scikit-learn — TF-IDF
* Scikit-learn — Cosine Similarity
* Conceito de Retrieval-Augmented Generation (RAG)
* Bancos de dados vetoriais
* Arquiteturas de aplicações com LLMs
