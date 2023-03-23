class Usuario():
    def __init__(self, nome_usuario=None):
        self.__nome_usuario = nome_usuario

    @property
    def nome_usuario(self):
        return self.__nome_usuario

    @nome_usuario.setter
    def nome_usuario(self, novo_nome):
        self.__nome_usuario = novo_nome


class Admin(Usuario):
    def escreva_nome(self):
        return "Admin"

    def diga_ola(self):
        return f"Olá admin, {self.nome_usuario}"


admin1 = Admin("Baltazar")
print(admin1.diga_ola())
