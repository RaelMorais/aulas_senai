class Produto:
    def __init__(self, nome, precoUnit, qtd):
        self.nome = nome
        self.precoUnit = precoUnit
        self.qtd = qtd

    def disponivel(self):
        if self.qtd >= 100:
            print("Estoque em Excesso")
        elif self.qtd <= 10:
            print("Estoque baixo")
        elif self.qtd == 0:
            print("Sem estoque")


    def calcularValor(self):
        valorTotal = self.qtd * self.precoUnit
        print(f"PRODUTO: {self.nome}")
        self.disponivel()
        print(f"PREÇO UNITARIO: R${self.precoUnit}")
        print(f"QUANTIDADE DISPONIVEL: {self.qtd}")
        print(f"PREÇO TOTAL DO ESTOQUE: R${valorTotal}")

prod = Produto("Nescau", 10.0, 100)
prod.calcularValor()

prod = Produto("Arroz", 23.0, 10)
prod.calcularValor()