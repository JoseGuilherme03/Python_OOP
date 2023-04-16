class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Rica(Pessoa):
    def __init__(self, nome, idade, dinheiro):
        super().__init__(nome, idade)
        self.dinheiro = dinheiro

    def faz_compras(self):
        print("Pessoa rica esta fazendo compras")


class Pobre(Pessoa):
    def trabalha(self):
        print("Pessoa pobre esta trabalhando")


class Miseravel(Pessoa):
    def mendiga(self):
        print("Pessoa miseravel esta mendigando")


pessoa_rico = Rica("João", 20, 1000)
pessoa_pobre = Pobre("Maria", 30)
pessoa_miseravel = Miseravel("José", 40)

pessoa_rico.faz_compras()
pessoa_pobre.trabalha()
pessoa_miseravel.mendiga()
