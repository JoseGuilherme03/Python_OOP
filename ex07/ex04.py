class Forma():
    def area(self, objeto):
        return f"Area da {objeto} = "

class Retangulo(Forma):
    def __init__(self, comprimento, largura, nome):
        self.nome = nome
        self.comprimento = comprimento
        self.largura = largura
    
    def area(self):
        return f"{super().area(self.nome)} {self.comprimento * self.largura}"


class Circulo(Forma):
    def __init__(self, raio, nome):
        self.nome = nome
        self.raio = raio

    def area(self):
        return f"{super().area(self.nome)} {3.14 * self.raio ** 2}"


sala = Retangulo(nome="sala" ,comprimento=10, largura=5)
bola = Circulo(nome="bola", raio=5)
print(sala.area())
print(bola.area())

    