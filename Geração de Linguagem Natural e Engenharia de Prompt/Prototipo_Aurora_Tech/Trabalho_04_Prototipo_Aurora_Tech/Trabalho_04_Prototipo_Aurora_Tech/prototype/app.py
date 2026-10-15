from prompt_loader import carregar_prompt, carregar_politica
from validator import validar_entrada, validar_rota, validar_saida
from model_client import call_model
from logger import registrar
import json

ROTA_PROMPT = {
    "T1_CONSULTAR_REGRA": "PROMPT-01",
    "T2_VERIFICAR_SITUACAO": "PROMPT-02",
    "T3_ENCAMINHAR": "PROMPT-03",
}

def _ambigua(texto):
    t = texto.strip().lower()
    return t in {"posso trabalhar de casa?", "e na terça?", "e se for diferente?"}

def _faltando_dados(texto):
    t = texto.lower()
    if t in {"minha situação é compatível?", "sou elegível?", "minha função pode trabalhar remoto?"}:
        return "Descreva apenas a situação ou função relevante para a política, sem dados pessoais desnecessários."
    return None

def executar(solicitacao, teste_id="manual", versao="v1.0", fail_mode=None):
    valido, erro = validar_entrada(solicitacao)
    log = {
        "teste_id": teste_id, "entrada": solicitacao, "versao": versao,
        "tentativas": 0, "repeticao": False, "latencia_ms": 0,
        "rota": None, "prompt_id": None, "validacao": None, "status": None, "falha": None
    }
    if not valido:
        log.update({"acao":"PEDIR_ESCLARECIMENTO","resposta":erro,"status":"entrada_invalida"})
        registrar(log, teste_id)
        return log

    if _ambigua(solicitacao):
        resposta = "A solicitação está ambígua. Especifique qual regra ou situação da política de trabalho híbrido você quer verificar."
        log.update({"acao":"PEDIR_ESCLARECIMENTO","resposta":resposta,"status":"ambiguidade"})
        registrar(log, teste_id)
        return log

    # TRIAGEM: PROMPT-04
    triagem = carregar_prompt("PROMPT-04", versao)
    for tentativa in (1, 2):
        try:
            raw, lat = call_model("PROMPT-04", triagem["conteudo"], solicitacao, fail_mode if fail_mode=="invalid_json_router" else None, tentativa)
            rota = validar_rota(raw)
            log["latencia_ms"] += lat
            log["tentativas"] += 1
            log["repeticao"] = tentativa == 2
            break
        except Exception as e:
            log["tentativas"] += 1
            if tentativa == 2:
                log.update({"acao":"FALHA_SEGURA","resposta":"Não foi possível processar a solicitação com segurança. Tente novamente mais tarde ou utilize o canal responsável.","status":"falha_triagem","falha":str(e),"validacao":"falhou"})
                registrar(log, teste_id)
                return log
    log["rota"] = rota["tarefa"]

    if rota["tarefa"] == "FORA_DO_ESCOPO":
        log.update({"acao":"RECUSAR","resposta":"Esta solicitação está fora do escopo da política de trabalho híbrido da Aurora Tech.","status":"fora_do_escopo","validacao":"aprovada"})
        registrar(log, teste_id)
        return log

    faltante = _faltando_dados(solicitacao)
    if faltante:
        log.update({"acao":"PEDIR_ESCLARECIMENTO","resposta":faltante,"status":"dados_ausentes","validacao":"aprovada"})
        registrar(log, teste_id)
        return log

    prompt_id = ROTA_PROMPT[rota["tarefa"]]
    especialista = carregar_prompt(prompt_id, versao)
    log["prompt_id"] = prompt_id

    for tentativa in (1, 2):
        try:
            raw, lat = call_model(prompt_id, especialista["conteudo"], solicitacao, fail_mode, tentativa)
            saida = validar_saida(prompt_id, raw)
            log["latencia_ms"] += lat
            log["tentativas"] += 1
            log["repeticao"] = tentativa == 2
            log.update({"acao":"RESPONDER","resposta":saida,"status":"sucesso","validacao":"aprovada"})
            registrar(log, teste_id)
            return log
        except Exception as e:
            log["tentativas"] += 1
            log["repeticao"] = True
            if tentativa == 2:
                log.update({"acao":"FALHA_SEGURA","resposta":"Não foi possível concluir a resposta com segurança. Tente novamente mais tarde ou procure o canal responsável.","status":"falha_tecnica","falha":str(e),"validacao":"falhou"})
                registrar(log, teste_id)
                return log

if __name__ == "__main__":
    while True:
        texto = input("\nSolicitação (ou 'sair'): ").strip()
        if texto.lower() == "sair":
            break
        resultado = executar(texto)
        print(json.dumps(resultado, ensure_ascii=False, indent=2))
