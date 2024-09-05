# Escribir un programa que contenga una contraseña inventada,
# que le pregunte al usuario la contraseña, y no le permita 
# continuar hasta que la haya ingresado correctamente.

# 1 - Definir la contra (pueden pasarla por param)
# 2 - **Pedirle** al usuario que ingrese una contra
# 3 - **Mientras** sea incorrecta volver a 2 

def adivinanza(contra):
    # Paso 2
    ingreso = input("Ingrese la contra: ")
    # Paso 3 
    while ingreso != contra:
        print("La contraseña " + ingreso + " es incorrecta")
        ingreso = input("Ingrese la contra: ")
    
    # En este punto si o si ingreso == contra, sino
    # no hubiera salido del while 
    print("Adivinaste la contra")

# Paso 1
contra = "AAAaaa"
adivinanza(contra)

# PYTUTOR 