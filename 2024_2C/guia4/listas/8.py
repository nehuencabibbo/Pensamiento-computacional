# Hay un metodo util que es find, que nos devuelve el indice en el 
# que se encuentra una subcadena en otra, si no se encuentra presente
# devuelve -1 

def buscar(texto, palabra):
    posiciones = []
    aparicion = texto.find(palabra, 0)
    while aparicion != -1:
        print(f"Encontre la apricion: {aparicion}")
        posiciones.append(aparicion)
        aparicion = texto.find(palabra, aparicion + 1)

    return posiciones 

texto = 'calcule el precio al valor actual'
palabra = 'al'
print(buscar(texto, palabra))
