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