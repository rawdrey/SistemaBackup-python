import os
import zipfile

from src.utils import gerar_nome_backup, verificar_pasta
from src.logger import registrar_log
from src.config import carregar_config
from src.incremental import obter_arquivos_modificados


def criar_backup_incremental_zip(origem, destino, nome_backup, arquivos):
    caminho_zip = os.path.join(destino, nome_backup + ".zip")

    with zipfile.ZipFile(caminho_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
        for caminho_arquivo in arquivos:
            caminho_relativo = os.path.relpath(caminho_arquivo, origem)
            zipf.write(caminho_arquivo, caminho_relativo)

    return caminho_zip


def executar_backup():
    print("\n=== Executando Backup Incremental ===")

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
        arquivos_modificados = obter_arquivos_modificados(origem)

        if not arquivos_modificados:
            print("\nNenhum arquivo novo ou modificado encontrado.")
            registrar_log(
                origem,
                destino,
                0,
                0,
                "Nenhuma alteração"
            )
            return

        caminho_zip = criar_backup_incremental_zip(
            origem,
            destino,
            nome_backup,
            arquivos_modificados
        )

        registrar_log(
            origem,
            caminho_zip,
            len(arquivos_modificados),
            0,
            "Sucesso"
        )

        print("\nBackup incremental criado com sucesso!")
        print(f"Arquivo: {caminho_zip}")
        print(f"Arquivos adicionados ao backup: {len(arquivos_modificados)}")

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