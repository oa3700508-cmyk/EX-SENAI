class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print("-" * 80)


c1 = Carro("Toyota", "Corolla", 2020)
c1.exibir()
c2 = Carro("Honda", "Civic", 2021)
c2.exibir()