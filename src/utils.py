import os
from datetime import datetime


def gerar_nome_backup():
    data_atual = datetime.now()
    return data_atual.strftime("backup_%Y-%m-%d_%H-%M-%S")


def verificar_pasta(caminho):
    return os.path.exists(caminho)