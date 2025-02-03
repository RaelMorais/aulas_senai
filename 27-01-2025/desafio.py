#Desafio 1
class Circulo:
    def __init__(self, raio):
        self.raio = raio 
        self.pi = 3.14
    def calculo(self):
        return self.pi * self.raio ** 2

    def calcular_perimetro(self):
        return 2 * self.pi * self.raio
    
raio = 10
CalcPerimetro = Circulo(raio)

area = CalcPerimetro.calculo()
perimetro = CalcPerimetro.calcular_perimetro()

print(f"Area {area} e seu perimetro {perimetro}")
    
#Desafio 02

class ContaBancaria:
    def __init__(self, nome, numConta, saldo):
        self.nome = nome
        self.numConta = numConta
        self.saldo = saldo
    
    def depositar(self, valor, condicao):
        if condicao: 
            self.saldo += valor
            print(f"O {self.nome} com a conta de número {self.numConta} está depositando R${valor:.2f}.")
        else:
            print("Erro")
    
    def sacar(self, valor, condicao):
        if condicao and self.saldo >= valor:
            self.saldo -= valor
            print(f"O valor de R${valor:.2f} foi sacado da conta de {self.nome}.")
        else:
            print("Erro: saldo insuficiente para o saque.")
    
    def exibir_saldo(self):
        print(f"Saldo atual da conta {self.numConta}: R${self.saldo:.2f}")


conta = ContaBancaria("João", 123456789, 1000)

conta.depositar(200, True)  
conta.exibir_saldo()


conta.sacar(150, True)  
conta.exibir_saldo()

conta.sacar(2000, True) 
conta.exibir_saldo()

#Desafio 03
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

#Desafio 04
class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def média(self, nota1, nota2, nota3):
        media = (nota1 + nota2 + nota3) / 3
        print(f"A média do {self.nome} com a matricula {self.matricula} é {media}")
        if media >= 7:
            print("Aprovado")
        elif media >= 4 and media <= 6:
            print("Em recuperação")
        else:
            print("Reprovado")
    
InfoAluno = Aluno("Joao Santos", 12345)
InfoAluno.média(10, 7, 10)

InfoAluno = Aluno("Joao Santos 2", 12346)
InfoAluno.média(10, 7, 0)

#Desafio 05
class Funcionário:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def salario_liquido(self, inss, beneficios):
        salario = self.salario - (inss + beneficios)
        print(f"O salario líquido do {self.nome} com cargo de {self.cargo} é {salario} caindo bruto {self.salario}")

FuncionarioSalario = Funcionário("Joao Alguma Coisa", 1512, "Aprendiz em Soluções Digitais" )
FuncionarioSalario.salario_liquido(200.0, 300.0)

FuncionarioSalario = Funcionário("Kauan Afonso", 4000.0, "Aprendiz em Soluções Digitais" )
FuncionarioSalario.salario_liquido(400.0, 1000.0)


#Desafio 06
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

#Desafio 07
class Triângulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def verificarTriangulo(self):
        if self.ladoA + self.ladoB > self.ladoC and self.ladoA + self.ladoC > self.ladoB and self.ladoB + self.ladoC > self.ladoA:
            print(f"É um triangulo e é {self.tipoTriangulo()}")
        else:
            print("Não é um triangulo")

    def tipoTriangulo(self):
        if self.ladoA == self.ladoB == self.ladoC:
            return "Triângulo Equilátero"
        if self.ladoA == self.ladoB or self.ladoA == self.ladoC or self.ladoB == self.ladoC:
            return "Triângulo Isósceles"
        else:
            return "Triângulo Escaleno"

tri = Triângulo(10, 7, 9)
tri.verificarTriangulo()

#Desafio 08 
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        self.ligado = True
        print(f"O {self.marca} {self.modelo} está ligado.")

    def desligar(self):
        self.ligado = False
        print(f"O {self.marca} {self.modelo} está desligado.")

    def acelerar(self):
        if self.ligado:
            self.velocidade += 10
            print(f"O {self.marca} {self.modelo} está a {self.velocidade} km/h.")
        else:
            print(f"O {self.marca} {self.modelo} precisa estar ligado para acelerar.")

    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 10
            print(f"O {self.marca} {self.modelo} está a {self.velocidade} km/h.")
        else:
            print(f"O {self.marca} {self.modelo} já está parado.")

carro1 = Carro("Chevrolet", "Onix", 2022)
carro2 = Carro("Chevrolet", "Prisma", 2014)
carro3 = Carro("Ford", "Fusion", 2019)

carro1.ligar()
carro1.acelerar()
carro1.frear()
carro1.desligar()

carro2.ligar()
carro2.acelerar()
carro2.frear()
carro2.desligar()

carro3.ligar()
carro3.acelerar()
carro3.frear()
carro3.desligar()

#Desafio 09
class Paciente:
    def __init__(self, nome, idade, AnoNsc, sexo, etnia):
        self.nome = nome 
        self.idade = idade
        self.sexo = sexo
        self.etnia = etnia
        self.AnoNsc = AnoNsc
        self.historico_consulta = []

    def adicionar_consulta(self, data, descricao):
        consulta = {
            "data":data,
            "descricao": descricao
        }

        self.historico_consulta.append(consulta)
    def exibir(self):
        print(f"Consultas do paciente {self.nome} \n Idade: {self.idade} anos \n Cor: {self.etnia} \n Genero: {self.sexo} \n Ano de Nascimento: {self.AnoNsc}")
        for consulta in self.historico_consulta:
                print(f"Data: {consulta['data']} | Descrição: {consulta['descricao']}")

