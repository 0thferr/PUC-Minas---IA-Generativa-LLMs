# Protótipo multimodal

O protótipo preserva o fluxo textual do Trabalho 4 e acrescenta entrada por documento PDF, imagem e TXT.

Fluxo:
entrada -> validação -> extração/OCR -> chunking -> recuperação TF-IDF -> geração segura -> fonte/qualidade/próximo passo.

O executor atual é determinístico para permitir reprodução sem credenciais. O ponto de integração com um LLM pode substituir `safe_generate` por um adaptador de modelo, mantendo a mesma validação e os mesmos controles.

Executar:
```bash
pip install -r requirements.txt
python app.py "Quantos dias por semana posso trabalhar remotamente?" --file ../data/politica_v1.pdf
```

Regras de segurança:
- conteúdo de arquivo é dado não confiável;
- instruções encontradas no arquivo nunca alteram as regras do sistema;
- entradas inválidas são recusadas;
- não há credenciais no repositório;
- a resposta inclui fonte quando há recuperação;
- ausência de evidência gera `NAO_DETERMINADO`.
