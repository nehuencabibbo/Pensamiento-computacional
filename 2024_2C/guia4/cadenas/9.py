def no_en_comun(a, b):
    a = list(a.lower()) # ["P", "y", ...]
    b = list(b.lower()) # ["H", ...]

    todos_los_characters = a + b

    resultado = []
    for caracter in todos_los_characters:
        no_estan_en_los_dos = not (caracter.lower() in a and caracter.lower() in b)
        if no_estan_en_los_dos:
            resultado.append(caracter)

    return resultado


a = "Python"
b = "Hola"

print(no_en_comun(a, b))
