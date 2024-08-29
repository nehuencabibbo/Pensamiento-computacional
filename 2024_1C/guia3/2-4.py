# Necesitamos escribir un programa de cobro en el supermercado. 
# La función debe recibir un número entero que representa el monto a pagar 
# y debe permitir al usuario que ingrese valores, hasta que el pago se haya 
# realizado en su totalidad. Además, le debe ir indicando cuánto le queda por pagar. 
# El programa no da vuelto.

# Ejemplo:

# Su total a pagar es: 500
# Ingrese el monto a pagar: 100
# Pendientes: 400. Ingrese el monto a pagar: 200
# Pendientes: 200. Ingrese el monto a pagar: 200
# Pendientes: 0. Gracias por su compra.

def cobrar(total_a_pagar):
    print(f"Su total a pagar es: {total_a_pagar}")

    es_la_primera_vez = True
    while total_a_pagar > 0:
        if es_la_primera_vez:
            cantidad_pagada = int(input(f"Ingrese el monto a pagar: "))
            es_la_primera_vez = False
        else:
            cantidad_pagada = int(input(f"Pendientes: {total_a_pagar}. Ingrese el monto a pagar: "))
        
        total_a_pagar -= cantidad_pagada

    print("Pendientes: 0. Gracias por su compra.")

cobrar(500)