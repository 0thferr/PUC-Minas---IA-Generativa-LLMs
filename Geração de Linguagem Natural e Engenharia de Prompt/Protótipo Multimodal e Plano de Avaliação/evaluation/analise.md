# Análise

Os 20 casos foram executados no mesmo artefato `v1.0`. A execução local é determinística e serve como evidência de integração e de validação do protocolo, não como resultado de benchmark de LLM.

A análise automática deve ser lida junto de `tests/resultados_v1.csv`. A avaliação humana de 10 casos por duas pessoas ainda precisa ser preenchida; por isso, ela não é apresentada como concluída.

A candidata deve ser considerada tecnicamente promissora porque a entrada adicional altera o processamento, a recuperação fornece fonte e arquivos inválidos/injeções são tratados antes da geração. A principal ressalva é a ausência de medição com LLM real e de duas avaliações humanas independentes.
