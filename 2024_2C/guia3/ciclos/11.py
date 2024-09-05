def suma_multiplos_de_siete(inicio, fin):
    suma = 0 
    contador = 0
    for numero in range(inicio, fin + 1):
        if numero % 2 == 0:
            continue 

        if numero % 7 == 0:
            suma += numero
            contador += 1

        if contador == 3:
            break

    if contador == 0:
        return  0
    
    return suma / contador 

print(suma_multiplos_de_siete(3, 4))