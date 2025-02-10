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