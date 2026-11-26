class Produto:
    def __init__(self,nome,categoria,preço,estoque):
        self.nome = nome
        self.categoria = categoria
        self.preço = preço
        self.estoque = estoque

    def exibir(self):
        print(f"Produto: {self.nome}")    
        print(f"Categoria: {self.categoria}")    
        print(f"Preço: {self.preço}")    
        print(f"Estoque: {self.estoque}")
        print("=" * 80)
    
    def valor_total(self):
        return self.preço * self.estoque        

    def aplicar_desconto(self,percentual):
        self.preço *= (1-percentual / 100)
        print(f"Desconto aplicado! Novo preço: R$ {self.preço}")

    def vender(self, quantidade):
        if quantidade > self.estoque:
            print("Status: \033[41mEsgotado\033[0m") #Muda a cor para vermelho caso o estoque esteja insuficiente
            print(F"{self.nome}")
        else:
            self.estoque -= quantidade
            print("\nStatus: \033[42mEm estoque\033[0m") #Muda a cor para Verde caso ainda haja produto no estoque
            print(f"Vendidos {quantidade} x {self.nome} - Estoque restante: {self.estoque}")
    
    def repor_estoque(self, quantidade):
        self.estoque += quantidade
        print(f"Novo estoque: { self.estoque}")     

p1 = Produto("Achocolatado Itambezinho", "Bebidas", 3.00, 35) 
p2 = Produto("Snake Venom", "Bebidas" ,513.00, 20)          

#Exibindo os Produtos 
p1.exibir()
p2.exibir()

#Mostra os itens vendidos no estoque
p1.vender(40)
p2.vender(10)

print("-" * 80)
p2.aplicar_desconto(35)

print("-" * 80)
p1.repor_estoque(20)
p2.repor_estoque(5)