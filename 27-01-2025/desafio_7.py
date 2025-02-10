class Triângulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def verificarTriangulo(self):
        if self.ladoA + self.ladoB > self.ladoC and self.ladoA + self.ladoC > self.ladoB and self.ladoB + self.ladoC > self.ladoA:
            print(f"É um triangulo e é {self.tipoTriangulo()}")
        else:
            print("Não é um triangulo")

    def tipoTriangulo(self):
        if self.ladoA == self.ladoB == self.ladoC:
            return "Triângulo Equilátero"
        if self.ladoA == self.ladoB or self.ladoA == self.ladoC or self.ladoB == self.ladoC:
            return "Triângulo Isósceles"
        else:
            return "Triângulo Escaleno"

tri = Triângulo(10, 7, 9)
tri.verificarTriangulo()
