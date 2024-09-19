# Una matriz se representa como una lista de listas, donde cada lista interna
# representa una fila

# [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# Se puede ver mejor asi: 

# [
#   [1, 0, 0], 
#   [0, 1, 0], 
#   [0, 0, 1]
# ]

# cada columna se corresponde con cada posicion dentro del array
# la posicion 0 es la columna 1, la posicion 1 es la columna 2, etc

# Yo se como crearme cada fila, si num_fila == num_col tengo que poner un 1, 
# caso contrario tengo que poner un 0

# 1 - num_filas veces tengo que: 
# 1.1 - crear una fila (lista)
# 1.2 - llenarla como corresponde (explicar pasaje por referencia)
# 1.3 - agregarla a mi matriz 
def crear_identidad(n):
    matriz = []

    columnas = n
    filas = n
    # Yo tengo que crearme n filas 
    for i in range(filas):
        fila = []
        # Tengo que llenar la fila de alguna manera 
        for j in range(columnas):
            if j == i:
                fila.append(1)
            else:
                fila.append(0)

        matriz.append(fila)

    return matriz
        

matriz = crear_identidad(3)
for fila in matriz:
    print(fila)