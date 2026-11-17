
numero = int(input("Digite um número: "))

if numero % 3 == 0:
    print("O número é múltiplo de 3")
else:
    print("O número não é múltiplo de 3")
for numero in range(1, 51):
    if numero % 3 == 0:
        print(numero)