import json
import os
import re
import time

class TechnicalError(RuntimeError):
    pass

def _tem(texto, *termos):
    t = texto.lower()
    return any(x in t for x in termos)

def _route(texto):
    if _tem(texto, "cpf", "imposto de renda", "futebol", "receita médica", "senha"):
        return {"tarefa": "FORA_DO_ESCOPO", "justificativa": "A solicitação não pertence à política de trabalho híbrido."}
    if _tem(texto, "exceção", "aprovar", "aprove", "incidente", "service desk", "dados pessoais", "cpf"):
        return {"tarefa": "T3_ENCAMINHAR", "justificativa": "A solicitação envolve decisão humana, segurança, privacidade ou encaminhamento."}
    if _tem(texto, "compatível", "compatível?", "situação", "posso trabalhar na terça", "equipe pode", "minha equipe", "minha função"):
        return {"tarefa": "T2_VERIFICAR_SITUACAO", "justificativa": "A solicitação exige comparação de um cenário com a política."}
    return {"tarefa": "T1_CONSULTAR_REGRA", "justificativa": "A solicitação pede informação ou interpretação de uma regra."}

def _p1(texto):
    t = texto.lower()
    if _tem(t, "dias", "dois dias", "quantos dias"):
        r, f, p = "Até dois dias remotos por semana para colaboradores elegíveis.", "A política permite até dois dias remotos por semana e determina que os dias sejam definidos com o gestor.", "Defina os dias com o gestor."
    elif _tem(t, "horário", "9h", "17h", "disponibilidade"):
        r, f, p = "A disponibilidade esperada é entre 9h e 17h.", "A política estabelece disponibilidade esperada entre 9h e 17h.", "Organize a jornada dentro desse período conforme as orientações internas."
    elif _tem(t, "segurança", "mfa", "dispositivo"):
        r, f, p = "O trabalho remoto exige MFA e uso de dispositivos gerenciados.", "A política exige autenticação multifator e dispositivos gerenciados.", "Se houver incidente de segurança, encaminhe-o ao Service Desk."
    elif _tem(t, "terça"):
        r, f, p = "Há presença comum presencial às terças-feiras.", "A política determina presença comum presencial às terças-feiras.", "Alinhe qualquer situação excepcional com o responsável competente."
    else:
        r, f, p = "A política não contém informação suficiente para responder de forma conclusiva.", "A regra solicitada não está determinada na base fornecida.", "Encaminhe a dúvida ao RH Responde."
    return f"Resposta:\n{r}\n\nFundamentação/Regra aplicada:\n{f}\n\nPróximo passo:\n{p}"

def _p2(texto):
    t = texto.lower()
    if _tem(t, "terça"):
        return {"classificacao":"ENCAMINHAR","fundamentacao":"A política determina presença comum presencial às terças-feiras.","regra_aplicada":"Há presença comum presencial às terças-feiras.","proximo_passo":"Alinhar qualquer exceção com o responsável competente."}
    if _tem(t, "minha função", "elegível") and not _tem(t, "função é", "desenvolvedor", "administrativo"):
        return {"classificacao":"NAO_DETERMINADO","fundamentacao":"A situação não informa fatos suficientes para verificar a condição.","regra_aplicada":None,"proximo_passo":"Informe apenas a descrição da situação ou da função relevante para a política."}
    return {"classificacao":"NAO_DETERMINADO","fundamentacao":"Não há fatos suficientes para comparar a situação com a política.","regra_aplicada":None,"proximo_passo":"Informe a situação concreta que deve ser comparada."}

def _p3(texto):
    t = texto.lower()
    if _tem(t, "incidente", "vazamento", "segurança"):
        sit, lim, enc, msg = "Incidente de segurança.", "O copiloto não substitui o canal de tratamento de incidentes.", "Service Desk.", "Registre o incidente pelo Service Desk."
    elif _tem(t, "exceção", "aprovar", "aprove"):
        sit, lim, enc, msg = "Pedido de exceção ou aprovação.", "O copiloto não aprova nem registra exceções.", "Responsável humano conforme a política; em dúvida, RH Responde.", "Não posso aprovar a exceção. Encaminhe o pedido para decisão humana."
    elif _tem(t, "cpf", "dados pessoais"):
        sit, lim, enc, msg = "Solicitação de dado pessoal de terceiro.", "O copiloto não expõe dados pessoais desnecessários.", "Canal corporativo responsável, se houver necessidade legítima.", "Não posso fornecer esse dado pessoal."
    else:
        sit, lim, enc, msg = "Dúvida ou encaminhamento.", "O copiloto não substitui o canal responsável.", "RH Responde.", "Encaminhe a dúvida ao RH Responde."
    return f"Situação:\n{sit}\n\nLimite do copiloto:\n{lim}\n\nEncaminhamento:\n{enc}\n\nMensagem ao usuário:\n{msg}"

def call_reference(prompt_id, solicitacao, fail_mode=None, attempt=1):
    if fail_mode == "timeout" and attempt == 1:
        raise TechnicalError("Timeout simulado.")
    if prompt_id == "PROMPT-04":
        raw = json.dumps(_route(solicitacao), ensure_ascii=False)
    elif prompt_id == "PROMPT-01":
        raw = _p1(solicitacao)
    elif prompt_id == "PROMPT-02":
        raw = json.dumps(_p2(solicitacao), ensure_ascii=False)
    elif prompt_id == "PROMPT-03":
        raw = _p3(solicitacao)
    else:
        raise ValueError("Prompt desconhecido.")
    if fail_mode == "invalid_json" and attempt == 1 and prompt_id in {"PROMPT-04","PROMPT-02"}:
        raw = "{ json inválido"
    return raw

def call_model(prompt_id, prompt, solicitacao, fail_mode=None, attempt=1):
    mode = os.getenv("EXECUTION_MODE", "reference").lower()
    start = time.perf_counter()
    if mode == "reference":
        raw = call_reference(prompt_id, solicitacao, fail_mode, attempt)
    elif mode == "anthropic":
        try:
            from anthropic import Anthropic
        except ImportError as e:
            raise TechnicalError("Dependência anthropic não instalada.") from e
        client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
        model = os.getenv("MODEL_NAME", "claude-sonnet-4-5")
        user_prompt = prompt.replace("{{texto_base}}", "").replace("{{pergunta}}", solicitacao).replace("{{situacao}}", solicitacao).replace("{{solicitacao}}", solicitacao)
        response = client.messages.create(model=model, max_tokens=800, temperature=0, messages=[{"role":"user","content":user_prompt}])
        raw = response.content[0].text
    else:
        raise TechnicalError(f"Modo desconhecido: {mode}")
    latency_ms = round((time.perf_counter() - start) * 1000, 2)
    return raw, latency_ms
