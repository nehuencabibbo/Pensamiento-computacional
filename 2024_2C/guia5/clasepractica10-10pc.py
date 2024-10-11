# 1. Archivos

### Ejercicio 1 : Escribir una función llamada **contar (o count)** que dado un archivo retorne la cantidad de filas que tiene.

def contar(path_archivo):
  archivo = open(path_archivo,'r')
  contador_lineas = 0

  lineas = archivo.readlines()

  for linea in archivo:
    contador_lineas += 1

  archivo.close()
  return contador_lineas

path = "sample_data/california_housing_train.csv"
print(contar(path))

#--------------------------------------------------------------------
### Ejercicio 4 : Escribir una función llamada **ver_final (o tail)** que dado un archivo y un número N retorne en una lista las últimas N lineas del archivo."""

def ver_final(path_archivo, N):
  archivo = open(path_archivo, 'r')
  lista_n_lineas = []
  contador_lineas = 0
  cantidad_lineas = contar(path_archivo)
  lineas_no_importantes = cantidad_lineas - N

  for linea in archivo:
    if contador_lineas >= lineas_no_importantes:
      lista_n_lineas.append(linea)
    contador_lineas += 1

  archivo.close()
  return lista_n_lineas

path = "sample_data/california_housing_train.csv"
ver_final(path, 1)
#----------------------------------------------------------
### Ejercicio 7 : Escribir una función, llamada grep, que reciba una cadena y un archivo de texto, e imprima las líneas del archivo que contienen la cadena recibida."""

def grep(cadena, path):
  with open(path,'r') as archivo:
    for linea in archivo:
      if cadena.lower() in linea.lower():
        print(linea)

path = "archivo2.txt"
grep("harry", path)
