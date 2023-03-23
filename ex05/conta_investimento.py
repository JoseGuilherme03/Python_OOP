class Conta_Investimento():
    def __init__(self, nome, numero_da_conta, saldo=1000, juros=0.10):
        self.numero_da_conta = numero_da_conta
        self._nome = nome
        self.saldo = saldo
        self.juros = juros

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

    def adicione_juros(self):
        self.saldo += self.saldo * self.juros


minha_conta_investimento = Conta_Investimento("José", 100)
minha_conta_investimento.adicione_juros()
minha_conta_investimento.adicione_juros()
minha_conta_investimento.adicione_juros()
minha_conta_investimento.adicione_juros()
minha_conta_investimento.adicione_juros()
print(minha_conta_investimento.saldo)
