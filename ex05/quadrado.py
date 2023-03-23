class Quadrado:
    def __init__(self, tamanho_do_lado):
        self.tamanho_do_lado = tamanho_do_lado

    def mudar_Valor_Lado(self, novo_tamanho):
        self.tamanho_do_lado = novo_tamanho

    def mostra_Area(self):
        return f"Area do Quadrado: {self.tamanho_do_lado * 2}"


quadrado = Quadrado(2)
quadrado.mudar_Valor_Lado(novo_tamanho=4)
print(quadrado.mostra_Area())
