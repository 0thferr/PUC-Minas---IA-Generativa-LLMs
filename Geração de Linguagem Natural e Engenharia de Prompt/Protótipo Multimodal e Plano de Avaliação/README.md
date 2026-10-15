# Trabalho 5 — Protótipo Multimodal e Plano de Avaliação

Disciplina: Geração de Linguagem Natural e Engenharia de Prompt  
Curso: IA Generativa e Aplicações com LLMs — PUC Minas  
Professor: Ricardo Brito Alves  
Projeto: Copiloto Corporativo de Apoio à Política de Trabalho Híbrido da Aurora Tech

## O que foi entregue
- `prototype/`: protótipo executável e prompts externos.
- `multimodal/especificacao.md`: contrato multimodal.
- `tests/casos_v1.csv`: 20 casos.
- `tests/resultados_v1.csv`: execução dos 20 casos.
- `evidencias/`: evidência individual por caso.
- `evaluation/`: métricas e rubrica.
- `risks/`: matriz e gate.
- `data/`: documentos sintéticos usados nos testes.
- `architecture/`: fluxo do sistema.

## Continuidade
O Trabalho 4 exige preservar o fluxo textual e seus 13 casos. Nesta entrega, os 13 comportamentos foram reaproveitados/adaptados e sete casos multimodais foram acrescentados.

## Execução
```bash
pip install -r prototype/requirements.txt
python tests/run_tests.py
```

Para executar um caso manual:
```bash
python prototype/app.py "Quantos dias por semana posso trabalhar remotamente?" --file data/politica_v1.pdf
```

## Integridade acadêmica
Os resultados dos 20 testes foram executados no executor determinístico local. Eles não devem ser interpretados como benchmark de LLM. A rubrica humana e a medição com LLM real estão explicitamente marcadas como pendências, evitando resultados experimentais inventados.
