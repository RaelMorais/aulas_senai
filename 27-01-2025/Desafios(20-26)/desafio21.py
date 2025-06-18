from datetime import datetime

class Produto:
    def __init__(self, id, nome, preco, categoria, estoque):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.estoque = estoque

    def __str__(self):
        return f"{self.nome} (ID: {self.id}, Categoria: {self.categoria}, Preço: R${self.preco:.2f}, Estoque: {self.estoque})"

class Cliente:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email
        self.historico_compras = []
        self.carrinho = Carrinho()

    def adicionar_ao_carrinho(self, produto, quantidade):
        if produto.estoque >= quantidade:
            self.carrinho.adicionar_item(produto, quantidade)
            produto.estoque -= quantidade
            print(f"Adicionado {quantidade} x {produto.nome} ao carrinho.")
        else:
            print(f"Estoque insuficiente para {produto.nome}. Disponível: {produto.estoque}")

    def ver_carrinho(self):
        self.carrinho.ver()

    def aplicar_desconto(self, codigo_desconto):
        self.carrinho.aplicar_desconto(codigo_desconto)

    def finalizar_compra(self):
        pedido = self.carrinho.finalizar(self)
        if pedido:
            self.historico_compras.append(pedido)
            print(f"Pedido {pedido.id} realizado com sucesso!")
        return pedido

    def ver_historico_compras(self):
        if not self.historico_compras:
            print("Sem histórico de compras.")
            return
        print(f"\nHistórico de Compras de {self.nome}:")
        for pedido in self.historico_compras:
            print(pedido)

    def obter_recomendacoes(self, produtos):
        categorias = {item['produto'].categoria for pedido in self.historico_compras for item in pedido.itens}
        recomendacoes = [p for p in produtos if p.categoria in categorias and p.estoque > 0]
        if not recomendacoes:
            print("Sem recomendações disponíveis.")
            return []
        print("\nProdutos Recomendados:")
        for p in recomendacoes[:3]:
            print(p)
        return recomendacoes

class Carrinho:
    def __init__(self):
        self.itens = []
        self.desconto = 0

    def adicionar_item(self, produto, quantidade):
        for item in self.itens:
            if item['produto'].id == produto.id:
                item['quantidade'] += quantidade
                return
        self.itens.append({'produto': produto, 'quantidade': quantidade})

    def aplicar_desconto(self, codigo):
        descontos = {'DESCONTO10': 0.10, 'DESCONTO20': 0.20}
        self.desconto = descontos.get(codigo, 0)
        print(f"Desconto de {self.desconto*100}% aplicado." if self.desconto else "Código de desconto inválido.")

    def calcular_frete(self):
        peso_total = sum(item['produto'].preco * item['quantidade'] * 0.1 for item in self.itens)
        return 10.0 if peso_total < 100 else 20.0

    def ver(self):
        if not self.itens:
            print("Carrinho vazio.")
            return
        print("\nConteúdo do Carrinho:")
        total = sum(item['produto'].preco * item['quantidade'] for item in self.itens)
        total *= (1 - self.desconto)
        frete = self.calcular_frete()
        for item in self.itens:
            print(f"{item['produto'].nome} x {item['quantidade']}: R${item['produto'].preco * item['quantidade']:.2f}")
        print(f"Subtotal: R${total:.2f}\nFrete: R${frete:.2f}\nTotal: R${(total + frete):.2f}")

    def finalizar(self, cliente):
        if not self.itens:
            print("Carrinho vazio. Não é possível finalizar.")
            return None
        pedido = Pedido(len(cliente.historico_compras) + 1, cliente, self.itens, self.desconto)
        self.itens = []
        self.desconto = 0
        return pedido

class Pedido:
    def __init__(self, id, cliente, itens, desconto):
        self.id = id
        self.cliente = cliente
        self.itens = itens
        self.desconto = desconto
        self.frete = sum(item['produto'].preco * item['quantidade'] * 0.1 for item in itens)
        self.frete = 10.0 if self.frete < 100 else 20.0
        self.data = datetime.now()
        self.total = sum(item['produto'].preco * item['quantidade'] for item in itens) * (1 - desconto) + self.frete

    def __str__(self):
        itens_str = "\n".join(f"  {item['produto'].nome} x {item['quantidade']}: R${item['produto'].preco * item['quantidade']:.2f}" for item in self.itens)
        return f"Pedido {self.id} ({self.data.strftime('%d/%m/%Y %H:%M')}):\n{itens_str}\nDesconto: {self.desconto*100}%\nFrete: R${self.frete:.2f}\nTotal: R${self.total:.2f}"

def main():
    produtos = [
        Produto(1, "Notebook", 3000.0, "Eletrônicos", 10),
        Produto(2, "Fone de Ouvido", 150.0, "Eletrônicos", 50),
        Produto(3, "Livro", 30.0, "Livros", 100),
        Produto(4, "Camiseta", 40.0, "Roupas", 200)
    ]
    cliente = Cliente(1, "João", "joao@email.com")

    while True:
        print("\nMenu E-commerce:")
        print("1. Ver Produtos\n2. Adicionar ao Carrinho\n3. Ver Carrinho\n4. Aplicar Desconto\n5. Finalizar Compra\n6. Ver Histórico\n7. Recomendações\n8. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            print("\nProdutos Disponíveis:")
            for p in produtos:
                print(p)
        elif escolha == '2':
            id_produto = int(input("ID do produto: "))
            quantidade = int(input("Quantidade: "))
            produto = next((p for p in produtos if p.id == id_produto), None)
            if produto:
                cliente.adicionar_ao_carrinho(produto, quantidade)
            else:
                print("Produto não encontrado.")
        elif escolha == '3':
            cliente.ver_carrinho()
        elif escolha == '4':
            codigo = input("Código de desconto (DESCONTO10/DESCONTO20): ")
            cliente.aplicar_desconto(codigo)
        elif escolha == '5':
            cliente.finalizar_compra()
        elif escolha == '6':
            cliente.ver_historico_compras()
        elif escolha == '7':
            cliente.obter_recomendacoes(produtos)
        elif escolha == '8':
            print("Até logo!")
            break
        else:
            print("Opção inválida.")
if __name__ == "__main__":
    main()