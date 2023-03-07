class Bola:
    def __init__(self, cor, circuferencia, material):
        self.cor = cor
        self.circunferencia = circuferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        return f"Cor da bola: {self.cor}"


bola_futebol = Bola(cor="branca", circuferencia="redonda", material="couro")
bola_futebol.trocaCor("vermelha")
print(bola_futebol.mostraCor())
