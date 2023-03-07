class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.altura += 0.05

    def engordar(self):
        self.peso += 1

    def emagrecer(self):
        self.peso -= 1

    def crescer(self):
        self.altura += 0.05

    def __str__(self):
        return f"nome: {self.nome}, idade: {self.idade} altura: {self.altura}, peso: {self.peso}."


pessoa1 = Pessoa(nome="José", idade=19, altura=1.70, peso=65)
pessoa1.engordar()
pessoa1.emagrecer()
pessoa1.envelhecer()
pessoa1.crescer()
print(pessoa1)