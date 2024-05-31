# Escribir un programa que le pida números al usuario e imprima si son pares o impares. 
# Si el usuario ingresa un valor que no es un número, el programa debe imprimir un mensaje 
# de error y seguir pidiendo números. El programa termina cuando el usuario ingresa "*".

# Solo los integers puede ser pares o impares (depende la def pero lo tomamos asi)
def par_o_impar():
    numero = input("Ingrese un numero: ")
    while numero != "*":
        try:
            numero = int(numero)
            if numero % 2 == 0:
                print("par")
            else:
                print("impar")

        except ValueError as e:
            print("Error")

        numero = input("Ingrese un numero: ")


par_o_impar()