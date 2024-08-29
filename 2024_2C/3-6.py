def manejo_de_contraseñas(contra, intentos):
  adivinanza = input("Adivina una contra: ") 
  intentos -= 1
  while adivinanza != contra and intentos > 0:
    adivinanza = input("Adivina una contra: ")
    intentos -= 1

  return adivinanza == contra

manejo_de_contraseñas("assddase", 3)