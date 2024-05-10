def comparar_cadenas(cadena1, cadena2):
    for i in range(len(cadena1)):
        if cadena1[i] > cadena2[i]:
            return cadena2
        elif cadena1[i] < cadena2[i]:
            return cadena1
        
    return cadena1

def cadenas_4(cadena1, cadena2):
    
    if len(cadena1) > len(cadena2):
        return comparar_cadenas(cadena2, cadena1)
    
    return comparar_cadenas(cadena1, cadena2)


print(cadenas_4("aaaa", "aab"))