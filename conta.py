from usuario import Usuario

contador_contas = 1

class ContaBancaria:
    def __init__(self, usuario):
        global contador_contas
        self.numero_agencia = '0001'
        self.numero_conta = str(contador_contas)
        contador_contas += 1
        self.usuario = usuario
        self.saldo = 0.0
        self.transacoes = []
        self.saques_diarios = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(('Depósito', valor))
            print(f"Depósito de R$: {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")
        return self.saldo, self.transacoes

    def sacar(self, *, valor, extrato=None, limite=None, numero_saques=None, limite_saques=None):
        if self.saques_diarios >= 3:
            print("Limite de saques diários atingido.")
            return
        if valor > 500:
            print("O limite máximo por saque é de R$: 500,00.")
            return
        if self.saldo >= valor:
            self.saldo -= valor
            self.transacoes.append(('Saque', valor))
            self.saques_diarios += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente para o saque.")
        return self.saldo, self.transacoes

    def extrato(self, saldo, *, extrato=None):
        print(f"\nExtrato - Ag: {self.numero_agencia} Conta: {self.numero_conta}")
        for operacao, valor in self.transacoes:
            print(f"{operacao}: R$: {valor:.2f}")
        print(f"Saldo atual: R$: {self.saldo:.2f}")
        print(f"Total de operações: {len(self.transacoes)}\n")
        return self.saldo, self.transacoes
