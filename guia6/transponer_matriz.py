def transponer(matriz):
    filas = len(matriz[0])
    columnas = len(matriz)

    resultado = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(matriz[j][i])

        resultado.append(fila)

    return resultado

ex = [[1, 2], [3, 4], [5, 6]]
print(f"Transpuesta a mano: {transponer(ex)}")

import numpy as np

print(f"Transpuesta con numpy: {np.transpose(ex)}")


