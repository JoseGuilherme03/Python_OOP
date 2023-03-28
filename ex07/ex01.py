class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Aluno(Pessoa):
    def __init__(self, nota, nome, idade):
        super().__init__(nome, idade)
        self.nota = nota

    def __str__(self):
        return f"O aluno {self.nome} tem {self.idade} anos e a nota {self.nota}"


aluno1 = Aluno(nome="José", idade=19, nota=10)
print(aluno1)
