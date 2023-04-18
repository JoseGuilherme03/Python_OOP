class Forma():
    def area(self):
        return "Área da forma: "


class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return super().area() + str(self.lado * self.lado)


class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return super().area() + str(3.14 * (self.raio**2))


lista_formas = [Quadrado(2), Circulo(2)]

for forma in lista_formas:
    print(forma.area())
