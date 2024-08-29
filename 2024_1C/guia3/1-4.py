# Escribir una función para determinar si una letra recibida es vocal o no.
# La misma debe devolver un valor booleano. Luego, escribir una función para 
# determinar si una letra es consonante o no.

#     Resolver sin el uso de in ni not in.
#     Resolver usando in y not in.
#     Resolver para que la función identifique tanto mayúsculas como minúsculas. 

#    Pista: investigar los métodos lower y upper de string.


# a)

def es_vocal(letra):
    if (letra == "a"):
        return True
    elif (letra == "e"):
        return True
    elif (letra == "i"):
        return True
    elif (letra == "o"):
        return True
    elif (letra == "u"):
        return True
    else:
        return False

# Mostrar que el else es redundante, porque para ese punto, ya sabemos que no es una vocal
# porque sino ya hubiera returneado la funcion

def es_vocal(letra):
    if (letra == "a"):
        return True
    elif (letra == "e"):
        return True
    elif (letra == "i"):
        return True
    elif (letra == "o"):
        return True
    elif (letra == "u"):
        return True
    
    return False
    
# Mostrar que es lo mismo usar if y elif, que lo escriban como les salga, y dado 
# el caso se fijen si pueden usar solo ifs

def es_vocal(letra):
    if (letra == "a"):
        return True
    if (letra == "e"):
        return True
    if (letra == "i"):
        return True
    if (letra == "o"):
        return True
    if (letra == "u"):
        return True
    
    return False

# b) 

def es_vocal(letra):
    vocales = "aeiou"
    if (letra in vocales):
        return True
    
    return False

# Mostrar que es redundante, la condicion de por si ya evalua a True o False,
# se puede reescribir de la siguiente manera

def es_vocal(letra):
    vocales = "aeiou"

    return letra in vocales

# c)

def es_vocal(letra):
    vocales = "aeiou"
    letra = letra.lower()

    if (letra in vocales):
        return True
    
    return False

# Idem punto anterior

def es_vocal(letra):
    vocales = "aeiou"

    return letra.lower() in vocales