class Bomba_Combustivel():
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self._tipo_combustivel = tipo_combustivel
        self._valor_litro = valor_litro
        self._quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, dinheiro):
        quantidade = dinheiro / self.valor_do_litro
        self.quantidade_combustivel -= quantidade
        return f"Pagamento: {dinheiro}, quantidade abastecida: {quantidade} litros"

    @property
    def valor_do_litro(self):
        return self._valor_litro

    @valor_do_litro.setter
    def valor_do_litro(self, novo_valor):
        self._valor_do_litro = novo_valor

    @property
    def tipo_combustivel(self):
        return self._tipo_combustivel

    @tipo_combustivel.setter
    def tipo_combustivel(self, novo_tipo):
        self._tipo_combustivel = novo_tipo

    @property
    def quantidade_combustivel(self):
        return self._quantidade_combustivel

    @quantidade_combustivel.setter
    def quantidade_combustivel(self, nova_quantidade):
        self._quantidade_combustivel = nova_quantidade


bomba_combustivel = Bomba_Combustivel("Gasolina", 5, 200)
print(bomba_combustivel.abastecer_por_valor(100))
bomba_combustivel.quantidade_combustivel = 300
bomba_combustivel.tipo_combustivel = "Diesel"
bomba_combustivel.valor_do_litro = 4
print(bomba_combustivel.abastecer_por_valor(50))
