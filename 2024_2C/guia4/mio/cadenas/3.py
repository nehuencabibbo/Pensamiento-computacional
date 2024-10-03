# Si tuviera una lista con cada palabra seria mas facil el problema, no?
# porque si tengo ["Ciclo", "Basico", "Comun"] entonces obtener cada inicial
# es simplemente recorrer la lista y quedarme con el primer elemento para cada 
# palabra

# Esto se puede hacer a mano, recorro la cadena y cada vez que me encuentro un
# espacio en blanco, todo lo que recorri me lo guardo en una lista 

def obtener_inicial(palabra):
    return palabra[0]

def iniciales(palabra):
    lista_de_palabras = palabra.split(" ")
    print(lista_de_palabras)

    lista_de_palabras = list(map(obtener_inicial, lista_de_palabras))

    return "".join(lista_de_palabras)

palabra = "Ciclo Basico Comun  "
print(iniciales(palabra))