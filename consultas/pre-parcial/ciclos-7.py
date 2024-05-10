import random

def ejericio_7(numero_a_adivinar):
    adivinanza = int(input("Adivina: ")) #10

    while adivinanza != numero_a_adivinar:
        if adivinanza < numero_a_adivinar:
            print("Es menor")

        if adivinanza > numero_a_adivinar:
            print("Es mayor")

        adivinanza = int(input("Adinie un numero: "))

    print("Adivinaste")


numero = random.randint(1, 10)
ejericio_7(5)
