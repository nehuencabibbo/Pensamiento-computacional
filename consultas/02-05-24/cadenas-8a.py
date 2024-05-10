def encontrar_todas_las_ocurrencias(texto, palabra):
    resultado = []
    inicio = 0
    indice = texto.find(palabra, inicio)
    while indice != -1:
        resultado.append(indice)
        inicio = indice + 1
        indice = texto.find(palabra, inicio)

    return resultado


print(encontrar_todas_las_ocurrencias('calcule el precio al valor actual', 'al'))