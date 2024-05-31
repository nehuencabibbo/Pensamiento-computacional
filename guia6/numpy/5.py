# Escribir una función que reciba:

# Una lista y devuelva True si su longitud es par y False si su longitud es impar.
# Una lista de números cualesquiera y devuelva el elemento máximo y el mínimo.
# Una lista de números y devuelva otra lista con los mismos números ordenados de menor a 
# mayor. Por ejemplo, si recibe [5, 10, 7, 3] debe devolver [3, 5, 7, 10].

def a(lista):
    return len(lista) % 2 == 0

def b(lista):
    return max(lista), min(lista)

def c(lista):
    return sorted(lista)

import numpy as np

def a_np(array):
    #shape me devuelve (filas, columnas) -> shape[0] es filas
    return array.shape[0] % 2 == 0

def b_np(array):
    return np.max(array), np.min(array)

def c_np(array):
    return np.sort(array)


lista = [65, 123, 1, 2, 5, 4, 3]

array = np.array(lista)

print(c_np(array))

