import os
import shutil

from src.utils import gerar_nome_backup, verificar_pasta
from src.logger import registrar_log
from src.config import carregar_config


def contar_itens(pasta):
    total_arquivos = 0
    total_pastas = 0

    for raiz, pastas, arquivos in os.walk(pasta):
        total_pastas += len(pastas)
        total_arquivos += len(arquivos)

    return total_arquivos, total_pastas


def criar_backup_zip(origem, destino, nome_backup):
    caminho_zip = os.path.join(destino, nome_backup)

    shutil.make_archive(
        caminho_zip,
        "zip",
        origem
    )

    return caminho_zip + ".zip"


def executar_backup():
    print("\n=== Executando Backup ===")

    config = carregar_config()

    origem = config.get("origem")
    destino = config.get("destino")

    if not verificar_pasta(origem):
        print("Erro: pasta de origem não encontrada.")
        return

    if not verificar_pasta(destino):
        print("Erro: pasta de destino não encontrada.")
        return

    nome_backup = gerar_nome_backup()

    try:
        caminho_zip = criar_backup_zip(
            origem,
            destino,
            nome_backup
        )

        total_arquivos, total_pastas = contar_itens(origem)

        registrar_log(
            origem,
            caminho_zip,
            total_arquivos,
            total_pastas,
            "Sucesso"
        )

        print("\nBackup compactado criado com sucesso!")
        print(f"Arquivo: {caminho_zip}")
        print(f"Arquivos copiados: {total_arquivos}")
        print(f"Pastas copiadas: {total_pastas}")

    except PermissionError:
        registrar_log(
            origem,
            destino,
            0,
            0,
            "Erro",
            "Permissão negada"
        )

        print("Erro: permissão negada.")

    except Exception as erro:
        registrar_log(
            origem,
            destino,
            0,
            0,
            "Erro inesperado",
            str(erro)
        )

        print("Erro inesperado.")
        print(f"Detalhes: {erro}")