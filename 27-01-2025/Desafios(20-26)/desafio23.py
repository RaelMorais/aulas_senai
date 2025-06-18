from datetime import datetime

class Tarefa:
    def __init__(self, id, titulo, descricao, prioridade, vencimento, categoria, status="Pendente"):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade  # Alta, Média, Baixa
        self.vencimento = datetime.strptime(vencimento, "%d/%m/%Y")
        self.categoria = categoria
        self.status = status

    def __str__(self):
        return (f"Tarefa {self.id}: {self.titulo} (Prioridade: {self.prioridade}, Vencimento: {self.vencimento.strftime('%d/%m/%Y')}, "
                f"Categoria: {self.categoria}, Status: {self.status})")

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def criar_tarefa(self, titulo, descricao, prioridade, vencimento, categoria):
        tarefa = Tarefa(len(self.tarefas) + 1, titulo, descricao, prioridade, vencimento, categoria)
        self.tarefas.append(tarefa)
        print(f"Tarefa '{titulo}' criada.")

    def editar_tarefa(self, id, titulo=None, descricao=None, prioridade=None, vencimento=None, categoria=None, status=None):
        tarefa = next((t for t in self.tarefas if t.id == id), None)
        if tarefa:
            if titulo:
                tarefa.titulo = titulo
            if descricao:
                tarefa.descricao = descricao
            if prioridade:
                tarefa.prioridade = prioridade
            if vencimento:
                tarefa.vencimento = datetime.strptime(vencimento, "%d/%m/%Y")
            if categoria:
                tarefa.categoria = categoria
            if status:
                tarefa.status = status
            print(f"Tarefa {id} editada.")
        else:
            print("Tarefa não encontrada.")

    def excluir_tarefa(self, id):
        tarefa = next((t for t in self.tarefas if t.id == id), None)
        if tarefa:
            self.tarefas.remove(tarefa)
            print(f"Tarefa {id} excluída.")
        else:
            print("Tarefa não encontrada.")

    def listar_tarefas(self, status=None, prioridade=None):
        print("\nLista de Tarefas:")
        for tarefa in self.tarefas:
            if (status is None or tarefa.status == status) and (prioridade is None or tarefa.prioridade == prioridade):
                print(tarefa)

def main():
    gerenciador = GerenciadorTarefas()
    while True:
        print("\nMenu Tarefas:")
        print("1. Criar Tarefa\n2. Editar Tarefa\n3. Excluir Tarefa\n4. Listar Tarefas\n5. Filtrar por Status\n6. Filtrar por Prioridade\n7. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            prioridade = input("Prioridade (Alta/Média/Baixa): ")
            vencimento = input("Vencimento (dd/mm/aaaa): ")
            categoria = input("Categoria: ")
            gerenciador.criar_tarefa(titulo, descricao, prioridade, vencimento, categoria)
        elif escolha == '2':
            id = int(input("ID da tarefa: "))
            print("Deixe em branco para não alterar.")
            titulo = input("Novo título: ") or None
            descricao = input("Nova descrição: ") or None
            prioridade = input("Nova prioridade: ") or None
            vencimento = input("Novo vencimento (dd/mm/aaaa): ") or None
            categoria = input("Nova categoria: ") or None
            status = input("Novo status (Pendente/Em Andamento/Concluída): ") or None
            gerenciador.editar_tarefa(id, titulo, descricao, prioridade, vencimento, categoria, status)
        elif escolha == '3':
            id = int(input("ID da tarefa: "))
            gerenciador.excluir_tarefa(id)
        elif escolha == '4':
            gerenciador.listar_tarefas()
        elif escolha == '5':
            status = input("Status (Pendente/Em Andamento/Concluída): ")
            gerenciador.listar_tarefas(status=status)
        elif escolha == '6':
            prioridade = input("Prioridade (Alta/Média/Baixa): ")
            gerenciador.listar_tarefas(prioridade=prioridade)
        elif escolha == '7':
            print("Até logo!")
            break
        else:
            print("Opção inválida.")
if __name__ == "__main__":
    main()