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
