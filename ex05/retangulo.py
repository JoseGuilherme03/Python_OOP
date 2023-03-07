class Retangulo:
    def __init__(self, comprimento=None, largura=None):
        self.comprimento = comprimento
        self.largura = largura

    def mudar_Valor_Dos_Lados(self, novo_comprimento, nova_largura):
        self.comprimento = novo_comprimento
        self.largura = nova_largura

    def calcularArea(self):
        area = self.comprimento * self.largura
        return area

    def calcularPerimetro(self):
        perimetro = 2 * self.calcularArea()
        return perimetro

    def mostra_Valor_Dos_Lados(self):
        return f"Medida da base do retângulo: {self.comprimento}, medida da altura do retângulo: {self.largura}"


# pedir as medidas do local ao usuário
comprimento = float(input("Informe o comprimento da sala de aula em mts²: "))
largura = float(input("Informe a largura da sala de aula em mts²: "))

# Cria o obejtto sala_de_aula
sala_de_aula = Retangulo(comprimento, largura)

# Calcular area e perimetro do piso
area_chao = sala_de_aula.calcularArea()
perimentro_chao = sala_de_aula.calcularPerimetro()

# Calcular quantidade de pisos e rodapés necessários para o local
dimensao_piso = float(input("Informe a area do piso em mts2: "))
dimensao_rodape = float(input("Informe a area do rodapé em mts2: "))
quantidade_pisos = area_chao / dimensao_piso
qunatidade_rodapes = perimentro_chao / dimensao_rodape

# Imprimir os resultados
print(f"Quantidade de pisos necessários: {quantidade_pisos}")
print(f"Quantidade de rodapés necessários: {qunatidade_rodapes}")
