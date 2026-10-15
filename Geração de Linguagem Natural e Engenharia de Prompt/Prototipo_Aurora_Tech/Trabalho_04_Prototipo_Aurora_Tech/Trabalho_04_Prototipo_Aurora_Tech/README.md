# Trabalho 4 — Fluxo de Geração e Protótipo Textual

## Projeto
Copiloto Corporativo de Apoio à Política de Trabalho Híbrido da Aurora Tech.

## Objetivo
Conectar a biblioteca versionada do Trabalho 3 a um fluxo executável que:

1. recebe e valida a solicitação;
2. classifica a tarefa;
3. identifica ambiguidade e dados ausentes;
4. carrega o prompt por ID e versão;
5. monta contexto mínimo;
6. chama o modelo;
7. valida a saída;
8. repete no máximo uma vez em caso de erro;
9. responde, pede esclarecimento, recusa ou encaminha.

## Biblioteca de prompts
- PROMPT-01 v1.0 — Consulta de Regra.
- PROMPT-02 v1.0 — Verificação de Situação.
- PROMPT-03 v1.0 — Encaminhamento Seguro.
- PROMPT-04 v1.0 — Triagem e Roteamento.

Os textos dos prompts ficam em `prompts/templates/` e são localizados por `prompts/catalogo.csv`. O código não contém os textos dos prompts.

## Estrutura

```text
Trabalho_04_Prototipo_Aurora_Tech/
├── architecture/
├── prompts/
├── prototype/
├── tests/
├── evidencias/
├── evaluation/
└── README.md
```

## Execução rápida

### Modo de referência determinístico
Não exige API:

```bash
cd prototype
python app.py
```

Para executar os 13 testes:

```bash
cd tests
python test_runner.py
```

Para reaplicar os sete casos do Trabalho 2:

```bash
python baseline_runner.py
```

### Modo real por API
O protótipo também possui adaptador para Anthropic:

```bash
pip install anthropic
```

Defina as variáveis de ambiente:

```text
EXECUTION_MODE=anthropic
ANTHROPIC_API_KEY=sua_chave
MODEL_NAME=claude-sonnet-4-5
```

## Erros controlados
- E1 simula saída JSON inválida na primeira tentativa.
- E2 simula timeout na primeira tentativa.
- O sistema tenta no máximo duas vezes no total.
- Persistindo a falha, registra a evidência e devolve mensagem segura.

## Limitação metodológica
O modo `reference` é determinístico e serve para demonstrar o fluxo, validação, roteamento e recuperação de falhas. Para produzir evidência empírica de um LLM, execute em modo real por API e preserve os resultados gerados.

## Resultados
Após executar os scripts:
- `tests/resultados.csv`: 13 casos.
- `evidencias/*.json`: evidências por execução.
- `evaluation/baseline_reaplicado_resultados.csv`: sete casos do Trabalho 2 reaplicados.
