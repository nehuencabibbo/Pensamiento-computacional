# deben asegurarse primero de quienes son 
# celíacos y quienes no, para evitar la 
# contaminación de la comida.

def grupos_festejo(participantes):
    celiacos = []
    no_celiacos = []
    for nombre, es_celiaco in participantes:
        if es_celiaco:
            celiacos.append(nombre)
        else: 
            no_celiacos.append(nombre)

    return [celiacos, no_celiacos]