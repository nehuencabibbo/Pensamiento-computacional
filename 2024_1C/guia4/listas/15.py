# Desafio (obligatorio): Escribir una función que reciba un tamaño y devuelva una matriz con 1 en la diagonal principal y 0 en el resto. Ejemplo: si recibe 4, debe devolver la matriz identidad de tamaño 4x4. 


# 1 - cantidad_de_filas veces: 
# 2 - Crear una fila 
# 3 - llenar la fila segun corresponde
# 4 - agregarla a la matriz

# llenarla segun corresponde: 
# 1 - cantidad_de_columnas veces:
# 2 - si el numero_de_columna (posicion en la fila) coincide con el numero de fila poner 1, sino 0

# Como se representan las matrices? En el apunte vieron que se usan listas anidadas, es decir, listas de listas. Si yo tengo, por ejemplo: [[1, 0], [0, 1]] esto representa la matriz identidad de 2x2, porque cada lista anidada representa una fila y cada fila tiene tantos elementos como columnas haya

# Voy a tener n filas, por lo tanto voy a tener que agregar n listas anidadas
def identidad(n):
    matriz = []
    for numero_de_fila in range(0, n):
        fila = []

#Cada fila tiene n elementos (cantidad de columnas que tengo), los voy a tener que agregar 
def identidad(n):
    matriz = []
    for numero_de_fila in range(0, n):
        fila = []
        for numero_de_columna in range(0, n):
            pass

#Cada fila va a tener una particularidad, como la diagonal va a estar llena de 1s y el resto de 0, eso quiere decir que cada posicion en la que numero_de_fila = numero_de_columna de la matriz va a tener un 1, y en otro caso 0
def identidad(n):
    matriz = []
    for numero_de_fila in range(0, n):
        fila = []
        for numero_de_columna in range(0, n):
            if (numero_de_fila == numero_de_columna):
                fila.append(1)
            else:
                fila.append(0)
        
#Por ultimo, una vez que ya tengo la fila completa, tengo que agregarla a la matriz, y por ultimo devolver la matriz
def identidad(n):
    matriz = []
    for numero_de_fila in range(0, n):
        fila = []
        for numero_de_columna in range(0, n):
            if (numero_de_fila == numero_de_columna):
                fila.append(1)
            else:
                fila.append(0)

        matriz.append(fila)
    
    return matriz

#Extra: 
def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

imprimir_matriz(identidad(6))

