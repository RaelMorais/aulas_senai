import random

class Personagem:
    def __init__(self, nome, saude=100, forca=10, defesa=5, nivel=1):
        self.nome = nome
        self.saude = saude
        self.saude_max = saude
        self.forca = forca
        self.defesa = defesa
        self.nivel = nivel
        self.experiencia = 0
        self.inventario = {"Poção de Cura": 2}
        self.habilidade_especial = "Ataque Crítico"

    def atacar(self, alvo):
        dano = max(0, self.forca - alvo.defesa)
        if random.random() < 0.2:  # 20% de chance de crítico
            dano *= 2
            print(f"{self.nome} usou {self.habilidade_especial}! Dano: {dano}")
        else:
            print(f"{self.nome} ataca {alvo.nome}! Dano: {dano}")
        alvo.saude -= dano
        if alvo.saude <= 0:
            self.ganhar_experiencia(50)
            print(f"{alvo.nome} foi derrotado!")
        return alvo.saude > 0

    def usar_item(self, item):
        if item in self.inventario and self.inventario[item] > 0:
            if item == "Poção de Cura":
                self.saude = min(self.saude + 30, self.saude_max)
                self.inventario[item] -= 1
                print(f"{self.nome} usou {item}. Saúde: {self.saude}")
            else:
                print("Item desconhecido.")
        else:
            print(f"{self.nome} não tem {item} no inventário.")

    def ganhar_experiencia(self, xp):
        self.experiencia += xp
        print(f"{self.nome} ganhou {xp} XP!")
        if self.experiencia >= self.nivel * 100:
            self.nivel += 1
            self.forca += 2
            self.defesa += 1
            self.saude_max += 10
            self.saude = self.saude_max
            self.experiencia = 0
            print(f"{self.nome} subiu para o nível {self.nivel}!")

    def __str__(self):
        return f"{self.nome} (Nível: {self.nivel}, Saúde: {self.saude}/{self.saude_max}, Força: {self.forca}, Defesa: {self.defesa}, XP: {self.experiencia})"

def main():
    jogador = Personagem("Herói")
    inimigo = Personagem("Orc", saude=80, forca=12, defesa=3)

    while True:
        print("\nEstado Atual:")
        print(jogador)
        print(inimigo)
        print("\nMenu Combate:")
        print("1. Atacar\n2. Usar Item\n3. Fugir")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            if not jogador.atacar(inimigo):
                print("Vitória!")
                break
            if inimigo.saude > 0 and not inimigo.atacar(jogador):
                print("Derrota!")
                break
        elif escolha == '2':
            item = input("Item (Poção de Cura): ")
            jogador.usar_item(item)
            if inimigo.saude > 0 and not inimigo.atacar(jogador):
                print("Derrota!")
                break
        elif escolha == '3':
            if random.random() < 0.5:
                print("Fuga bem-sucedida!")
                break
            else:
                print("Fuga falhou!")
                if inimigo.saude > 0 and not inimigo.atacar(jogador):
                    print("Derrota!")
                    break
        else:
            print("Opção inválida.")
if __name__ == "__main__":
    main()