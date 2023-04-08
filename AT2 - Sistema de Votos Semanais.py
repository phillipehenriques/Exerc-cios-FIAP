# sistema de votação

v_segunda = int(input("Digite o valor de votos da segunda-feira: "))
v_terça = int(input("Digite o valor de votos da terça-feira: "))
v_quarta = int(input("Digite o valor de votos da quarta-feira: "))
v_quinta = int(input("Digite o valor de votos da quinta-feira: "))
v_sexta = int(input("Digite o valor de votos da sexta-feira: "))

# definindo variáveis 

maioria = v_segunda
escolhido = "A maioria dos votos são para Segunda-feira"

# script

if v_terça > maioria:
    escolhido = "A maioria dos votos são para Terça-feira"
    maioria = v_terça

if v_quarta > maioria:
    escolhido = "A maioria dos votos são para Quarta-feira"
    maioria = v_quarta

if v_quinta > maioria:
    escolhido = "A maioria dos votos são para Quinta-feira"
    maioria = v_quinta

if v_sexta > maioria:
    escolhido = "A maioria dos votos são para Sexta-feira"
    maioria = v_sexta

else:
    print("O dia escolhido foi {}, com {} votos!".format(escolhido, maioria))
