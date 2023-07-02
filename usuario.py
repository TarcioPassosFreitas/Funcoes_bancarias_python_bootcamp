import re

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = self.limpar_e_validar_cpf(cpf)
        self.endereco = endereco

    def limpar_e_validar_cpf(self, cpf):
        cpf = re.sub(r'\D', '', cpf)

        if len(cpf) != 11:
            raise ValueError("CPF inválido")

        if cpf == cpf[0] * 11:
            raise ValueError("CPF inválido")

        for i in range(9, 11):
            soma = sum(int(d) * (i+1 - j) for j, d in enumerate(cpf[:i]))
            digito = (soma * 10) % 11
            digito = 0 if digito == 10 else digito
            if cpf[i] != str(digito):
                raise ValueError("CPF inválido")

        return cpf
