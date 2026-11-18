"""Exercício 3: números primos entre 1 e 100."""


def eh_primo(n):
    """Verifica se um número inteiro é primo.

    Um número primo é maior que 1 e divisível apenas por 1 e por ele mesmo.
    Basta testar divisores até a raiz quadrada de n.

    Args:
        n (int): número inteiro a ser verificado.

    Returns:
        bool: True se n for primo, False caso contrário.
    """
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


def main():
    """Imprime todos os números primos entre 1 e 100."""
    print("Números primos entre 1 e 100:")
    for numero in range(1, 101):
        if eh_primo(numero):
            print(numero)


if __name__ == "__main__":
    main()
