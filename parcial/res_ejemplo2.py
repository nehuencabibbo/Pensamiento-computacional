from random import randint

def simular_tiro_dado(t, n):
    #Lo vimos en clase
    datos = {}
    for _ in range(t):
        cara = randint(1, n)
        if not cara in datos:
            datos[cara] = 1
        else:
            datos[cara] += 1

    return datos

def experimento(t, n):
    #Muestro la cantidad de tiros y caras del experimento
    print(f"Cantidad de tiros: {t} - Cantidad de caras: {n}")

    #En caso de que la cantidad de tiros sea menor a 10, 
    #muestro lo que me piden y termino la funcion
    if t < 10:
        print("No se puede determinar si esta defectuoso el dado")
        #En este caso, inmediatamente salgo de la funcion
        #return asecas = return None
        return
    
    #Simulo el experimento y obtengo sus datos
    datos_experimento = simular_tiro_dado(t, n)

    #Muestro los datos de mi experimento
    #Esta hecho para el bonus, para hacerlo de manera normal
    #simplemente usar datos_experimento.items()
    #OBS: Recordar que diccionario.items() devuelve [(key, value), ... , (key, value)]
    #para toda llave del diccionario
    for cara, apariciones in sorted(datos_experimento.items(), key=lambda x: x[0]):
        print(f"La cara {cara} salio {apariciones} veces")

    #Si salio la mitad o menos del total de caras,
    #el dado esta defectuoso
    if len(datos_experimento) <= n // 2:
        print("El dado esta defectuoso")

    #Caso contrario, el dado no estaba defectuoso
    else:
        print("El dado NO esta defectuoso")

#Para ejecutar varias veces y jugar sin tener que cambiar a mano
tiros = randint(1, 20)
caras = randint(2, 25)

experimento(tiros, caras)