#for i in range(len(numero)-1, -1, -1):

#range(inicio, fin, paso) -> Si paso negativo: recorre al reves

#range(10, -1, -1) 


def cadenas_2(numero):
    resultado = []
    for i in range(len(numero)-1, -1, -1):
        if (i - 1) % 3 == 0: 
            resultado.append(numero[i])
            resultado.append(".")
        else:
            resultado.append(numero[i])

    return str(resultado.reverse())


def cadenas_2(numero):
    resultado = ""
    for i in range(len(numero)-1, -1, -1):
        if (i - 1) % 3 == 0:
            resultado += numero[i]
            resultado += "."
        else:
            resultado += numero[i]

    return resultado[::-1]


print(cadenas_2("1234567890"))

print(list(range(10, -1, -3))) 






