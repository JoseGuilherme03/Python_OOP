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


cliente = ContaCorrente("123", 1000, "josé")
cliente.depositar(500)
cliente.sacar(500)
print(cliente.saldo)
cliente2 = ContaPoupanca("1234", 1000, "joão", 50)
cliente2.depositar(500)
cliente2.sacar(500)
print(cliente2.saldo)      