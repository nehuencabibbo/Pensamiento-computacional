# def insertar_separador(palabra, separador):
#     lista_de_caracteres = list(palabra)
    
#     return "-".join(lista_de_caracteres)

def insertar_cada_3(string, separador):
    elementos_a_unir = []

    while len(string) > 0:
        primeros_tres = string[:3]
        elementos_a_unir.append(primeros_tres)

        string = string[3:] # equivalente: [3:len(string):1]
    
    return ".".join(elementos_a_unir)

string = "2552552550"
separador = "."

resultado = insertar_cada_3(string, separador)

print(resultado)