from datetime import datetime, date


class Evento:
    def __init__(self, id, nome, data, hora, local, descricao):
        self.id = id
        self.nome = nome
        self.data = datetime.strptime(data, "%d/%m/%Y")
        self.hora = hora
        self.local = local
        self.descricao = descricao
        self.tarefas = []
        self.fornecedores = []
        self.convidados = []
        self.pagamentos = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
        print(f"Tarefa '{tarefa.descricao}' adicionada ao evento {self.nome}.")

    def adicionar_fornecedor(self, fornecedor):
        self.fornecedores.append(fornecedor)
        print(f"Fornecedor {fornecedor.nome} associado ao evento {self.nome}.")

    def adicionar_convidado(self, convidado):
        self.convidados.append(convidado)
        print(f"Convidado {convidado.nome} adicionado ao evento {self.nome}.")

    def adicionar_pagamento(self, pagamento):
        self.pagamentos.append(pagamento)
        print(f"Pagamento de R${pagamento.valor:.2f} adicionado ao evento {self.nome}.")

    def requisitos_especificos(self):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")

    def __str__(self):
        return (f"Evento {self.id}: {self.nome} ({self.data.strftime('%d/%m/%Y')} às {self.hora}, "
                f"Local: {self.local}, Descrição: {self.descricao})")

class Casamento(Evento):
    def __init__(self, id, nome, data, hora, local, descricao, noivos):
        super().__init__(id, nome, data, hora, local, descricao)
        self.noivos = noivos

    def requisitos_especificos(self):
        return "Casamento requer: decoração floral, buffet especial, música ao vivo, fotógrafo."

class EventoCorporativo(Evento):
    def __init__(self, id, nome, data, hora, local, descricao, empresa):
        super().__init__(id, nome, data, hora, local, descricao)
        self.empresa = empresa

    def requisitos_especificos(self):
        return "Evento corporativo requer: projetor, coffee break, material de apresentação."

class Festa(Evento):
    def __init__(self, id, nome, data, hora, local, descricao, tema):
        super().__init__(id, nome, data, hora, local, descricao)
        self.tema = tema

    def requisitos_especificos(self):
        return f"Festa requer: decoração temática ({self.tema}), DJ, pista de dança."


class Tarefa:
    def __init__(self, id, descricao, prazo, responsavel, status="Pendente"):
        self.id = id
        self.descricao = descricao
        self.prazo = datetime.strptime(prazo, "%d/%m/%Y")
        self.responsavel = responsavel
        self.status = status
        self.atualizar_status()

    def atualizar_status(self):
        if self.status != "Concluída" and self.prazo.date() < date.today():
            self.status = "Atrasada"

    def __str__(self):
        return (f"Tarefa {self.id}: {self.descricao} (Prazo: {self.prazo.strftime('%d/%m/%Y')}, "
                f"Responsável: {self.responsavel.nome}, Status: {self.status})")


class Fornecedor:
    def __init__(self, id, nome, servico):
        self.id = id
        self.nome = nome
        self.servico = servico

    def __str__(self):
        return f"Fornecedor {self.id}: {self.nome} ({self.servico})"


class Responsavel:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome


class Convidado:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Pagamento:
    def __init__(self, id, descricao, valor, vencimento):
        self.id = id
        self.descricao = descricao
        self.valor = valor
        self.vencimento = datetime.strptime(vencimento, "%d/%m/%Y")
        self.pago = False

    def marcar_como_pago(self):
        self.pago = True
        print(f"Pagamento {self.id} ({self.descricao}) marcado como pago.")

    def __str__(self):
        status = "Pago" if self.pago else "Pendente"
        return (f"Pagamento {self.id}: {self.descricao}, Valor: R${self.valor:.2f}, "
                f"Vencimento: {self.vencimento.strftime('%d/%m/%Y')}, Status: {status}")

