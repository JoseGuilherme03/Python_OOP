class Usuario:
    def __init__(self, primeironome, ultimonome):
        self.primeironome = primeironome
        self.ultimonome = ultimonome

    def hello(self):
        return f"Olá {self.primeironome} {self.ultimonome}"


usuario1 = Usuario("José", "Fernandes")
usuario2 = Usuario("Jane", "Silva")

print(usuario1.hello())
print(usuario2.hello())
