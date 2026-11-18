"""Exercício 2: maior de três números, sem usar max()."""


def maior_de_tres(a, b, c):
    """Retorna o maior entre três números, sem usar a função max().

    Args:
        a (float): primeiro número.
        b (float): segundo número.
        c (float): terceiro número.

    Returns:
        float: o maior dos três números.
    """
    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    return maior


def main():
    """Pede três números ao usuário e mostra o maior."""
    a = float(input("Digite o primeiro número: ").replace(",", "."))
    b = float(input("Digite o segundo número: ").replace(",", "."))
    c = float(input("Digite o terceiro número: ").replace(",", "."))
    print(f"O maior número é: {maior_de_tres(a, b, c)}")


if __name__ == "__main__":
    main()
