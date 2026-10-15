import json
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
LOG_DIR = ROOT / "evidencias"
LOG_DIR.mkdir(exist_ok=True)

def registrar(evento: dict, nome: str):
    evento = dict(evento)
    evento["timestamp"] = datetime.now().isoformat(timespec="seconds")
    caminho = LOG_DIR / f"{nome}.json"
    caminho.write_text(json.dumps(evento, ensure_ascii=False, indent=2), encoding="utf-8")
    return caminho
