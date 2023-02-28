class Usuario:
    __primeiro_nome = ""
    ultimo_nome = ""

    @property
    def primeiro_nome(self):
        return self.__primeiro_nome
    
    @primeiro_nome.setter
    def primeiro_nome(self, primeiro_nome):
        self.__primeiro_nome = primeiro_nome

    def hello(self):
        return f"Olá {self.primeiro_nome} {self.ultimo_nome}"

usuario1 = Usuario()
usuario1.primeiro_nome = "Joe"
print(usuario1.hello())


class Empregado():
    __nome = ""
    __salario = ""
    projeto = ""

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    def trabalho(self):
        return f"O funcionario(a) {self.nome} está trabalhando no projeto {self.projeto}"

    def mostrar(self):
        return f"Funcionario: {self.nome}, Salário: {self.salario}"


funcionario1 = Empregado()
funcionario1.nome = "João"
funcionario1.salario = 1000
funcionario1.projeto = "Site de vendas"
print(funcionario1.trabalho())
print(funcionario1.mostrar())


class Robo():
    __nome = ""
    __ano_construcao = ""

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def ano_construcao(self):
        return self.__ano_construcao

    @ano_construcao.setter
    def ano_construcao(self, ano_construcao):
        self.__ano_construcao = ano_construcao

    def diga_alo(self):
        return f"Nome do robo: {self.nome}, Ano de construção: {self.ano_construcao}"


robo1 = Robo()
robo1.nome = "Robocop"
robo1.ano_construcao = "2002"
print(robo1.diga_alo())


class Laptop():
    __preco = ""

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        self.__preco = novo_preco


laptop1 = Laptop()
laptop1.preco = "3999"
print(laptop1.preco)


class Pessoa():
    __primeiro_nome = ""
    __ultimo_nome = ""

    @property
    def primeiro_nome(self):
        return self.__primeiro_nome

    @primeiro_nome.setter
    def primeiro_nome(self, primeiro_nome):
        self.__primeiro_nome = primeiro_nome

    @property
    def ultimo_nome(self):
        return self.__ultimo_nome

    @ultimo_nome.setter
    def ultimo_nome(self, ultimo_nome):
        self.__ultimo_nome = ultimo_nome


pessoa1 = Pessoa()
pessoa1.primeiro_nome = "João"
pessoa1.ultimo_nome = "Carvalho"
print(f"Meu nome é {pessoa1.primeiro_nome} {pessoa1.ultimo_nome}")
