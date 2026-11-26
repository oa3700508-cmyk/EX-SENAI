class Figura:
    def __init__(self):
        self.area = []

    def calcular_area(self,area):
        return area

class Retangulo(Figura):

    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        self.area = self.base * self.altura
        print(f"A area do Retangulo é de {self.area}")

class Circulo(Figura):

    def __init__(self,raio):
        self.raio = raio

    def calcular_area(self):
        self.area = 3.14 * (self.raio ** 2 )
        print(f"A area do Circulo é de {self.area}")

ret1 = Retangulo(12,24)
cir1 = Circulo(12)

cir1.calcular_area()
ret1.calcular_area()