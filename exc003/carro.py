class Carro():
    def __init__(self, modelo):
        self.modelo = modelo
        self.speed = 0

    def acelerar(self):
        self.speed += 10 

    def frear(self):
        self.speed -= 10

    def mostrarVelocidade(self):
        print(f"O carro está a {self.speed} KM por hora.") 