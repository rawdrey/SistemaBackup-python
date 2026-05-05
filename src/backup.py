import os
import shutil
from src.utils import gerar_nome_backup, verificar_pasta


def criar_pasta_backup(destino, nome_backup):
    caminho_backup = os.path.join(destino, nome_backup)
    os.makedirs(caminho_backup, exist_ok=True)
    return caminho_backup


def contar_itens(pasta):
    total_arquivos = 0
    total_pastas = 0

    for raiz, pastas, arquivos in os.walk(pasta):
        total_pastas += len(pastas)
        total_arquivos += len(arquivos)

    return total_arquivos, total_pastas


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

    try:
        copiar_arquivos(origem, caminho_backup)

        total_arquivos, total_pastas = contar_itens(caminho_backup)

        print()
        print("Backup finalizado com sucesso!")
        print(f"Origem: {origem}")
        print(f"Destino: {caminho_backup}")
        print(f"Arquivos copiados: {total_arquivos}")
        print(f"Pastas copiadas: {total_pastas}")

    except PermissionError:
        print("Erro: permissão negada ao copiar algum arquivo ou pasta.")

    except FileNotFoundError:
        print("Erro: algum arquivo ou pasta não foi encontrado durante o backup.")

    except Exception as erro:
        print("Erro inesperado durante o backup.")
        print(f"Detalhes: {erro}")