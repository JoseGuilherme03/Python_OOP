class Conta_Corrente():
    def __init__(self, nome, numero_da_conta=0, saldo=0):
        self.numero_da_conta = numero_da_conta
        self._nome = nome
        self.saldo = saldo

    def deposito(self, valor):
        if valor >= 0:
            self.saldo += valor
        else:
            raise ValueError("Depósito invalido")

    def saque(self, valor):
        if valor <= self.saldo and valor >= 0:
            self.saldo -= valor
        else:
            raise ValueError("Saque invalido")

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome


pessoa = Conta_Corrente(nome="João", numero_da_conta=123, saldo=1000)
pessoa.deposito(100)
print(pessoa.saldo)
pessoa.saque(500)
print(pessoa.saldo)
pessoa.nome = "Maria"
print(pessoa.nome)
