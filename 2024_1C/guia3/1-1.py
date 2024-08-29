#Escribir una función que, dado un número entero , calcule si es impar o no.

#Dejar que lo hagan, solucion con lo que saben:
def es_impar(numero):
    if numero % 2 == 0:
        return True
    else: 
        return False
    
#Abarca todos los casos, se puede sacar el else
def es_impar(numero):
    if numero % 2 == 0:
        return True
    
    return False

#Mas elegante

def es_impar(numero):
    return numero % 2 == 0

