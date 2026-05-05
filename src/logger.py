from datetime import datetime


def registrar_log(origem, destino, total_arquivos, total_pastas, status, detalhes=""):
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open("backup.log", "a", encoding="utf-8") as arquivo:
        arquivo.write("=" * 50 + "\n")
        arquivo.write(f"Data/Hora: {data_hora}\n")
        arquivo.write(f"Origem: {origem}\n")
        arquivo.write(f"Destino: {destino}\n")
        arquivo.write(f"Arquivos copiados: {total_arquivos}\n")
        arquivo.write(f"Pastas copiadas: {total_pastas}\n")
        arquivo.write(f"Status: {status}\n")

        if detalhes:
            arquivo.write(f"Detalhes: {detalhes}\n")

        arquivo.write("\n")