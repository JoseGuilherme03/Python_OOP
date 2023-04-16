class Ingresso():
    def __init__(self, valor):
        self.valor = valor

    def imprime_valor(self):
        return f"Valor do ingresso: R$ {self.valor}"


class Vip(Ingresso):
    def __init__(self, valor, adicional):
        super().__init__(valor)
        self.adicional = adicional

    def imprime_valor(self):
        return f"Valor do ingresso: R$ {self.valor + self.adicional}"


class Normal(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)

    def __str__(self):
        return "Ingresso Normal"


class CamaroteInferior(Vip):
    def __init__(self, localizacao, valor, adicional):
        super().__init__(valor, adicional)
        self.localizacao = localizacao


class CamaroteSuperior(Vip):
    def __init__(self, valor, adicional, taxa_camarote, localizacao):
        super().__init__(valor, adicional)
        self.taxa_camarote = taxa_camarote
        self.localizacao = localizacao

    def imprime_valor(self):
        return f"Valor do ingresso: R$ {self.valor + self.adicional + self.taxa_camarote}"


ingresso_vip = Vip(100, 50)
ingresso_normal = Normal(100)
ingresso_camarote_inferior = CamaroteInferior("Camarote_1", 100, 50)
ingresso_camarote_superior = CamaroteSuperior(100, 50, 100, "Camarote_2")


print(ingresso_vip.imprime_valor())
print(ingresso_normal.imprime_valor())
print(ingresso_camarote_inferior.imprime_valor())
print(ingresso_camarote_superior.imprime_valor())
