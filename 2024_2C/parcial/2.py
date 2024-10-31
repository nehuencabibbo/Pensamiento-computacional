# deben asegurarse
# primero de quienes 
# son celíacos y quienes no

def grupos_fiesta(estudiantes):
    celiacos = []
    no_celiacos = []
    for nombre, es_celiaco in estudiantes:
        if es_celiaco:
            celiacos.append(nombre)
        else: 
            no_celiacos.append(nombre)

    return (no_celiacos, celiacos)

estudiantes = [
    ("Juana", False), 
    ("Martina", True), 
    ("Juliana", True)
]
grupos_fiesta(estudiantes)