# Idade BPM
# Ate 2 anos > 120 a 140
# De 8 anos ate 17 anos > 80 a 100
# De 18 anos ate 59 anos > 70 a 80
# Acima de 60 anos > 50 a 60

bpm = int(input("Insira o batimento cardiaco")) # Coletando batimentos
idade = int(input("Insira sua idade")) # Coletando idade

# Checando idade menor ou igual a 2 anos
if idade <= 2:
    if bpm >= 120:
        if bpm <=140:
            print("Batimentos considerados normais")
        else:
            print("Batimentos considerados maiores que o normal")
    else:
        print("Batimentos considerados menores que o normal")

    # Checando idade de 8 a 17 anos

elif idade >= 8:
    if idade <= 17:

        # Checando batimentos de 80 a 100

        if bpm >= 80:
            if bpm <= 100:
                print("Batimentos considerados normais")
            else:
                print("Batimentos considerados maiores que o normal")
        else:
            print("Batimentos considerados menores que a média")

    # Idade de 18 a 50 anos

    if idade >= 18:
        if idade <= 59:

            # Checando batimentos de 70 a 80

            if bpm >= 70:
                if bpm <= 80:
                    print("Batimentos considerados normais")
                else:
                    print("Batimentos considerados maiores que o normal")
            else:
                print("Batimentos considerados menores que o normal")

        # Considerando o paciente idoso já que ele não tem idade menor a 50 anos

        else:
            bpm >= 60
            if bpm >= 60:
                if bpm <= 80:
                    print("Batimentos considerados normais")
                else:
                    print("Batimentos considerados maiores que o normal")
            else:
                print("Batimentos considerados menores que o normal")

# Explicando que o script só consegue ler de 0 a 60 anos de idade

else: print("Idade fora do script de análise")