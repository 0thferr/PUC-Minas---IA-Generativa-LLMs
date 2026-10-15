# Manifesto final — Trabalho 6 — Aurora Tech

Versão do release: v1.0-final
Data de consolidação: 18/09/2026
Projeto: Copiloto Corporativo de Apoio à Política de Trabalho Híbrido da Aurora Tech

## Componentes congelados
- Caso de uso: apoio à interpretação da política-piloto de trabalho híbrido.
- Modelo de referência histórico: Claude Sonnet 5, conforme Trabalhos 1–2.
- Evidência empírica adicional nesta entrega: GPT-5.6 Luna, executado nesta sessão como avaliação de LLM real. Esta execução não substitui uma medição da API do Claude.
- Fluxo: validação → extração/OCR → chunking → RAG TF-IDF → triagem → especialista → validação → resposta/fallback.
- Prompts: TRH-01, TRH-02, TRH-03 e TRH-04, versão v1.0.
- Base de conhecimento final de teste: política sintética v1.0 fornecida no pacote do Trabalho 5.
- Suíte: 20 casos, arquivo casos_v1.csv.
- Multimodalidade: PDF, TXT, PNG e JPG/JPEG; OCR para imagens.
- Limites: não aprovar exceções, não alterar política, não solicitar/expor PII desnecessária, não substituir RH/gestores/Service Desk.
- RAG: TF-IDF com evidência identificável por arquivo/página.

## Regra de rastreabilidade
Qualquer mudança no modelo, prompts, base, fluxo, multimodalidade ou conjunto de testes exige nova versão e nova execução dos 20 casos antes do congelamento.
