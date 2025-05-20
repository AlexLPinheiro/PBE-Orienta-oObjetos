class Cachorro:
    def __init__(self,nome,comida,sono):
        self.nome = nome
        self.comida = comida
        self.sono = sono

    def comer(self):
        self.comida -= 1

    def dormir(self):
        self.sono = False

