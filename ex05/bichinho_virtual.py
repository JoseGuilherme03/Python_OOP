class Tamagushi():
    def __init__(self, nome, fome, saude, idade):
        self._nome = nome
        self._fome = fome
        self._saude = saude
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def fome(self):
        return self._fome
    
    @fome.setter
    def fome(self, nova_fome):
        self._fome = nova_fome
    
    @property
    def saude(self):
        return self._saude
    
    @saude.setter
    def saude(self, nova_saude):
        self._saude = nova_saude
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, nova_idade):
        self._idade = nova_idade

    def calcular_humor(self):
        return (self._fome + self._saude) / 2
    
    
    def __str__(self):
        return f"""
    Nome: {self.nome}
    Fome: {self._fome}
    Saúde: {self._saude}
    Idade: {self._idade}
    Humor: {self.calcular_humor()}
        """
    

baby_dino = Tamagushi("Baby Dino", 0, 0, 0)
chickpet = Tamagushi("Chickpet", 0, 0, 0)
yuki_penguim = Tamagushi("Yuki Penguim", 0, 0, 0)

fazenda_tamagushi = [baby_dino, chickpet, yuki_penguim]

opcao = 0

while opcao != 4:
    print("----- CUIDANDO DA FAZENDA DE TAMAGUSHI -----")
    print("1 - Alimentar")
    print("2 - Brincar")
    print("3 - Dormir")
    print("4 - Sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        for tamagushi in fazenda_tamagushi:
            tamagushi.fome -= 1
            tamagushi.saude += 1
    elif opcao == 2:
        for tamagushi in fazenda_tamagushi:
            tamagushi.fome += 1
    elif opcao == 3:
        for tamagushi in fazenda_tamagushi:
            tamagushi.fome += 1
            tamagushi.saude += 1
            tamagushi.idade += 1
    elif opcao == 4:
        print("Até mais!")
    else:
        print("Opção inválida!")
    for tamagushi in fazenda_tamagushi:
        print(tamagushi)

