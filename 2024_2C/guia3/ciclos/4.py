# 1 - **Mostrar** el total a pagar al usuario
# 2 - **Pedirle** al usuario una cantidad a pagar
# 3 - **Mientras** nos deba plata mostrarle sus pendientes y 
# pedirle una cantidad a pagar
# 4 - **Mostar** el mensaje de despedida

def total_a_pagar(monto_a_pagar):
    # Paso 1
    print(f"Debe pagar {monto_a_pagar}.")
    # Paso 2
    ingreso = int(input("Ingrese el monto a pagar: "))
    monto_a_pagar -= ingreso
    # Paso 3
    while monto_a_pagar > 0:
        ingreso = int(input(f"Pendientes: {monto_a_pagar}. Ingrese el monto a pagar: "))
        monto_a_pagar -= ingreso

    if monto_a_pagar < 0:
        # Paso 4
        monto_a_pagar = abs(monto_a_pagar)
        print(f"Pendientes: 0. Su vuelto es: {monto_a_pagar}. Gracias por su compra")
    else: 
        print(f"Pendientes: 0. Gracias por su compra")


total_a_pagar(500)