# Importante: Leer el apunte (https://pensamientocomputacional.dev.ar/unidad_6.html). Los ejercicios son sencillos pero van a servir para la siguiente parte

"""
5. Escribir una función que reciba:
- Una lista y devuelva True si su longitud es par y False si su longitud es impar.
- Una lista de números cualesquiera y devuelva el elemento máximo y el mínimo.
- Una lista de números y devuelva otra lista con los mismos números ordenados de menor a mayor. Por ejemplo, si recibe [5, 10, 7, 3] debe devolver [3, 5, 7, 10].
"""

# Acordarse de importar la biblioteca numpy
import numpy as np

def es_par(numeros):
    return np.size(numeros) % 2 == 0

def maximo_minimo(numeros):
    return np.max(numeros), np.min(numeros)

def ordenar(numeros):
    return np.sort(numeros)

"""6. Escribir una función que reciba dos vectores y devuelva su prod_escalar. Si los vectores no tienen las mismas dimensiones, la función debe devolver None."""

def prod_escalar(v1, v2):
    if np.size(v1) != np.size(v2):
        return None
    return np.dot(v1, v2)

"""7. Escribir una función que reciba una matriz y una tupla (fila, columna), y devuelva el valor ubicado en esa posición de la matriz. Ejemplo: si se recibe la matriz [[1, 2], [3, 4]] y la tupla (0, 1), debe devolver 2."""

## Pensar que los parametros van a estar definidos:
# matriz = np.array([[1, 2], [3, 4]])
# posicion = (0, 1)

def obtener_valor(matriz, posicion):
    return matriz[posicion[0], posicion[1]]

# Pensar si se puede aplicar manejo de errores!

"""8. Desafio (obligatorio): Escribir una función que reciba un tamaño y devuelva una matriz con 1 en la diagonal principal y 0 en el resto. Ejemplo: si recibe 4, debe devolver la matriz identidad de tamaño 4x4."""

def matriz_identidad(dimension):
    return np.eye(dimension)

"""9. Desafio (obligatorio): Escribir una función que reciba una matriz y devuelva su transpuesta. Ejemplo: si recibe la matriz [[1, 2, 3], [4, 5, 6]], debe devolver [[1, 4], [2, 5], [3, 6]]."""

def transponer_matriz(matriz):
    return np.transpose(matriz)