class Produto:
    def __init__(self, nome, preco, fornecedor):
        self.nome = nome
        self.preco = preco
        self.fornecedor = fornecedor
    def __str__(self):
        return f"{self.nome} - R${self.preco}"

class Carrinho:
        def __init__(self):
            self.produtos = []
        def adicionar_produto(self, produto):
            self.produtos.append(produto)

        def remover_produto(self, produto):
            self.produtos.remove(produto)

        def calcular_total(self):
            return sum(produto.preco for produto in self.produtos)

        def listar_produtos(self):
            return [str(produto) for produto in self.produtos]

class LojaVirtual:
        def __init__(self):
            self.produtos_cadastrados = []
            self.carrinho = Carrinho()

        def cadastrar_produto(self, nome, preco, fornecedor):
            produto = Produto(nome, preco, fornecedor)
            self.produtos_cadastrados.append(produto)

        def listar_produtos(self):
            return [str(produto) for produto in self.produtos_cadastrados]

        def adicionar_ao_carrinho(self, nome_produto):
            for produto in self.produtos_cadastrados:
                if produto.nome == nome_produto:
                    self.carrinho.adicionar_produto(produto)
                    return f"{produto.nome} adicionado ao carrinho."
            return "Produto não encontrado."

        def remover_do_carrinho(self, nome_produto):
            for produto in self.carrinho.produtos:
                if produto.nome == nome_produto:
                    self.carrinho.remover_produto(produto)
                    return f"{produto.nome} removido do carrinho."
            return "Produto não encontrado no carrinho."

        def aplicar_desconto(self, percentual):
            total = self.carrinho.calcular_total()
            desconto = total * (percentual / 100)
            return total - desconto

        def calcular_total(self):
            return self.carrinho.calcular_total()
loja = LojaVirtual()
loja.cadastrar_produto("Camiseta", 49.90, "Adidas")
loja.cadastrar_produto("Calça", 89.90, "Nike")
loja.cadastrar_produto("Tênis", 199.90, "Puma")
print("+"*20)

print("Produtos disponíveis:")
for produto in loja.listar_produtos():
    print(produto)
print("+"*20)
print(loja.adicionar_ao_carrinho("Camiseta"))
print(loja.adicionar_ao_carrinho("Tênis"))

print(f"Total do carrinho: R$ {loja.calcular_total()}")

total_com_desconto = loja.aplicar_desconto(25) 
print(f"Total com desconto: R$ {total_com_desconto}")

print(loja.remover_do_carrinho("Camiseta"))
print(f"Total do carrinho: R$ {loja.calcular_total():.2f}")
