# Arquitetura v1.0

```text
Usuário
  |
  v
Entrada textual + arquivo opcional
  |
  v
Validação de tipo/tamanho/páginas
  |---- inválido ----> recusa segura
  |
  v
Extração PDF/TXT ou OCR de imagem
  |---- ilegível ----> baixa qualidade + pedir nova entrada
  |
  v
Chunking identificado
  |
  v
Recuperação RAG (TF-IDF)
  |
  v
Roteamento TRH-04
  |
  +--> TRH-01 explicar regra
  +--> TRH-02 verificar situação
  +--> TRH-03 orientar segurança
  +--> encaminhar/recusar
  |
  v
Validação da resposta
  |
  v
Resposta + fonte + qualidade + incerteza + próximo passo

O arquivo nunca é tratado como instrução de sistema.
