# La profesora Llamell guarda las notas del parcial de Pensamiento Computacional en una 
# lista de diccionarios. Cada diccionario tiene la siguiente información: nombre, apellido, 
# intento, nota.

# Los intentos pueden ser 1 (si es la primera vez que rinde el parcial) o 2 
# (si está en el recuperatorio).

# Se pide hacer una función que dada esta lista de diccionarios, se devuelva el 
# promedio de las notas en la primera oportunidad de los alumnos. 

# Generalizar la función anterior, para que también reciba el número de intento y se 
# pueda devolver el promedio de cualquiera de los dos intentos.

ejemplo_notas = [
    {"nombre": "Violeta", "apellido": "Perez", "intento": 2, "nota": 2}, 
    {"nombre": "Manuela", "apellido": "Gomez", "intento": 1, "nota": 6}, 
    {"nombre": "Carla", "apellido": "Guanca", "intento": 1, "nota": 8}
]

# Hay varias opciones para hacerlo, al final del dia quiero devolver:
# suma_total_notas_primer_intento/ cantidad_notas_primer_intento

# Puedo: 
# 1 - Quedarme solo con las notas del primer intento
# 2 - Calcular el promedio de las notas 

# Puedo: 
# 1 - Para cada nota: 
# 1.1 - Ver si es del primer intento, en ese caso, sumo a al 
# total actual de notas del primer intento 
# y a la cantidad total de notas del primer intento

# A) 
# Forma 1 
def calcular_promedio(notas): 
    suma = 0
    total = 0
    for datos_nota in notas: 
        intento = datos_nota["intento"]
        nota = datos_nota["nota"]

        if intento == 1: 
            suma += nota
            total += 1

    return suma/total

# Forma 2 
def primer_intento(nota):
    return nota["intento"] == 1 

def calcular_promedio(notas): 
    notas_del_primer_intento = list(filter(primer_intento, notas))
    suma = 0
    for datos_nota in notas_del_primer_intento: 
        nota = datos_nota["nota"]

        suma += nota

    return suma/len(notas)

# B) 
# El filter habria que hacerlo a mano o pasar una lambda que tome del entorno el intento
# list(filter(lambda datos_nota: datos_nota["nota"] == intento, notas))
def calcular_promedio(notas, intento): 
    suma = 0
    total = 0
    for datos_nota in notas: 
        intento_act = datos_nota["intento"]
        nota = datos_nota["nota"]

        if intento_act == intento: 
            suma += nota
            total += 1

    return suma/total
