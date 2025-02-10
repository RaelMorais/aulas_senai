class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        self.ligado = True
        print(f"O {self.marca} {self.modelo} está ligado.")

    def desligar(self):
        self.ligado = False
        print(f"O {self.marca} {self.modelo} está desligado.")

    def acelerar(self):
        if self.ligado:
            self.velocidade += 10
            print(f"O {self.marca} {self.modelo} está a {self.velocidade} km/h.")
        else:
            print(f"O {self.marca} {self.modelo} precisa estar ligado para acelerar.")

    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 10
            print(f"O {self.marca} {self.modelo} está a {self.velocidade} km/h.")
        else:
            print(f"O {self.marca} {self.modelo} já está parado.")

carro1 = Carro("Chevrolet", "Onix", 2022)
carro2 = Carro("Chevrolet", "Prisma", 2014)
carro3 = Carro("Ford", "Fusion", 2019)

carro1.ligar()
carro1.acelerar()
carro1.frear()
carro1.desligar()

carro2.ligar()
carro2.acelerar()
carro2.frear()
carro2.desligar()

carro3.ligar()
carro3.acelerar()
carro3.frear()
carro3.desligar()