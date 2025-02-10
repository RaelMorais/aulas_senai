class Produto:
    def __init__(self, nome, preco, fornecedor):
        self.nome = nome
        self.preco = preco
        self.fornecedor = fornecedor

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"

class MaquinaDeVendas:
    def __init__(self):
        self.produtos_cadastrados = []
        self.saldo = 0.0 
        self.carrinho = []

    def cadastrar_produto(self, nome, preco, fornecedor):
        produto = Produto(nome, preco, fornecedor)
        self.produtos_cadastrados.append(produto)

    def listar_produtos(self):
        if not self.produtos_cadastrados:
            return "Sem estoque"
        return "\n".join(str(produto) for produto in self.produtos_cadastrados)# Usei o chatgpt

    def selecionar_produto(self, nome_produto):
        for produto in self.produtos_cadastrados:
            if produto.nome == nome_produto:
                self.carrinho.append(produto)
                return f"{produto.nome} adicionado ao carrinho."
        return "Produto não encontrado"

    def inserir_dinheiro(self, valor):
        if valor <= 0:
            return "Valor não compativel"
        self.saldo += valor
        return f">>>R$ {valor:.2f} inseridos.\n>>>Saldo atual: R$ {self.saldo:.2f}"

    def calcular_total_carrinho(self):
        return sum(produto.preco for produto in self.carrinho)

    def calcular_troco(self):
        total = self.calcular_total_carrinho()
        if self.saldo < total:
            return f"Saldo insuficiente.\nFaltam R$ {total - self.saldo:.2f}."
        troco = self.saldo - total
        self.saldo = 0  
        self.carrinho.clear()  
        return f"Troco: R$ {troco:.2f}"

    def exibir_estoque(self):
        return self.listar_produtos()


maquina = MaquinaDeVendas()

maquina.cadastrar_produto("Camiseta", 49.90, "Adidas")
maquina.cadastrar_produto("Calça", 89.90, "Nike")
maquina.cadastrar_produto("Tênis", 199.90, "Puma")

print("Produtos disponíveis:")
print(maquina.exibir_estoque())

print(maquina.selecionar_produto("Camiseta"))
print(maquina.selecionar_produto("Tênis"))

print(maquina.inserir_dinheiro(100.0))

print(f"Total do carrinho: R$ {maquina.calcular_total_carrinho():.2f}")
print(maquina.calcular_troco())

print("Produtos disponíveis após a compra:")
print(maquina.exibir_estoque())
