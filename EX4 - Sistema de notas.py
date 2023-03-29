notas = []

opcao = -1
while opcao !=4:
    print("- Digite 1 para informar notas \n - Digite 2 para exibir notas \n Digite 3 para calcular a média \n - Digite 4 para sair")
    opcao = int(input("Escolha sua opção: "))

    if opcao ==1:
        notas.append(float(input("Digite a nota!")))
    elif opcao ==2:
        for x in notas:
            print(x)
    elif opcao ==3:
        print(sum(notas) / len(notas))