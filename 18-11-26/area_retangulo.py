"""Exercício 1: área do retângulo."""


def calcular_area_retangulo(base, altura):
    """Calcula a área de um retângulo.

    Fórmula: área = base * altura

    Args:
        base (float): medida da base do retângulo.
        altura (float): medida da altura do retângulo.

    Returns:
        float: área do retângulo.
    """
    return base * altura


def main():
    """Pede base e altura ao usuário e mostra a área."""
    base = float(input("Digite a base: ").replace(",", "."))
    altura = float(input("Digite a altura: ").replace(",", "."))
    print(f"Área do retângulo: {calcular_area_retangulo(base, altura)}")


if __name__ == "__main__":
    main()
