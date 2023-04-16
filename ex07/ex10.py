class Funciario():
    def __init__(self, nome, endereco, telefone, email, salario):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.salario = salario

    def __str__(self):
        return f"Nome: {self.nome}, Endereço: {self.endereco}, Telefone: {self.telefone}, Email: {self.email}"


class Assistente(Funciario):
    def __init__(self, nome, endereco, telefone, email, matricula, salario):
        super().__init__(nome, endereco, telefone, email, salario)
        self.matricula = matricula


class AssistenteTecnico(Assistente):
    def __init__(self, nome, endereco, telefone, email, matricula, salario, bonus):
        super().__init__(nome, endereco, telefone, email, matricula, salario)
        self.bonus = bonus


class AssistenteAdministrativo(Assistente):
    def __init__(self, nome, endereco, telefone, email, matricula, salario, turno):
        super().__init__(nome, endereco, telefone, email, matricula, salario)
        self.turno = turno


assistente_tecnico1 = AssistenteTecnico(
    nome="João", endereco="Rua 1", telefone="123456789", email="joão@gmail.com", matricula="123", salario=1000, bonus=100)
assistente_administrativo1 = AssistenteAdministrativo(
    nome="Maria", endereco="Rua 2", telefone="987654321", email="maria@gmail.com", matricula="456", salario=1000, turno="Manhã")

print(f"Nome: {assistente_tecnico1.nome}, Matricula: {assistente_tecnico1.matricula}, Bonus: {assistente_tecnico1.bonus}")
print(f"Nome: {assistente_administrativo1.nome}, Matricula: {assistente_administrativo1.matricula}, Turno: {assistente_administrativo1.turno}")
