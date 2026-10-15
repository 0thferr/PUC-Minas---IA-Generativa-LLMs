from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
CATALOGO = ROOT / "prompts" / "catalogo.csv"

def carregar_prompt(prompt_id: str, versao: str = "v1.0") -> dict:
    with CATALOGO.open(encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            if row["ID"] == prompt_id and row["Versao_ativa"] == versao:
                caminho = ROOT / "prompts" / row["Arquivo"]
                return {
                    "id": prompt_id,
                    "versao": versao,
                    "conteudo": caminho.read_text(encoding="utf-8"),
                    "arquivo": str(caminho),
                }
    raise ValueError(f"Prompt não encontrado: {prompt_id} {versao}")

def carregar_politica() -> str:
    return (ROOT / "prompts" / "politica_aurora_tech.txt").read_text(encoding="utf-8")
