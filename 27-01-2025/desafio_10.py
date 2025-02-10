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