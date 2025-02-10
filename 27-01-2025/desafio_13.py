class Agenda:
    def __init__(self):
        self.contatos = {}

    def adicionar_numero(self, nome, ddd, numero):
        self.contatos[nome] = (ddd, numero)
        print("Contato adicionado")

    def editar_numero(self, nome, novoNome = None, novoNumero = None):
        if nome in self.contatos:
            if novoNome:
                self.contatos[novoNome] = self.contatos.pop(nome)
                nome = novoNome  
            if novoNumero:
                ddd, _ = self.contatos[nome]
                self.contatos[nome] = (ddd, novoNumero)
                print(f"Contato {nome} atualizado")
        else:
            print(f"Erro: Contato {nome} não encontrado!")

    def remover_numero(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            print(f"Contato {nome} removido com sucesso!")
        else:
            print(f"Erro: Contato {nome} não encontrado!")

    def buscaContato(self, nome, numero):
        encontrados = [nome for nome, (ddd, num) in self.contatos.items() if num == numero]
        if nome in self.contatos and self.contatos[nome][1] == numero:
            print(f"Contato encontrado: {nome} - {self.contatos[nome][1]}")
        elif encontrados:
            for nome in encontrados:
                print(f"Contato encontrado: {nome} - {numero}")
        else:
            print(f"Erro: Não há contatos com o número {numero}.")

    def exibir_numeros(self):
        if not self.contatos:
            print("A agenda está vazia.")
        else:
            print("Contatos na agenda:")
            for nome, (ddd, numero) in self.contatos.items():
                print(f"{nome}: ({ddd}) {numero}")

# Criando a agenda
agenda = Agenda()

# Adicionando contatos
agenda.adicionar_numero("Alice", "11", "123456789")
agenda.adicionar_numero("Bob", "21", "987654321")

# Exibindo contatos
agenda.exibir_numeros()

# Editando um contato
agenda.editar_numero("Alice", novoNumero="111223344")

# Buscando um contato
agenda.buscaContato("Alice", "111223344")

# Removendo um contato
agenda.remover_numero("Bob")
