# Que tengo que hacer? 

# 1 - Para todos los archivos, tengo que abrirlos y procesarlos,
# de cada archivo necesito cierta informacion para luego escribirla
# 2 - Para cada archivo procesado, tengo que escribir en el archivo
# indicado la informacion que procese de ese archivo

# Procesar el archivo (necesito la cantidad total de palabras y
# las apariciones de la palabra buscada)
# 1 - Para cada linea del archivo:
# 1.1 - Obtener todas las palabas de la linea y guardarme el resultado
# 1.2 - Contar las veces que aparece la palabra en la linea y guardarme el resultado


#procesar un archivo quiero que me de la informacion relevante de ese archivo,
#asi me lo voy guardando y por ultimo lo escribo
def procesar_archivos(archivos, palabra_buscada):
    lineas_a_escribir = []
    for archivo in archivos:
        lineas_a_escribir.append(procesar_archivo(archivo, palabra_buscada))

    escribir_resultado(lineas_a_escribir)

#Como va a ser la funcion de procesar archivo? necesito que me devuelva un string 
#que sea "archivo;total_palabras;apariciones" para un determinado archivo. Entonces
#para cada linea del archivo voy a ver cuantas veces aparece mi palabra y guardarlo
# y a su vez voy a ver cuantas palabras hay en la linea y guardarlas
def procesar_archivo(nombre_archivo, palabra_buscada):
    apariciones = 0
    total = 0
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        
    for linea in lineas:
        #No es magia, en verdad hicieron esta funcion si darse cuenta, 
        #se acuerdan del ejercicio del find? Se puede hacer de varias
        #formas
        apariciones += linea.strip('\n').lower().count(palabra_buscada.lower())

        total += len(linea.split('\n'))

    return f"{nombre_archivo};{total};{apariciones}"

def procesar_archivos(archivos, palabra_buscada):
    lineas_a_escribir = []
    for archivo in archivos:
        lineas_a_escribir.append(procesar_archivo(archivo, palabra_buscada))

    escribir_resultado(lineas_a_escribir)

#Listo, y ahora la funcion para escribir resultado como seria? no olvidarse de 
#escribir el header

def escribir_resultado(lineas_a_escribir):
    #Si no existe lo crea, si existe borra todo y arranca
    #a escrbiri
    with open('reporte_plagio.txt', 'w') as archivo:
        #No olvidarse el header
        archivo.write('archivo;total;apariciones' + '\n')
        for linea in lineas_a_escribir:
            archivo.write(linea + '\n')

def procesar_archivo(nombre_archivo, palabra_buscada):
    apariciones = 0
    total = 0
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            #No es magia, en verdad hicieron esta funcion si darse cuenta, 
            #se acuerdan del ejercicio del find? Se puede hacer de varias
            #formas
            apariciones += linea.strip('\n').lower().count(palabra_buscada.lower())

            total += len(linea.split(' '))

    return f"{nombre_archivo};{total};{apariciones}"

def procesar_archivos(archivos, palabra_buscada):
    lineas_a_escribir = []
    for archivo in archivos:
        lineas_a_escribir.append(procesar_archivo(archivo, palabra_buscada))

    escribir_resultado(lineas_a_escribir)


archivos = ["archivo1.txt", "archivo2.txt"]
palabra = "harry"

procesar_archivos(archivos, palabra)