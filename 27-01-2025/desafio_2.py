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