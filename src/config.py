import json
import os

ARQUIVO_CONFIG = "config.json"


def carregar_config():
    if not os.path.exists(ARQUIVO_CONFIG):
        return {"origem": "", "destino": ""}

    with open(ARQUIVO_CONFIG, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_config(origem, destino):
    dados = {
        "origem": origem,
        "destino": destino
    }

    with open(ARQUIVO_CONFIG, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4)