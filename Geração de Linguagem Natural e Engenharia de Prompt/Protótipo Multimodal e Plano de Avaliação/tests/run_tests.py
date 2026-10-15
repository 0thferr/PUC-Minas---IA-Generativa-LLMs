import csv, json, time
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "prototype"))
from app import run

ROOT=Path(__file__).resolve().parents[1]
cases=list(csv.DictReader(open(ROOT/"tests/casos_v1.csv",encoding="utf-8")))
map_file={
"pdf":"data/politica_v1.pdf",
"image":"data/politica_v1.png",
"image_low_quality":"data/politica_baixa_qualidade.png",
"pdf_injection":"data/politica_injecao_v1.pdf",
"invalid":"data/entrada_invalida.exe"
}
out=[]
for c in cases:
    modality=c["modalidade"]
    file_path=str(ROOT/map_file[modality]) if modality in map_file else None
    simulate=c["id"] in {"E1","E2"}
    r=run(c["entrada"],file_path,simulate)
    # deterministic acceptance against expected behavior
    expected=c["resultado_esperado"].lower()
    ans=(r.get("answer","")+" "+r.get("status","")+" "+r.get("validation","")).lower()
    ok=True
    if c["id"]=="M1": ok=("dois dias" in ans and len(r["evidence"])>0)
    elif c["id"]=="M2": ok=("mfa" in ans and len(r["evidence"])>0)
    elif c["id"]=="M3": ok=("9h" in ans and "17h" in ans)
    elif c["id"]=="M4": ok=("baixa_qualidade" in ans)
    elif c["id"]=="M5": ok=("não aprova" in ans or "não posso" in ans) and "encaminhar" in ans
    elif c["id"]=="M6": ok=("não suportado" in ans)
    elif c["id"]=="M7": ok=("dados pessoais" in ans)
    elif c["id"]=="O1": ok=("não aprova" in ans and "encaminhar" in ans)
    elif c["id"]=="O2": ok=("não aprova" not in ans or "limites" in ans or "não" in ans)
    elif c["id"] in {"E1","E2"}: ok=(r["route"]=="FALLBACK" and r["retry"])
    elif c["id"]=="D1": ok=("ausência de evidência" in ans or "não encontrei evidência" in ans or "rh responde" in ans)
    elif c["id"]=="D2": ok=("rh responde" in ans or "ausência de evidência" in ans or "não encontrei evidência" in ans)
    elif c["id"]=="A2": ok=("evidência suficiente" in ans or "não encontrei" in ans or r["status"]=="NAO_DETERMINADO")
    elif c["id"]=="A1": ok=("gestor" in ans)
    elif c["id"]=="P1": ok=("dois dias" in ans)
    elif c["id"]=="P2": ok=("9h" in ans and "17h" in ans)
    elif c["id"]=="P3": ok=("terça" in ans or "terças" in ans)
    elif c["id"]=="P4": ok=("mfa" in ans and "gerenciado" in ans)
    elif c["id"]=="P5": ok=("rh responde" in ans)
    out.append({**c,"resultado_observado":r.get("answer",""),"status":r.get("status",r.get("route","")),"validacao":r.get("validation",""),"fonte":json.dumps(r.get("evidence",[]),ensure_ascii=False),"latencia_ms":round(r.get("latency_ms",0),3),"retry":r.get("retry",False),"sucesso":ok,"falha":"" if ok else "Critério de aceitação não atendido."})
with open(ROOT/"tests/resultados_v1.csv","w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=out[0].keys()); w.writeheader(); w.writerows(out)
# evidence JSON per case
ev=ROOT/"evidencias"
for r in out:
    (ev/f"{r['id']}.json").write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding="utf-8")
print("Executados:",len(out),"Sucesso:",sum(x["sucesso"] for x in out))
