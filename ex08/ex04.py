class Carro():
    def __init__(self, nome):
        self.nome = nome

    def dirigir(self):
        return "Estou dirigindo um carro"


class CarroGasolina(Carro):
    def dirigir(self):
        return super().dirigir() + " a gasolina"


class CarroEletrico(Carro):
    def dirigir(self):
        return super().dirigir() + " elétrico"


carro1 = CarroGasolina("Fusca")
carro2 = CarroEletrico("Tesla")

print(carro1.dirigir())
print(carro2.dirigir())
