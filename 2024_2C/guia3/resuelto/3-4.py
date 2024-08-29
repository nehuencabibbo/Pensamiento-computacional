# 1 - Mostrar el total a pagar
# 2 - Pedirle al usuario que me pague una vez
# 3 - Mientras me siga debiendo plata, mostrarle lo que le 
# falta y pedirle que me pague denuevo
# 4 - Mostrar mensaje final
def cobro(monto_a_pagar):
  print(f"Su total a pagar es: {monto_a_pagar}")
  monto_pagado = int(input("Ingrese el monto a pagar: "))
  monto_a_pagar -= monto_pagado
  while monto_a_pagar > 0:
    monto_pagado = int(input(f"Pendientes: {monto_pagado}. Ingrese el monto a pagar: "))
    monto_a_pagar -= monto_pagado

  print(f"Pendientes: 0. Gracias por su compra")

