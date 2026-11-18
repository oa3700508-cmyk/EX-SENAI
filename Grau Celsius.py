while True:
    print("\n=== MENU ===" \
          "\n1 - Celsius para Fahrenheit" \
          "\n0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = (celsius * 1.8) + 32
        print(f"{celsius}°C é igual a {fahrenheit:.2f}°F")






    elif opcao == "0":
        print("Saindo do programa...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")   