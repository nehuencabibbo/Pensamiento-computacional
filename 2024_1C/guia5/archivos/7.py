# Escribir una función, llamada grep, que reciba una cadena y un archivo de texto, 
# e imprima las líneas del archivo que contienen la cadena recibida.

#Queremos leer todas las lineas del archivo que nos pasan, si la linea que
#leemos tiene la cadena que nos indicaron, tendriamos que imprimirla
def grep(cadena, archivo):
    with open(archivo, 'r') as archivo:
        #readlines() retorna una LISTA con las lineas del
        #archivo, una vez que leimos el archivo, estamos 
        #en un problema de listas
        lineas = archivo.readlines()

    for linea in lineas:
        if cadena in linea:
            print(linea.strip('\n'))

archivo = "7.py"
cadena = "Escribir una funci"

grep(cadena, archivo)

