class usuario():
    def __init__(self, primeironome, ultimonome):
        self.primeironome = primeironome
        self.ultimonome = ultimonome

    def hello(self, pessoa):
        return f"Olá {pessoa.primeironome} {pessoa.ultimonome}, meu nome é {self.primeironome}"
    

usuario1 = usuario("Jonnie", "Bravo")
usuario2 = usuario("Maria", "Silva") 

# Usuario1 dando olá para o usuario2 e vice e versa
print(usuario1.hello(usuario2))
print(usuario2.hello(usuario1))