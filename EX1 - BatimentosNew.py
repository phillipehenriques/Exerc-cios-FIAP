# Idade BPM
# Ate 2 anos > 120 a 140
# De 8 anos ate 17 anos > 80 a 100
# De 18 anos ate 59 anos > 70 a 80
# Acima de 60 anos > 50 a 60

bpm = int(input("Insira o batimento cardiaco")) # Coletando batimentos
idade = int(input("Insira sua idade")) # Coletando idade

# ChTeste lógico:

if idade <= 2:
    if bpm >= 120 and bpm <= 140:
        print("Frequencia dentro da média")
    else:
        print("Frequencia cardíaca fora da média")
elif idade >= 8 and idade <= 17:
    if bpm >= 80 and bpm <= 100:
        print("Frequencia dentro da média")
    else:
        print("Frequencia cardíaca fora da média")
elif idade >= 18 and idade <= 59:
    if bpm >= 70 and bpm <= 80:
        print("Frequencia dentro da média")
    else:
        print("Frequencia cardíaca fora da média")
elif idade >= 60:
    if bpm >= 70 and bpm <= 80:
        print("Frequencia dentro da média")
    else:
        print("Frequencia cardíaca fora da média")
