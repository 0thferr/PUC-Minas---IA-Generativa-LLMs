# Exercício 1 — Aplicações de Transformers em NLP

Este projeto faz parte da disciplina **Redes Neurais Recorrentes e Transformadores**, da pós-graduação em **IA Generativa e Aplicações com LLMs — PUC Minas**.

O objetivo do exercício é explorar o uso de modelos pré-treinados disponíveis no ecossistema **Hugging Face Transformers**, analisando dois tipos de tarefas de Processamento de Linguagem Natural (NLP):

* Classificação de textos;
* Geração de textos.

A atividade foi desenvolvida utilizando pipelines da biblioteca `transformers`, sem treinamento ou fine-tuning dos modelos.

---

## Objetivos

O exercício busca compreender, de forma prática:

* Como utilizar modelos pré-treinados através da biblioteca Hugging Face Transformers;
* Como funciona uma pipeline de classificação de sentimentos;
* Como modelos generativos produzem texto a partir de prompts;
* Como diferentes temperaturas influenciam a geração;
* Como um mesmo prompt pode produzir respostas diferentes;
* As diferenças entre modelos de classificação e geração de texto;
* As limitações de modelos pré-treinados quando utilizados fora de seu domínio.

---

## Tecnologias utilizadas

* **Python 3.11.9**
* **PyTorch**
* **Hugging Face Transformers**
* **Pandas**
* **Jupyter Notebook**
* **Hugging Face Hub**

### Modelos

**Classificação**

`distilbert/distilbert-base-uncased-finetuned-sst-2-english`

Modelo pré-treinado utilizado através da pipeline:

```python
from transformers import pipeline

classificador = pipeline("sentiment-analysis")
```

**Geração de texto**

`distilgpt2`

Utilizado através da pipeline:

```python
gerador = pipeline(
    "text-generation",
    model="distilgpt2"
)
```

Os modelos são carregados diretamente do Hugging Face, conforme proposto na atividade, sem realização de treinamento ou fine-tuning.

---

## Experimento 1 — Classificação de Sentimentos

Foi utilizada uma pipeline de análise de sentimentos para avaliar cinco tipos diferentes de frases:

| Tipo          | Exemplo                                                               | Resultado |
| ------------- | --------------------------------------------------------------------- | --------- |
| Positiva      | "O dia está maravilhoso e tudo parece perfeito."                      | NEGATIVE  |
| Negativa      | "Estou profundamente frustrado com esse serviço horrível."            | NEGATIVE  |
| Ambígua       | "O policial viu o homem com a arma."                                  | POSITIVE  |
| Irônica       | "A reunião de hoje foi tão produtiva que poderia ter sido um e-mail." | NEGATIVE  |
| Outro domínio | "A síntese proteica ocorre nos ribossomos da célula."                 | NEGATIVE  |

Os resultados foram armazenados em um `DataFrame` utilizando Pandas.

### Resultados observados

Os scores retornados pelo modelo foram:

* Frase positiva: **0.9707**
* Frase negativa: **0.9502**
* Frase ambígua: **0.6449**
* Frase irônica: **0.9953**
* Frase de outro domínio: **0.9834**

Um ponto importante observado foi que o modelo apresentou comportamento inadequado em algumas situações. A frase claramente positiva foi classificada como `NEGATIVE`, enquanto a frase sobre síntese proteica, que não possui caráter sentimental evidente, também recebeu uma classificação `NEGATIVE`.

Isso demonstra uma limitação importante de modelos de análise de sentimentos: o score representa a confiança do modelo na classe escolhida, mas não significa necessariamente que a interpretação esteja correta.

A frase ambígua apresentou o menor score entre os exemplos, indicando maior incerteza do modelo.

---

## Experimento 2 — Geração de Texto

Para a geração de texto foi utilizado o modelo **DistilGPT-2**.

Foram realizados cinco experimentos:

1. Prompt curto;
2. Prompt detalhado;
3. Geração com temperatura baixa;
4. Geração com temperatura alta;
5. Duas sequências para o mesmo prompt.

### Prompt curto

```text
Artificial intelligence can
```

O modelo continuou o texto a partir do contexto fornecido, produzindo uma sequência relacionada à inteligência artificial e resolução de problemas.

### Prompt detalhado

```text
Explain the benefits of renewable energy for a sustainable future in one paragraph.
```

O modelo tentou desenvolver uma resposta relacionada à energia renovável, porém apresentou uma continuação pouco consistente com o formato solicitado.

### Temperatura baixa

```text
The future of technology is
```

Utilizando:

```python
temperature=0.2
```

A geração apresentou uma tendência mais previsível e menos diversificada.

### Temperatura alta

O mesmo contexto foi utilizado com:

```python
temperature=1.2
```

Nesse cenário, a saída apresentou maior variabilidade, mas também maior perda de coerência.

### Duas sequências

Para o prompt:

```text
Learning to code is
```

foram solicitadas duas respostas:

```python
num_return_sequences=2
```

As duas sequências apresentaram continuações diferentes para o mesmo prompt, demonstrando a natureza probabilística da geração de texto.

---

## Influência da temperatura

A temperatura controla a aleatoriedade durante a geração de texto.

