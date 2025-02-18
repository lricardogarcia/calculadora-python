def calcular():
    primeira_execucao = True
    while True:
        if not primeira_execucao:
            sair = input("Deseja sair? (s/n): ").strip().lower()
            if sair == 's':
                print("Saindo... Obrigado por usar a calculadora!")
                break
        primeira_execucao = False

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Por favor, insira valores numéricos válidos.")
            continue

        print("\nEscolha a operação:")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")

        opcao = input("Digite o número da operação desejada: ")

        if opcao == "1":
            print(f"Resultado: {num1} + {num2} = {num1 + num2}\n")
        elif opcao == "2":
            print(f"Resultado: {num1} - {num2} = {num1 - num2}\n")
        elif opcao == "3":
            print(f"Resultado: {num1} * {num2} = {num1 * num2}\n")
        elif opcao == "4":
            if num2 == 0:
                print("Erro: divisão por zero não é permitida.\n")
            else:
                print(f"Resultado: {num1} / {num2} = {num1 / num2}\n")
        elif opcao == "5":
            print("Saindo... Obrigado por usar a calculadora!")
            break
        else:
            print("Opção inválida! Escolha uma opção entre 1 e 5.\n")


if __name__ == "__main__":
    calcular()
