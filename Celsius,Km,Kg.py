def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

def km_para_milhas(km):
    milhas = km * 0.621371
    return milhas

def kg_para_libras(kg):
    libras = kg * 2.20462
    return libras


while True:
    print("Escolha a conversão:")
    print("1. Celsius para Fahrenheit")
    print("2. Quilômetros para Milhas")
    print("3. Quilogramas para Libras")
    print("0. Sair")
    
    escolha = input("Digite o número da opção desejada: ")
    
    if escolha == "0":
        break
    elif escolha == "1":
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = celsius_para_fahrenheit(celsius)
        print(f"{celsius}°C é igual a {fahrenheit}°F")
    elif escolha == "2":
        km = float(input("Digite a distância em quilômetros: "))
        milhas = km_para_milhas(km)
        print(f"{km} km é igual a {milhas} milhas")
    elif escolha == "3":
        kg = float(input("Digite o peso em quilogramas: "))
        libras = kg_para_libras(kg)
        print(f"{kg} kg é igual a {libras} libras")
    else:
        print("Opção inválida!")