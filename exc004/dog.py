class Cachorro:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def latir(self):
        print(f"Au au! Meu nome é {self.nome}, da raça {self.raca}.")