import json

ROTAS = {"T1_CONSULTAR_REGRA", "T2_VERIFICAR_SITUACAO", "T3_ENCAMINHAR", "FORA_DO_ESCOPO"}
CLASSIFICACOES = {"COMPATIVEL", "NAO_DETERMINADO", "ENCAMINHAR", "FORA_DO_ESCOPO"}

def validar_entrada(texto):
    if not isinstance(texto, str) or not texto.strip():
        return False, "A solicitação está vazia."
    if len(texto) > 5000:
        return False, "A solicitação excede o tamanho permitido."
    return True, None

def parse_json(raw):
    if isinstance(raw, dict):
        return raw
    return json.loads(raw)

def validar_rota(raw):
    obj = parse_json(raw)
    if set(obj.keys()) != {"tarefa", "justificativa"}:
        raise ValueError("Formato do roteador inválido.")
    if obj["tarefa"] not in ROTAS:
        raise ValueError("Rota não permitida.")
    return obj

def validar_saida(prompt_id, raw):
    if prompt_id in {"PROMPT-02", "PROMPT-04"}:
        obj = parse_json(raw)
        if prompt_id == "PROMPT-02":
            obrigatorios = {"classificacao", "fundamentacao", "regra_aplicada", "proximo_passo"}
            if set(obj.keys()) != obrigatorios or obj["classificacao"] not in CLASSIFICACOES:
                raise ValueError("JSON especialista inválido.")
        return obj

    campos = {
        "PROMPT-01": ["Resposta:", "Fundamentação/Regra aplicada:", "Próximo passo:"],
        "PROMPT-03": ["Situação:", "Limite do copiloto:", "Encaminhamento:", "Mensagem ao usuário:"],
    }
    for campo in campos[prompt_id]:
        if campo not in str(raw):
            raise ValueError(f"Campo obrigatório ausente: {campo}")
    return raw
