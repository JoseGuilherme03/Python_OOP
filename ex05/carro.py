class Carro():
    def __init__(self, consumo_por_km):
        self.consumo_por_km = consumo_por_km
        self.nivel_combustivel = 0
        
    def adicionar_gasolina(self, litros_gasolina):
        self.nivel_combustivel += litros_gasolina

    def andar(self, km):
        self.nivel_combustivel -= km / self.consumo_por_km

    def __str__(self):
        return f"Você tem {self.nivel_combustivel} litros de gasolina disponivel"


bmw = Carro(10)
bmw.adicionar_gasolina(20)
bmw.andar(100)
print(bmw)
