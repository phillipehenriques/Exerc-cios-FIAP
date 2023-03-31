
# Atribuindo a resposta do usuário à variável 'tipoAssinatura"

tipoAssinatura = int(input("Tabela de Assinaturas: \n 1 - Basic \n 2 - Silver \n 3 - Gold \n 4 - Platinum \n Informe por favor, qual é a sua assinatura: 2")) 

# Atribuindo a resposta do usuário á variável 'valorFaturamento'

valorFaturamento = float(input("Informe por favor, o seu faturamento anual em reais: "))

# Criando Script para processamento dos valores digitados, e efetuando o calculo com base no percentual correto da assinatura

if tipoAssinatura == 1:
    desconto = valorFaturamento * 0.3
    print("O valor que você precisa pagar é de R${:.2f}".format(desconto))
elif tipoAssinatura == 2:
    desconto = valorFaturamento * 0.2
    print("O valor que você precisa pagar é de R${:.2f}".format(desconto))
elif tipoAssinatura == 3:
    desconto = valorFaturamento * 0.1
    print("O valor que você precisa pagar é de R${:.2f}".format(desconto))
elif tipoAssinatura == 4:
    desconto = valorFaturamento * 0.05
    print("O valor que você precisa pagar é de R${:.2f}".format(desconto))
else:
    print("Desculpe, faltam irformações para processamento")

# fim (:2