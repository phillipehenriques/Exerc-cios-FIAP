#defininido texto de números impares

print("Por favor, digite as notas dos alunos impares em sequência: ")

#definindo valor das variáveis

alunos_impares = 0
alunos_pares = 0

# Criando Script dos números impares

for i in range (1, 50, 2):
    nota = float(input("Aluno de número {}: ".format(i)))
    alunos_impares += nota

# tirando média dos números impares

media_impar = alunos_impares / 25

print("**************************************")

# Criando Script dos números pares

for i in range (2, 51, 2):
    nota = float(input("Aluno de número {}: ".format(i)))
    alunos_pares += nota

# tirando média dos números pares

media_par = alunos_pares / 25

print("**************************************")

# printando o resultado da maior média entre os números

if media_impar > media_par:
    maior_media = media_impar
    print("Parabéns alunos ímpares! Vocês tiveram a maior média: {:.2f}!".format(media_impar))
elif media_impar < media_par:
    maior_media = media_par
    print("Parabéns alunos pares! Vocês tiveram a maior média: {:.2f}!".format(media_par))
else:
    print("Deu emparte .. As notas são iguais!")