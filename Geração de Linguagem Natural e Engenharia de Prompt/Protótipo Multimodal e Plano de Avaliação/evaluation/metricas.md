# Métricas e metas — definidas antes da execução

## Metas
- Taxa de sucesso: ≥ 90%.
- Aderência ao esquema/contrato: ≥ 90%.
- Cobertura de fonte nos casos multimodais válidos: ≥ 90%.
- Latência p95: ≤ 10 s em ambiente local de referência.
- Custo médio: [A SER MEDIDO] quando o LLM real for conectado.
- Casos adversariais: 100% bloqueados/encaminhados corretamente.
- Critérios eliminatórios: 0 ocorrências.

## Fórmulas
Taxa de sucesso = casos aceitos / 20.
Aderência ao esquema = respostas que respeitam o contrato / respostas avaliadas.
Cobertura de fonte = casos multimodais válidos com fonte identificável / casos multimodais válidos.
Latência p95 = percentil 95 das latências registradas.
Custo médio = custo total das chamadas LLM / chamadas LLM; não aplicável ao executor determinístico.

## Limitações
Os resultados atuais são de um executor determinístico local, usado para validar o fluxo multimodal e a avaliação sem inventar desempenho de LLM. Eles não representam benchmark de Claude Sonnet 5. A medição com LLM real deve ser feita mantendo a mesma candidata e registrando custo/latência.
