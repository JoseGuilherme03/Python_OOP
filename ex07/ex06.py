class ContaCorrente():
    def __init__(self, numero, saldo, cliente):
        self.numero = numero
        self._saldo = saldo
        self.cliente = cliente

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    @property
    def saldo(self):
        return self._saldo


class ContaPoupanca(ContaCorrente):
    def __init__(self, numero, saldo, cliente, saldo_minimo):
        super().__init__(numero, saldo, cliente)
        self._saldo_minimo = saldo_minimo

    def atualizar_saldo(self, novo_saldo):
        self.saldo = novo_saldo

    @property
    def saldo_minimo(self):
        return self._saldo_minimo


class ContaEspecial(ContaCorrente):
    def __init__(self, numero, saldo, cliente, limite):
        super().__init__(numero, saldo, cliente)
        self.limite = limite


class ContaInvestimento(ContaCorrente):
    def __init__(self, numero, saldo, cliente, periodo, data_investimento):
        super().__init__(numero, saldo, cliente)
        self.data_investimento = data_investimento
        self.periodo = periodo


cliente1 = ContaCorrente("1234", 1000, "José")
cliente2 = ContaEspecial("4321", 1000, "Ana", 2000)
cliente3 = ContaPoupanca("4567", 1000, "João", 50)
cliente4 = ContaInvestimento("7654", 1000, "Pedro", "1 ano", "10/04/20203")

cliente1.depositar(1000)
print(cliente1.saldo)
cliente2.depositar(1000)
print(cliente2.saldo)
print(cliente3.saldo_minimo)
