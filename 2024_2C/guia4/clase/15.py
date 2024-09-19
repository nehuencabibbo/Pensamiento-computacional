identidad = [
    [1, 0, 0], 
    [0, 1, 0], 
    [0, 0, 1]
]

# 1 - n (cant_filas) veces crearme una fila 
# 2 - n (cant_columnas) tendria que agregar
# un elemento 
# 3 - Si el num_fila == num_columna pongo 1, 
# caso contrario pongo un 0

def identidad(n):
    matriz = []

    filas = n 
    columnas = n
    for num_fila in range(filas):
        fila = []
        for num_columna in range(columnas):
            if num_fila == num_columna:
                fila.append(1)
            else:
                fila.append(0)

        matriz.append(fila)

    return matriz 

tres_por_tres = identidad(3)
for fila in tres_por_tres:
    print(fila)