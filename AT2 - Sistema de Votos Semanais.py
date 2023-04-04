# sistema de votação

val1 = int(input("Digite o valor de votos da segunda-feira"))
val2 = int(input("Digite o valor de votos da terça-feira"))
val3 = int(input("Digite o valor de votos da quarta-feira"))
val4 = int(input("Digite o valor de votos da quinta-feira"))
val5 = int(input("Digite o valor de votos da sexta-feira"))

list = [val1, val2, val3, val4, val5]
dias_da_semana = ["Segunda-feira", "Terça-Feira", "quarta-feira", "Quinta-Feira", "Sexta-feira"]

# script

maior_valor_da_lista = 0
for valor in list:
    if valor > maior_valor_da_lista:
        maior_valor_da_lista = valor
        
posicao_do_maior_valor = list.index(maior_valor_da_lista)

# printando resultado

print(dias_da_semana[posicao_do_maior_valor])
