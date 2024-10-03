# Escribir una función que reciba una cantidad de iteraciones N.

# Se deberá simular una persona que tira un dado N veces, y se 
# deberá devolver un diccionario con la cantidad de apariciones de 
# cada valor en el dado. Nota: para simular una tirada, usar import 
# random y random.randint(1, 6).

# Repetir el punto anterior, si ahora en vez de tirar 1 dado, tira 2. 
# Se debe devolver un diccionario con la cantidad de apariciones de cada
# valor de la suma de ambos dados.

# Que es lo que quieren que devolvamos? 

# Si por ejemplo tiro 2 veces y en las tiradas me salieron un 6 y un 5, 
# deberia devolver {6: 1, 5: 1}. Si tire 2 veces y en ambas me salio un 6, 
# deberia devolver {6: 2}

# Paso a paso que es lo que deberiamos hacer?

# 1 - N veces deberia simular la tirada y guardar el resultado
# (Dejar que vean que pasa cuando no tienne definida la llave en el dict)

# A)
import random

def simular_tiradas(n):
    tiradas = {}
    for num_tirada in range(n):
        numero_obtenido = random.randint(1, 6) # Me da un numero "aleatorio" que este entre 1 inclusive y 6 inclusive
        # Si no esta la tirada en el diccionario, lo pongo en 1, caso contrario
        # ya esta definido algun valor para la tirada, entonces solo le sumo 1
        if not numero_obtenido in tiradas:
            tiradas[numero_obtenido] = 1
        else: 
            tiradas[numero_obtenido] += 1

        # one liner de lo anterior: 
        # tiradas[numero_obtenido] = tiradas.get(numero_obtenido, 0) + 1

    return tiradas 

# B)

# Me piden hacer algo muy similar al ejercicio anterior, solo que N veces voy a tener que 
# simular dos tiradas, y lo que me voy a tener que guardar es la aparicion de la suma 

# Si tire dos veces y me salieron 6 y 5 // 4 y 2 me deberia devolver: {11: 1, 6: 1}
# Si tire dos veces y me salieron 6 y 5 // 5 y 6 me deberia devolver: {11: 2}

import random

def simular_tiradas(n):
    tiradas = {}
    for num_tirada in range(n):
        primer_numero_obtenido = random.randint(1, 6) 
        segundo_numero_obtenido = random.randint(1, 6) 

        suma = primer_numero_obtenido + segundo_numero_obtenido

        # Si no esta la tirada en el diccionario, lo pongo en 1, caso contrario
        # ya esta definido algun valor para la tirada, entonces solo le sumo 1
        if not suma in tiradas:
            tiradas[suma] = 1
        else: 
            tiradas[suma] += 1

        # one liner de lo anterior: 
        # tiradas[numero_obtenido] = tiradas.get(numero_obtenido, 0) + 1

    return tiradas 