class Usuario():
    def __init__(self, primeiro_nome, ultimo_nome):
        self.__primeiro_nome = primeiro_nome
        self.__ultimo_nome = ultimo_nome

    def __str__(self):
        return f"Nome Completo: {self.__primeiro_nome} {self.__ultimo_nome}"


print(Usuario("José", "Fernandes"))
