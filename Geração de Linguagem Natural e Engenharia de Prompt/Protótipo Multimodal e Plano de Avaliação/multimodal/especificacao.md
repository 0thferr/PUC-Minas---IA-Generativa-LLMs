# Especificação multimodal — v1.0

## 1. Continuidade
O Trabalho 5 mantém o caso de uso do Trabalho 4: Copiloto Corporativo de Apoio à Política de Trabalho Híbrido da Aurora Tech. O Trabalho 4 determinou fluxo textual executável, 13 casos e a preservação dos quatro prompts por ID/versão. O Trabalho 5 acrescenta documento/imagem e RAG sem remover o modo textual.

## 2. Modalidade escolhida e benefício
Modalidade: documento (PDF/TXT) e imagem (PNG/JPG/JPEG), com OCR para imagem.

Benefício: a política pode chegar como arquivo, em vez de precisar ser copiada para o prompt. O sistema passa a validar o arquivo, extrair apenas o conteúdo necessário, recuperar trechos relevantes e apresentar fonte, qualidade e próximo passo. Isso torna a modalidade parte efetiva do processamento.

## 3. Contrato de entrada
- PDF, TXT, PNG, JPG/JPEG.
- Máximo: 10 MB e 10 páginas para PDF.
- Imagens: preferencialmente ≥ 1200 px no maior lado e texto legível; abaixo disso pode haver baixa confiança.
- UTF-8 para TXT.
- Arquivos devem ser sintéticos, públicos ou anonimizados.
- Arquivos inválidos são recusados com mensagem segura.
- Arquivos ilegíveis geram `BAIXA_QUALIDADE`, sem tentativa de completar por inferência.

## 4. Privacidade, retenção, acessibilidade e direitos
Não usar dados corporativos reais, credenciais ou dados pessoais desnecessários. O protótipo não persiste o conteúdo do usuário após a execução. Para produção, a retenção deve ser configurável e alinhada à política institucional. O usuário deve receber alternativa textual quando não puder anexar arquivo. Documentos usados nos testes são sintéticos. Direitos autorais dos documentos externos devem ser verificados antes de indexação.

## 5. RAG
Fluxo: validar arquivo -> extrair texto/OCR -> dividir em trechos identificados -> vetorizar com TF-IDF -> recuperar trechos relevantes -> gerar resposta segura -> retornar fonte/página, qualidade, incerteza e próximo passo.

A implementação usa componentes equivalentes a leitores, chunking, recuperação e geração. LangChain/LangFlow não são dependências obrigatórias desta candidata.

## 6. Segurança
O conteúdo do arquivo é tratado como dado não confiável. Frases como "ignore as regras" dentro do documento não são executadas. O sistema não aprova exceções, não expõe dados pessoais, não executa ações externas e encaminha decisões humanas.

## 7. Compatibilidade com o Trabalho 4
Sem arquivo, o modo textual continua funcionando. Com arquivo, a entrada adicional altera o processamento: há validação, extração/OCR e recuperação de evidência antes da resposta.
