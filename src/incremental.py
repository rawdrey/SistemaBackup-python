import json
import os

ARQUIVO_ESTADO = "backup_state.json"


def carregar_estado():
    if not os.path.exists(ARQUIVO_ESTADO):
        return {}

    with open(ARQUIVO_ESTADO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_estado(estado):
    with open(ARQUIVO_ESTADO, "w", encoding="utf-8") as arquivo:
        json.dump(estado, arquivo, indent=4)


def obter_arquivos_modificados(origem):
    estado_atual = {}
    estado_anterior = carregar_estado()
    arquivos_modificados = []

    for raiz, pastas, arquivos in os.walk(origem):
        for nome_arquivo in arquivos:
            caminho_completo = os.path.join(raiz, nome_arquivo)
            caminho_relativo = os.path.relpath(caminho_completo, origem)

            data_modificacao = os.path.getmtime(caminho_completo)
            estado_atual[caminho_relativo] = data_modificacao

            if caminho_relativo not in estado_anterior:
                arquivos_modificados.append(caminho_completo)
            elif estado_anterior[caminho_relativo] != data_modificacao:
                arquivos_modificados.append(caminho_completo)

    salvar_estado(estado_atual)

    return arquivos_modificados