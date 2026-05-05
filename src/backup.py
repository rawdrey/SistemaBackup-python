import os
import shutil
from src.utils import gerar_nome_backup, verificar_pasta


def criar_pasta_backup(destino, nome_backup):
    caminho_backup = os.path.join(destino, nome_backup)
    os.makedirs(caminho_backup, exist_ok=True)
    return caminho_backup


def copiar_arquivos(origem, destino_backup):
    shutil.copytree(origem, destino_backup, dirs_exist_ok=True)


def executar_backup():
    print("=== Sistema de Backup em Python ===")

    origem = input("Digite o caminho da pasta de origem: ")
    destino = input("Digite o caminho da pasta onde o backup será salvo: ")

    if not verificar_pasta(origem):
        print("Erro: a pasta de origem não existe.")
        return

    if not verificar_pasta(destino):
        print("Erro: a pasta de destino não existe.")
        return

    nome_backup = gerar_nome_backup()
    caminho_backup = criar_pasta_backup(destino, nome_backup)

    copiar_arquivos(origem, caminho_backup)

    print("\nBackup finalizado com sucesso!")
    print(f"Destino: {caminho_backup}")