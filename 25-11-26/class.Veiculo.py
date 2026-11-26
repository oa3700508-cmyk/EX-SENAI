class Veiculo:
    def __init__(self,marca,Vmax):
        self.marca = marca
        self.Vmax = Vmax
   
    def mover(self):
        return "Move"

class Bicicleta(Veiculo):
    def __init__(self,marca,Vmax,num_marchas):
        self.num_marchas = num_marchas
        super().__init__(marca,Vmax)

    def mover(self):
        print(f"A {self.marca} se movimenta numa velocidade de {self.Vmax}")

    def marchas(self):
        print(f"A {self.marca} tem um total de {self.num_marchas} marchas")

class Carro(Veiculo):
    def __init__(self, marca, Vmax,num_portas):
        self.num_portas = num_portas
        super().__init__(marca, Vmax)                    
   
    def mover(self):
        print(f"O {self.marca} faz uma arrancada numa velocidade máxima de {self.Vmax}")
   
    def portas(self):
        print(f"O {self.marca} tem um total de {self.num_portas} portas")

C1 = Carro("Celta",150,4)
B1 = Bicicleta("Santa Cruz",200,6)

print("-" * 80)
B1.mover()
B1.marchas()
print("-" * 80)
C1.mover()
C1.portas()
print("-" * 80)
B1.mover()