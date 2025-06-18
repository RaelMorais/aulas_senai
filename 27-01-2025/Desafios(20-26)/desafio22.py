class Produto:
    def __init__(self, id, nome, preco_compra, preco_venda, quantidade, categoria, fornecedor):
        self.id = id
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.quantidade = quantidade
        self.categoria = categoria
        self.fornecedor = fornecedor

    def __str__(self):
        return f"{self.nome} (ID: {self.id}, Categoria: {self.categoria.nome}, Fornecedor: {self.fornecedor.nome}, Estoque: {self.quantidade}, Preço Venda: R${self.preco_venda:.2f})"

class Categoria:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Fornecedor:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Compra:
    def __init__(self, id, produto, quantidade, preco_unitario):
        self.id = id
        self.produto = produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.total = quantidade * preco_unitario

    def __str__(self):
        return f"Compra {self.id}: {self.produto.nome} x {self.quantidade} (Total: R${self.total:.2f})"

class Venda:
    def __init__(self, id, produto, quantidade, preco_unitario):
        self.id = id
        self.produto = produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.total = quantidade * preco_unitario

    def __str__(self):
        return f"Venda {self.id}: {self.produto.nome} x {self.quantidade} (Total: R${self.total:.2f})"

class Estoque:
    def __init__(self):
        self.produtos = []
        self.compras = []
        self.vendas = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print(f"Produto {produto.nome} adicionado.")

    def registrar_compra(self, produto, quantidade, preco_unitario):
        if produto in self.produtos:
            produto.quantidade += quantidade
            compra = Compra(len(self.compras) + 1, produto, quantidade, preco_unitario)
            self.compras.append(compra)
            print(f"Compra registrada: {compra}")
        else:
            print("Produto não encontrado.")

    def registrar_venda(self, produto, quantidade, preco_unitario):
        if produto in self.produtos and produto.quantidade >= quantidade:
            produto.quantidade -= quantidade
            venda = Venda(len(self.vendas) + 1, produto, quantidade, preco_unitario)
            self.vendas.append(venda)
            print(f"Venda registrada: {venda}")
        else:
            print("Produto não encontrado ou estoque insuficiente.")

    def relatorio_inventario(self):
        print("\nRelatório de Inventário:")
        valor_total = 0
        for produto in self.produtos:
            print(produto)
            valor_total += produto.quantidade * produto.preco_venda
        print(f"Valor total do estoque: R${valor_total:.2f}")

def main():
    estoque = Estoque()
    categorias = [Categoria(1, "Eletrônicos"), Categoria(2, "Roupas")]
    fornecedores = [Fornecedor(1, "Tech Ltda"), Fornecedor(2, "Moda SA")]
    produtos = [
        Produto(1, "Smartphone", 1000.0, 1500.0, 10, categorias[0], fornecedores[0]),
        Produto(2, "Camiseta", 20.0, 50.0, 50, categorias[1], fornecedores[1])
    ]
    for p in produtos:
        estoque.adicionar_produto(p)

    while True:
        print("\nMenu Estoque:")
        print("1. Registrar Compra\n2. Registrar Venda\n3. Ver Inventário\n4. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            id_produto = int(input("ID do produto: "))
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço unitário de compra: "))
            produto = next((p for p in estoque.produtos if p.id == id_produto), None)
            if produto:
                estoque.registrar_compra(produto, quantidade, preco)
            else:
                print("Produto não encontrado.")
        elif escolha == '2':
            id_produto = int(input("ID do produto: "))
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço unitário de venda: "))
            produto = next((p for p in estoque.produtos if p.id == id_produto), None)
            if produto:
                estoque.registrar_venda(produto, quantidade, preco)
            else:
                print("Produto não encontrado.")
        elif escolha == '3':
            estoque.relatorio_inventario()
        elif escolha == '4':
            print("Até logo!")
            break
        else:
            print("Opção inválida.")
if __name__ == "__main__":
    main()