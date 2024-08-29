def cadenas_1(cadena, caracter):
    for i in range(len(cadena)):
        if cadena[i].isdigit():
            cadena = cadena.replace(str(cadena[i]), caracter)

    return cadena

def cadenas_1(cadena, caracter):
    resultado = ""
    for letra in cadena:
        if letra.isdigit():
            resultado += caracter
        else:
            resultado += letra

    return resultado


print(cadenas_1("su clave es: 1540", "*"))