def formatar_reais(valor):
    """Formata um número no padrão brasileiro: R$ 9.458,00"""
    texto = f"{valor:,.2f}"
    return "R$ " + texto.replace(",", "X").replace(".", ",").replace("X", ".")


class Produto:
    def __init__(self, nome, categoria, preco, estoque):
        if preco < 0 or estoque < 0:
            raise ValueError("Preço e estoque não podem ser negativos.")
        self.nome = nome.strip()
        self.categoria = categoria.strip().lower()
        self.preco = preco
        self.estoque = estoque

    def __str__(self):
        return (f"{self.nome} | {self.categoria} | "
                f"{formatar_reais(self.preco)} | estoque: {self.estoque}")

    def exibir(self):
        print(f"Produto:   {self.nome}")
        print(f"Categoria: {self.categoria}")
        print(f"Preço:     {formatar_reais(self.preco)}")
        print(f"Estoque:   {self.estoque}")
        print(f"Valor em estoque: {formatar_reais(self.valor_total())}")

    def valor_total(self):
        return self.preco * self.estoque

    def aplicar_desconto(self, percentual):
        if not 0 < percentual <= 100:
            print("Percentual inválido! Use um valor entre 0 e 100.")
            return False
        self.preco = round(self.preco * (1 - percentual / 100), 2)
        print(f"Desconto de {percentual}% aplicado! Novo preço: {formatar_reais(self.preco)}")
        return True

    def vender(self, quantidade):
        if quantidade <= 0:
            print("Quantidade inválida!")
            return False
        if quantidade > self.estoque:
            print(f"Estoque insuficiente! Disponível: {self.estoque}")
            return False
        self.estoque -= quantidade
        total = quantidade * self.preco
        print(f"Vendido {quantidade} x {self.nome} ({formatar_reais(total)}). "
              f"Estoque restante: {self.estoque}")
        return True

    def repor_estoque(self, quantidade):
        if quantidade <= 0:
            print("Quantidade inválida!")
            return False
        self.estoque += quantidade
        print(f"Estoque reposto! Novo estoque: {self.estoque}")
        return True


class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar(self, produto):
        self.produtos.append(produto)

    def listar(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.")
        for i, produto in enumerate(self.produtos, 1):
            print(f"{i}. {produto}")

    def buscar_por_categoria(self, categoria):
        categoria = categoria.strip().lower()
        return [p for p in self.produtos if p.categoria == categoria]

    def valor_total(self):
        return sum(p.valor_total() for p in self.produtos)

    def sem_estoque(self):
        return [p for p in self.produtos if p.estoque == 0]


def ler_numero(mensagem, tipo=float):
    try:
        return tipo(input(mensagem).replace(",", "."))
    except ValueError:
        print("Valor inválido.")
        return None


def escolher_produto(estoque):
    estoque.listar()
    indice = ler_numero("Número do produto: ", int)
    if indice is None or not 1 <= indice <= len(estoque.produtos):
        print("Produto não encontrado.")
        return None
    return estoque.produtos[indice - 1]


def main():
    estoque = Estoque()
    estoque.adicionar(Produto("Kopke Colheita Porto", "bebidas", 9458.00, 300))
    estoque.adicionar(Produto("Nescafé", "bebidas", 15, 20))

    while True:
        print("\n--- CONTROLE DE ESTOQUE ---")
        print("1. Listar        2. Cadastrar     3. Detalhes")
        print("4. Vender        5. Repor         6. Desconto")
        print("7. Por categoria 8. Valor total   0. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            estoque.listar()
        elif opcao == "2":
            nome = input("Nome: ")
            categoria = input("Categoria: ")
            preco = ler_numero("Preço (ex: 15,90): ")
            qtd = ler_numero("Estoque inicial: ", int)
            if preco is None or qtd is None:
                continue
            try:
                estoque.adicionar(Produto(nome, categoria, preco, qtd))
                print("Produto cadastrado!")
            except ValueError as erro:
                print(erro)
        elif opcao in ("3", "4", "5", "6"):
            produto = escolher_produto(estoque)
            if not produto:
                continue
            if opcao == "3":
                produto.exibir()
            elif opcao == "4":
                qtd = ler_numero("Quantidade: ", int)
                if qtd is not None:
                    produto.vender(qtd)
            elif opcao == "5":
                qtd = ler_numero("Quantidade: ", int)
                if qtd is not None:
                    produto.repor_estoque(qtd)
            else:
                pct = ler_numero("Desconto (%): ")
                if pct is not None:
                    produto.aplicar_desconto(pct)
        elif opcao == "7":
            for produto in estoque.buscar_por_categoria(input("Categoria: ")):
                print(produto)
        elif opcao == "8":
            print(f"Valor total em estoque: {formatar_reais(estoque.valor_total())}")
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()