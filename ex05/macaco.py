class Macaco():
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, *comidas):
        for comida in comidas:
            if isinstance(comida, Macaco):
                self.bucho.append(comida.nome)
            else:
                self.bucho.append(comida)

    def digerir(self):
        del self.bucho[0]

    def ver_Bucho(self):
        estomago = ", ".join(str(comida) for comida in self.bucho)
        return f"Comidas no estomago: {estomago}"

    def __str__(self):
        return self.nome


cesar = Macaco("Cesar")
koba = Macaco("Koba")
cesar.comer("banana", "maçã", "mamão", koba)
print(cesar.ver_Bucho())
