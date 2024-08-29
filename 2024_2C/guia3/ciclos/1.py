# Para ejecutar descomentar la llamada

# a)
def imprimir_entre(inicio, fin):
  for numero in range(inicio, fin + 1):
    print(numero)

# imprimir_entre(0, 10)

# b)
def saludar(lista):
  for nombre in lista:
    print(f"Hola {nombre} vamos a aprender a programar!")

lista_de_personas = ["Flaminia", "Serena", "Agustina", "Priscila", "Sol", "Agostina", "Iara", "Lu"]

# saludar(lista_de_personas)

# c)
def suma_total():
  total = 0
  for i in range(5): #[0, 1, 2, 3, 4]
    numero = int(input(f"[Ingreso numero {i + 1}] Ingrese un numero: "))
    total += numero

  print(f"Su total es {total}")


# suma_total()

# d)
def imprimir_entre_100_y_199():
  for numero in range(100, 200):
    if numero % 7 == 0:
      print(numero)

# imprimir_entre_100_y_199()

# e) 
def imprimir_par_o_impar(inicio, fin):
    for numero in range(inicio, fin + 1, 2):
        if numero % 2 == 0:
            print(f"{numero} es par")
        else:
            print(f"{numero} es impar")

# imprimir_par_o_impar(0, 10)