# A)
estudiante1 = {
  "nombre": "Violeta",
  "apellido": "Perez",
  "dni": 42000000,
  "carrera": "Informática"
}
estudiante2 = {
  "nombre": "Carla",
  "apellido": "Guanca",
  "dni": 42001001,
  "carrera": "Mecánica"
}
estudiante3 = {
  "nombre": "Manuela",
  "apellido": "Gómez",
  "dni": 42002002,
  "carrera": "Química"
}

estudiantes = [estudiante1, estudiante2, estudiante3]

# B
estudiante1 = {
  "nombre": "Violeta",
  "apellido": "Perez",
  "dni": 42000000,
  "carrera": "Informática",
  "notas": {
    7541: 10,
    7503: 7
  }
}

# C
estudiante1["notas"][7507] = 7
estudiante1["notas"][6103] = 4

# D
def obtener_cant_notas(estudiante):
  return len(estudiante["notas"])

# Para el ejemplo no anda porque tendria que definirle notas a los otros
# dos estudiantes, sino estudiante["nota"] tira un KeyError
def obtener_estudiante_mas_notas(lista):
    maxima_cantidad_de_notas = 0
    estudiante_con_mas_notas = None
    for estudiante in lista:
        cantidad_de_notas = len(estudiante["notas"])
        if cantidad_de_notas > maximo:
            maximo = cantidad_de_notas
            estudiante_con_mas_notas = estudiante["nombre"]

    return estudiante_con_mas_notas


  