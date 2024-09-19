# ["Ciclo", "Basico", "Comun"]

def separar(palabra):
    lista = palabra.split(" ")

    resultado = "" 
    for palabra in lista: 
        resultado += palabra[0]

    return resultado

# palabra = "Ciclo Basico Comun"
# palabra_separada = separar(palabra)
# print(palabra_separada)

def es_palindromo(palabra):
    lista_de_palabras = palabra.split(" ")
    palabra_sin_espacios = "".join(lista_de_palabras)

    palindromo = palabra_sin_espacios == palabra_sin_espacios[::-1]
    if palindromo:
        print("Es palindromo")

    return palindromo

palabra = "ab"
print(es_palindromo(palabra))