paciente1 = Paciente("Joao da Silva", 47, 1978, "Masculino", "Pardo")
paciente1.adicionar_consulta("2025-01-20", "Clinico Geral")
paciente1.adicionar_consulta("2024-12-12", "Clinico Geral")
paciente1.exibir()

paciente2 = Paciente("Kauan", 18, 2007, "Masculino", "Branco")
paciente2.adicionar_consulta("2025-01-31", "Clinico Geral")
paciente2.adicionar_consulta("2024-12-11", "Clinico Geral")
paciente2.exibir()

#Desafio 10
class Livro:
    def __init__(self, titulo, autor, genero, numPag):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.numPag = numPag
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"Livro: {self.titulo} \n Autor: {self.autor} \n Genero: {self.genero}\n Numero de páginas: {self.numPag}\n Está emprestado")
        else:
            print(f"O livro {self.titulo} não está disponivel")
    
    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"Livro: {self.titulo} \n Autor: {self.autor} \n Genero: {self.genero}\n Numero de páginas: {self.numPag}\n Foi devolvido")
        else:
            print(f"O livro {self.titulo} está disponivel")
    def disponibilidade(self):
        if self.disponivel:
            print(f"Livro: {self.titulo} \n Autor: {self.autor} \n Genero: {self.genero}\n Numero de páginas: {self.numPag}\n Está disponivel")
        else:
            print("Nao disponivel")

livro1 = Livro("Dom Quixote", "Miguel de Cervantes", "Fantasia", 512)
livro1.emprestar()
livro1.devolver()
livro1.disponibilidade()

#Desafio 11
class Cliente:
    def __init__(self, nome, cpf, numConta):
        self.nome = nome
        self.cpf = cpf
        self.numConta = numConta

class Conta:
    def __init__(self, cliente, saldo_inicial=0):
        self.cliente = cliente
        self.saldo = saldo_inicial
        self.numConta = cliente.numConta

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} na conta {self.cliente.numConta}.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def transferir(self, valor, conta_destino):
        if valor <= self.saldo:
            self.saldo -= valor
            conta_destino.saldo += valor
            print(f"Transferência de R${valor} realizada com sucesso para a conta de {self.cliente.nome}.")
        else:
            print("saldo insuficiente.")

    def consultar_saldo(self):
        return f"SALDO ATUAL DE {self.cliente.nome}: {self.saldo}"

class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def cadastrar_cliente(self, nome, cpf, numConta):
        novo_cliente = Cliente(nome, cpf, numConta)
        self.clientes.append(novo_cliente)
        print(f"Cliente {nome} cadastrado com sucesso.")

    def abrir_conta(self, cpf, saldo_inicial=0):
        cliente = self.buscar_cliente(cpf)
        if cliente:
            nova_conta = Conta(cliente, saldo_inicial)
            self.contas.append(nova_conta)
            print("#"*20)
            print(f"Conta aberta para o cliente {cliente.nome} \nNúmero da conta: {cliente.numConta}.")
            print("#"*20)
            return nova_conta
        else:
            print(f"Cliente com CPF {cpf} não encontrado.")
            return None

    def buscar_cliente(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

banco = Banco()

banco.cadastrar_cliente("João Alguma coisa", "12342567810", 10000)
banco.cadastrar_cliente("Mariazinha sei la oq", "12456781189", 200)
banco.cadastrar_cliente("Kauanzera", "34512387632", 12)

conta1 = banco.abrir_conta("12342567810", 1000)
conta2 = banco.abrir_conta("12456781189", 1000)
conta3 = banco.abrir_conta("34512387632", 100)

conta1.depositar(200)
conta1.sacar(100)

conta1.transferir(100, conta2)
conta2.transferir(200, conta3)

print(conta1.consultar_saldo())
print(conta2.consultar_saldo())
print(conta3.consultar_saldo())

#DESAFIO 12
#Crie uma classe chamada “LojaVirtual” que represente uma plataforma de vendas
#online. Essa classe deve ter funcionalidades para cadastrar produtos, gerar carrinho de
#compras, aplicar descontos e calcular o valor total da compra.
# 
#         


class Produto:
    def __init__(self, nome, preco, fornecedor):
        self.nome = nome
        self.preco = preco
        self.fornecedor = fornecedor

        return f"{self.nome} - R${self.preco}"

class Carrinho:
        def __init__(self):
            self.produto = []
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

        def cadastrar_produto(self, nome, preco):
            produto = Produto(nome, preco)
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
loja.cadastrar_produto("Camiseta", 49.90, "Nike")
loja.cadastrar_produto("Calça", 89.90, "Adidas")
loja.cadastrar_produto("Tênis", 199.90, "Rebook")

print("Produtos disponíveis:")
for produto in loja.listar_produtos():
    print(produto)

print(loja.adicionar_ao_carrinho("Camiseta"))
print(loja.adicionar_ao_carrinho("Tênis"))

print(f"Total do carrinho: R$ {loja.calcular_total():.2f}")

total_com_desconto = loja.aplicar_desconto(10)  # 10% de desconto
print(f"Total com desconto: R$ {total_com_desconto:.2f}")

print(loja.remover_do_carrinho("Camiseta"))
print(f"Total do carrinho após remoção: R$ {loja.calcular_total():.2f}")













