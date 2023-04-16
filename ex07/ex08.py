class Empregado():
    def __init__(self, codigo, nome, email, salario):
        self.codigo = codigo
        self.nome = nome
        self.email = email
        self._salario = salario

    @property
    def salario(self):
        return self._salario

    def aumento_salarial(self, porcentagem):
        self._salario += ((self._salario * porcentagem) / 100)


class Chefe(Empregado):
    def __init__(self, codigo, nome, email, salario, beneficio):
        super().__init__(codigo, nome, email, salario)
        self.beneficio = beneficio

    def aumento_salarial(self, porcentagem):
        super().aumento_salarial(porcentagem)
        self._salario += self.beneficio


class Estagiario(Empregado):
    def __init__(self, codigo, nome, email, salario, desconto):
        super().__init__(codigo, nome, email, salario)
        self.desconto = desconto

    def aumento_salarial(self, porcentagem):
        super().aumento_salarial(porcentagem)
        self._salario -= self.desconto


chefe1 = Chefe("1234", "José", "jose@gmail.com", 5000, 500)
estagiario1 = Estagiario("4321", "João", "joão@gmail.com", 2000, 200)


print(chefe1.salario)
print(estagiario1.salario)
chefe1.aumento_salarial(10)
estagiario1.aumento_salarial(10)
print(chefe1.salario)
print(estagiario1.salario)
