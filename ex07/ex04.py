class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
    
    def aumento(self, porcentagem_aumento):
        self.salario += ((self.salario * porcentagem_aumento) / 100)

    def __str__(self):
        return f"nome: {self.nome}, idade: {self.idade}, salário: {self.salario}"


funcionario1 = Funcionario("João", 19, 1000)
funcionario1.aumento(10)
print(funcionario1)




