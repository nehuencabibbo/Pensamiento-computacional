# 1 - Mientras no haya adivinado todas las letras 
# y me queden intentos
# 1.1 Mostrar los intentos disponibles 
# 1.2 - Pedirle al usuario que adivine una letra
# 1.3 - Si la letra estaba en mi lista de palabras,
# imprimir que fue correcto y las letras incorrectas
# 1.4 - Si la letra no estaba en mi lista de palabras,
# imprimir que fue incorrecto y las letras incorrectas 


def ahorcado(caracteres_a_adivinar, intentos):
    letras_incorrectas = []
    while len(caracteres_a_adivinar) > 0 and intentos > 0:
        print(f"Intentos disponibles: {intentos}")
        adivinanza = input("Adivine una letra: ").lower()

        if adivinanza in caracteres_a_adivinar:
            caracteres_a_adivinar.remove(adivinanza)
            print(f"Correcto! Letras incorrectas {letras_incorrectas}")
        else:
            letras_incorrectas.append(adivinanza)
            print(f"Incorrecto. Letras incorrectas: {letras_incorrectas}")    

    if len(caracteres_a_adivinar) == 0:
        print("Ganaste")
    else:
        print("Te quedaste sin intentos")