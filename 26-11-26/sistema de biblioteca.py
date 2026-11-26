class usuario:
    def __init__(self, nome,):
        self.nome = nome
        self.limite = 1
        self.emprestimos = []

    def pegar_livro(self, livro):
        if len(self.emprestimos) < self.limite:
            livro.empretar()
            self.emprestimos.append(livro)

class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True

    def emprestar(self):
        """Marca o livro como emprestado. Retorna True se deu certo."""
        if not self.disponivel:
            return False
        self.disponivel = False
        return True

    def devolver(self):
        self.disponivel = True

    def descricao(self):
        status = "disponível" if self.disponivel else "emprestado"
        return f"{self.titulo} - {self.autor} (ISBN: {self.isbn}) [{status}]"


class Usuario:
    """Classe base: limite de 1 livro."""

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.limite = 1
        self.livros_emprestados = []

    def pegar_livro(self, livro):
        if len(self.livros_emprestados) >= self.limite:
            print(f"{self.nome} já atingiu o limite de {self.limite} livro(s).")
            return False
        if not livro.emprestar():
            print(f"'{livro.titulo}' não está disponível.")
            return False
        self.livros_emprestados.append(livro)
        print(f"{self.nome} pegou '{livro.titulo}'.")
        return True

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            livro.devolver()
            self.livros_emprestados.remove(livro)
            print(f"{self.nome} devolveu '{livro.titulo}'.")


class Aluno(Usuario):
    """Aluno: máximo de 2 livros."""

    def __init__(self, nome, matricula):
        super().__init__(nome, matricula)
        self.limite = 2

    def pegar_livro(self, livro):
        if len(self.livros_emprestados) >= self.limite:
            print(f"[Aluno] {self.nome} só pode ter {self.limite} livros ao mesmo tempo.")
            return False
        return super().pegar_livro(livro)


class Professor(Usuario):
    """Professor: máximo de 5 livros."""

    def __init__(self, nome, matricula):
        super().__init__(nome, matricula)
        self.limite = 5

    def pegar_livro(self, livro):
        if len(self.livros_emprestados) >= self.limite:
            print(f"[Professor] {self.nome} só pode ter {self.limite} livros ao mesmo tempo.")
            return False
        return super().pegar_livro(livro)


if __name__ == "__main__":
    livros = [
        Livro("Senhor dos Anéis", "Luciano", "111"),
        Livro("O Hobbit", "Robert Martin", "222"),
        Livro("Magico de Oz", "Julia", "333"),
        Livro("Sitio do picapau Amarelo", "Monteiro Lobato", "444"),
    ]

    ana = Aluno("Ana", "A001")
    carlos = Professor("Carlos", "P001")

    print("--- Aluno ---")
    ana.pegar_livro(livros[0])
    ana.pegar_livro(livros[1])
    ana.pegar_livro(livros[2])   # bloqueado: limite de 2

    print("\n--- Professor ---")
    carlos.pegar_livro(livros[0])  # bloqueado: já emprestado
    carlos.pegar_livro(livros[2])
    carlos.pegar_livro(livros[3])

    print("\n--- Devolução ---")
    ana.devolver_livro(livros[0])
    carlos.pegar_livro(livros[0])  # agora disponível

    print("\n--- Situação do acervo ---")
    for livro in livros:
        print(livro.descricao())