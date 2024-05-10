

# Escribir una función que reciba una tupla, un índice, y un nuevo valor. La función debe modificar la tupla, cambiando el valor en la posición dada por el índice, por el nuevo valor pasado como parámetro. Devolver la tupla modificada.

# Repetir el ejercicio anterior, pero con una lista.

# Repetir ambos si ahora, en vez de recibir un índice, se recibe el valor a eliminar. Si no se contiene al valor, se devuelve la estructura tal cual se recibió.

def ej_siete(tupla, indice, valor):
    #(4, 5) -> indice = 1, valor = 2

    #(4, 2)
    resultado = []
    for i in range(len(tupla)):
        if i == indice:
            resultado.append(valor)
        else:
            resultado.append(tupla[i])

    return tuple(resultado)

print(ej_siete((4, 5), 1, 2))
