class Animal():
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        return "Fala do animal: "


class Cachorro(Animal):
    def falar(self):
        return super().falar() + "Au au"


class Gato(Animal):
    def falar(self):
        return super().falar() + "Miau"


class Peixe(Animal):
    def falar(self):
        return super().falar() + "não fala"


cachorro1 = Cachorro("Rex")
gato1 = Gato("Garfield")
peixe1 = Peixe("Nemo")

print(cachorro1.falar())
print(gato1.falar())
print(peixe1.falar())
