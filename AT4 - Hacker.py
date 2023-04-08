# Importando

from datetime import datetime

#estruturando a variável e a lógica

def fatorial(minutos_agora):
    
    fat = 1
    i = 2
    while i <= minutos_agora:
        fat = fat * i
        i = i + 1

    return fat

# atribuindo 'minute' á variável 'minutos agora'

minutos_agora = datetime.now().minute

# Mostrando resultado na tela

print(f"LIBERDADE{fatorial(minutos_agora)}")
