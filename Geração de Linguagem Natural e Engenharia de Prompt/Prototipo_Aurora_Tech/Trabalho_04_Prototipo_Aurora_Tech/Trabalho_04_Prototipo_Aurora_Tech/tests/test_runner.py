import csv, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "prototype"))
from app import executar

ROOT = Path(__file__).resolve().parents[1]

def run():
    rows = []
    with (ROOT/"tests"/"casos.csv").open(encoding="utf-8-sig") as f:
        for caso in csv.DictReader(f):
            entrada = caso["Entrada"]
            # Caso de correção: mantém somente a correção como contexto útil.
            if caso["ID"] == "P5" and "Correção:" in entrada:
                entrada = entrada.split("Correção:", 1)[1].strip()
            fail_mode = caso.get("Fail_mode") or None
            result = executar(entrada, caso["ID"], fail_mode=fail_mode)
            esperado_rota = caso["Rota_esperada"]
            rota_ok = result.get("rota") == esperado_rota or result.get("acao") == esperado_rota
            if esperado_rota == "PEDIR_ESCLARECIMENTO":
                rota_ok = result.get("acao") == "PEDIR_ESCLARECIMENTO"
            rows.append({
                "ID":caso["ID"], "Categoria":caso["Categoria"], "Rota":result.get("rota"),
                "Prompt_ID":result.get("prompt_id"), "Versao":"v1.0",
                "Acao":result.get("acao"), "Status":result.get("status"),
                "Validacao":result.get("validacao"), "Latencia_ms":result.get("latencia_ms"),
                "Tentativas":result.get("tentativas"), "Repeticao":result.get("repeticao"),
                "Falha":result.get("falha"), "Resultado_esperado":caso["Resultado_esperado"],
                "Passou":rota_ok, "Saida":json.dumps(result.get("resposta"), ensure_ascii=False)
            })
    with (ROOT/"tests"/"resultados.csv").open("w",newline="",encoding="utf-8-sig") as f:
        w=csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    return rows

if __name__ == "__main__":
    rows=run()
    for r in rows:
        print(r["ID"], "PASSOU" if r["Passou"] else "FALHOU", "|", r["Status"], "|", r["Prompt_ID"])
