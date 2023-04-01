
val1 = int(input("Digite o valor de votos da segunda-feira"))
val2 = int(input())
val3 = int(input())
val4 = int(input())
val5 = int(input())

list = [val1, val2, val3, val4, val5]
dias_da_semana = ["Segunda-feira", "Terça-Feira", "quarta-feira", "Quinta-Feira", "Sexta-feira"]

maior_valor_da_lista = 0
for valor in list:
    if valor > maior_valor_da_lista:
        maior_valor_da_lista = valor
        
posicao_do_maior_valor = list.index(maior_valor_da_lista)

print(dias_da_semana[posicao_do_maior_valor])
