class Circulo:
    def __init__(self, raio):
        self.raio = raio 
        self.pi = 3.14
    def calculo(self):
        return self.pi * self.raio ** 2

    def calcular_perimetro(self):
        return 2 * self.pi * self.raio
    
raio = 10
CalcPerimetro = Circulo(raio)

area = CalcPerimetro.calculo()
perimetro = CalcPerimetro.calcular_perimetro()

print(f"Area {area} e seu perimetro {perimetro}")