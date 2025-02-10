class Retângulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calcularArea(self):
        return self.comprimento * self.largura
comprimento = 10
largura = 10

Calcretangulo = Retângulo(comprimento, largura)

valor = Calcretangulo.calcularArea()

print(f"A area é {valor}")