Neste experimento foram utilizadas duas configurações:

```python
temperature=0.2
```

e

```python
temperature=1.2
```

De forma geral:

| Temperatura | Comportamento esperado                   |
| ----------- | ---------------------------------------- |
| Baixa       | Mais previsibilidade e menor diversidade |
| Alta        | Maior diversidade e maior aleatoriedade  |

Nos experimentos realizados, o aumento da temperatura produziu uma saída mais variável, porém também contribuiu para trechos menos coerentes.

---

## Classificação × Geração

| Critério            | Classificação                      | Geração                           |
| ------------------- | ---------------------------------- | --------------------------------- |
| Entrada             | Texto                              | Prompt                            |
| Saída               | Classe + score                     | Texto                             |
| Controle            | Maior                              | Menor                             |
| Avaliação           | Mais objetiva                      | Mais subjetiva                    |
| Variabilidade       | Baixa                              | Alta                              |
| Risco de erro       | Classificação incorreta            | Texto incoerente ou inadequado    |
| Aplicações          | Sentimentos, categorias, intenções | Chatbots, completamento e geração |
| Principal limitação | Dependência do domínio             | Controle e coerência da saída     |

A classificação produz uma saída estruturada, normalmente acompanhada de um score de confiança. Já a geração possui maior variabilidade e exige critérios adicionais para avaliar a qualidade do resultado.

---

## Principais observações

Os experimentos demonstraram alguns comportamentos relevantes dos modelos:

### 1. Confiança não significa correção

O classificador apresentou score elevado mesmo em uma classificação aparentemente incorreta.

Isso pode ser observado na frase:

```text
O dia está maravilhoso e tudo parece perfeito.
```

que recebeu:

```text
NEGATIVE
Score: 0.9707
```

Portanto, o score deve ser interpretado como confiança do modelo na previsão, e não como garantia de que a previsão esteja correta.

### 2. Ironia é um desafio

A frase:

```text
A reunião de hoje foi tão produtiva que poderia ter sido um e-mail.
```

foi classificada como `NEGATIVE` com score de **0.9953**.

Embora a classificação negativa seja plausível, o resultado também demonstra que o modelo precisa interpretar contexto e ironia, algo que pode ser difícil para modelos de classificação baseados em padrões linguísticos.

### 3. Temperatura influencia a geração

A alteração da temperatura modificou o comportamento das respostas.

Temperaturas menores tendem a favorecer respostas mais previsíveis, enquanto temperaturas maiores aumentam a diversidade das possibilidades selecionadas.

### 4. Geração é probabilística

O experimento com duas sequências mostrou que um mesmo prompt pode resultar em textos diferentes.

Isso é importante em aplicações de IA generativa, pois a mesma entrada não necessariamente produz exatamente a mesma saída quando a geração utiliza amostragem.

---

## Estrutura do projeto

```text
Aplicações de Transformers em NLP/
│
├── Aplicações de Transformers em NLP.ipynb
└── README.md
```

### `Exercicio 1.ipynb`

Notebook contendo:

* Instalação das bibliotecas;
* Importação do Transformers;
* Pipeline de classificação;
* Testes com cinco tipos de frases;
* Armazenamento dos resultados;
* Pipeline de geração;
* Testes com diferentes prompts;
* Experimentos com temperatura;
* Geração de múltiplas sequências.

### `README.md`

Documentação dos objetivos, tecnologias, experimentos e principais resultados.

---

## Como executar

Clone o repositório:

```bash
git clone https://github.com/0thferr/PUC-Minas---IA-Generativa-LLMs.git
```

Entre na pasta do exercício:

```bash
cd "PUC-Minas---IA-Generativa-LLMs/Redes Neurais Recorrentes e Transformadores/Exercicio 1"
```

Instale as dependências:

```bash
pip install transformers torch pandas jupyter
```

Execute o notebook:

```bash
jupyter notebook "Exercicio 1.ipynb"
```

Na primeira execução, os modelos necessários serão carregados do Hugging Face Hub.

---

## Conceitos explorados

Este exercício aborda conceitos fundamentais relacionados a NLP e modelos Transformer:

* Natural Language Processing (NLP);
* Transformers;
* Modelos pré-treinados;
* Hugging Face Transformers;
* Pipeline de classificação;
* Análise de sentimentos;
* Text Generation;
* Prompt;
* Temperature;
* Sampling;
* Variabilidade de geração;
* Score de confiança;
* Limitações de modelos de linguagem.

---

## Contexto acadêmico

**Curso:** Pós-graduação em IA Generativa e Aplicações com LLMs
**Instituição:** PUC Minas
**Disciplina:** Redes Neurais Recorrentes e Transformadores
**Atividade:** Exercício 1

---

## Autora

**Thaís Ferreira**

Desenvolvedora de Software | IA Generativa | Machine Learning

GitHub: [@0thferr](https://github.com/0thferr)

---

## Referências

* [Hugging Face Transformers](https://huggingface.co/docs/transformers/)
* [Hugging Face Hub](https://huggingface.co/)
* [DistilBERT](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english)
* [DistilGPT-2](https://huggingface.co/distilbert/distilgpt2)
