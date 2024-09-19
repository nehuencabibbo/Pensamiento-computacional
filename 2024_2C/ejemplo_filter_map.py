def mappear_dia(numero_de_dia):
    nombres_dias = [
        "Lunes", 
        "Martes", 
        "Miercoles", 
        "Jueves", 
        "Viernes", 
        "Sabado", 
        "Domingo"
    ]
        
    return nombres_dias[numero_de_dia - 1]

def obtener_dia_de_la_semana(dias):  
    return list(map(mappear_dia, dias))

def filtrar_dias(dia):
    return dia[0].lower() == "m"

def obtener_dias_que_comienzan_con_m(dias):
    return list(filter(filtrar_dias, dias))

dias = [1, 3, 4, 2]

print(obtener_dias_que_comienzan_con_m(obtener_dia_de_la_semana(dias)))