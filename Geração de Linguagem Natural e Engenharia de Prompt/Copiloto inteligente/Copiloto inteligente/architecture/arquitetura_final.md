# Arquitetura final

Interface textual/multimodal → validação da entrada → validação de arquivo → extração PDF/TXT ou OCR → chunking → recuperação TF-IDF → triagem TRH-04 → especialista TRH-01/TRH-02/TRH-03 → validação da saída → uma tentativa de correção → resposta com evidência/fonte ou fallback seguro → revisão humana quando houver decisão individual → logs/auditoria.

Arquivos são tratados como dados não confiáveis; conteúdo recuperado não pode substituir as instruções do sistema. O fluxo não aprova exceções, não altera a política e não expõe dados pessoais desnecessários.

LangGraph e MCP: não há evidência nos materiais consolidados de que tenham sido efetivamente implementados na versão final. Portanto, não são declarados como componentes implementados; ficam como evolução arquitetural possível.
