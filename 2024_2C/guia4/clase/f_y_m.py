def mappear_a_nombre(numero_de_dia):
    if numero_de_dia == 1:
        return "Lunes"
    elif numero_de_dia == 2:
        return "Martes"
    elif numero_de_dia == 3:
        return "Miercoles"
    elif numero_de_dia == 4: 
        return "Jueves"
    else:
        return "Viernes"

def obtener_dia_de_la_semana(numeros_de_dias):
    return list(map(mappear_a_nombre, numeros_de_dias))

def arranca_por_m(dia):
    return dia[0].upper() == "M"

# ["Lunes", "Martes", "Miercoles"]
def arrancan_con_m(dias):
    return list(filter(arranca_por_m, dias))

numero_de_dias = [1, 2, 3, 5] 

dias_por_nombre = obtener_dia_de_la_semana(numero_de_dias)
print(dias_por_nombre)

dias_que_arrancan_con_m = arrancan_con_m(dias_por_nombre)
print(dias_que_arrancan_con_m)