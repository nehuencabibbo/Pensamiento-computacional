# 1 - Crear lista de supermercado
# 2 - Pedirle al usuario que ingrese un
# producto o una X
# 3 - Mientras el ingreso sea distinto de X:
# 3.1 - Me guardo el producto
# 3.2 - repetir 2 

def compras():
    lista_supermercado = []
    ingreso = input("Ingrese un producto o una X para salir: ")
    while ingreso.upper() != "X":
        lista_supermercado.append(ingreso)
        ingreso = input("Ingrese un producto o una X para salir: ")

    return ", ".join(lista_supermercado)


print(compras())