# Se quiere crear una lista de supermercado, solicitándole al usuario productos hasta que ingrese el valor ‘X’. La función debe devolver los productos en un string, separados por comas. Ejemplo: si se ingresa ‘pan’, ‘arroz’, ‘pescado’, ‘X’, debe devolver "pan, arroz, pescado".

# Vamos a escribirlo como en la guia 1,si tengo una conversacion con alguien, como haria? primero le pido un producto, me lo dice, y yo me fijo si es X, si no lo es lo agrego a la lista y vuelvo a preguntarle

# 1 - Solicitarle al usuario un producto
# 2 - Mientras el producto no sea X, agregar a la lista 
# y volver a 1
# 3 - Devolver la lista

#La implementacion es directa (Es muy parecido a los q di la otra vez):

def lista_de_supermercado(): 
    lista = []

    producto = input("Ingrese un producto o X para salir: ")
    while producto.upper() != "X":
        lista.append(producto)
        producto = input("Ingrese un producto o X para salir: ")


    return ",".join(lista)
        
print(lista_de_supermercado())
