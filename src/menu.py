from src.backup import executar_backup
from src.config import carregar_config, salvar_config


def alterar_configuracoes():
    print("\n=== Alterar Configurações ===")

    origem = input("Nova pasta de origem: ")
    destino = input("Nova pasta de destino: ")

    salvar_config(origem, destino)

    print("\nConfigurações salvas com sucesso!")


def visualizar_configuracoes():
    config = carregar_config()

    print("\n=== Configurações Atuais ===")
    print(f"Origem: {config.get('origem')}")
    print(f"Destino: {config.get('destino')}")


def exibir_menu():
    while True:
        print("\n=== Sistema de Backup ===")
        print("1 - Executar backup")
        print("2 - Ver configurações")
        print("3 - Alterar configurações")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            executar_backup()

        elif opcao == "2":
            visualizar_configuracoes()

        elif opcao == "3":
            alterar_configuracoes()

        elif opcao == "4":
            print("\nEncerrando sistema...")
            break

        else:
            print("\nOpção inválida.")