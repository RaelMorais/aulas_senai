import random

class JogoAdivinhacao:
    def __init__(self):
        self.numero_secreto = random.randint(1, 100)
        self.tentativas = 0

    def fazer_palpite(self, palpite):
        self.tentativas += 1
        if palpite == self.numero_secreto:
            print(f"Parabéns! Você acertou o número {self.numero_secreto} em {self.tentativas} tentativas!")
            return True
        elif palpite < self.numero_secreto:
            print("Seu palpite é menor que o número secreto. Tente novamente!")
            return False
        else:
            print("Seu palpite é maior que o número secreto. Tente novamente!")
            return False

    def reiniciar_jogo(self):
        self.numero_secreto = random.randint(1, 100)
        self.tentativas = 0
        print("Jogo reiniciado! Um novo número secreto foi gerado.")