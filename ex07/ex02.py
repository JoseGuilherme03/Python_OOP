class Veiculo():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, quantidade_portas):
        super().__init__(marca, modelo, ano)
        self.quantidade_portas = quantidade_portas

    def __str__(self):
        return f"O carro {self.marca} {self.modelo} {self.ano} tem {self.quantidade_portas} portas."
    

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas

    def __str__(self):
        return f"A moto {self.marca} {self.modelo} {self.ano} tem {self.cilindradas} cilindradas."
    

carro1 = Carro(marca="BMW", modelo="X1", ano=2022, quantidade_portas=4)
moto1 = Moto(marca="Honda", modelo="CG", ano=2015, cilindradas=150)
print(carro1)
print()
print(moto1)


