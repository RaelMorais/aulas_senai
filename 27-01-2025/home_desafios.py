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
        self.saldo = 0.0  # Dinheiro inserido pelo cliente
        self.carrinho = []

    def cadastrar_produto(self, nome, preco, fornecedor):
        """Cadastra um novo produto na máquina de vendas."""
        produto = Produto(nome, preco, fornecedor)
        self.produtos_cadastrados.append(produto)

    def listar_produtos(self):
        """Exibe os produtos disponíveis no estoque da máquina."""
        if not self.produtos_cadastrados:
            return "Nenhum produto disponível."
        return "\n".join(str(produto) for produto in self.produtos_cadastrados)

    def selecionar_produto(self, nome_produto):
        """Seleciona um produto para compra, se disponível."""
        for produto in self.produtos_cadastrados:
            if produto.nome == nome_produto:
                self.carrinho.append(produto)
                return f"{produto.nome} adicionado ao carrinho."
        return "Produto não encontrado."

    def inserir_dinheiro(self, valor):
        """Permite que o cliente insira dinheiro para a compra."""
        if valor <= 0:
            return "O valor inserido precisa ser maior que zero."
        self.saldo += valor
        return f"R$ {valor:.2f} inseridos. Saldo atual: R$ {self.saldo:.2f}"

    def calcular_total_carrinho(self):
        """Calcula o total dos produtos no carrinho."""
        return sum(produto.preco for produto in self.carrinho)

    def calcular_troco(self):
        """Calcula o troco, se houver, após o pagamento."""
        total = self.calcular_total_carrinho()
        if self.saldo < total:
            return f"Saldo insuficiente. Faltam R$ {total - self.saldo:.2f}."
        troco = self.saldo - total
        self.saldo = 0  # Após o pagamento, o saldo é zerado
        self.carrinho.clear()  # O carrinho é esvaziado após a compra
        return f"Troco: R$ {troco:.2f}"

    def exibir_estoque(self):
        """Exibe todos os produtos disponíveis no estoque."""
        return self.listar_produtos()


# Testando a Máquina de Vendas
maquina = MaquinaDeVendas()

# Cadastrar produtos
maquina.cadastrar_produto("Camiseta", 49.90, "Adidas")
maquina.cadastrar_produto("Calça", 89.90, "Nike")
maquina.cadastrar_produto("Tênis", 199.90, "Puma")

# Exibindo os produtos disponíveis
print("Produtos disponíveis:")
print(maquina.exibir_estoque())

# Selecionando produtos
print(maquina.selecionar_produto("Camiseta"))
print(maquina.selecionar_produto("Tênis"))

# Inserindo dinheiro
print(maquina.inserir_dinheiro(100.0))

# Calculando total do carrinho e troco
print(f"Total do carrinho: R$ {maquina.calcular_total_carrinho():.2f}")
print(maquina.calcular_troco())

# Verificando o estoque após a compra
print("Produtos disponíveis após a compra:")
print(maquina.exibir_estoque())
