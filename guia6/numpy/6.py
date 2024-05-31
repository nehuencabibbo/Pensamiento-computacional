# Escribir una función que reciba dos vectores y devuelva su producto escalar.
# El producto escalar se calcula como: Siendo y , entonces
# Si los vectores no tienen las mismas dimensiones, la función debe devolver None.

import numpy as np

def producto_escalar(un_array, otro_array):
    if un_array.size != otro_array.size:
        return None
    
    array_de_productos = np.multiply(un_array, otro_array)

    return np.sum(array_de_productos)

def producto_escalar(un_array, otro_array):
    if un_array.size != otro_array.size:
        return None
    
    return np.dot(un_array, otro_array)

a = np.array([3, 3, 3, 3, 3, 3])

print(producto_escalar(a, a))
