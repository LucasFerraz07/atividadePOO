class Produto():
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def comprar(self, qtd):
        if self.estoque >= qtd:
            self.estoque -= qtd

    def repor(self, qtd):
        self.estoque += qtd

    def consultarEstoque(self):
        print(f"{self.nome}")
        print(f"Preço: {self.preco}$")
        print(f"Quantidade disponível: {self.estoque}")
