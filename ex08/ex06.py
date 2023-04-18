class Empregado():
    def __init__(self, nome):
        self.nome = nome

    def pagar_salario(self):
        return f"O salário do empregado {self.nome} é de R$"


class EmpregadoHora(Empregado):
    def __init__(self, nome, horas_trabalhadas, valor_hora):
        super().__init__(nome)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def pagar_salario(self):
        salario = self.horas_trabalhadas * self.valor_hora
        return super().pagar_salario() + str(salario)


class EmpregaMes(Empregado):
    def __init__(self, nome, salario_mensal):
        super().__init__(nome)
        self.salario_mensal = salario_mensal

    def pagar_salario(self):
        return super().pagar_salario() + str(self.salario_mensal)


empregado_hora1 = EmpregadoHora("João", 160, 10)
empregado_mes1 = EmpregaMes("Maria", 1000)

lista_empregados = [empregado_hora1, empregado_mes1]

for empregado in lista_empregados:
    print(empregado.pagar_salario())
