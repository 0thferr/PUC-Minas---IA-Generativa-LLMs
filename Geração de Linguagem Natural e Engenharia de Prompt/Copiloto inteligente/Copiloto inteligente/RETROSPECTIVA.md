# Retrospectiva

## Funcionou
A evolução incremental preservou o caso de uso, ampliou a biblioteca de prompts, incorporou validação, fallback, recuperação de evidências e multimodalidade.

## Não funcionou completamente
A telemetria de API do modelo-alvo não foi obtida e a avaliação humana 10×2 permanece pendente.

## Principais aprendizados
Versionar prompt/base/fluxo e separar executor determinístico de comportamento de LLM evita conclusões indevidas. Entradas multimodais precisam de validação de qualidade e de fonte.

## Melhorias futuras
Concluir avaliação humana, medir custo/latência/tokens em API autenticada, endurecer testes de segurança e, se necessário, implementar LangGraph/MCP de forma efetiva e auditável.
