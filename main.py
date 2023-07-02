import banco

def obter_conta_usuario(nome):
    usuario = banco.buscar_usuario(nome)
    if usuario is None:
        print(f"Usuário {nome} não encontrado.")
        return None, None

    for conta in banco.contas:
        if conta.usuario == usuario:
            return usuario, conta

    print(f"Usuário {nome} não tem uma conta corrente.")
    return usuario, None

def main():
    while True:
        print("\n=== Menu ===")
        print("1 - Criar usuário")
        print("2 - Criar conta corrente")
        print("3 - Listar usuários")
        print("4 - Listar contas")
        print("5 - Depositar")
        print("6 - Sacar")
        print("7 - Extrato")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do usuário: ")
            data_nascimento = input("Digite a data de nascimento (DD-MM-YYYY): ")
            cpf = input("Digite o CPF (apenas números): ")
            endereco = input("Digite o endereço: ")
            banco.criar_usuario(nome, data_nascimento, cpf, endereco)

        elif opcao == '2':
            nome = input("Digite o nome do usuário para criar a conta: ")
            usuario = banco.buscar_usuario(nome)
            if usuario is not None:
                banco.criar_conta_corrente(usuario)

        elif opcao == '3':
            print("\n=== Usuários ===")
            for usuario in banco.usuarios:
                print(f"Nome: {usuario.nome}, CPF: {usuario.cpf}")

        elif opcao == '4':
            print("\n=== Contas ===")
            banco.listar_contas()

        elif opcao == '5':
            nome = input("Digite o nome do usuário para depósito: ")
            valor = float(input("Digite o valor do depósito: "))
            usuario, conta = obter_conta_usuario(nome)
            if conta is not None:
                conta.depositar(valor)

        elif opcao == '6':
            nome = input("Digite o nome do usuário para saque: ")
            valor = float(input("Digite o valor do saque: "))
            usuario, conta = obter_conta_usuario(nome)
            if conta is not None:
                conta.sacar(valor=valor)

        elif opcao == '7':
            nome = input("Digite o nome do usuário para extrato: ")
            usuario, conta = obter_conta_usuario(nome)
            if conta is not None:
                conta.extrato(0)

        elif opcao == '0':
            print("Saindo")
            break

        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
