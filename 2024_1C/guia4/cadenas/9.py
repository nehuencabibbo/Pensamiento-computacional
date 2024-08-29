def letras_unicas(a, b): 
    #Obtengo todos los caracteres
    todos_los_caracteres = list(a) + list(b)

    #Me quedo con (Filtro) los caracteres de la lista que NO (esten en a y b)
    letras_unicas = filter(lambda x: not (x.lower() in list(a.lower()) and x.lower() in list(b.lower())), todos_los_caracteres)

    return list(letras_unicas)

#Mas lindo, si una funcion tiene una linea y no se reutiliza se puede definir como una lambda:
def letras_unicas(a, b): 
    todos_los_caracteres = list(a) + list(b)

    esta_en_cadena = lambda x, cadena: x.lower() in list(cadena.lower())

    letras_unicas = filter(lambda x: not (esta_en_cadena(x, a) and esta_en_cadena(x, b)), todos_los_caracteres)

    return list(letras_unicas)

a = "Python"
b = "Hola"

print(letras_unicas(a, b))