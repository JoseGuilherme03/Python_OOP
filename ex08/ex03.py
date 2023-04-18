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


cachorro1 = Cachorro("Rex")
gato1 = Gato("Garfield")

lista_animais = [cachorro1, gato1]

for animal in lista_animais:
    print(animal.falar())
