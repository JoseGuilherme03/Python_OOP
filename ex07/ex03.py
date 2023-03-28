class Animal():
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso

    def comer(self):
        return "Comendo..."


class Cachorro(Animal):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)
    
    def latir(self):
        return "Au au au"
    

class Gato(Animal):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)
    
    def miar(self):
        return "Miau miau miau"
    

gato1 = Gato(nome="Garfield", peso=5)
cachorro1 = Cachorro(nome="Snoopy", peso=10)
print(gato1.comer())
print(gato1.miar())
print(cachorro1.comer())
print(cachorro1.latir())

        