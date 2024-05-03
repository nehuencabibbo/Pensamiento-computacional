# Escribir una función que reciba una cantidad de iteraciones N.

# a)
# Se deberá simular una persona que tira un dado N veces, y se deberá devolver 
# un diccionario con la cantidad de apariciones de cada valor en el dado. 
# Nota: para simular una tirada, usar import random y random.randint(1, 6).

#b)
# Repetir el punto anterior, si ahora en vez de tirar 1 dado, tira 2. Se debe
# devolver un diccionario con la cantidad de apariciones de cada valor de la 
# suma de ambos dados.

from random import randint

def simular_tiro_de_dado(cantidad_de_tiros):
    tiradas = {}
    for _ in range(cantidad_de_tiros):
        tirada = randint(1, 6)

#Tengo que checkear si esta o no la clave en el diccionario, si intento acceder a una clave que no 
#existe, me va a tirar un error

def simular_tiro_de_dado(cantidad_de_tiros):
    tiradas = {}
    for _ in range(cantidad_de_tiros):
        tirada = str(randint(1, 6))

        if tirada in tiradas: #Si ya esta la clave, agrego 1
            tiradas[tirada] += 1
        else: #Si no esta la clave, la defino en 1
            tiradas[tirada] = 1

    return tiradas

# {}

# -> tiro 1, esta? no, lo agergo

# {"1": 1}

# tiro 1, esta? si, le sumo uno al valor

# {"1": 2}

# ...

#B) 
def simular_tiro_de_dos_dados(cantidad_de_tiros):
    tiradas = {}
    for _ in range(cantidad_de_tiros):
        tirada1 = randint(1, 6)
        tirada2 = randint(1, 6)

        tirada = str(tirada1 + tirada2)

        if tirada in tiradas: #Si ya esta la clave, agrego 1
            tiradas[tirada] += 1
        else: #Si no esta la clave, la defino en 1
            tiradas[tirada] = 1

    return tiradas


print(simular_tiro_de_dado(6))

