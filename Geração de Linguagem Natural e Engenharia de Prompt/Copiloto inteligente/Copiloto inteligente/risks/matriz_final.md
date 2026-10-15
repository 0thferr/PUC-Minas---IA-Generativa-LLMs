# Matriz final de riscos

| Risco | Probabilidade | Impacto | Controle/Mitigação | Status |
|---|---|---|---|---|
| Alucinação | Média | Alto | Base restrita, evidência, validação e encaminhamento | Controlado |
| Informação desatualizada | Média | Alto | Versionamento da base e atualização controlada | Pendente em produção |
| Base incompleta | Média | Alto | Declarar insuficiência e encaminhar RH Responde | Controlado |
| Prompt injection | Alta | Alto | Conteúdo externo tratado como dado não confiável | Testado |
| Arquivo malicioso | Baixa/Média | Alto | Validação de tipo/tamanho e processamento controlado | Controlado |
| OCR incorreto | Média | Médio/Alto | Validação de qualidade e recusa de baixa qualidade | Testado |
| Resposta sem fonte | Média | Alto | Evidência identificável no fluxo | Controlado |
| Acesso indevido/PII | Média | Alto | Não solicitar/expor PII desnecessária | Testado |
| Decisão indevida | Baixa/Média | Alto | Revisão humana e proibição de aprovação automática | Controlado |
| Falha do modelo | Média | Alto | Validação, retry único e fallback | Controlado |
| Indisponibilidade da API | Média | Alto | Fallback e tratamento de erro | Pendente em produção |
| Erro de roteamento | Média | Médio | TRH-04 + testes | Controlado |
| Falso encaminhamento | Média | Médio | Casos de borda e revisão humana | Parcial |
| Vazamento de informação | Baixa/Média | Alto | Limites de dados e logs sem PII | Controlado |
