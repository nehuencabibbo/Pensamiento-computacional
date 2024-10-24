"""
### **Ejercicio** 11 :

La señora Rowling sospecha que su vecino le robo algunos manuscritos y los publicó como propios con algunas modificaciones. Se desea procesar una lista de archivos y guardar en un archivo llamado reporte_plagio.txt la siguiente información:

archivo;palabras;apariciones
archivo1.txt;765030;547

* archivo: es el nombre del archivo que se proceso.
* palabras: es la cantidad de palabras de ese archivo.
* apariciones: es la cantidad de veces que aparece una palabra especificada.

En procesar_archivos se tiene que analizar los archivos y dejar el resultado en reporte_plagio.txt
"""

# 1. Itero cada archivo
  # 1.1 Leo el archivo
  # 1.2 Obtengo las lineas
  # 1.3 Divido las lineas en palabras para poder contar el total de palabras y si se repite la palabra especifica
#2. Creo y escribo el reporte_plagio.txt

def procesar_archivos(archivos, palabra):
    reporte = []
    apariciones_palabra = 0
    cantidad_palabras = 0

    for archivo in archivos:
        with open(archivo, 'r') as archivo:
            lineas = archivo.read()
        palabras = lineas.split()
        cantidad_palabras = len(palabras)
        for linea in palabras:
            if linea == palabra:
                apariciones_palabra = apariciones_palabra + 1

        reporte.append(f"{archivo};{cantidad_palabras};{apariciones_palabra}")

    with open('reporte_plagio.txt', 'w') as archivo_reporte:
      archivo_reporte.write('archivo;palabras;apariciones\n')  # No olvidarse del encabezado
      archivo_reporte.writelines(reporte)


# Mencionamos en clase que tambien se podia escribir el archivo en forma append:

def procesar_archivos_con_append(archivos, palabra):
    with open('reporte_plagio.txt', 'a') as archivo_reporte:
        archivo_reporte.write(f'archivo;palabras;apariciones\n')

        for archivo in archivos:
          with open(archivo, 'r') as archivo:
              lineas = archivo.read()
          palabras = lineas.split()
          cantidad_palabras = len(palabras)
          for linea in palabras:
              if linea == palabra:
                  apariciones_palabra = apariciones_palabra + 1

          # Escribo los datos obtenidos directamente en el archivo de reporte
          archivo_reporte.write(f"{archivo};{cantidad_palabras};{apariciones_palabra}\n")


"""Manejo de errores**
Ej 6. Desafio: Para la venta de entradas de un teatro se cuenta con un diccionario que contiene las filas: “A”, “B”, “C”… y en cada fila contiene una lista con las ubicaciones disponibles en forma de lista ["L","O","O","O","L","L","L"] donde “L” es libre y “O” es ocupada.

Escribir una funcion que reciba el diccionario, la fila y la ubicación en ella, y reserve el asiento en caso de que este libre. Considerar que el tamaño de la lista de ubicaciones puede variar por fila. Si la fila o la ubicación no son correctas, mostrar un mensaje descriptivo. Si el asiento ya se encuentra ocupado, mostrar el mensaje: El asiento ya se encuentra ocupado.
"""

def reservar_butaca(sala, fila, ubicacion):
    try:
        if sala[fila][ubicacion] == "O":
              print(f"El asiento en la fila {fila}, ubicación {ubicacion}, ya está ocupado.")
        else:
            sala[fila][ubicacion] = "O"
            print(f"Se ha reservado el asiento en la fila {fila}, ubicación {ubicacion}.")
    except KeyError:
        print(f"La fila '{fila}' no existe en la sala.")
    except IndexError:
        print(f"La ubicación '{ubicacion}' no existe en la fila '{fila}'.")