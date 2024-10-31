# En cada turno

#  Si el usuario se equivoca, 
# se le resta una chance

# si adivina, no se le resta nada

# Continúa hasta que se adivinen 
# todas las letras de la palabra o 
# el usuario se quede sin intentos.

# 1 - Mientras no se hayan adivinado
# todas las letras de la palabra y 
# le queden intentos al usuario
# 1.1 - Pedirle al usuario que ingrese
# una letra a adivinar 
# 1.2 - 
# Si la letra estaba en mi lista
# de caracteres => muestro el mensaje
# correspondiente. OBS: No restar inten-
# tos 
# Caso contrario => muestro el mensaje
# correspondiente y resto un intento

# ["e", "s", "s", "i"] 
def ahorcado(caracteres, chances):
    errores = []
    while len(caracteres) > 0 and chances > 0:
        adivinanza = input("Ingrese una letra a adivinar: ")
        if adivinanza.lower() in caracteres:
            print(f"Correcto! Errores: {errores}")
            caracteres.remove(adivinanza)
        else: 
            errores.append(adivinanza)
            print(f"Incorrecto! Errores: {errores}")
            chances -= 1

    if chances == 0:
        print("Te has quedado sin intentos")
    else: 
        print("Ganaste")