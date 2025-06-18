class Animal:
    def __init__(self, id, nome, especie, dieta, habitat):
        self.id = id
        self.nome = nome
        self.especie = especie
        self.dieta = dieta
        self.habitat = habitat
        self.saude = "Saudável"
        self.alimentacao_log = []

    def __str__(self):
        return f"{self.nome} (ID: {self.id}, Espécie: {self.especie}, Habitat: {self.habitat.nome}, Saúde: {self.saude})"

class Habitat:
    def __init__(self, id, nome, tipo_ambiente):
        self.id = id
        self.nome = nome
        self.tipo_ambiente = tipo_ambiente

class Alimentacao:
    def __init__(self, id, animal, tipo_comida, quantidade):
        self.id = id
        self.animal = animal
        self.tipo_comida = tipo_comida
        self.quantidade = quantidade

    def __str__(self):
        return f"Alimentação {self.id}: {self.animal.nome} recebeu {self.quantidade}kg de {self.tipo_comida}"

class Veterinario:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def verificar_saude(self, animal, status_saude):
        animal.saude = status_saude
        print(f"Saúde de {animal.nome} atualizada para: {status_saude}")

class Funcionario:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Zoologico:
    def __init__(self):
        self.animais = []
        self.habitats = []
        self.alimentacoes = []
        self.veterinarios = []
        self.funcionarios = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)
        print(f"Animal {animal.nome} adicionado.")

    def adicionar_habitat(self, habitat):
        self.habitats.append(habitat)
        print(f"Habitat {habitat.nome} adicionado.")

    def registrar_alimentacao(self, animal, tipo_comida, quantidade):
        if animal in self.animais:
            alimentacao = Alimentacao(len(self.alimentacoes) + 1, animal, tipo_comida, quantidade)
            self.alimentacoes.append(alimentacao)
            animal.alimentacao_log.append(alimentacao)
            print(f"Alimentação registrada: {alimentacao}")
        else:
            print("Animal não encontrado.")

    def mover_animal(self, animal, novo_habitat):
        if animal in self.animais and novo_habitat in self.habitats:
            animal.habitat = novo_habitat
            print(f"{animal.nome} movido para {novo_habitat.nome}.")
        else:
            print("Animal ou habitat não encontrado.")

    def relatorio_animais(self):
        print("\nRelatório de Animais:")
        for animal in self.animais:
            print(animal)

def main():
    zoo = Zoologico()
    habitats = [Habitat(1, "Savana", "Terrestre"), Habitat(2, "Aquário", "Aquático")]
    for h in habitats:
        zoo.adicionar_habitat(h)
    animais = [
        Animal(1, "Simba", "Leão", "Carnívoro", habitats[0]),
        Animal(2, "Nemo", "Peixe", "Plâncton", habitats[1])
    ]
    for a in animais:
        zoo.adicionar_animal(a)
    veterinario = Veterinario(1, "Dr. Ana")
    zoo.veterinarios.append(veterinario)

    while True:
        print("\nMenu Zoológico:")
        print("1. Registrar Alimentação\n2. Verificar Saúde\n3. Mover Animal\n4. Relatório Animais\n5. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            id_animal = int(input("ID do animal: "))
            tipo_comida = input("Tipo de comida: ")
            quantidade = float(input("Quantidade (kg): "))
            animal = next((a for a in zoo.animais if a.id == id_animal), None)
            if animal:
                zoo.registrar_alimentacao(animal, tipo_comida, quantidade)
            else:
                print("Animal não encontrado.")
        elif escolha == '2':
            id_animal = int(input("ID do animal: "))
            saude = input("Status de saúde (Saudável/Doente): ")
            animal = next((a for a in zoo.animais if a.id == id_animal), None)
            if animal:
                veterinario.verificar_saude(animal, saude)
            else:
                print("Animal não encontrado.")
        elif escolha == '3':
            id_animal = int(input("ID do animal: "))
            id_habitat = int(input("ID do novo habitat: "))
            animal = next((a for a in zoo.animais if a.id == id_animal), None)
            habitat = next((h for h in zoo.habitats if h.id == id_habitat), None)
            if animal and habitat:
                zoo.mover_animal(animal, habitat)
            else:
                print("Animal ou habitat não encontrado.")
        elif escolha == '4':
            zoo.relatorio_animais()
        elif escolha == '5':
            print("Até logo!")
            break
        else:
            print("Opção inválida.")
if __name__ == "__main__":
    main()