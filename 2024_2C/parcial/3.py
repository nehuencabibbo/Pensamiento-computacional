#  sólo se consideran las 
# primeras N inscripciones

# Hay un año de ingreso límite. 
# Las personas no deben superar
# ese año de ingreso.

def inscripciones(n, año_limite, estudiantes):
    estudiantes = estudiantes[:n]
    estudiantes_aceptados = []
    for nombre, año in estudiantes:
        if año < año_limite:
            estudiantes_aceptados.append(nombre)

    return estudiantes_aceptados