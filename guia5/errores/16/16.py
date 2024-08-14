# Se tiene una lista de archivos y se quiere imprimir las primeras 5 líneas de cada uno.
# Si el archivo no existe, se lo debe crear e imprimir el mensaje: ‘el archivo {nombre} no existe. 
# Se crea y deja vacío.

def listar(archivos):
    print()
    for archivo in archivos:
        print("\n")
        try:
            with open(archivo, 'r') as a:
                # Mas eficiente
                # linea = a.readline()
                # for _ in range(5):
                #     if linea == "":
                #         break

                #     print(linea.strip("\n"))
                #     linea = a.readline()
                for linea in a.readlines():
                    print(linea.strip('\n'))

        except FileNotFoundError as e:
            print(f"el archivo {archivo} no existe")
            open(archivo, 'w').close()


archivos = ["archivo1.txt", "archivo2.txt", "archivo3.txt"]
listar(archivos)