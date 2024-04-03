import csv

def ler_dados_csv(nome_arquivo):
    dados = []
    try:
        with open(nome_arquivo, 'r') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                dados.append(linha)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    return dados

def escrever_dados_csv(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'w', newline='') as arquivo:
            campos = list(dados[0].keys()) if dados else []
            campos.extend(['x_position', 'y_position'])
            escritor = csv.DictWriter(arquivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(dados)
    except IOError:
        print("Erro ao escrever no arquivo.")

def adicionar_registro(nome_arquivo, dados):
    timestamp = input("Digite o timestamp do clique: ")
    x_position = input("Digite a posição X do clique: ")
    y_position = input("Digite a posição Y do clique: ")

    novo_registro = {"timestamp": timestamp, "x_position": x_position, "y_position": y_position}

    dados.append(novo_registro)
    escrever_dados_csv(nome_arquivo, dados)
    print("Registro adicionado com sucesso.")

def exibir_registros(dados):
    for registro in dados:
        print(registro)

def atualizar_registro(nome_arquivo, dados):
    exibir_registros(dados)
    indice = int(input("Digite o índice do registro a ser atualizado: "))
    if 0 <= indice < len(dados):
        timestamp = input("Digite o novo timestamp do clique: ")
        x_position = input("Digite a nova posição X do clique: ")
        y_position = input("Digite a nova posição Y do clique: ")

        dados[indice]["timestamp"] = timestamp
        dados[indice]["x_position"] = x_position
        dados[indice]["y_position"] = y_position

        escrever_dados_csv(nome_arquivo, dados)
        print("Registro atualizado com sucesso.")
    else:
        print("Índice inválido.")

def excluir_registro(nome_arquivo, dados):
    exibir_registros(dados)
    indice = int(input("Digite o índice do registro a ser excluído: "))
    if 0 <= indice < len(dados):
        del dados[indice]
        escrever_dados_csv(nome_arquivo, dados)
        print("Registro excluído com sucesso.")
    else:
        print("Índice inválido.")

def menu():
    nome_arquivo = "dados_navegacao.csv"
    dados = ler_dados_csv(nome_arquivo)
    while True:
        print("\n=== MENU ===")
        print("1. Adicionar Registro")
        print("2. Exibir Registros")
        print("3. Atualizar Registro")
        print("4. Excluir Registro")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_registro(nome_arquivo, dados)
        elif opcao == "2":
            exibir_registros(dados)
        elif opcao == "3":
            atualizar_registro(nome_arquivo, dados)
        elif opcao == "4":
            excluir_registro(nome_arquivo, dados)
        elif opcao == "5":
            print("Salvando e saindo...")
            escrever_dados_csv(nome_arquivo, dados)
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
