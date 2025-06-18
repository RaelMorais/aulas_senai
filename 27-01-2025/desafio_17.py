class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.emprestimos = {}

    def cadastrar_livro(self, isbn, titulo, autor, ano):
        self.livros[isbn] = {
            "titulo": titulo,
            "autor": autor,
            "ano": ano,
            "disponivel": True
        }
        print(f"Livro '{titulo}' cadastrado com sucesso!")

    def fazer_emprestimo(self, isbn, usuario):
        if isbn in self.livros:
            if self.livros[isbn]["disponivel"]:
                self.livros[isbn]["disponivel"] = False
                self.emprestimos[isbn] = usuario
                print(f"Livro '{self.livros[isbn]['titulo']}' emprestado para {usuario}.")
            else:
                print(f"Livro '{self.livros[isbn]['titulo']}' não está disponível.")
        else:
            print("Livro não encontrado.")

    def devolver_livro(self, isbn):
        if isbn in self.livros:
            if not self.livros[isbn]["disponivel"]:
                self.livros[isbn]["disponivel"] = True
                usuario = self.emprestimos.pop(isbn, None)
                print(f"Livro '{self.livros[isbn]['titulo']}' devolvido por {usuario}.")
            else:
                print(f"Livro '{self.livros[isbn]['titulo']}' já está disponível.")
        else:
            print("Livro não encontrado.")

    def verificar_disponibilidade(self, isbn):
        if isbn in self.livros:
            if self.livros[isbn]["disponivel"]:
                print(f"Livro '{self.livros[isbn]['titulo']}' está disponível.")
            else:
                print(f"Livro '{self.livros[isbn]['titulo']}' não está disponível.")
        else:
            print("Livro não encontrado.")