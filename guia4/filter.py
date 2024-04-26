a = "Algoritmos"

def es_consontante(letra):
    vocales = "aeiou"
    return not letra.lower() in vocales

print(tuple(filter(es_consontante, a)))