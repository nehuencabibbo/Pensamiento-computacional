alumnos = [
    {
        "nombre": "Nehuén",
        "padron": 108025,
        "año_de_nacimiento": 2002,
        "notas": [9, 8, 6, 7, 10, 9],
    },
    {
        "nombre": "Lucas",
        "padron": 108026,
        "año_de_nacimiento": 2001,
        "notas": [8, 7, 9],
    },
    {
        "nombre": "Maria",
        "padron": 108027,
        "año_de_nacimiento": 2000,
        "notas": [10, 9, 8, 10, 9, 8, 4, 5, 6],
    },
    {
        "nombre": "Juan",
        "padron": 108028,
        "año_de_nacimiento": 2003,
        "notas": [7, 8, 10],
    },
    {
        "nombre": "Ana",
        "padron": 108029,
        "año_de_nacimiento": 2004,
        "notas": [9, 8, 9, 8, 9],
    }
]

#B) paso a paso

def agregar_promedio(alumno):
    alumno["promedio"] = sum(alumno["notas"]) / len(alumno["notas"])
    
    return alumno


def mappear_a_string(alumno):
    #Otra forma: f'{x["nombre"]} - {x["padron"]} - {sum(x["notas"])/len(x["notas"])}'
    datos = (str(alumno["nombre"]), str(alumno["padron"]), str(alumno["promedio"]))

    return " - ".join(datos)


def top_3_promedios(alumnos):
    #Quiero trabajar con el promedio, mappeo a eso
    #Se puede hacer con for a mano tambien
    alumnos = list(map(agregar_promedio, alumnos))

    #Quiero obtener el top3, para eso necesito algun orden
    #asi que ordeno de mayor a menor segun promedio
    alumnos.sort(key=lambda x: x["promedio"], reverse=True)

    #De cada alumno quiero mostrar cierta informacion en un
    #string, mappeo al string correspondiente
    #Se puede hacer directamente en el for de abajo tambien
    alumnos = list(map(mappear_a_string, alumnos))

    #Quiero solo el top3, asi que me quedo con un slice
    #de 3 elementos de la lista
    for alumno in alumnos[:3]:
        print(alumno)

top_3_promedios(alumnos)


