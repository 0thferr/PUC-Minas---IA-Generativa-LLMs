# Exercício – Redes Neurais Recorrentes e Transformadores

---

## Objetivo

Utilizar o ecossistema **Hugging Face** para testar e comparar dois tipos de modelos baseados em **Transformers**:

1. Modelo para **classificação de textos**;
2. Modelo para **geração de textos**.

Ao final da atividade, deverá ser realizada uma comparação entre as entradas, saídas, comportamento e limitações dos dois modelos.

> **Importante:** Não é necessário realizar treinamento ou *fine-tuning*. Os modelos devem ser carregados diretamente da biblioteca **Transformers**, utilizando modelos pré-treinados disponíveis no Hugging Face. :contentReference[oaicite:0]{index=0}

---

# Organização da Atividade

A atividade poderá ser realizada individualmente ou em dupla.

A entrega deverá ser feita em **um único arquivo PDF** (por exemplo, um notebook Jupyter exportado para PDF). :contentReference[oaicite:1]{index=1}

---

# Parte 1 – Modelo de Classificação

## Objetivo

Escolher um modelo de classificação de textos disponível no Hugging Face.

Uma sugestão é utilizar uma pipeline de **Análise de Sentimentos**.

### Exemplo

```python
from transformers import pipeline

classificador = pipeline("sentiment-analysis")
```

---

## Testes

Executar o modelo utilizando **cinco frases diferentes**.

As frases devem contemplar obrigatoriamente:

- Frase claramente positiva;
- Frase claramente negativa;
- Frase ambígua;
- Frase com ironia;
- Frase pertencente a um domínio diferente daquele para o qual o modelo parece ter sido treinado.

### Exemplo de frase irônica

> "O atendimento foi tão rápido que só precisei esperar duas horas." :contentReference[oaicite:2]{index=2}

---

## Registrar para cada teste

- Frase utilizada;
- Classe retornada pelo modelo;
- Score obtido;
- Pequena análise indicando se o resultado parece correto ou incorreto. :contentReference[oaicite:3]{index=3}

---

## Modelo de Tabela

| Tipo da frase | Frase utilizada | Classe retornada | Score | Análise |
|---------------|-----------------|------------------|-------|----------|
| Positiva      |                 |                  |       |          |
| Negativa      |                 |                  |       |          |
| Ambígua       |                 |                  |       |          |
| Irônica       |                 |                  |       |          |
| Outro domínio |                 |                  |       |          |

---

# Parte 2 – Modelo de Geração

## Objetivo

Escolher um modelo de geração de texto disponível no Hugging Face.

### Exemplo

```python
from transformers import pipeline

gerador = pipeline(
    "text-generation",
    model="distilgpt2"
)
```

:contentReference[oaicite:4]{index=4}

---

## Testes

Realizar os seguintes experimentos:

1. Prompt curto;
2. Prompt detalhado;
3. Temperatura baixa;
4. Temperatura alta;
5. Duas sequências para o mesmo prompt. :contentReference[oaicite:5]{index=5}

---

## Exemplo

```python
saida = gerador(
    "Artificial intelligence can",
    max_new_tokens=40
)

print(saida[0]["generated_text"])
```

---

## Exemplo utilizando temperatura

```python
saida = gerador(
    "Artificial intelligence can",
    max_new_tokens=40,
    do_sample=True,
    temperature=0.8
)
```

---

## Gerando duas respostas

```python
saida = gerador(
    "Artificial intelligence can",
    max_new_tokens=40,
    do_sample=True,
    temperature=0.8,
    num_return_sequences=2
)
```

:contentReference[oaicite:6]{index=6}

---

## Registrar para cada teste

- Prompt utilizado;
- Parâmetros utilizados;
- Texto gerado;
- Breve análise do resultado.

Na análise, observar:

- Diversidade;
- Coerência;
- Repetição;
- Criatividade;
- Relação entre o prompt e o texto gerado. :contentReference[oaicite:7]{index=7}

---

## Modelo de Tabela

| Teste | Prompt e parâmetros | Resultado | Análise |
|--------|---------------------|-----------|----------|
| Prompt curto                 |           |          |
| Prompt detalhado             |           |          |
| Temperatura baixa            |           |          |
| Temperatura alta             |           |          |
| Duas sequências              |           |          |

---

# Parte 3 – Comparação entre os Modelos

Após os experimentos, preencher a tabela comparando os dois modelos.

| Critério | Modelo de Classificação | Modelo de Geração |
|----------|-------------------------|-------------------|
| Tipo de entrada |                  |                   |
| Tipo de saída |                    |                   |
| Nível de controle sobre a resposta |                   |
| Facilidade de avaliação |          |                   |
| Variabilidade dos resultados |     |                   |
| Risco de erro |                    |                   |
| Possíveis aplicações |             |                   |
| Principais limitações |            |                   |

:contentReference[oaicite:8]{index=8}

---

# Parte 4 – Perguntas de Análise

Responder objetivamente às seguintes questões:

1. O modelo de classificação errou algum dos exemplos? Explique o possível motivo.
2. Como o modelo lidou com a frase irônica?
3. A geração mudou quando a temperatura foi alterada?
4. Alguma saída perdeu coerência?
5. Qual dos dois modelos seria mais fácil de colocar em produção? Justifique considerando controle da saída, previsibilidade, custo e risco de erro. :contentReference[oaicite:9]{index=9}

---

# Entrega

O PDF deverá conter:

1. Nome do aluno ou integrantes;
2. Nome do modelo de classificação;
3. Nome do modelo de geração;
4. Resultados dos cinco testes de classificação;
5. Resultados dos cinco testes de geração;
6. Tabela comparativa;
7. Respostas às perguntas de análise;
8. Principais trechos do código ou prints do notebook.

Não é necessário incluir todo o código nem uma introdução teórica extensa. O foco deve estar nos experimentos, resultados e análises. :contentReference[oaicite:10]{index=10}

---

# Nome do Arquivo

Individual:

```text
NomeSobrenome_AtividadeAula3.pdf
```

Em dupla:

```text
NomeSobrenome1_NomeSobrenome2_AtividadeAula3.pdf
```

:contentReference[oaicite:11]{index=11}

---

# Estrutura Recomendada

1. Identificação
2. Modelos utilizados
3. Experimento de classificação
4. Experimento de geração
5. Comparação entre os modelos
6. Perguntas de análise
7. Código utilizado

:contentReference[oaicite:12]{index=12}

---

