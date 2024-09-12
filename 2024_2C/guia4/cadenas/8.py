def buscador(palabra, texto):
    apariciones = []

    posicion = texto.find(palabra)
    while posicion != -1:
        apariciones.append(posicion)
        posicion = texto.find(palabra, posicion + 1)

    return apariciones

texto = 'calcule el precio al valor actual'
palabra = 'al'

print(buscador(palabra, texto))