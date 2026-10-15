import csv, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "prototype"))
from app import executar
ROOT=Path(__file__).resolve().parents[1]

def metricas(resultado):
    status=resultado.get("status")
    saida=str(resultado.get("resposta","")).lower()
    return {
        "Conclusao_util": status in {"sucesso","fora_do_escopo"},
        "Formato_correto": resultado.get("validacao")=="aprovada",
        "Factualidade": status != "falha_tecnica",
        "Encaminhamento_correto": ("service desk" in saida or "rh responde" in saida or "exce" in saida or status=="fora_do_escopo"),
    }

rows=[]
with (ROOT/"tests"/"baseline_trabalho2_reaplicado.csv").open(encoding="utf-8-sig") as f:
    for c in csv.DictReader(f):
        r=executar(c["Pergunta"], f"baseline_{c['ID']}")
        m=metricas(r)
        rows.append({
            "ID":c["ID"], **m, "Latencia_ms":r.get("latencia_ms"),
            "Rota":r.get("rota"), "Prompt_ID":r.get("prompt_id"),
            "Falha_observada":r.get("falha") or ""
        })
with (ROOT/"evaluation"/"baseline_reaplicado_resultados.csv").open("w",newline="",encoding="utf-8-sig") as f:
    w=csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
print("Baseline reaplicado:", len(rows), "casos.")
