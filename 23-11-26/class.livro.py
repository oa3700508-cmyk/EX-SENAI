class Livro:
    def __init__(self, titulo, autor, paginas, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponivel = disponivel

    def descrição(self):
       print(f"titulo: {self.titulo}")
       print(f"autor: {self.autor}")
       print(f"paginas: {self.paginas}")
       print(f"diponivel: {self.disponivel}")
       print("-" * 80)
   
    def devolver(self):
        if  self.disponivel == False:
            print("Livro Devolvido")
            self.disponivel = True
        else:
            print("O livro já foi devolvido")
    
    def emprestar(self):
        if self.disponivel == True:
            self.disponivel = False
        else:
            print("Livro Emprestado")

L1 = Livro("Tudo e Rio", "Carla Madeira", 302, False)


L1.emprestar()
L1.descrição()
L1.devolver()
L1.descrição()