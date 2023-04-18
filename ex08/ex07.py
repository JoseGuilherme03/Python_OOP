class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    def retirada(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor


class ContaPoupanca(ContaBancaria):
    def __init__(self, saldo=0, taxa_juros=0.05):
        super().__init__(saldo)
        self.taxa_juros = taxa_juros

    def calcula_juros(self):
        self.saldo += self.saldo * self.taxa_juros


class ContaCorrente(ContaBancaria):
    def __init__(self, saldo=0, taxa_juros=0.02):
        super().__init__(saldo)
        self.taxa_juros = taxa_juros

    def calcula_juros(self):
        self.saldo += self.saldo * self.taxa_juros


conta_poupanca1 = ContaPoupanca(1000)
conta_corrente1 = ContaCorrente(1000)

conta_poupanca1.calcula_juros()
conta_corrente1.calcula_juros()

print("Saldo da conta poupança:", conta_poupanca1.saldo)
print("Saldo da conta corrente:", conta_corrente1.saldo)
