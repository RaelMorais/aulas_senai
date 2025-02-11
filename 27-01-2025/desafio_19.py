import random as rd

class JogoAdivinhacao:
    def __init__(self):
        self.numeroSecreto = rd.randint(1, 100)
    
    def palpite(self, palpite):
        if palpite > self.numeroSecreto:
            return "Número é menor"
        elif palpite < self.numeroSecreto:
            return "Número é maior"
        else:
            return f"Parabéns, o número era {self.numeroSecreto}"
        
   
jogo = JogoAdivinhacao()

chances = 3

while chances > 0:
    input_usuario = int(input(">>>Chute "))
    resultado = jogo.palpite(input_usuario)
    print(resultado)
    if resultado != jogo.palpite:
        chances -=1
        print(f"Tente de novo possui {chances} chances")
    if chances == 0:
        print(f"Sem chances o número era {jogo.numeroSecreto}")