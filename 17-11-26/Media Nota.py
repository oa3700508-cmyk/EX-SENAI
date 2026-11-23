
soma = 0

for i in range(1, 5):
    nota = float(input(f"Digite a {i}ª nota: "))
    soma = soma + nota

media = soma / 4

print("A média do aluno é:", media)

if media >= 7:
    print("Aluno aprovado!")
elif media >= 5:
    print("Recuperação!")
else:
    print("Aluno reprovado!")   