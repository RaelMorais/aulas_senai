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