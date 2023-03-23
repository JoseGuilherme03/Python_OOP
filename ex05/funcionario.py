class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def get_nome(self):
        return self.nome

    def get_salario(self):
        return self.salario

    def set_salario(self, salario):
        self.salario = salario

    def aumenta_salario(self, percentual):
        self.salario = self.salario + (self.salario * percentual / 100)

    def __str__(self):
        return f"Nome: {self.nome} - Salário: {self.salario}"


gerente = Funcionario("João", 1000)
gerente.aumenta_salario(10)
print(gerente)
