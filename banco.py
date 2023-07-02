from usuario import Usuario
from conta import ContaBancaria

usuarios = []
contas = []

def criar_usuario(nome, data_nascimento, cpf, endereco):
    try:
        usuario = Usuario(nome, data_nascimento, cpf, endereco)
        if not any(u.cpf == cpf for u in usuarios):
            usuarios.append(usuario)
            print(f"Usuário {nome} criado com sucesso.")
        else:
            print("Erro ao criar o usuário: CPF já existe.")
    except ValueError as e:
        print(f"Erro ao criar o usuário: {e}")

def criar_conta_corrente(usuario):
    if usuario in usuarios:
        conta = ContaBancaria(usuario)
        contas.append(conta)
        print(f"Conta número {conta.numero_conta} criada com sucesso.")
    else:
        print("Erro ao criar a conta: usuário não encontrado.")

def listar_contas():
    for conta in contas:
        print(f"Agência: {conta.numero_agencia} Conta: {conta.numero_conta} Usuário: {conta.usuario.nome}")

def buscar_usuario(nome):
    for usuario in usuarios:
        if usuario.nome == nome:
            print(f"Usuário encontrado: {usuario.nome}, CPF: {usuario.cpf}")
            return usuario
    print("Usuário não encontrado.")
    return None