class GerenciadorEventos:
    def __init__(self):
        self.eventos = []
        self.fornecedores = []
        self.responsaveis = []
        self.convidados = []

    def criar_evento(self, tipo, id, nome, data, hora, local, descricao, extra):
        if tipo == "Casamento":
            evento = Casamento(id, nome, data, hora, local, descricao, extra)
        elif tipo == "Evento Corporativo":
            evento = EventoCorporativo(id, nome, data, hora, local, descricao, extra)
        elif tipo == "Festa":
            evento = Festa(id, nome, data, hora, local, descricao, extra)
        else:
            print("Tipo de evento inválido.")
            return
        self.eventos.append(evento)
        print(f"Evento '{nome}' criado: {evento.requisitos_especificos()}")

    def adicionar_tarefa(self, evento_id, descricao, prazo, responsavel_id):
        evento = next((e for e in self.eventos if e.id == evento_id), None)
        responsavel = next((r for r in self.responsaveis if r.id == responsavel_id), None)
        if evento and responsavel:
            tarefa = Tarefa(len(evento.tarefas) + 1, descricao, prazo, responsavel)
            evento.adicionar_tarefa(tarefa)
        else:
            print("Evento ou responsável não encontrado.")

    def adicionar_fornecedor(self, evento_id, fornecedor_id):
        evento = next((e for e in self.eventos if e.id == evento_id), None)
        fornecedor = next((f for f in self.fornecedores if f.id == fornecedor_id), None)
        if evento and fornecedor:
            evento.adicionar_fornecedor(fornecedor)
        else:
            print("Evento ou fornecedor não encontrado.")

    def adicionar_convidado(self, evento_id, convidado_id):
        evento = next((e for e in self.eventos if e.id == evento_id), None)
        convidado = next((c for c in self.convidados if c.id == convidado_id), None)
        if evento and convidado:
            evento.adicionar_convidado(convidado)
        else:
            print("Evento ou convidado não encontrado.")

    def adicionar_pagamento(self, evento_id, descricao, valor, vencimento):
        evento = next((e for e in self.eventos if e.id == evento_id), None)
        if evento:
            pagamento = Pagamento(len(evento.pagamentos) + 1, descricao, valor, vencimento)
            evento.adicionar_pagamento(pagamento)
        else:
            print("Evento não encontrado.")

    def marcar_pagamento_pago(self, evento_id, pagamento_id):
        evento = next((e for e in self.eventos if e.id == evento_id), None)
        if evento:
            pagamento = next((p for p in evento.pagamentos if p.id == pagamento_id), None)
            if pagamento:
                pagamento.marcar_como_pago()
            else:
                print("Pagamento não encontrado.")
        else:
            print("Evento não encontrado.")

    def relatorio_eventos(self, data=None, status_tarefa=None, fornecedor_id=None):
        print("\nRelatório de Eventos:")
        for evento in self.eventos:
            if data and evento.data.date() != datetime.strptime(data, "%d/%m/%Y").date():
                continue
            print(evento)
            print("Tarefas:")
            for tarefa in evento.tarefas:
                tarefa.atualizar_status()
                if status_tarefa and tarefa.status != status_tarefa:
                    continue
                print(f"  {tarefa}")
            print("Fornecedores:")
            for fornecedor in evento.fornecedores:
                if fornecedor_id and fornecedor.id != fornecedor_id:
                    continue
                print(f"  {fornecedor}")
            print("Pagamentos:")
            for pagamento in evento.pagamentos:
                print(f"  {pagamento}")

def main():
    gerenciador = GerenciadorEventos()
    gerenciador.fornecedores = [Fornecedor(1, "Buffet Sabor", "Catering"), Fornecedor(2, "Decora Mais", "Decoração")]
    gerenciador.responsaveis = [Responsavel(1, "Ana"), Responsavel(2, "Carlos")]
    gerenciador.convidados = [Convidado(1, "João"), Convidado(2, "Maria")]

    while True:
        print("\nMenu Gerenciador de Eventos:")
        print("1. Criar Evento\n2. Adicionar Tarefa\n3. Adicionar Fornecedor\n4. Adicionar Convidado\n5. Adicionar Pagamento\n6. Marcar Pagamento como Pago\n7. Relatório de Eventos\n8. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            tipo = input("Tipo (Casamento/Evento Corporativo/Festa): ")
            id = len(gerenciador.eventos) + 1
            nome = input("Nome do evento: ")
            data = input("Data (dd/mm/aaaa): ")
            hora = input("Hora (HH:MM): ")
            local = input("Local: ")
            descricao = input("Descrição: ")
            extra = input("Noivos/Empresa/Tema: ")
            gerenciador.criar_evento(tipo, id, nome, data, hora, local, descricao, extra)
        elif escolha == '2':
            evento_id = int(input("ID do evento: "))
            descricao = input("Descrição da tarefa: ")
            prazo = input("Prazo (dd/mm/aaaa): ")
            responsavel_id = int(input("ID do responsável: "))
            gerenciador.adicionar_tarefa(evento_id, descricao, prazo, responsavel_id)
        elif escolha == '3':
            evento_id = int(input("ID do evento: "))
            fornecedor_id = int(input("ID do fornecedor: "))
            gerenciador.adicionar_fornecedor(evento_id, fornecedor_id)
        elif escolha == '4':
            evento_id = int(input("ID do evento: "))
            convidado_id = int(input("ID do convidado: "))
            gerenciador.adicionar_convidado(evento_id, convidado_id)
        elif escolha == '5':
            evento_id = int(input("ID do evento: "))
            descricao = input("Descrição do pagamento: ")
            valor = float(input("Valor: "))
            vencimento = input("Vencimento (dd/mm/aaaa): ")
            gerenciador.adicionar_pagamento(evento_id, descricao, valor, vencimento)
        elif escolha == '6':
            evento_id = int(input("ID do evento: "))
            pagamento_id = int(input("ID do pagamento: "))
            gerenciador.marcar_pagamento_pago(evento_id, pagamento_id)
        elif escolha == '7':
            data = input("Filtrar por data (dd/mm/aaaa, deixe em branco para todos): ") or None
            status = input("Filtrar por status de tarefa (Pendente/Concluída/Atrasada, deixe em branco para todos): ") or None
            fornecedor_id = int(input("Filtrar por ID de fornecedor (0 para todos): ")) or None
            gerenciador.relatorio_eventos(data, status, fornecedor_id)
        elif escolha == '8':
            print("Até logo!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()