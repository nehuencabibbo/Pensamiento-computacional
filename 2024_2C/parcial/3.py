# sólo se consideran las primeras 
# N inscripciones

# Hay un año de ingreso límite. 
# Las personas no deben superar 
# ese año de ingreso.

def inscripciones_fiubaton(n, año_limite, inscriptos):
    # Solo analizamos los primeros N inscriptos
    inscriptos = inscriptos[:n]

    entraron = []
    for nombre, año_ingreso in inscriptos:
        if año_ingreso < año_limite: 
            entraron.append(nombre)

    return entraron

inscriptos = [
    ("Agustina F", 2020), 
    ("Florencia D", 2021), 
    ("Sasha S", 2023), 
    ("Maria G", 2020)
]