# Matriz de riscos

| Risco | Controle | Evidência | Risco residual | Responsável | Ação pendente |
|---|---|---|---|---|---|
| Prompt injection no arquivo | Conteúdo do arquivo tratado como dado não confiável | M5 + politica_injecao_v1.pdf | Baixo | Desenvolvimento | Reexecutar com LLM real |
| Vazamento de dados | Não solicitar/expor PII; dados sintéticos | M7 + O2 | Baixo | Segurança | Revisão humana |
| Ação não autorizada | Não aprovar exceções; encaminhar | O1 | Baixo | Produto | Validar com avaliadores |
| Documento ilegível | Validação de qualidade | M4 | Baixo | Desenvolvimento | Testar outros níveis de OCR |
| Formato inválido | Lista de extensões permitidas | M6 | Baixo | Desenvolvimento | Manter testes de regressão |
| Alucinação/ausência de evidência | RAG + declaração explícita de ausência | D1/D2 | Médio | Produto | Avaliar com LLM |
| OCR incorreto | Qualidade mínima + recusa quando insuficiente | M3/M4 | Médio | Desenvolvimento | Criar conjunto maior de imagens |
| Latência/custo do LLM | Medição p95 e custo médio | Métricas definidas | Médio | Desenvolvimento | Medir API real |
| Decisão humana substituída | Encaminhamento e revisão humana para maior impacto | O1 | Baixo | RH/Produto | Definir SLA de revisão |
