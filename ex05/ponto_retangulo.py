class Ponto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Coordenadas do ponto: ({self.x}, {self.y})"


class Retangulo:
    def __init__(self, largura, altura, ponto_inicial):
        self.largura = largura
        self.altura = altura
        self.ponto_inicial = ponto_inicial

    def centro(self):
        x_centro = self.ponto_inicial.x + self.largura/2
        y_centro = self.ponto_inicial.y + self.altura/2
        return Ponto(x_centro, y_centro)


ponto1 = Ponto(0, 0)
retangulo1 = Retangulo(5, 3, ponto1)

ponto2 = Ponto(2, 2)
retangulo2 = Retangulo(4, 6, ponto2)

opcao = 0

while opcao != 3:
    print("Escolha uma opção:")
    print("1 - Alterar valores do retângulo 1")
    print("2 - Alterar valores do retângulo 2")
    print("3 - Sair")

    opcao = int(input("Opção escolhida: "))

    if opcao == 1:
        largura = float(input("Nova largura do retângulo 1: "))
        altura = float(input("Nova altura do retângulo 1: "))
        x = float(input("Nova coordenada x do ponto inicial do retângulo 1: "))
        y = float(input("Nova coordenada y do ponto inicial do retângulo 1: "))

        ponto1 = Ponto(x, y)
        retangulo1 = Retangulo(largura, altura, ponto1)

        centro_retangulo1 = retangulo1.centro()
        print(centro_retangulo1)

    elif opcao == 2:
        largura = float(input("Nova largura do retângulo 2: "))
        altura = float(input("Nova altura do retângulo 2: "))
        x = float(input("Nova coordenada x do ponto inicial do retângulo 2: "))
        y = float(input("Nova coordenada y do ponto inicial do retângulo 2: "))

        ponto2 = Ponto(x, y)
        retangulo2 = Retangulo(largura, altura, ponto2)

        centro_retangulo2 = retangulo2.centro()
        print(centro_retangulo2)

    elif opcao == 3:
        print("Encerrando o programa...")

    else:
        print("Opção inválida!")
