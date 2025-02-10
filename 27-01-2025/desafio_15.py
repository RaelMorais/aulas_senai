import random
import time
import pyttsx3

naipes = ("Espadas ♠", "Paus ♣", "Corações ♥", "Ouros ♦")
ranks = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
valores = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11,
}
engine = pyttsx3.init()
jogando = True

class Carta:
    def __init__(self, naipe, rank):
        self.naipe = naipe
        self.rank = rank

    def __str__(self):
        return f"{self.rank} de {self.naipe}"
class Baralho:
    def __init__(self):
        self.baralho = [Carta(naipe, rank) for naipe in naipes for rank in ranks]

    def embaralhar(self):
        random.shuffle(self.baralho)

    def distribuir(self):
        return self.baralho.pop()
class Mao:
    def __init__(self):
        self.cartas = []
        self.valor = 0
        self.ases = 0

    def adicionar_carta(self, carta):
        self.cartas.append(carta)
        self.valor += valores[carta.rank]
        if carta.rank == "A":
            self.ases += 1

    def ajustar_para_ace(self):
        while self.valor > 21 and self.ases:
            self.valor -= 10
            self.ases -= 1
def mostrar_mao(jogador, dealer, mostrar_dealer=False):
    print("\nMão do Jogador:", *jogador.cartas, sep="\n ")
    print(f"Mão do Jogador = {jogador.valor}")
    print("\nMão do Dealer:")
    if mostrar_dealer:
        print(*dealer.cartas, sep="\n ")
        print(f"Mão do Dealer = {dealer.valor}")
    else:
        print(" <carta oculta>")
        print(f" {dealer.cartas[1]}")

def resultado_final(jogador, dealer):
    print("\n----------------------------------------------------------------")
    print("                     ★ Resultados Finais ★")
    print("----------------------------------------------------------------")
    mostrar_mao(jogador, dealer, mostrar_dealer=True)

def mensagem_vitoria(vencedor):
    if vencedor == "jogador":
        print("Você ganhou!")
        speak("Jogador tem blackjack! Você ganhou!")

    elif vencedor == "dealer":
        print("\n--- Dealer ganhou! ---")
        speak("Dealer ganhou")
    elif vencedor == "empate":
        print("\nFoi um empate!")
        speak("Empate")
    elif vencedor == "estouro_jogador":
        print("\n--- Jogador estourou! ---")
        speak("Voce estourou, logo o dealer ganhou")
    elif vencedor == "estouro_dealer":
        print("\n--- Dealer estourou! Você ganhou! ---")
        speak("O dealer estourou, logo voce ganhou")

def pedir_ou_ficar():
    while True:
        speak("Deseja ficar ou sair?")
        opcao = input("\nVocê gostaria de Pedir ou Ficar? Digite [p/f] ").lower()
        if opcao == "p":
            return "pedir"
        elif opcao == "f":
            return "ficar"
        else:
            print("Desculpe, entrada inválida. Por favor, digite [p/f].")

def jogar_novamente():
    while True:
        novo_jogo = input("\nJogar outra mão? [S/N] ").lower()
        if novo_jogo == "s":
            return True
        elif novo_jogo == "n":
            print("\n------------------------Obrigado por jogar!---------------------\n")
            speak("SOLTA CARTA CARAI TIGRINHO FILHA DA... ATÉ MAIS")
            return False
        else:
            speak("Entrada inválida. Por favor, digite 's' ou 'n'.")
while True:
    def speak(speech):
        engine.say(speech)
        engine.runAndWait()
    print("\n----------------------------------------------------------------")
    print("                ♠♣♥♦ BEM-VINDO AO JOGO DO TIGRINHO! ♠♣♥♦")
    print("                          SOLTA A CARTA!")
    print("----------------------------------------------------------------")
    print("Regras do Jogo: Chegue o mais próximo de 21 que você puder sem ultrapassar!\n"
          "O dealer pede até alcançar 17.\nOs ases podem contar como 1 ou 11.")
    speak("Regras do Jogo: Chegue o mais próximo de 21 que você puder sem ultrapassar!\n"
          "O dealer pede até alcançar 17.\nOs ases podem contar como 1 ou 11.")
    
    baralho = Baralho()
    baralho.embaralhar()

    mao_jogador = Mao()
    mao_dealer = Mao()

    mao_jogador.adicionar_carta(baralho.distribuir())
    mao_jogador.adicionar_carta(baralho.distribuir())

    mao_dealer.adicionar_carta(baralho.distribuir())
    mao_dealer.adicionar_carta(baralho.distribuir())

    mostrar_mao(mao_jogador, mao_dealer)

    while jogando:
        acao = pedir_ou_ficar()
        if acao == "pedir":
            mao_jogador.adicionar_carta(baralho.distribuir())
            mao_jogador.ajustar_para_ace()
            mostrar_mao(mao_jogador, mao_dealer)
            if mao_jogador.valor > 21:
                mensagem_vitoria("estouro_jogador")
                break
        elif acao == "ficar":
            print("Jogador ficou. O dealer está jogando.")
            speak("Jogador ficou. O dealer está jogando.")
            jogando = False

    if mao_jogador.valor <= 21:
        while mao_dealer.valor < 17:
            mao_dealer.adicionar_carta(baralho.distribuir())
            mao_dealer.ajustar_para_ace()
        time.sleep(1)
        resultado_final(mao_jogador, mao_dealer)
        if mao_dealer.valor > 21:
            mensagem_vitoria("estouro_dealer")
        elif mao_dealer.valor > mao_jogador.valor:
            mensagem_vitoria("dealer")
        elif mao_dealer.valor < mao_jogador.valor:
            mensagem_vitoria("jogador")
        else:
            mensagem_vitoria("empate")
        if jogar_novamente() == False:
            break
