class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    #forma curta de chamar
    def exibir(self):
        print(f"produto: {self.nome}")
        print(f"preco: {self.preco}")
        print(f"estoque: {self.estoque}")
        print("-" * 80)

p1 = Produto("Arroz", 5.99, 30)
p2 = Produto("Feijão", 8.99, 20)

print(type(p1))
print(p1)
print(p1 == p2)      


#forma extensa de chamar
print(p1.nome)
print(p1.preco)
print(p1.estoque)


p1.exibir()
