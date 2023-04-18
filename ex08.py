class Usuario():
    def __init__(self, primereiro_nome, ultimo_nome, pontos=0, numero_artigos=0):
        self.primeiro_nome = primereiro_nome
        self.ultimo_nome = ultimo_nome
        self.pontos = pontos
        self.__numero_artigos = numero_artigos

    @property
    def numero_artigos(self):
        return self.__numero_artigos
    
    @numero_artigos.setter
    def numero_artigos(self, nart):
        self.__numero_artigos = nart

    def calcular_pontos(self):
        return self.numero_artigos


class Autor(Usuario):
    def calcular_pontos(self):
        self.pontos = super().calcular_pontos()
        return ((super().calcular_pontos() * 10) + 20)


class Editor(Usuario):
    def calcular_pontos(self):
        return ((super().calcular_pontos() * 6) + 15)
        

autor1 = Autor("José", "Fernandes", pontos=0, numero_artigos=5)
editor1 = Editor("Maria", "Silva", pontos=0, numero_artigos=5)
print(autor1.calcular_pontos())
print(editor1.calcular_pontos())
