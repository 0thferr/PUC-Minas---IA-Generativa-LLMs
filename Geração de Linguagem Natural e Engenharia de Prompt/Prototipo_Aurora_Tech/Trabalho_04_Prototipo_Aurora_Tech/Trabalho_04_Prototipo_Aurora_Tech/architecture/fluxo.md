# Fluxo do Protótipo

```mermaid
flowchart TD
    A[Solicitação do usuário] --> B{Entrada válida?}
    B -- Não --> C[Pedir correção]
    B -- Sim --> D[PROMPT-04 v1.0: triagem]
    D --> E{JSON/rota válida?}
    E -- Não --> F[Repetir uma vez]
    F --> G{Persistiu?}
    G -- Sim --> H[Registrar falha + mensagem segura]
    G -- Não --> D
    E -- Sim --> I{Rota}
    I -- FORA_DO_ESCOPO --> J[Recusar com segurança]
    I -- T1/T2/T3 --> K{Há ambiguidade ou dado essencial ausente?}
    K -- Sim --> L[Pedir somente o esclarecimento necessário]
    K -- Não --> M[Carregar prompt por ID + versão]
    M --> N[Montar contexto mínimo]
    N --> O[Chamar modelo]
    O --> P{Saída válida?}
    P -- Não/erro técnico --> Q[Repetir uma vez]
    Q --> R{Persistiu?}
    R -- Sim --> H
    R -- Não --> P
    P -- Sim --> S[Responder / encaminhar]
```

Decisões principais:
- PROMPT-04 executa somente a triagem.
- PROMPT-01 responde consultas de regra.
- PROMPT-02 compara situações e exige JSON válido.
- PROMPT-03 trata limites, exceções, segurança e encaminhamentos.
- Conversa antiga irrelevante é descartada; apenas a pergunta atual e uma correção útil são usadas.
- Para erro técnico ou saída inválida, existe no máximo uma repetição controlada.
