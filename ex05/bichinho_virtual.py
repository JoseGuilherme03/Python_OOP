class Tamagushi():
    def __init__(self, nome, fome, saude, idade):
        self._nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
