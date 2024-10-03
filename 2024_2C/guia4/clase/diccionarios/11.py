notas = [
    {"nombre": "Violeta", "apellido": "Perez", "intento": 2, "nota": 2}, 
    {"nombre": "Manuela", "apellido": "Gomez", "intento": 1, "nota": 6}, 
    {"nombre": "Carla", "apellido": "Guanca", "intento": 1, "nota": 8}
]

# suma_notas_del_primer_intento / total_de_notas_del_primer_intento

# Dos opciones: 

# 1 - Quedarme solo con las notas del primer intento
# 2 - Calcular el promedio de notas

# 1 - Para cada nota ver si es del primer intento
# y e irse guardando los valores parciales de suma y nota

def calcular_promedio(notas_estudiantes, intento):
    total = 0
    cant_notas = 0
    for estudiante in notas_estudiantes: 
        # {"nombre": , "apellido": , "intento": , "nota": }
        if estudiante["intento"] == intento:
            total += estudiante["nota"]
            cant_notas += 1
        
    return total / cant_notas
