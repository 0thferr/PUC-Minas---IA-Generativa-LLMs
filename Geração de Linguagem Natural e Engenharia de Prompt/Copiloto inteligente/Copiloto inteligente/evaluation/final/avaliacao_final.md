# Avaliação final — Trabalho 6

## 1. Resultados da execução local da candidata v1.0

Os 20 casos existentes no Trabalho 5 foram preservados e analisados sem alteração.

- Taxa de sucesso: 100% (20/20), meta ≥ 90%.
- Aderência ao contrato: 100%, conforme critérios automatizados da suíte.
- Cobertura de fonte nos casos multimodais válidos M1–M3: 100%, meta ≥ 90%.
- p95 de latência local: 140.268 ms, meta ≤ 10.000 ms.
- Casos adversariais bloqueados/encaminhados corretamente: 100%, meta 100%.
- Critérios eliminatórios observados na execução local: 0.
- Custo real de LLM: não medido nesta execução.

Importante: esses números são evidência de integração e protocolo do executor determinístico local. Não são benchmark de um LLM.

## 2. Evidência empírica com LLM real

Foi realizada uma execução real com um LLM conversacional disponível nesta sessão: GPT-5.6 Luna. Os 20 casos foram submetidos ao modelo com as regras da política e os critérios do conjunto v1.0, e as respostas estão em `evidencia_empirica_llm.csv`.

O resultado dessa etapa é evidência empírica de comportamento de LLM, mas não deve ser confundido com uma medição de Claude Sonnet 5 via API.

Resultado qualitativo da execução:
- respostas factuais para os casos representativos;
- preservação dos limites de autoridade nos casos O1/O2;
- tratamento de ausência de evidência em D1/D2;
- recusa de formato inválido em M6;
- recusa de PII em M7;
- preservação do limite de autoridade diante da injeção em M5;
- tratamento explícito de baixa qualidade em M4.

Limitações:
- a sessão não expõe tokens de entrada/saída, custo financeiro ou latência de API;
- não houve chamada autenticada à API do Claude;
- E1/E2 são cenários de falha controlada, não incidentes espontâneos observados no LLM.

## 3. Avaliação humana

A rubrica exige 10 casos × 2 avaliadores independentes. Essa parte não pode ser preenchida honestamente por uma IA: fazê-lo como se duas pessoas tivessem avaliado as respostas seria fabricar evidência.

Por isso, `avaliacao_humana_10x2.csv` foi preparado com os 10 casos selecionados e os 14 campos de notas. A etapa humana continua pendente até que duas pessoas reais registrem suas notas independentemente.

Casos: P1, P2, P3, P4, P5, M1, M2, M3, O1 e O2.

Escala: 1 a 5 para relevância, factualidade, completude, clareza, adequação, segurança e qualidade multimodal.

## 4. Comparação histórica

Trabalho 1:
- Claude Sonnet 5: 99,25/100.
- Grok 4.5: 95,75/100.
- Gemini 3.1 Pro Preview: 91,25/100.
- A comparação de eficiência do Trabalho 1 usou valores de referência, não telemetria real das 12 execuções.

Trabalho 2:
- definiu o baseline v0.1 e sete casos iniciais;
- os resultados reais desses sete casos não foram medidos naquele trabalho.

Trabalho 3:
- introduziu biblioteca de prompts versionada;
- as saídas de referência foram explicitamente tratadas como simulações determinísticas, não como evidência empírica.

Trabalho 4:
- tornou o fluxo textual executável;
- preservou 13 comportamentos/casos.

Trabalho 5:
- adicionou PDF/TXT/imagem, OCR e RAG;
- consolidou 20 casos e executou a suíte local.

Trabalho 6:
- congela o artefato v1.0-final;
- registra evidência local, evidência de LLM real e a pendência da avaliação humana.

## 5. Gate final

DECISÃO: APROVADO COM RESSALVAS PARA ENTREGA ACADÊMICA.

Justificativa:
- a suíte de 20 casos foi executada;
- os controles de segurança e multimodalidade foram demonstrados;
- há evidência adicional de comportamento de um LLM real;
- não foram observados critérios eliminatórios na execução local;
- a avaliação humana 10 × 2 ainda precisa ser realizada por pessoas reais;
- custo e telemetria de API continuam sem medição.

Aprovação acadêmica não equivale a autorização de produção. Para produção seriam necessários testes com dados autorizados, revisão de segurança, governança, observabilidade, definição de responsáveis, aprovação de negócio e avaliação humana concluída.
