class Tv():
    def __init__(self, numero_do_canal=1, volume=0):
        self.numero_do_canal = numero_do_canal
        self.volume = volume

    def aumentar_volume(self):
        self.volume += 1
    
    def diminuir_volume(self):
        self.volume -= 1
    
    def trocar_canal(self, novo_canal):
        self.numero_do_canal = novo_canal


controle = Tv()
controle.trocar_canal(5)
controle.aumentar_volume()
controle.aumentar_volume()
controle.diminuir_volume()
print(controle.numero_do_canal)
print(controle.volume)
